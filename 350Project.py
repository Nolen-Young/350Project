from pyeda.inter import *

def main():
    #create BDD's for R, [EVEN], and [PRIME]
    RR = generateRR()
    EVEN = generateEVEN()
    PRIME = generatePRIME()


    return 0

# generates the EVEN BDD
def generateEVEN():
    # create our domain
    X = exprvars('x', 5)
    iterX = list(iter_points(X))

    boolExpString = ""

    for itemX in iterX:
        # find unsigned 5 bit int representations of the boolean variables
        x = int("{}{}{}{}{}".format(itemX[X[4]],
                                    itemX[X[3]],
                                    itemX[X[2]],
                                    itemX[X[1]],
                                    itemX[X[0]]), 2) % 2 ** 5

        if x % 2 == 0:
            temp = "("
            for key in itemX:
                if (itemX[key] == 0):
                    temp = "{}{}".format(temp, "~{} & ".format(key))
                else:
                    temp = "{}{}".format(temp, "{} & ".format(key))

            temp = "{}{}".format(temp[:-3], ") | ")
            boolExpString = "{} {}".format(boolExpString, temp)

    boolExp = expr(boolExpString[:-2])
    print("EVEN: {}".format(boolExp))
    bdd = expr2bdd(boolExp)
    return bdd

# generates the PRIME BDD
def generatePRIME():
    # create our domain
    X = exprvars('x', 5)
    iterX = list(iter_points(X))

    boolExpString = ""

    for itemX in iterX:
        # find unsigned 5 bit int representations of the boolean variables
        x = int("{}{}{}{}{}".format(itemX[X[4]],
                                    itemX[X[3]],
                                    itemX[X[2]],
                                    itemX[X[1]],
                                    itemX[X[0]]), 2) % 2 ** 5

        if isPrime(x):
            temp = "("
            for key in itemX:
                if (itemX[key] == 0):
                    temp = "{}{}".format(temp, "~{} & ".format(key))
                else:
                    temp = "{}{}".format(temp, "{} & ".format(key))

            temp = "{}{}".format(temp[:-3], ") | ")
            boolExpString = "{} {}".format(boolExpString, temp)

    boolExp = expr(boolExpString[:-2])
    print("PRIME: {}".format(boolExp))
    bdd = expr2bdd(boolExp)
    return bdd

# checks if a number is prime
def isPrime(n):
    # If given number is greater than 1
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

# generates the edges BDD
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
    print("R: {}".format(boolExp))
    bdd = expr2bdd(boolExp)
    return bdd

if __name__ == "__main__":
    main()
