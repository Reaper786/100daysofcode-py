# dictionaries
# {key: value

# eg
# {"Bug": "An error in a program that prevents the program from running as expected.",
#    "Function": "A piece of code that you can easily call over and over again."}

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again",
# }

# calling item from dictionary
# print(programming_dictionary["Bug"])

# adding to dictionary / editing the entry by using the same key
# programming_dictionary["key"] = "value"
# creating dictionary when starting/ deleting everything in the dictionary
# new_dictionary = {}

# loop through a dictionary
# will bring only the key
# for key in programming_dictionary:
#     print(key)
#
# # if you want to get the value
#     print(programming_dictionary[key])

# nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# # nesting a list in dictionaries
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# # nesting dictionary in dictionary
# travel_log ={
# # what i did
#     "France": [{"Paris": 3, "Lille": 4, "Dijon": 6, }],
# # what lecturer did
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
#
# }
#
# # list with Dictionary in it
#
# travel_log = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12,
#     },
#     {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 12,
#     },
# ]
#
