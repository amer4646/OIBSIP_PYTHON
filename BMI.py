#BMI CALCULATOR

#input from the users for height and weight
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  

#Body Mass Index(BMI) formula  
BMI = weight / (height/100)**2  

# BMI value
print("Your Body Mass Index is:",BMI)

# using the if-elif-else conditions  
if BMI <= 18.5:  
    print("You are underweight.")  
elif BMI <= 24.9:  
    print("You are normal.")  
elif BMI <= 29.9:  
    print("You are overweight.")  
else:  
    print("You are obese.")  
