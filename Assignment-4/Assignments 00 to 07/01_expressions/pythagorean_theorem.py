#Problem Statement

#Write a program that asks the user for the lengths of the two perpendicular sides of a 
#right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# Solution :

import math 

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))


if __name__ == '__main__':
    main()