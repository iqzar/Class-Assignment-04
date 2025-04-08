# Problem Statement

#Write a program which prompts the user for an adjective, then a noun, 
#then a verb, and then prints a fun sentence with those words!

# Solution :

SENTENCE_START: str = "Learning Python is exciting. Today, I created an " 

def main():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " that"+ " " + verb + "!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()