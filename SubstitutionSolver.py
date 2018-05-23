#!/usr/bin/python

english_2words = ['OF', 'TO', 'IN', 'IS', 'IT']
english_3words = ['THE', 'AND', 'FOR', 'WAS', 'HIS']
double_letters = ['L', 'E', 'S', 'O', 'T']

def sort_dict(to_sort):
    return sorted(to_sort.keys(), key=lambda k: to_sort[k], reverse=True)

def get_doubles(text):
    doubles = {}
    for word in text.split(' '):
        last_char = ''
        for c in word:
            if c == last_char:
                if c in doubles:
                    doubles[c] += 1
                else:
                    doubles[c] = 1
            last_char = c
    return doubles


def get_best_key(*arg):
    best_key = {}
    best_key_fitness = 0
    text = arg[0]
    for key in arg[1:]:
        key_fitness = text_fitness(decrypt_text(text, key))
        if key_fitness > best_key_fitness:
            best_key = key
            best_key_fitness = key_fitness
    return best_key



def make_freq_key(text):
    frequency, total = count_occurences(text)
    freq_sorted = sort_dict(frequency)
    english_sorted = sort_dict(english_frequency)
    key = {}
    for i in range(min(len(freq_sorted), len(english_sorted))):
        key[freq_sorted[i]] = english_sorted[i]
    return key


#Depend on the dictionary
def make_dict_key(text):
    doubles = get_doubles(text)
    sorted_doubles = sort_dict(doubles)
    print(doubles)
    key = {}
    for i in range(min(len(double_letters), len(sorted_doubles))):
        key[sorted_doubles[i]] = double_letters[i]
    return key



def decode_text(text):
    print("Decrypted text:")
    freq_key = make_freq_key(text)
    dict_key = make_dict_key(text)
    key = get_best_key(text, dict_key)
    decrypted_text = decrypt_text(text, key)
    print(decrypted_text)
    print("Key: ")
    print(''.join(key.keys()))
    print(''.join(key.values()))


def decrypt_text(text, key):
    decrypted_text = ''
    for c in text:
        if c in key:
            decrypted_text += key[c]
        elif c == ' ':
            decrypted_text += ' '
        else:
            decrypted_text += '?'
    return decrypted_text


def text_fitness(text):
    fitness = 0
    for word in english_2words + english_3words:
        fitness += text.count(word)
    return fitness/len(text)

def count_word_occurences(text):
    word_occurences = {}
    for word in text.split(' '):
        if word in word_occurences:
            word_occurences[word] += 1
        else:
            word_occurences[word] = 1


def len_word_occurences(word_occurences, length):
    to_return = {}
    for word in word_occurences:
        if len(word) == length:
            to_return.append(word)
    return to_return

