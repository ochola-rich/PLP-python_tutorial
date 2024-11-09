class person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"This person is {self.name} of age {self.age} years and gender {self.gender}")


jerom = person("jero",29,"male")
jerom.introduce()
