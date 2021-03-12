"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Above 35 they are clinically obese.
- Over 30 but below 35 they are obese

https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
"""
#
# main
#
if __name__ == "__main__":
    # 🚨 Don't change the code below 👇
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    bmi = round(weight / (height * height))
    # Underweight
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    # Normal weight
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    # Slightly overweight
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    # Obese
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    # Clinically obese
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")