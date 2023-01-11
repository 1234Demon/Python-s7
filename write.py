def style1(adr):
    with open('book1.txt', 'a') as file:
        for line in adr:
            file.write(line + '\n')

def style2(adr):
    with open('book2.txt', 'a') as file:
        for i in range(len(adr)):
            if i == 3:
                file.write(adr[i])
            else:
                file.write(f'{adr[i]}, ')

        file.write('\n')
