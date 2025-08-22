F_to_C_factor = 5/9
C_to_F_factor = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * F_to_C_factor


def convert_to_fahrenheit(celsius):
    return (celsius * C_to_F_factor) + 32

if __name__ == "__main__":
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

