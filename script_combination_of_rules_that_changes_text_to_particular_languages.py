# For refrence https://www.fosslinux.com/46256/python-script-examples.htm

#latin_translator.py

#request user for input
user_input = input("Input text to translate to pig latin: ")
print("User Text: ", user_input)

#This step breaks the words into a list
updated_user_input = user_input.split(' ')

for j in updated_user_input:
 if len(j) >= 3: #only translate words with more than 3 characters
  j = j + "%say" % (j[0]) 
  j = j[1:]
  print(j)
else:
    pass




# To execute latin_translator.py from the terminal, type the following code.
# python3 latin_translator.py

