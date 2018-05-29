def sphere_areae(r):
    return ((4/3)*(3.14)*(r**3))
radius=float(input("Enter radius of sphere: "))
print("Area of sphere with radius {} = {}".format(radius,sphere_area(radius)))
