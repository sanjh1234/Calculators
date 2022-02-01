while True:

	try:
		num1 = int(input("""
Enter Your 1st Number OR 000 To Quit """))
	
		if num1 == 000 :
			quit()
	
		else:
			sign = input("""
To know sign directory type sign 
Enter Your Sign OR 000 to quit """)
			
			if sign == "000" :
				print("THANK YOU!")
				quit()

			elif sign == "sign":
				print("""To add : +
subtract : -
multiply : *
divide : /
to the power : ^
root : rt
reminder : rmdr
""")
				sign = input("Enter Your Sign OR 000 to quit ")
				if sign == "000" :
					print("THANK YOU!")
					quit()

				else:
					num2 = int(input("""
Enter Your 2nd Number OR 000 To Quit """))
					
					if num2 == 000 :
						print("THANK YOU!")
						quit()
					
					elif sign == "+":
						print(num1 + num2)
		
					elif sign == "*" :
						print(num1 * num2)
		
					elif sign == "/" :
						print(num1 /num2)
		
					elif sign == "-" :
						print(num1 - num2)
		
					elif sign == "^" :
						print(num1 ** num2)
		
					elif sign == "rt" :
						print(num1 ** 1/num2)
		
					elif sign == "rmdr" :
						print(num1 % num2)
		
					else:
						print("Sorry ! System dont recognise this sign")

			
			else:
				num2 = int(input("enter your 2nd number OR 000 to quit "))
				
				if num2 == 000 :
					quit()
				
				elif sign == "+":
					print(num1 + num2)
	
				elif sign == "*" :
					print(num1 * num2)
	
				elif sign == "/" :
					print(num1 /num2)
	
				elif sign == "-" :
					print(num1 - num2)
	
				elif sign == "^" :
					print(num1 ** num2)
	
				elif sign == "rt" :
					print(num1 ** 1/num2)
	
				elif sign == "rmdr" :
					print(num1 % num2)
	
				else:
					print("Sorry ! System dont recognise this sign")
	
	
	except ValueError :
		print("please enter valid characters")
