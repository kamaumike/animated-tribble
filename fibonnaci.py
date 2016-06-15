#get input from user and validate if the input is an integer
number = int(input("Enter a number: "))

#prints a list of fibonnaci numbers
def fibonacci(number):
	mylist = [0,1];
	for i in range(2,number):
		mylist.append(mylist[i-1] + mylist[i-2]);
		
	print("Your Fibonacci numbers are" , mylist)

#calling the fibonnaci function 	
fibonacci(number)