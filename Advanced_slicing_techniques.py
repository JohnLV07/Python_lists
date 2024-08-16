#Task 1
# You have a list of daily temperatures for one month, and you'd like to extract specific data from it.
# Given temperatures: temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]
print(f"The temperatures from the second week are: {second_week}")


#Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

high_temperature = temperatures[23:30]
print(f"The highest tempertures of the month were: {high_temperature}")
