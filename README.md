#Python-cryptanalysis

Python-cryptanalysis is a cool library.

##Code examples
Please note that these are basically the cryptopal challenges. If you want to solve those, don't look because there's spoilers here. But also, you should do it from scratch to learn more.
```python
#Given is a ciphertext encoded with a one-bit XOR. Find the correct key

from Cryptanalysis import *

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')
keys = []
for i in range(255):
	keys.append([chr(i)])

#This line opens the file War_and_Peace.txt, and does some sort af 4-gram analysis on them. Then we can use the probabilities file when we want to compare a text with the English language. The specific book is super long, so it's quite representative.
probabilities = fitness.ngram_logs(open('./TextSamples/en/War_and_Peace.txt').read(), 4)

#This function basically tries all the keys supplied, and returns the key with the highest fitness
real_key = fitness.get_highest_fitness(ciphertext, fitness.qgram_fitness, keys, xor.xor, probabilities)

print('The key is: ' + str(real_key))
print('And the plaintext message is: ' + xor.xor(ciphertext, real_key))

```
