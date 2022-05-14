import sys
if __name__=='__name__':
    n=int(input())
    my_list=[]
    command=[]
    for i in range(n):
        a=input()
        command.append(a)
    for i in command:
        if i[:2]=='in':
            idx=list(map(int,[s for s in i.split()][1:]))
            my_list.insert(idx[0],idx[1])
        elif i[:2]=='pr':
            print(my_list)
        elif i[:2]=='re':
            idx=list(map(int,[s for s in i.split()][1:]))
            my_list.remove(idx[0])
        elif i[:2]=='ap':
            idx=list(map(int,[s for s in i.split()][1:]))
            my_list.extend(idx[0])
        elif i[:2]=='so':
            my_list.sort()
        elif i[:2]=='po':
            my_list.pop()
        elif i[:4]=='reve':
            my_list.reverse()
