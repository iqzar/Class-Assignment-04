# Problem Statement
#Write a program that prints out the calls for a spaceship
#that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Solution :

def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(10 , 0 , -1):
        print (i)  # Use the 'i' value inside the for-loop
    print ("Liftoff!")
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()