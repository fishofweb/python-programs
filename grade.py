first = int(input("Your first grade: "))
second = int(input("Your second grade:"))
third = int(input("your third grade:"))
fourth = int(input("your fourth grade: "))

grades = [first, second, third, fourth]
print("Your grades are", grades)

print("your highest to lowest are: ", sorted(grades, reverse=True))
grades.reverse()
print("your grades from highest to lowest are:",grades)
print("The two grades will now bw dropped.\n")
rm1 = grades.pop()
rm2 = grades.pop()
print("Removed Grade:", rm1,"\n","Removed Grade:",rm2)
print("Your remaining grades are:", grades)
print(f"Nice work! Your highest grade is a {grades[0]}")

