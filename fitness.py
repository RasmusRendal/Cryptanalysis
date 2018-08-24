from __future__ import division
import frequency
import math
import inspect
import os


#The coeffecient of determination, or r^2
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
    qgrams = frequency.get_ngrams(text, n)
    for qgram in qgrams:
        if qgram in probs:
            fitness += probs[qgram]
        else:
            fitness += probs['unknown']
    return fitness


def get_probs(lang='en', n=4):
    cur_data = ""
    root_dir = os.path.dirname(inspect.getfile(frequency)) + '/TextSamples/' + lang + '/'
    for text in os.listdir(root_dir):
        if text.endswith(".txt"):
            with open(root_dir + text, 'r') as data:
                cur_data += '\n' + data.read()
    return ngram_logs(cur_data, n)



#If you know the key, like a single-character XOR like in Cryptopals 1-3, this might be useful
def get_highest_fitness(text, keys, decode, fitness_func=ngram_fitness, probs=None):
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
