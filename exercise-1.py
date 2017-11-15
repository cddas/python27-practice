import time

name, age = raw_input("Give me your name and age: ").split(" ")

years_to_centenary = 100 - int(age)
current_year = time.strftime("%Y")
current_year = int(current_year)

message = "Hi " + name + ". You will turn 100 years in the year - " + str( current_year + years_to_centenary )

repeat_times = raw_input("Enter the times you want to see the welcome message : ")
repeat_times = int(repeat_times)

for times in range(repeat_times):
    print message
