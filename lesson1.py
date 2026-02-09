['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890'].

def format_phone_number(number):
    number.replace('-', '')

formatted_numbers = map()