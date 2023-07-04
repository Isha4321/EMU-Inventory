text = "My name is {} and I am from {}"
name="Isha"
state = "Uttar Pradesh"
text = f"My name is {name} and I am from {state}"
print(text)
letter = "the price of tomato is {}"
price = 129.789
letter = f"the price of tomato is {price:.2f}"
print(letter)

# text = "My name is {0} and I am from {1}"
# name="Isha"
# state = "Uttar Pradesh"
# print(text.format(name,state))

text = "My name is {{}} and I am from {{}}"
print(text)
