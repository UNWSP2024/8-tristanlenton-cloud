schedule = {}
add = True
while add:
    courseID = input("Enter course ID: ")
    courseName = input("Enter course name: ")
    schedule[courseID] = courseName
    cont = input("Would you like to add another course? (Y/N): ")
    if cont == "N":
        add = False
subject = input("Enter a subject to search for: ").upper()
print("Courses with subject '{subject}':")
found = False
for course_id, course_name in schedule.items():
    if course_id.upper().startswith(subject):
        print(f"{course_id}: {course_name}")
        found = True

if not found:
    print("No courses found with that subject.")
