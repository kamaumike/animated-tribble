#get input from user and validate if the input is an integer
my_number = int(input("Enter a number: "))

#checks if a number is prime and prints the prime numbers
def prime_numbers(my_number):
	for n in range(my_number + 1):
	   # check if a number is greater than 1
	   if n > 1:
	       for i in range(2,n):
	           if (n % i) == 0:
	               break
	       else:
	           print(n)
	           
#calling the prime_number function	           
prime_numbers(my_number)	