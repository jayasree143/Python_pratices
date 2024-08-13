from string import Template
# In string formatting with % operator python 2
name = 'Jaya'
age = 32
sen = "Hi %s" % name
print(sen)
# formatting with format() string method
print("hello we to python {}".format('world'))
# formatting with string literal, called f-string
central = 'python'
subject = 'programming'
place = 'the Testing Academy'
print(f"I am learning {central} {subject} from {place}.")
num1 = 42
num2 = 34
print(f"The first number is {num1} and The another number is {num2} the addition of two number is {num1+num2}")
num3 = 51
print(f"The number {num3} is even {True if num3 % 2 == 0 else False }")
number = 34.134566
formatting_number = f"{number:.5f}"
print(formatting_number)
# formatting with string template class
# definition :  In simpler terms python string template class allows us to create
# variable stings that can be updated with a value as per need.
# Note: The $(Dollar) sign is used to define the placeholder in Template string formatting.
from string import Template
template = Template('$name likes $sport')
values = {'name': 'Alice', 'sport': 'tennis'}
result = template.substitute(values)
print(result)

tem_obj = Template('$name1 and $age')
result_obj = tem_obj.substitute(
    {'name1': "Jayasree",'age': 32}
)
print(result_obj)

tem1_obj = Template('$name2 and $age2')
result_obj1 = tem1_obj.safe_substitute(
    {'name2': "Preethi",'age2': 21}
)
print(result_obj1)

# now we can see the difference between substitute and safe_substitute
# Create a template string object
# that acts as a placeholder
template_object = Template('$greetings! You are at $platform.')


# Substitute values of
# platform in above template object
# using safe_substitute() method
formatted_string_1=template_object.safe_substitute(
    {'platform' : "Naukri E-learning"}
    )
print(formatted_string_1)

# Substitute values of
# platform in above template object
# using substitute() method
formatted_string_2=template_object.substitute(
    {'platform' : "Naukri E-learning"}
    )
print(formatted_string_2)
# $greetings! You are at Naukri E-learning.
# Traceback (most recent call last):
#   File "0d655531-4f1f-4220-8f81-9ee563826234.py", line 21, in <module>
#     {'platform' : "Naukri E-learning"}
#   File "/usr/local/lib/python3.7/string.py", line 132, in substitute
#     return self.pattern.sub(convert, self.template)
#   File "/usr/local/lib/python3.7/string.py", line 125, in convert
#     return str(mapping[named])
# KeyError: 'greetings'
# As you can observe in the above output, we have not provided the value of
# placeholder $greetings. In the case of safe_substitute() method, the placeholder
# is set to the template string itself as the default value and prints out the
# output, whereas in the case of the substitute () method, it raises a keyError.
