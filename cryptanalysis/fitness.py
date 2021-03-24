#!/usr/bin/env python3
"""Module for computing the fitness of strings

This module defines different ways to get the fitness of a candidate decryption.
In more primitive cryptography schemes, this can allow optimization algorithms
to find the decryption key.
"""
from __future__ import division
import frequency
import math
import inspect
import os


# The coeffecient of determination, or r^2
def ngram_logs(text, n):
    frequency_list, total_ngrams = frequency.count_ngrams(text, n)
    probabilities = {}
    for ngram in frequency_list.keys():
        probabilities[ngram] = math.log1p(frequency_list[ngram]/total_ngrams)
    probabilities['unknown'] = math.log1p(1/total_ngrams)
    return probabilities


# Gets the fitness based on the occurences of q-grams
def ngram_fitness(text, probs, n=4):
    fitness = 0
    qgrams = frequency.get_ngrams(text.upper(), n)
    for qgram in qgrams:
        if qgram in probs:
            fitness += probs[qgram]
        else:
            fitness += probs['unknown']
    return fitness


def get_probs(lang='en', n=4):
    return ngram_logs(get_texts(lang), n)


def get_texts(lang='en'):
    root_dir = os.path.dirname(os.path.dirname(
        __file__)) + '/TextSamples/' + lang + '/'
    cur_data = ""
    for text in os.listdir(root_dir):
        if text.endswith(".txt"):
            with open(root_dir + text, 'r') as data:
                cur_data += '\n' + data.read()
    return cur_data


# If you know the key, like a single-character XOR like in Cryptopals 1-3, this might be useful
def get_highest_fitness(text, keys, decode, fitness_func=ngram_fitness, probs=None):
    """Given an array of keys, find the most likely decryption.

    Args:
        text (c): The ciphertext you're trying to decode
        keys (list): The list of keys of type k
        decode (func): A function f: c, k -> m that decodes messages given a key
        fitness_func (func): A function f: m, p -> i that gives a fitness value to a plaintext
        prob (p): A data structure given as argument to the fitness function

    Returns:
        k: The best key

    Example:
        This example allows the user to get the best single-byte xor key::

            import cryptanalysis
            ciphertext = "7d7c3573677c707b71".decode('hex')
            keys = [chr(i) for i in range(255)]
            real_key = cryptanalysis.fitness.get_highest_fitness(ciphertext, keys, cryptanalysis.xor.xor)
            print(cryptanalysis.xor.xor(ciphertext, real_key))

    """
    if probs == None:
        probs = get_probs()

    highest_fitness = 0
    highest_key = ''
    for key in keys:
        p = decode(text, key)
        fitness = fitness_func(p, probs)
        if fitness > highest_fitness:
            highest_fitness = fitness
            highest_key = key
    return highest_key
