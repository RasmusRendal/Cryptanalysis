from __future__ import division
import fitness
from random import randint

def hill_climb(ciphertext, decrypt, key, max_successes=50):
    probs = fitness.get_probs()
    cur_fitness = fitness.ngram_fitness(decrypt(ciphertext, key), probs)
    failures = 0
    successes = 0
    attempted_mixes = []
    while failures < 1000 and successes < max_successes:
        rand1 = list(key.keys())[randint(0, len(key)-1)]
        rand2 = list(key.keys())[randint(0, len(key)-1)]
        mix = (rand1, rand2)
        if mix not in attempted_mixes:
            key2 = dict(key)
            key2[rand1] = key[rand2]
            key2[rand2] = key[rand1]
            new_fitness = fitness.ngram_fitness(decrypt(ciphertext, key2), probs)
            if new_fitness > cur_fitness:
                cur_fitness = new_fitness
                key = key2
                failures = 0
                successes += 1
        failures += 1
    print("Final fitness: " + str(cur_fitness))
    print("Failures: " + str(failures))
    print("Successes: " + str(successes))
    return key
