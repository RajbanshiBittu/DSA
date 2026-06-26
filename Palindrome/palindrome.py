def check_palindrome(number):
    num = number
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if reverse == number:
        return True
print(check_palindrome(1223221))