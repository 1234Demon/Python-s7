def read1():
    with open('book1.txt', 'r') as file:
        print(*file)

def read2():
    with open('book2.txt', 'r') as file:
        print(*file)

read1()