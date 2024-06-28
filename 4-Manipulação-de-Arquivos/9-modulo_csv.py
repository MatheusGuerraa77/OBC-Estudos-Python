import csv

courses = []

with open("dados/courses.csv", "r", encoding="utf-8")as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append({"language":row["language"], "category":row["category"]})

for course in sorted(courses, key=lambda course: course['language'], reverse=True):
    print(f"{course['language']}-{course['category']}")
