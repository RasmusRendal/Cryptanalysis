#!/usr/bin/env python3
"""This module contains functions for working with substitution ciphers.
It allows for automatically solving monoalphabetic substitution ciphers.
"""
import fitness
import frequency
from typing import Callable
from random import randint

def hill_climb(ciphertext: str, decrypt: Callable[[str, dict], str], key: dict, max_failures: int = 10000):
    """Basic hill climb based on randomly permuting a key

    Args:
        ciphertext: A input ciphertext
        decrypt: A function that decrypts the ciphertext
        key: An initial key
        max_failures: The amount of permutations to try before assuming we've reached a maxima
    """
    probs = fitness.get_probs()
    cur_fitness = fitness.ngram_fitness(decrypt(ciphertext, key), probs)
    failures = 0
    attempted_mixes = []
    while failures < max_failures:
        rand1 = list(key.keys())[randint(0, len(key)-1)]
        rand2 = list(key.keys())[randint(0, len(key)-1)]
        mix = (rand1, rand2)
        if mix not in attempted_mixes:
            key2 = dict(key)
            key2[rand1] = key[rand2]
            key2[rand2] = key[rand1]
            new_fitness = fitness.ngram_fitness(
                decrypt(ciphertext, key2), probs)
            if new_fitness > cur_fitness:
                cur_fitness = new_fitness
                key = key2
                failures = 0
        failures += 1
    return key


def substitution_decode(ciphertext: str, key: dict):
    """Using a key, decode a substitution cipher

    Case is ignored, to the extent that the function assumes that
    upper-case ciphertext characters are always decoded to upper-case
    plaintext characters. Any ciphertext character not in the key does
    not get decoded

    Args:
        ciphertext: The ciphertext
        key: A dictionary with keys as values and decryptions as values"""
    output_text = ""
    for c in ciphertext:
        try:
            if c.islower():
                output_text += key[c.upper()].lower()
            else:
                output_text += key[c.upper()]
        except:
            output_text += c
    return output_text


def substitution_solve(ciphertext: str, lang: str = 'en', max_failures: int = 1000):
    """Using hillclimbing, solve a monoalphabetic substitution cipher

    The hillclimbing optimizes for the probability of 4-grams in the text.

    Args:
        ciphertext: The ciphertext to decode
        lang: The language the ciphertext is in
        max_failures: The amount of permutations to try before assuming we've reached a maxima"""
    qprobs = fitness.get_probs(lang=lang)
    sfreq = frequency.count_occurences(
        frequency.get_ngrams(fitness.get_texts(lang), 1))
    freq = frequency.count_occurences(frequency.get_ngrams(ciphertext, 1))

    sfreq_sorted = sorted(sfreq.items(), key=lambda t: -t[1])
    freq_sorted = sorted(freq.items(), key=lambda t: -t[1])

    key = {}
    for i in range(len(freq_sorted)):
        key[freq_sorted[i][0]] = sfreq_sorted[i][0]

    key = hill_climb(ciphertext, substitution_decode, key, max_failures)

    return (substitution_decode(ciphertext, key), key)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Decrypt substitution ciphers")
    parser.add_argument('--file', dest='file')
    args = parser.parse_args()
    with open(args.file, 'r') as ciphertext:
        print(substitution_solve(ciphertext.read()))


