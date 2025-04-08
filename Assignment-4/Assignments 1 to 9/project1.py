# Mad Libs Python Project

def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create your own fun story.")

    # Getting user inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")

    # Story template
    story = f"""
    One day, {name} went to {place}. There, they saw a very {adjective} {animal}.
    It was {verb} around a {noun}. {name} couldn't believe their eyes!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    mad_libs()