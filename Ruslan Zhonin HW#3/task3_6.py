#task6
email = input('enter your email: ')
if '@' in email:
    array_from_email = email.split('@')
    if array_from_email[1] == 'gmail.com':
        print(array_from_email[0])
    else:
        print('DOMAIN NAME is not supported')
else:
    print('You entered wrong value')