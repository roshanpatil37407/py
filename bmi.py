def calculate_bmi(weight, height):
    try:
        # Convert height to meters if provided in centimeters
        if height > 10:  # Assuming height is in cm if it's above 10
            height = height / 100  # Convert to meters

        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."
    except Exception as e:
        return f"An error occurred: {e}"

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters or cm: "))

        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)  # Error message if any
        else:
            category = get_bmi_category(bmi)
            print(f"Your BMI is: {bmi}")
            print(f"Your BMI category is: {category}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()
