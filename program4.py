numbers = [1,2,8,9,12,46,76,82,15,20,30]

result = {}

for i in range(1, 10):      # numbers 1 to 9
    count = 0
    for n in numbers:       # check each number in list
        if n % i == 0:      # divisible condition
            count += 1
    result[i] = count       # store result

print(result)

    