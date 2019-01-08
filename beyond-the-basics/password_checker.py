password = 'hello'
user_try = input('Enter your password: ')
while user_try != password:
    print('That is wrong!')
    user_try = input('Please try again: ')
print('Welcome to the portal! 🚀')
