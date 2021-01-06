import random
import string
NUM_MAX = 9
NUM_MIN = 0
LETTERA_MIN = 65
LETTERA_MAX = 70
N_CAR = 12
password = ""

for j in range (6):
    password = password + ''.join(random.choice(string.hexdigits)for k in range (2)) + ':'

print(password)
