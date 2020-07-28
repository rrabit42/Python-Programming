pi = 3.141592653589793

def area_of_circle(radius):
    area = radius*radius*pi
    return area

def volumn_of_cylinder(radius,height):
    top_area = area_of_circle(radius)
    volumn = top_area*height
    return volumn

result = volumn_of_cylinder(5,10)
print(result)
