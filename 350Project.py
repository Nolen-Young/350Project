from pyeda.inter import *

def main():
    #define x and y
    x = exprvars('x', 32)
    y = exprvars('y', 32)
    print(x)
    print(y)
    print()

    print(list(iter_points([x,y])))

    return 0


if __name__ == "__main__":
    main()






