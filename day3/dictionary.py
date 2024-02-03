string_to_iterate = "Martina"

char_dict = {index: char for index, char in enumerate(string_to_iterate)}

for index, char in char_dict.items():
    print(index, char, end="")  

