'''
6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments. When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.
'''

mass = int(input("enter body mass in kg: "))
height = int(input("enter height in meter: "))

BMI = (mass / height)

print(f"Your Body Mass Index is: {BMI}")