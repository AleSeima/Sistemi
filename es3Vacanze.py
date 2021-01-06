
def fibonacci(k):
    if k == 0:
        return 0
    else:
        if(k==1):
            return 1
        else:
            return fibonacci(k-1) + fibonacci(k-2)


for k in range (20):
    print(fibonacci(k))