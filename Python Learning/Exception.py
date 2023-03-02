x = input("Enter num1 ")
y= input('Enter num2 ')
try:
    z= x/int(y)
except Exception as e:
    print('Exception is ', type(e).__name__)
    z = None
print("Division is: ",z) 