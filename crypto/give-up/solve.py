import base64
import itertools

#let KEYSIZE be the guessed length of the key

def repeat_key_xor(plain, key): # take in bytes
    output = b''
    mod = len(key)

    i = 0
    for byte in plain:
        output += bytes([byte ^ key[i]])
        i = (i + 1) % mod

    return output

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def get_english_score(input_bytes):
    """Returns a score which is the sum of the probabilities in how each letter of the input data
    appears in the English language. Uses the above probabilities.
    """
    score = 0

    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0) # default value in get is set to 0 here

    return score


def singlechar_xor(input_bytes, key_value):
    """XORs every byte of the input with the given key_value and returns the result."""
    output = b''

    for char in input_bytes:
        output += bytes([char ^ key_value])

    return output


# this is the main function
def singlechar_xor_brute_force(ciphertext): # ciphertext is passed as bytes
    """Tries every possible byte for the single-char key, decrypts the ciphertext with that byte
    and computes the english score for each plaintext. The plaintext with the highest score
    is likely to be the one decrypted with the correct value of key.
    """
    candidates = []

    for key_candidate in range(256):
        plaintext_candidate = singlechar_xor(ciphertext, key_candidate)
        candidate_score = get_english_score(plaintext_candidate)

        # ooh a dictionary is a handy data type here
        result = {
            'key': key_candidate,
            'score': candidate_score,
            'plaintext': plaintext_candidate
        }

        candidates.append(result)

    # Return the candidate with the highest English score, sorted is super useful
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]

# 2. Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits
def find_hamming_distance(bin_string1, bin_string2):
    assert len(bin_string1) == len(bin_string2)

    # auto-add difference in sizes
    distance = 0
    # then for every different bit, add one
    for byte1, byte2 in zip(bin_string1, bin_string2):
        difference = byte1 ^ byte2
        # takes the sum of bit difference per byte
        distance += sum([1 for bit in bin(difference) if bit == '1'])

    return distance


def break_repeating(ciphertext):
    #this is an updated implementation designed to fix the issues that my old implementation above doesn't resolve...
    distance_indexes = {} #dictionary of distances and scores

    # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
    #       and find the edit distance between them. Normalize this result by dividing by KEYSIZE

    # honestly if there's a key larger than 40, just extend this
    for key_size in range(2, 40):

        # 4. The KEYSIZE with the smallest normalized edit distance is probably the key. 
        #       You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances

        chunks = [ciphertext[i:i + key_size] for i in range(0, len(ciphertext), key_size)][:4] #first 4 keysize blocks

        distance = 0
        pairs = itertools.combinations(chunks, 2) # all sets of the chunks
        for (x,y) in pairs: # cuz they're stored as tuples
            distance += find_hamming_distance(x,y)

        distance /= 6 # there are 6 sets of pairs in the cartesian product of 4 items, therefore average is / 6
        distance /= key_size # normalize

        distance_indexes[key_size] = distance #set the value in the dictionary
    
    possible_key_sizes = sorted(distance_indexes, key=distance_indexes.get)[:3] # top 3 based on the values
    possible_plaintext = []

    for key_size in possible_key_sizes:
        key = b''

        # 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length
        for i in range(key_size):
            block = b''

            for j in range(i, len(ciphertext), key_size):
                block += bytes([ciphertext[j]]) # if this isn't surrounded in [] it just makes a series of null bytes key_size long!

            key += bytes([singlechar_xor_brute_force(block)['key']]) # ... same here...
        
        possible_plaintext.append((repeat_key_xor(ciphertext, key), key))
    
    return max(possible_plaintext, key=lambda k: get_english_score(k[0])) # grabs the highest scoring english pal


def main():
    #test hamming distance with an assert between "this is a test" and "wokka wokka!!!"
    assert find_hamming_distance(b"this is a test", b"wokka wokka!!!") == 37
    
    with open("you.txt") as input:
        ciphertext = bytes.fromhex(input.read())

    result = break_repeating(ciphertext)
    print("Key = ", result[1].decode(), " -- Plaintext = ", result[0].decode().rstrip())

    return "end"

if __name__ == "__main__":
    main()


"""
Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two strings. 
    The Hamming distance is just the number of differing bits. 
    The distance between: this is a test and wokka wokka!!! is 37. Make sure your code agrees before you proceed.
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
    and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
The KEYSIZE with the smallest normalized edit distance is probably the key. 
    You could proceed perhaps with the smallest 2-3 KEYSIZE values. 
    Or take 4 KEYSIZE blocks instead of 2 and average the distances.
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, 
    and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte 
    for that block. Put them together and you have the key.
This code is going to turn out to be surprisingly useful later on. 
    Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, 
    a "Crypto 101" thing. But more people "know how" to break it than can actually break it, 
    and a similar technique breaks something much more important.
"""