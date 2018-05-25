#!/usr/bin/python
#Frequency analysis tool by Rasmus Rendal

import argparse
import re

english_frequency = {
        'A': 8.167,
        'B': 1.492,
        'C': 2.782,
        'D': 4.253,
        'E': 12.702,
        'F': 2.228,
        'G': 2.015,
        'H': 6.094,
        'I': 6.966,
        'J': 0.153,
        'K': 0.772,
        'L': 4.025,
        'M': 2.406,
        'N': 6.749,
        'O': 7.507,
        'P': 1.929,
        'Q': 0.095,
        'R': 5.987,
        'S': 6.327,
        'T': 9.056,
        'U': 2.758,
        'V': 0.978,
        'W': 2.360,
        'X': 0.150,
        'Y': 1.974,
        'Z': 0.074
}


def sort_dict(to_sort):
    return sorted(to_sort.keys(), key=lambda k: to_sort[k], reverse=True)


def count_occurences(text):
    frequency_list = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0,
            'H': 0,
            'I': 0,
            'J': 0,
            'K': 0,
            'L': 0,
            'M': 0,
            'N': 0,
            'O': 0,
            'P': 0,
            'Q': 0,
            'R': 0,
            'S': 0,
            'T': 0,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0,
    }
    regex = re.compile('[^a-zA-Z ]')
    text = regex.sub('', text)
    text = text.upper()

    total_occurences = 0
    for c in text:
        if c in frequency_list:
            frequency_list[c] += 1
        if c is not ' ':
            total_occurences += 1
    return (frequency_list, total_occurences)


def print_table(frequencies, sort):
    print("| Char | Frequency | English Frequency | English Char |")
    print("-------------------------------------------------------")
    if not args.sort:
        keys = list(frequencies.keys())
        english_keys = list(english_frequency.keys())
    else:
        keys = sort_dict(frequencies)
        english_keys = sort_dict(english_frequency)
    m = len(keys)
    print(keys)
    print(len(keys))
    if m > 26:
        m = 26
    for n in range(m):
        c = keys[n]
        english_c = english_keys[n]
        freq = 0
        if c in per_list:
            freq += per_list[c]*100
        if chr(ord(c)+32) in per_list:
            freq += per_list[chr(n+32)]*100
        freq_str = str(freq)[:5]
        freq_str += "0"*(6-len(freq_str))
        efreq_str = str(english_frequency[english_c])[:5]
        efreq_str += "0"*(6-len(efreq_str))
        print('| ' + c + '    |   ' + freq_str + '% |           ' + efreq_str + '% |            ' + english_c + ' |')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the frequency of characters in a text file')
    parser.add_argument('text', metavar='Text', nargs='*',
                        help='The text to parse')
    parser.add_argument('--file', dest='file', nargs=1,
                        help='Read text from file')
    parser.add_argument('--sort', dest='sort', action='store_true',
                        help="Sort the letters by frequency, instead of alphabetically")
    parser.add_argument('--ic', dest='ic', action='store_true',
                        help='Calculate the index of coincidence')

    args = parser.parse_args()
    text = ""
    if args.text:
        text = ' '.join(args.text)
    elif args.file:
        with open(args.file[0], 'r') as myfile:
            text=myfile.read().replace('\n', '')
    else:
        raise Exception('No text given')


    frequency_list, total_occurences = count_occurences(text)


    per_list = {}
    for c in frequency_list:
        per_list[c] = frequency_list[c]/total_occurences

    if args.ic:
        phi_o = 0
        for n in range(ord('A'), ord('Z')):
            c = chr(n)
            if c in frequency_list:
                phi_o += (frequency_list[c]/total_occurences)*((frequency_list[c]-1)/(total_occurences-1))
        print("Index of Coincidence: " + str(phi_o))
        print("Common IC's:")
        print("English plaintext ≈ 0.066")
        print("Vigenere Cipher ≈ 0.042")
    else:
        print_table(frequency_list, args.sort)
