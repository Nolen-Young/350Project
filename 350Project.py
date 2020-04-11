from pyeda.inter import *

def main():
    #define x and y
    RR = generateRR();

    return 0

def generateRR():
    X = exprvars('x', 5)
    Y = exprvars('y', 5)
    iterX = list(iter_points(X))
    iterY = list(iter_points(Y))
    for itemX in iterX:
        for itemY in iterY:
            print("X: {}".format(itemX))
            print("Y: {}".format(itemY))
            print()





    return 0





if __name__ == "__main__":
    main()






