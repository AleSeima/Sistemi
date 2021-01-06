import random
import string
MAX = 65
MIN = 122
DIM_MIN = 8
DIM_MAX = 20
n = 20

if n == 8:
    
    password = ''.join(random.choice(string.ascii_letters)for k in range (DIM_MIN))
    
else:
        password = ''.join(random.choice(string.ascii_letters + string.octdigits)for k in range (DIM_MAX))

print(password)

