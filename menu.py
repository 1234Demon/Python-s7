from read import read_cont as rc
from write import style1 as s1
from write import style2 as s2

def menu():
    adr = rc()
    a = int(input('Enter method of write? (1-line by line, 2-in one term) '))
    if a == 1:
        s1(adr)
    else:
        s2(adr)
