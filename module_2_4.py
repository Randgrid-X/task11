numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = numbers[1:]

list_simple_numbers = []
list_not_simple_numbers = []

j = 0
for j in range(len(numbers)):
    number = numbers[j]
    if number != 1:
        amount = 0
        i=0
        for i in range(number):
            if number%(i+2)==0:
                amount = amount + 1
            i = i + 1
        if amount==1:
            list_simple_numbers.append(number)
        else:
            list_not_simple_numbers.append(number)
    j = j + 1
print('Primes: ', list_simple_numbers)
print('Not primes: ', list_not_simple_numbers)
