import sys

first_number = input("Input the 1st number: ")
if int(first_number) >= 10000:
    print("The computer couldn't read the number\nbecause it was too big")
    sys.exit()

second_number = input("Input the 2nd number: ")

sum = int(first_number) * int(second_number)

print("The answer is: " + str(sum))
