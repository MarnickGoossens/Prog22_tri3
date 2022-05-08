# This file should be used to show the implementation of dojo.py
# For instructions read the README.md
from dojo import *

jan = Student("Jan Hancock", "trying to learn programming", ["Python", "C++", "HTML"])
piet = Student(
    "Piet Pieters", "I am really excited to learn programming", ["C", "R", "Java"]
)
joris = Instructor(
    "Joris Engelen", "Wants to help people learn programming", ["Python", "C#", "R"]
)
korneel = Instructor("Korneel Kaneel", "Has been programming for 5 years")
workshop_1 = Workshop("03/05/2022", "Python")
workshop_2 = Workshop("08/06/2022", "C#")

print(joris.introduce())
print(piet.description())

print(workshop_1.add_participant(jan))
print(workshop_1.add_participant(piet))
print(workshop_1.add_participant(joris))
print(workshop_1.add_participant(korneel))
print(workshop_2.add_participant(jan))
print(workshop_2.add_participant(piet))
print(workshop_2.add_participant(joris))
print(workshop_2.add_participant(korneel))
