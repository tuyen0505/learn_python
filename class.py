class Student:
    def __init__(self, name, age, math_score, literature_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.literature_score = literature_score
        self.teacher = "Tuyen"
    
    def average_score(self):
        self.ave_score = (self.math_score + self.literature_score) / 2
        return self.ave_score
        
    def a(self):
        print("hehheeh")
    
    def print_informations(self):
        print("student name " + self.name + " study with " + self.teacher)
        print(self.average_score())
        print_info()
    

def print_info():
    print("tuyen dep dai")

def main():
    s1 = Student("david", 21, 9, 7)

    print(s1.average_score())

    s1.teacher = "TUYEN"
    
    print(s1.ave_score)
    s1.print_informations()
    s1.a()
    #_______________________________________

    s2 = Student("Tuyen", 19, 10 , 10)

    print(s2.average_score())











main()