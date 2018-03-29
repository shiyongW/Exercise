#coding=utf-8

def main(n):
    for i in range(n):
        print((' * '*i).center(n*3));
    for i in range(n,0,-1):
        print((' * '*i).center(n*3));


main(3);


for x in range(10,0,-1):
    print(x);
