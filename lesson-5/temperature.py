def convert_cel_to_far(celsius):
    fahrenheit = round((celsius * 9 / 5 + 32), 2)
    print(f"{celsius} degrees C = {fahrenheit} degrees F")
def convert_far_to_cel(fahrenheit):
    celsius = round(((fahrenheit - 32) * 5 / 9), 2)
    print(f"{fahrenheit} degrees F = {celsius} degrees C")
fahrenheit = float(input("Enter a temperature in degrees F: "))
convert_far_to_cel(fahrenheit)
celsius = float(input("\nEnter a temperature in degrees C: "))
convert_cel_to_far(celsius)
