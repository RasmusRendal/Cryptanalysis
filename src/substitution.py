import fitness
import frequency
from hillclimb import hill_climb


def substitution_decode(ciphertext, key):
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


#Solves monoalphabetic substitution ciphers
def substitution_solve(ciphertext, lang='en', max_successes=50):
    qprobs = fitness.get_probs(lang=lang)
    sfreq = frequency.count_occurences(frequency.get_ngrams(fitness.get_texts(lang), 1))
    freq = frequency.count_occurences(frequency.get_ngrams(ciphertext, 1))

    sfreq_sorted = sorted(sfreq.items(), key=lambda t: -t[1])
    freq_sorted = sorted(freq.items(), key=lambda t: -t[1])

    key = {}
    for i in range(len(freq_sorted)):
        key[freq_sorted[i][0]] = sfreq_sorted[i][0]

    key = hill_climb(ciphertext, substitution_decode, key, max_successes)

    return (substitution_decode(ciphertext, key), key)
