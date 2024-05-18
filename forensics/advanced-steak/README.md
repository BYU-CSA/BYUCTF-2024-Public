# Advanced Steak
Description:
```markdown
The Mad Cow APT has been responsible for a significant amount of attacks against organizations in the technology, finance, and energy domains. They first started their attacks around 3 years ago, though they have been dormant in the last 2 years. Recently, the APT started to resurface.

Field agents were able to conduct a raid against a known Mad Cow hideout. In the process, the agents pulled a flash drive from one of the Mad Cow computers. Unfortunately, it looks like one of the threat actors was able to begin wiping the flash drive with random data before the analyst pulled the drive. The field agent pulled the drive before the wipe was complete, but parts of the drive have been corrupted. Our team has already created a forensic image of the drive: Mad Cow.001.

Analysts who studied the Mad Cow APT two years ago are highly confident that the APT is utilizing the same tactics as they have in previous years. One such tactic is communicating through a custom file type. Fortunately, one of analysts built a decryptor for this custom file type. Using this, we can turn any `.cow` files into a standard PNG. The decryptor does not offer any useful information on finding these files, however.

Your job is to find any .cow files on the corrupted flash drive (`Mad Cow.001`) and pull them from the image file. You can use the two provided `.cow` files as reference to help understand what the files look like. Then, run any discovered `.cow` file(s) through the decryptor to determine if there is any useful data. The data will be in the format `byuctf{flag}`.

*Note: this is not a reverse engineering challenge. The `cow_decryptor.py` is intentionally missing important data. You do not need to reverse engineer the script in order to find the file(s). This challenge can be solved without examining the `cow_decryptor.py` file.*

[steak.zip]
```

## Writeup
### Summary
At it's heart, the challenge is a simple file signature carve. There are a few problems included in this challenge that add layers of complexity:
1. The image file has been partially overwritten with random data, so it is missing its metadata (`$MFT` in this case, as it was originally an NTFS volume)
2. The file that needs to be carved is a custom file type, so no forensic tool will come with the ability to find its signature
3. The competitor is not expressly told that they need to carve a file

In order to solve the challenge, the following is required:
* A competitor must identify the custom file signature (header and trailer) used by the `.cow` files
* A competitor must manually carve a .cow file from a forensic image
* A competitor cannot rely on forensic tools (at least, not with default settings) since the forensic image is corrupted

### Solution Method
The solution method I used is not the easiest method, but it does clearly demonstrate the steps.

To find the file signature header and trailer, a competitor can use any hex viewer. I used `xxd`. I then analyzed the header for both provided `.cow` files.
```bash
xxd 'Cow 1.cow' | head
xxd 'Cow 2.cow' | head
```

Following this, I used `xxd` to find the file trailer.
```bash
xxd 'Cow 1.cow' | tail
xxd 'Cow 2.cow' | tail
```

This demonstrated that the header is `1337beef` and the trailer is `4d6f6f6f` (the competitor may have a slightly larger header due to the nature of a PNG file, this is fine and should not interfere with the search).

From here, I used `hexedit` to examine the file.
```bash
hexedit 'Mad Cow.001'
```

From here, I used the following commands:
* `CTRL-S`, using `1337beef` as the search parameter (this found the beginning of the file)
* `CTRL-Space` (or `F9`) (this set the beginning of the marker, essentially the start of the copy)
* `CTRL-S`, using `4d6f6f6f` as the search parameter (this found the end of the file)
* I then highlighted a few bytes over to make sure I got the whole `4d6f6f6f` section, as `hexedit` search takes you to the beginning of the search parameter
* `ESC-W` (this copies the selected bytes)
* `ESC-Y` (this pastes the selected bytes into a new file)

I called the new file `'cow_file.out'`. I then verified that the header and trailer were what I expected.
```bash
xxd 'cow_file.out' | head
xxd 'cow_file.out' | tail
```

After confirming that the section I exported had the `1337beef` header and the `4d6f6f6f` trailer, ran the file through the file decryptor.

```bash
python3 ./cow_decryptor.py -i cow_file.out -o cow_file.png
```

Opening the `cow_file.png` file, the flag was visible!

**Flag** - `byuctf{incredi-bull}`

## Challenge Creation
### Challenge Overview
This challenge is rather advanced, and it is not expected that every student will know how to solve it – even advanced competitors may have difficulty. It addresses two important issues in digital forensics, however:

