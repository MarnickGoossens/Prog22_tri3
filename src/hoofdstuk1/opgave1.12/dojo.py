class Member:
    def __init__(self, name):
        string = name.split()
        self.first_name = string[0]
        self.last_name = string[1]

    def introduce(self):
        string = f"Hi, my name is {self.first_name} {self.last_name}"
        return string

    def description(self):
        pass


class Student(Member):
    def __init__(self, name, reason, interests=[]):
        super().__init__(name)
        self.reason = reason
        self.interests = interests

    def add_interest(self, interest):
        if interest in self.interests:
            print(f"{interest} already in interests")
        else:
            self.interests.append(interest)

    def remove_interest(self, interest):
        if interest not in self.interests:
            print(f"{interest} not in your interests")
        else:
            self.interests.remove(interest)

    def description(self):
        return self.reason


class Instructor(Member):
    def __init__(self, name, bio, skills=[]):
        super().__init__(name)
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill):
        if skill in self.skills:
            print(f"{skill} already in your skills")
        else:
            self.skills.append(skill)

    def description(self):
        return self.bio


class Workshop:
    def __init__(self, date, subject, Instructors=[], students=[]):
        self.date = date
        self.subject = subject
        self.Instructors = Instructors
        self.students = students

    def add_participant(self, person):
        if type(person) is Instructor:
            if person not in self.Instructors:
                if self.subject in person.skills:
                    self.Instructors.append(person)
                else:
                    return f"{person.first_name} has no skill that maches with the workshop"
            else:
                return f"{person.first_name} is already signed in!"
        if type(person) is Student:
            if person not in self.students:
                if self.subject in person.interests:
                    self.students.append(person)
                else:
                    return f"{person.first_name} has no interests that maches with the workshop"
            else:
                return f"{person.first_name} is already signed in!"

    def update(self):
        for person in self.students:
            if self.subject not in person.interests:
                self.students.remove(person)
