from pyeda.inter import *

def main():
    #create BDD's for R, [EVEN], and [PRIME]
    RR = generateRR()
    EVEN = generateEVEN()
    ODD = generateODD()
    print(RR)

    return 0

def generateEVEN():
    return 0

def generateODD():
    return 0

def generateRR():
    # create our domain
    X = exprvars('x', 5)
    Y = exprvars('y', 5)
    iterX = list(iter_points(X))
    iterY = list(iter_points(Y))

    # init variables
    boolExpString = ""

    # loop through iterators to get all possible combos of boolean variables
    for itemX in iterX:
        for itemY in iterY:
            # find unsigned 5 bit int representations of the boolean variables
            x = int("{}{}{}{}{}".format(itemX[X[4]],
                                    itemX[X[3]],
                                    itemX[X[2]],
                                    itemX[X[1]],
                                    itemX[X[0]]), 2) % 2**5
            y = int("{}{}{}{}{}".format(itemY[Y[4]],
                                        itemY[Y[3]],
                                        itemY[Y[2]],
                                        itemY[Y[1]],
                                        itemY[Y[0]]), 2) % 2**5

            # test to see if it fits our edge condition
            if ((x + 3) % 32 == y % 32):
                # if it is an edge in our graph, add its edge to the boolean expression
                # that we are building.
                temp = "("
                for key in itemX:
                    if (itemX[key] == 0):
                        temp = "{}{}".format(temp, "~{} & ".format(key))
                    else :
                        temp = "{}{}".format(temp, "{} & ".format(key))

                for key in itemY:
                    #print("Key: {} Value: {}".format(key, itemX[key]))
                    if (itemY[key] == 0):
                        temp = "{}{}".format(temp, "~{} & ".format(key))
                    else :
                        temp = "{}{}".format(temp, "{} & ".format(key))

                temp = "{}{}".format(temp[:-3], ") | ")
                boolExpString = "{} {}".format(boolExpString, temp)

    boolExp = expr(boolExpString[:-2])
    bdd = expr2bdd(boolExp)
    return bdd

if __name__ == "__main__":
    main()
