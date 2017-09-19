# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

def name_from_email(email_address):
    at_sign = email_address.index('@')
    name_part = email_address[ : at_sign]
    dot_position = name_part.index('.')
    first_name = name_part[ : dot_position]
    last_name = name_part[dot_position + 1 : ]
    capitalized_format = last_name.capitalize() + ' ' + first_name.capitalize()
    return capitalized_format


print(name_from_email("elek.viz@exam.com"))

