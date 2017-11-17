user_string = raw_input("Enter a name for Palindrome check : ")

list_string = []
reverse_list_string = []

for letter in user_string:
    list_string.append(letter)

reverse_list_string = list_string[:]
reverse_list_string.reverse()

if (list_string == reverse_list_string):
    print("The entered string " + user_string + " is a pallindrome")
else:
    print("The entered string " + user_string + " is not a pallindrome")



