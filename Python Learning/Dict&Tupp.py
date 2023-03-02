# Stock Prices Dictionary

StockP= {
    "info":   [600,630,620],
    "ril":    [1430,1490,1567],
    "mtl":    [234,180,160],
}

# Functions
# For printing the stock prices
def printing(dict):
    c=0
    for i in dict:
        # Using List Comprehension
        print(i,"-->",      
        list(dict.values())[c],
        "--> Avg: ",
        round(sum([
            i for i in list(dict.values())[c]])/
            len([i for i in list(dict.values())[c]]),4
            ))
        c+=1

def insert(stk,pri):
    if stk in StockP:
        StockP[stk].append(pri)
    else:
        StockP[stk]= []
        StockP[stk].append(pri)


# Driver Code

print("""
Press Enter to Add/Update in the List 
---------------------------------------""")
printing(StockP)

stock = input("Enter the stock name")
price = int(input('Enter the price'))

insert(stock,price)

print("""
New Prices in the List 
---------------------------------------""")
printing(StockP)