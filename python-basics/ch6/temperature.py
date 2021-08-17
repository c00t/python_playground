def convert_cel_to_far(cel):
    """Convert temperature from (Celsius) to (Fahrenheit)"""
    return cel * 9/5 + 32


def convert_far_to_cel(far):
    """Convert temperature from (Fahrenheit) to (Celsius)"""
    return (far - 32) * 5/9


far = input("Enter a temperature in degrees F:")
far = float(far)
print(f"{far} degrees F = {convert_far_to_cel(far):.2f} degrees C")

cel = input("Enter a temperature in degrees C:")
cel = float(cel)
print(f"{cel} degrees C = {convert_cel_to_far(cel):.2f} degrees F")
