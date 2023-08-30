def main():
    mass = float(input("Enter mass in kilograms): "))
    velocity = float(input("Enter velocity in m/s: "))
    ke = kinetic_energy(m=mass, v=velocity)
    print(f"The kinetic energy of the object is: {ke:.0f} Joule")
def kinetic_energy(m, v):
    # formula of kinetic energy
    ke = 0.5 * m * v**2
    return ke
main()



