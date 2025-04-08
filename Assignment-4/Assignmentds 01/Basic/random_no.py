import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    
    values = []

    for i in range(10):
        value = random.randint(1, 100)
        values.append(value)
    print("Random number:", *values)
        



if __name__ == '__main__':
    main()