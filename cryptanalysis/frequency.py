#!/usr/bin/env python3
# Frequency analysis tool by Rasmus Rendal

import argparse
import crypt_args
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


def count_occurences(text):
    frequency_list = {}
    for c in text:
        if c in frequency_list:
            frequency_list[c] += 1
        else:
            frequency_list[c] = 1
    return frequency_list


def get_ngrams(text, n):
    text = text.upper()
    ngrams = []
    for c in range(len(text)-n+1):
        ngram = text[c:c+n]
        if ngram.isalpha():
            ngrams.append(ngram)
    return ngrams


# Counts n-grams
# Only does alpha characters, and does not care about case.
def count_ngrams(text, n):
    frequency_list = {}
    total_ngrams = 0
    ngrams = get_ngrams(text, n)
    for ngram in ngrams:
        if ngram in frequency_list:
            frequency_list[ngram] += 1
        else:
            frequency_list[ngram] = 1
    return (frequency_list, len(ngrams))


def count_total(frequency_list, to_count):
    total = 0
    for i in to_count:
        if i in frequency_list:
            total += frequency_list[i]
    return total


def print_table(frequencies, sort):
    print("| Char | Frequency | English Frequency | English Char |")
    print("-------------------------------------------------------")
    if not args.sort:
        keys = list(frequencies.keys())
        english_keys = list(english_frequency.keys())
    else:
        keys = crypt_common.sort_dict(frequencies)
        english_keys = crypt_common.sort_dict(english_frequency)
    m = len(keys)
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
        print('| ' + c + '    |   ' + freq_str + '% |           ' +
              efreq_str + '% |            ' + english_c + ' |')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Count the frequency of characters in a text file')
    parser = crypt_args.add_parser_args(parser)
    parser.add_argument('--sort', dest='sort', action='store_true',
                        help="Sort the letters by frequency, instead of alphabetically")
    parser.add_argument('--ic', dest='ic', action='store_true',
                        help='Calculate the index of coincidence')

    args = parser.parse_args()
    text = crypt_args.get_text(args)

    frequency_list = count_occurences(text)

    per_list = {}
    for c in frequency_list:
        per_list[c] = frequency_list[c]/len(text)

    if args.ic:
        phi_o = 0
        for n in range(ord('A'), ord('Z')):
            c = chr(n)
            if c in frequency_list:
                phi_o += (frequency_list[c]/len(text)) * \
                    ((frequency_list[c]-1)/(len(text)-1))
        print("Index of Coincidence: " + str(phi_o))
        print("Common IC's:")
        print("English plaintext: 0.066")
        print("Vigenere Cipher: 0.042")
    else:
        print_table(frequency_list, args.sort)
