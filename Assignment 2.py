# Q.writa a program to find the prime number Enter a number to program and get the output "prime" or "Not prime"

num = 5
# prime numbers are greater than 1
if num>1:
	# check for factors
	for i in range(2 ,num):
		if (num% i )==0:
			print(num,"is not a prime number")
			break
	else:
				print(num,"is a prime number")
# if input number is less than or equal to1,it is not prime
else:
	print(num,"is not a prime number")

