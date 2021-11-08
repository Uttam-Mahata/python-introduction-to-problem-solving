"""Write a Python program to convert temperature in 
degree Celsius to degree Fahrenheit. If water boils 
at 100 degree C and freezes as 0 degree C, use the 
program to find out what is the boiling point and 
freezing point of water on the Fahrenheit scale"""
c = float(input("Enter the value of temperature in celcius scale : "))
f = float(((9*c)/5) + 32)
print('The value of temperature in ferenhite scale is :  ' , f)
