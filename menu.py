from read import read_cont as rc
from write import style1 as s1
from write import style2 as s2
from read_book import read1 as r1
from read_book import read1 as r2

def menu():
    b = int(input('Wonna write or read? (1-Write, 2-Read) '))
    if b == 1:
        adr = rc()
        a = int(input('Enter method of write? (1-line by line, 2-in one term) '))
        if a == 1:
            s1(adr)
        else:
            s2(adr)
    else:
        c = int(input('Enter file want to read? (1-Book1, 2-Book2) '))
        if c == 1:
            r1()
        else:
            r2()