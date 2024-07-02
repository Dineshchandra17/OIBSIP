def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                raise ValueError
            return weight, height
        except ValueError:
            print("Please enter valid positive numbers for weight and height.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")

if __name__ == "__main__":
    main()