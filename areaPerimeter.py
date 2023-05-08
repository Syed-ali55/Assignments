#Program to calculate area and perimeter of geometrical shapes"""

print("Calculator to find Area and Perimeter of the Geometrical shapes")

#"""Function to calculate area and perimeter of square"""


def square():

    side = float(input("enter side of the square\n"))
    area = side*side
    perimeter = (4)*side
    return area, perimeter

#"""Function to calculate area and perimeter of Rectangle"""


def rectangle():

    length = float(input("enter the length of rectangle"))
    breadth = float(input("enter the breadth of rectangle"))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

#"""Function to calculate area and perimeter of Rectangle"""


def triangle():
    base = float(input("enter the base of triangle"))
    height = float(input("enter the height of triangle"))
    side_a, side_b = float(input("enter the side_A and side_b of triangle"))
    area = (0.5) * (base * height)
    perimeter = 2 * int(side_a + side_b + base)
    return area, perimeter

def main():

   shape=input("enter the shape(Square\ Rectangle\ Triangle)")
    #print("1:Square\n 2:Rectangle\n 3:Triangle")
   if shape=="square":
      area, perimeter=square()
   elif shape=="rectangle":
      area, perimeter=rectangle()  
   elif shape=="triangle":
      area, perimeter=triangle() 
   else:
       print("invalid inputs")  
       return
   print(f"area of {shape} is {area}")
   print(f"perimeter of{shape} is {perimeter}") 
    
if __name__=="__main__":
    main()