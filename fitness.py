import frequency
import math


#The coeffecient of determination, or r^2
def ngram_logs(text, n):
    frequency_list, total_ngrams = frequency.count_ngrams(text, n)
    probabilities = {}
    for ngram in frequency_list.keys():
        probabilities[ngram] = -math.log(total_ngrams/frequency_list[ngram])
    probabilities['unknown'] = math.log(total_ngrams/1)
    return probabilities


def qgram_fitness(text, probs):
    fitness = 0
    qgrams = frequency.get_ngrams(text, 4)
    for qgram in qgrams:
        if qgram in probs:
            fitness += probs[qgram]
        else:
            fitness += probs['unknown']
    return fitness


#If you know the key, like a single-character XOR like in Cryptopals 1-3, this might be useful
def get_highest_fitness(text, fitness_func, keys, decode, probs):
    highest_fitness = 100000
    highest_key = ''
    for key in keys:
        p = decode(text, key)
        fitness = fitness_func(p, probs)
        if fitness < highest_fitness:
            highest_fitness = fitness
            highest_key = key
    return highest_key
