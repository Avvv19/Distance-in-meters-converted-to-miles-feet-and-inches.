
def capital_vowels(string):
#created a list
 vowels = 'aeiou'

 modify_string = ""
 
#looping
 for character in string :
    if character.lower() in vowels :
      modify_string += character.upper()
    else:
      modify_string += character
 return modify_string
#user input
user_input = input("enter a string: ")

#Display length of string
print("The string is ", len(user_input), "characters long")

#capitalize all the vowels and display the modified string
modify_string = capital_vowels(user_input)
print("Modify string:", modify_string)

#Displays the list of words
words_list = user_input.split()
print("List of words:", words_list)

#Convert string into list of words and display length
print("The list has", len(words_list),"items")
