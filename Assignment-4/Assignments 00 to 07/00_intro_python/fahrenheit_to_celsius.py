

def main():
    temp_F : int = input("Enter the temperature in Fahrenheit to convert in Celsius : ")
    temp_F : float = float(temp_F)
    conv  = (temp_F - 32) * 5.0/9.0
    conv : float = float(conv)
    print(f"Temprature in Celsius is {conv}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()