import math

radius=float(input("Enter the radius of circle: "))


circumference=2*math.pi*radius
area=math.pi*pow(radius,2)

print(f"The circumference of circle is: {round(circumference,2)}  and the area is: {round(area,2)} cm^2")