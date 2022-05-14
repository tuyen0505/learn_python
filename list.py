from numpy import sort


def main():

    colors = ["red", (1, 2, True), "green", "green"]

    # thêm vào cuối: có thê + * append extend
    colors.append("green")
    print("after append obj:",colors)

    # chèn (vị trí, obj)
    colors.insert(2, 3)
    print('after insert obj:',colors)

    # xóa phần tử
    colors.remove("red")
    print('after remove obj:',colors)

    # xóa vị trí
    colors.pop(1)
    print('after remove by pop of obj:',colors)

    # vị trí đàu tiên nó găp
    print("green occur in the start:",colors.index("green"))

    # đêm số lân xuất hiện
    print("how many times 'green' occurs:",colors.count("green"))

    print('last:',colors)


    #ngoại lệ
    try:
        colors.remove("jfdg")
    except ValueError: 
        print("😉🫠🫥😘", end = " ")

    # sort list:
    a = [1, 1.4, 0.8, -1, -4]
    a.sort()
    b = sorted(a)
    print('sort list:', a)
    
    # clear all obj:
    a.clear()
    print("after clear:", a)
    # agument obj diffence
    a.append(1)
    a[0] = 'tuyên'
    print("after agument:", a)

    


main()