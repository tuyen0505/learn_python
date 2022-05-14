def main():
    user_input = int(input("input:"))

    with open("file.txt", "w") as f:
        #f.write("tuyen\n") # k tự có xuống dòng
        #number = []

        #data = f.readline()
        #print(f.tell())
        #data = data.split()
        #print(data)
        for i in range(user_input):
            f.write(str(user_input - i ) + "\n")
    
    numbers = []

    with open("file.txt", "r") as f:
        numbers = f.read().split()
        #numbers.pop()

    for i in range(len(numbers)):
        print("line", i + 1, ':', numbers[i])

        




main()