class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    # YOUR CODE HERE



    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    # YOUR CODE HERE



    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    # YOUR CODE HERE



    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    # YOUR CODE HERE
    
def__init__(self, width, height):
    self.width = width
    self.height = height 

#Done 

def __str__(self): 
    return "A rectangle with width ___ and height ___"

def verify_input(self):
    if self.width > 0 and self.height > 0:
        return True
    else:
        return False
 #this function calculates the area of the rectangle   
def area(self):
    if not self.verify_input():
        return "Invalid Input"
    else:
        return self.width * self.height
    #This function calculates the perimeter of the rectangle 
def perimeter(self):
    if not self.verify_input:
        return "Invalid Input"
    else:
        return (2 * self.width) + (2 * self.height)


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()