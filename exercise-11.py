def reverse_input_string(usr_str_reverse):
    global usr_str_output
    usr_str_output = " ".join(usr_str_reverse)

user_str = raw_input("Enter a sentence : ").split(" ")

usr_str_reverse = user_str
usr_str_reverse.reverse()

reverse_input_string(usr_str_reverse)

print(usr_str_output)