1. What does an examiner do when they come across a file that their tools cannot parse?
2. What does an examiner do when they come across a corrupted file system that their tools don't understand?

In addition, the challenge gives students hands-on experience carving a file (maybe even manually carving the file).

### Summary
At it's heart, the challenge is a simple file signature carve. There are a few problems included in this challenge that add layers of complexity:
1. The image file has been partially overwritten with random data, so it is missing its metadata (`$MFT` in this case, as it was originally an NTFS volume)
2. The file that needs to be carved is a custom file type, so no forensic tool will come with the ability to find its signature
3. The competitor is not expressly told that they need to carve a file

In order to create the challenge, the following are required:
* A forensic image file small enough to be parsed by competitors with low-powered hardware, yet large enough to hide a file within it
* A custom file type that can be turned into something every OS is expected to read
* A file "encryptor" that can turn a normal file into the custom file
* A file "decryptor" that can turn the custom file back into a normal file
* Several example files that students can use to create their own custom signatures

### Creating the Forensic Image File
This was perhaps the easiest of the tasks. I chose to use 25 MB as the forensic image file size. This is easy to download, easy to work with, yet large enough to hide a small file.

To create this, I first made a 25 MB partition on a Windows machine. I chose to make that partition NTFS. I then used FTK Imager to create a raw (dd) image file of the partition. This is the beginning of the `Mad Cow.001` file.

Next, the file had to be partially overwritten so that competitors could not rely on `$MFT` parsing to find the file. I chose to move the `Mad Cow.001` file to a Linux machine and overwrite the first 18 MB of the file with random data. The exact command was the following:

```bash
dd if=/dev/urandom of=./Mad\ Cow.001 bs=1M count=18 conv=notrunc
```

Note the use of `conv=notrunc`. This was very important to ensure the original image file retained the NTFS trailer.

### Creating the Custom `.cow` File Type
I knew from the beginning that I wanted a file to have the signature `1337beef` in hex (elite beef, using leetspeak). I decided that it needed an ending, which I chose to have be ASCII "Mooo" (hex `4d6f6f6f`). Technically, one could try carving by block and assume that a block ending in many null bytes (00 bytes) would be the end of the file, but this is prone to error. In order to create the file, I first made an "encryption" program. This program does the following, in order:
1. Take a PNG file as input
2. Run an XOR operation against every byte in the file, using `ff` (`11111111`) as the XOR sequence
3. Replace the first 4 bytes with `1337beef`
4. Replace the last 4 bytes with `4d6f6f6f`
5. Output a new file defined by the user

I wrote this program in Python so that it could be run on any OS.

I then created a file decryptor that could turn one of these custom files (arbitrarily given `.cow` as an extension) back into a PNG. The program does the following, in order:
1. Take a `.cow` file as input
2. Run an XOR operation against every byte in the file, using `ff` (`11111111`) as the XOR sequence (note that XOR twice with the same sequence reverts the original XOR)
3. Replace the first 4 bytes with `89504e47` – the proper PNG header
4. Replace the last 4 bytes with `ae426082` – the proper PNG trailer
5. Output a new file defined by the user

This was also written in Python.

### Putting the Flag in the Image File
In order to put the flag in the image file, I first needed a flag file. I took a picture of a cow and put the flag in the image as text. I then used dd to paste that file in the middle of the forensic image.

```bash
dd if=./Cow\ Flag.cow of=./Mad\ Cow.001 bs=512 count=1149 conv=notrunc seek=28672
```

A little overview of the options used:
* `if=./Cow\ Flag.cow` this is the input file, being the `.cow` file with a flag
* `of=./Mad\ Cow.001` this is the output file, being the forensic image
* `bs=512` since we are only writing a fixed number of bytes, it is very important that we know exactly how big our file is. We use a multiple of 512 bytes for convenience
* `count=1149` the Cow Flag.cow file is 587966 bytes. Divided by 512, this is just over 1148. We use 1149 to ensure the trailer is included (dd, without the count option, will just keep writing data as it loops over the file until you kill it)
* `conv=notrunc` this option prevents dd from deleting the data after the file
* `seek=28672` this option tells dd to start writing the file somewhere deep in the file (2867 * 512 bytes, to be precise)