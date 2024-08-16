# Task 1 Given the lis, sort the grades in decending order:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

# Task 2: Calculate the average and print it

grades_summed = sum(grades)
total_grades = len(grades)
average_grade = grades_summed / total_grades
print(f"The average grade is: {average_grade}")
