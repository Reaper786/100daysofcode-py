# normal function

# def my_function():

# function with input
# def my_function(hello):

# function with output
# def my_function():
#     result = 3 * 2
#     return result

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     # print
#     # print(f"{formated_f_name} {formated_l_name}")
#     # return
#     return f"{formated_f_name} {formated_l_name}"
#
#
# formated_string = format_name("AMEER", "hoosain")
# print(formated_string)
#

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("whats is your first name?"),
#                   input("whats is your last name?")))

# early return
def format_name(f_name, l_name):
    """"Take a first and last name and format it
    to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "\n no input provided"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("whats is your first name?"),
                  input("whats is your last name?")))