# # Day 9 - 1
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     score = student_scores[key]
#     if score <= 70:
#         student_grades[key] = "Failed"
#     elif 71 <= score <= 80:
#         student_grades[key] = "Acceptable"
#     elif 81 <= score <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif 91 <= score <= 100:
#         student_grades[key] = "Outstanding"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

######################################################################################

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# my code
# def add_new_country(country, visits, listed_cities):
#   travel_log.append({"country": country, "visits": visits, "cities": listed_cities},)

# lecturers code
def add_new_country(country, visits, listed_cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = listed_cities

  travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

