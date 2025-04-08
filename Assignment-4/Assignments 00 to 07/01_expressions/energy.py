# Problem Statement :

# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

#E = m * c**2

C: int = 299792458

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)


    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")


if __name__ == '__main__':
    main()