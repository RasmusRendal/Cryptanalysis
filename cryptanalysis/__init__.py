import os, sys
sys.path.append(os.path.dirname(__file__))
import frequency
import fitness
import xor
import aes
import block_oracle
import substitution

__all__ = ["xor", "frequency", "fitness", "aes", "block_oracle", "substitution"]
