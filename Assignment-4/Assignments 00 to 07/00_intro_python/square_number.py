# PROBLEM STATEMENT :
#Ask the user for a number and print its square (the product of the number times itself).

# SOLUTION :

def main():
    num: float = float(input("Type a number to see its square: "))
    result: float = float (num ** num)
    print(str(num) + " squared is " + str(result))
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

