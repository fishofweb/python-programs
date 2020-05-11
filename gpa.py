print("Welcome to the Average Calcutator App.")
print("\n")

name = input("What is your name: ")
no_of_grades = int(input("How many grades would you like to enter: "))
grades = []
for i in range(no_of_grades):
    marks=float(input("Enter grade: "))
    grades.append(marks)


print("\n")
print("Grades From Highest to lowest: \n")
grades.sort(reverse=True)
for c in grades[:]:
    print("\t\t", c)


print(name+"'s Grade Summary:\n")

print("\t\tTotal Number of Grades", no_of_grades)
print("\t\tHighest Grade: ", max(grades))
print("\t\tLowest Grade:  ", min(grades))
print("\t\tAverage: ",sum(grades)/no_of_grades)
average_ =sum(grades)/no_of_grades
desired_average = float(input("What is your desired average: "))
per = (1/ 100) * sum(grades)

print("You will need ", (desired_average*(no_of_grades+1))/sum(grades),"marks in your next assignment to get ",desired_average)

change_grade = float(input("what grade would you like to change: "))
grades.remove(change_grade)
new_grade = float(input("What would you like to change "+str(change_grade)+" to:"))
grades.append(new_grade)

print(name+"'s New Grades summary:")
print("\t\tHighest Grade: ", max(grades))
print("\t\tLowest Grade:  ", min(grades))
print("\t\tAverage: ",sum(grades)/no_of_grades)
average_new =sum(grades)/no_of_grades

print("Your new grade would be a ",average_new,"That's a difference of ", average_new-average_,"as compared to to your real average.")

print("Too bad your original grades are still the same! haha")
print(grades)

print("You should go ask for extra credit!")