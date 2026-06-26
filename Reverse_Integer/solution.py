def reverse_integer(number):
    reverse = 0
    while number > 0:
        digit = number%10
        reverse = reverse * 10 + digit
        number = number // 10
    return reverse
print(reverse_integer(12334))