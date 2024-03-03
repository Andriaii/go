
number =int(input("please type 1 numbers :"))
number2 = int(input("please type another number "))
result = 0

for number in range(number , number2 + 1):
    result = result + number
    print(number)
print(result)