"""
The volume of a sphere with radius r is 4/3πr3. Write 
a Python program to find the volume of spheres with 
radius 7cm, 12cm, 16cm, respectively.
"""
pi = 22/7
print("In this program we will find the volume for sphere with radii 7 cm, 12 cm, 16 cm respectively...")
r = float(input("Enter the radius of sphere(in cm) : "))
volume_one = float((4/3)*(22/7)*(7)**3)
volume_two = float((4/3)*(22/7)*(12)**3)
volume_three = float((4/3)*(22/7)*(16)**3)

if r == 7 :
  print("The volume of the sphere will be : ", volume_one)
elif r == 12:
  print("The volume of the sphere will be :  ", volume_two)
else :
  print("The volume of the sphere will be :  ", volume_three)
    
