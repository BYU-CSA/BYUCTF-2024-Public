# You might think to yourself, "I will reverse engineer this code to find the solution!"
# This is not a reverse engineering challenge. You don't need to know how I messed up some nice, normal pictures in order to understand how to find them on a hard drive.
# I'm not going to stop you from wasting your time by reverse engineering this, but I am going to be polite and encourage you not to waste to much time on it.
from argparse import ArgumentParser

# Handle arguments
def get_args():
    parser = ArgumentParser(description="This script turns the unusual files used by the Mad Cow APT into a standard picture file.",epilog="If you think that the answer to this challenge is found in reverse engineering this script, remember that this is a forensics challenge - not a reverse engineering challenge. You can solve this problem without needing to understand this script.")
    parser.add_argument("-i", "--infile", dest="input_file", help="input file, this should be the obfuscated file", metavar="FILEPATH", required=True)
    parser.add_argument("-o", "--outfile", dest="output_file", help="output file, this should be the file of the new, unobfuscated file", metavar="FILEPATH", required=True)
    args = parser.parse_args()
    return(args)

# Turn the input file into a byte stream
def read_file(filepath):
    with open(filepath, mode='rb') as file:
        fileContent = file.read()
        return(fileContent)

# Write a byte stream to an output file
def write_file(input_binary, filepath):
    with open(filepath, mode='wb') as file:
        file.write(input_binary)

# Oooooh look at you, you found out that my cRaZy encryption scheme is just an xor.
def xor(a):
    return bytearray([b^0xff for b in bytearray(a)])

# Fix the first few bytes to make sure that programs know this is a PNG
def fix_start(input_binary):
    writeable_bytes = bytearray(input_binary)
    writeable_bytes[0] = 137
    writeable_bytes[1] = 80
    writeable_bytes[2] = 78
    writeable_bytes[3] = 71
    return(bytes(writeable_bytes))

# Fix the last few bytes to make sure that programs know this is a PNG
def fix_end(input_binary):
    writeable_bytes = bytearray(input_binary)
    writeable_bytes[-1] = 130
    writeable_bytes[-2] = 96
    writeable_bytes[-3] = 66
    writeable_bytes[-4] = 174
    return(bytes(writeable_bytes))

# Run the program
if __name__=='__main__':
    args = get_args()
    in_bytes = read_file(args.input_file)
    out_bytes = xor(in_bytes)
    fixed_start = fix_start(out_bytes)
    fixed_end = fix_end(fixed_start)
    write_file(fixed_end, args.output_file)
