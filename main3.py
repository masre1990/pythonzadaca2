print("This is km to mile converter")

while True:
    print("Please enter the number of km you would like to convert:")
    km = input("Kilometers: ")

    km = float(km.replace(",", "."))

    miles = km * 0.621371

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print("Thank you for using km2mile converter")
        break