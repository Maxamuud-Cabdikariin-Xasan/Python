# This  program asks the user to enter a distance in kilometers, then converts that
# distance to miles.
# The conversion formula is as follows:
# Miles 5 Kilometers 3 0.6214


# create main function

CONVERTION_RATE = 0.6214 # named constant
def main():
    distance_km = float(input("Enter Distance In KM: "))
    km_mile(distance_km)

# create km_mile (kilo_meter):

# create km function

def km_mile(kilo_meter):
    mile = kilo_meter * CONVERTION_RATE
    print(f'{kilo_meter}KM is equal to {mile:.2f} Mile')


# create main function
main()



