def calculate_armstrong_sum(number):
    armstrong_sum = 0
    digit_count = 0

    temp_number = number
    while temp_number > 0:
        digit_count += 1
        temp_number //= 10

    temp_number = number
    for digit in range(1, temp_number + 1):
        last_digit = temp_number % 10
        armstrong_sum += (last_digit ** digit_count)
        temp_number //= 10
    return armstrong_sum

user_input = int(input("Please Enter the Number to Check for Armstrong: "))

if user_input == calculate_armstrong_sum(user_input):
    print("%d is an Armstrong Number." % user_input)
else:
    print("%d is Not an Armstrong Number." % user_input)
