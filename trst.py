number = int(input("Give me a number: "))
numberIsOdd = number%2
print(numberIsOdd)
numberMultipleOf4 = number%4


if numberIsOdd > 0:
    print("odd")
else:
    print("even")

#f numberIsOdd == 0 and numberMultipleOf4 == 0:
#	print("Your number " + str(number) + " is even and a multiple of four.")
#	if numberIsOdd > 0 and numberMultipleOf4 is False:
#		print("Your number " + str(number) + " is even.")
#	else:
#		print()
#lse:
#	print("Your number " + str(number) + " is odd.")