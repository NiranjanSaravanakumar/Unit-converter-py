def kilometers_to_miles(kilometers):
    miles_conversion_factor = 0.621371
    miles = kilometers * miles_conversion_factor
    return miles

def miles_to_kilometers(miles):
    kilometers_conversion_factor = 1.60934
    kilometers = miles * kilometers_conversion_factor
    return kilometers

def main():
    print("Welcome to the Unit Converter!")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
    elif choice == 2:
        miles = float(input("Enter distance in miles: "))
        kilometers = miles_to_kilometers(miles)
        print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

