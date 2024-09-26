#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

#Student Name: Katherine Tucker   
#Program Title: IT Programming 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    print("Welcome to your bill calculator :) ")

    billStart = input("Please enter your bill amount")

    billTax = (int(billStart) * 0.15)

    billTip = (int(billStart) * 0.20)

    billTotal = (int(billStart) + billTip + billTax)

    print ("Your original bill amount is:{0}".format(billStart))
    print ("Your tax is: {0:.2f}".format(billTax))
    print ("Your tip is: {0:.2f}".format(billTip))
    print ("Your total is {0:.2f}".format(billTotal))
 
    # YOUR CODE ENDS HERE

main()