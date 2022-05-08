class Family:
    def __init__(self, sex, hair, relation, age, name):
        self.race = "human"
        self.sex = sex
        self.hair = hair
        self.relation = relation
        self.age = age
        self.name = name

    def Is_age(self):
        return self.age

    def Is_sex(self):
        return self.sex

    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}"

    def related(self):
        return self.relation

    def paint_hair(self, color):
        self.hair = color


marnick = Family("Man", "blond", "mezelf", 17, "Marnick")
marnick.paint_hair("zwart")
print(marnick.hair)

print()

inge = Family("Woman", "bruin", "moeder", 47, "Inge")
inge.birthday()
print(inge.Is_age())

print()

peter = Family("Man", "bruin", "vader", 49, "Peter")
print(peter.Is_sex())

print()

yannick = Family("Man", "blond", "broer", 19, "Yannick")
print(yannick.related())
