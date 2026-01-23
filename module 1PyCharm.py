# 4.1 Capitalize the word starting with m:
song = """When an eel grabs your arm,      
... And it causes great harm,
... That's - a moray!\n"""

song = song.replace("moray", "Moray")
print(song)


# 4.2 Write the following poem by using old-style formatting.
# Substitute the strings roast "beef", "ham", "head", and "clam" into this string:

b='beef'
ha ='ham'
he = 'head'
c ='clam'

print(f"My kitty cat likes {b},")
print(f"My kitty cat likes {ha},")
print(f"My kitty cat fell on his {he},")
print(f"And now thinks he's a {c}\n")

# 4.3 Write a form letter by using new-style formatting.
# Save the following string as letter (you’ll use it in the next exercise):

letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and amount for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}\n
"""
# 4.4 Assign values to variable strings named salutation,
# name, product, verbed (past tense verb), room, animals, amount
# percent, spokesman, and job_title. Print letter with these values, using letter.format().

salutation = "Ms"
name = "Azevedo"
product = "sweater"
verbed = "shrunk"
room = "dryer"
animals = "cats"
percent = "30"
spokesman = "Alex McKinstry"
job_title = "Customer Service Manager"

letter = f"""Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and amount for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}\n
"""

print(letter)

# 4.5 After public polls to name things, a pattern emerged: an English submarine (Boaty McBoatface),
# an Australian racehorse (Horsey McHorseface), and a Swedish train (Trainy McTrainface).
# Use % formatting to print the winning name at the state fair for a prize duck, gourd, and spitz.

story = """After public polls to name things, a pattern emerged: 
an English submarine (Boaty McBoatface), 
an Australian racehorse (Horsey McHorseface), 
and a Swedish train (Trainy McTrainface).\n"""

winner_1 = "Duck"
winner_2 = "Gourd"
winner_3 =  "Spitz"

print(story)
print("The winners are: ")
print(f"{winner_1}y, Mc{winner_1}face")
print(f"{winner_2}y, Mc{winner_2}face")
print(f"{winner_3}y, Mc{winner_3}face")





