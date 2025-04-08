# Prompt the user to enter the lengths of each side of a triangle 
#and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def main():
    num_1 : float = float (input("What is the length of side 1 ? "))
    num_2 : float = float (input("What is the length of side 2 ? "))
    num_3 : float = float (input("What is the length of side 3 ? "))
    print("The perimeter of the triangle is " + str(num_1+num_2+num_3))

if __name__ == '__main__':
    main()