# Functions with outputs

f_name = input("Write your first name: ")
l_name = input("Write your last name: ")


# Angela's solution with .title() function

def format_name(f_name, l_name):
    # My first Docstring
    """ Take a first and last name and format it to return the title case version of the name """
    if f_name == "" or l_name == "":
        return "Yoy didn't provide a valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(f_name, l_name)
print(formated_string)

'''def format_name(name):
    result = ""
    first_letter = True
    for letter in name:
        if name.index(letter) == 0 and first_letter:
            result += letter.capitalize()
            first_letter = False
        else:
            result += letter.lower()
    return result'''



#result_f_name = format_name(f_name)
#result_l_name = format_name(l_name)

#print(f"Before: {f_name} {l_name}\nNow: {result_f_name} {result_l_name}")