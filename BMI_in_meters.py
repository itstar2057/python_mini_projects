#Input from User
name = input("Enter your name? ")
height = float(input("Enter your height in meters? "))
weight = float(input("Enter your weight in Kg? "))

#Calculate BMI
def body_mass_index(height, weight):
    bmi = round(weight/height**2,2)
    return bmi

# call BMI Function

bmi = body_mass_index(height,weight)

#Condition
if bmi >= 18 and bmi <=25:
    print(f"{name} your BMI is = {bmi} and Normal.")
elif bmi < 18 and bmi > 16:
    print(f"{name} your BMI is = {bmi} and Under Weight.")
elif bmi < 16:
    print(f"{name} your BMI is = {bmi} and Severly Under Weight.")
elif bmi > 25 and bmi < 30:
    print(f"{name} your BMI is  = {bmi} and Over Weight.")
else:
    print(f"{name} your BMI is  = {bmi} and Obese.")