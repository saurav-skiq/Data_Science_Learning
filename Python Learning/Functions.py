

# Functions
# ----------------
# Function to find area of a triangele

def tarea(height, base, type):
    if type == 1:
        return(0.5*height*base)
    else:
        return(height*base)


# Driver Codes
# -------------------
# Area of a triangele
print("Program to find the area of a Triangle/ Rectangle")
ty=int(input("Enter 1 for triangle (By default it is Rectangle)"))
heig= int(input("Enter the Height of the Triangle: "))
bas= int(input("Enter the Base of the Triangle: "))
print(tarea(heig,bas,type=ty))