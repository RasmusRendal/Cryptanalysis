# Python-cryptanalysis
Python-cryptanalysis is a library for solving cryptography challenges.
It is mostly designed for use in CTFs, and is therefore very forgiving with the input you give it in many functions.

## Code examples
Please note that these are basically the cryptopal challenges. If you want to solve those, don't look because there's spoilers here. But also, you should do it from scratch to learn more.
```python
# Gives in is a ciphertext as a XOR. Find the correct key

from Cryptanalysis import *

ciphertext = open('text.txt').read()

key = xor.break_repeating_xor(ciphertext)

print("The key is: " + key)
print("Message:")
print(xor.xor(ciphertext, key))

```
