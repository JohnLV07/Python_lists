# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.
# With the given list; Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if "Alice" in submitted and attended:
    print("She both submitted and attended to classes")
else:
    print("no,she either missed the class or did not submitted the assignment")

    