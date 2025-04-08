def main():

    while True:

        curr_val = int(input("Enter your number : "))

        while curr_val < 100:
            curr_val = curr_val ** 2
            print(f"Douled value is : {curr_val}")

if __name__ == "__main__":
    main()