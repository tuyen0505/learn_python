from unicodedata import name


def main():
    name = input()
    a = input()
    b = input()
    student(name, a, b)

def student(name, point, point1):
    print("name: " + name)
    print('math_score: '+ point)
    print("""literature_score: """, point1) 

main()  