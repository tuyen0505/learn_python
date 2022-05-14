
if __name__=="__main__":
    n=int(input())
    a=map(int,input().split())
    b=tuple(a)
    print(hash(b))