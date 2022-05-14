
if __name__ == '__main__':
    lit=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lit+=[[name,score]]
    print(lit)