from django import template
import num2words

register=template.Library()

# Turn first five letter of the words to uppercase
def first_five_upper(value):
    result = value[:5].upper()
    return result

# Turn as many letters of the words as you want to uppercase
def first_n_upper(value, n):
    result = value[:n].upper()
    return result

# Checking the length of the words
def length_limit(value,limit):
    if len(value) > limit:
        return value[0:limit] + '....'
    else:
        return value

# Rating
def rating(value):
    if(float(value) >= 4):
        return value + "[Excellent]"
    elif (float(value) >= 3):
        return value + "[Very Good]"
    elif (float(value) >= 1.5):
        return value + "[Average]"
    else:
        return value + "[Poor]"
  


# Converting numbers to words
def conver_number_to_words(value):
    return num2words(value)


register.filter('firstfiveupper', first_five_upper)
register.filter('firstnupper', first_n_upper)
register.filter('lengthlimit', length_limit)
register.filter('rating', rating)
register.filter('convertnumbertowords', conver_number_to_words)