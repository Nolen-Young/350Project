################################################################
# Nolen Young, id: 11517296, email: nolen.young@wsu.edu
# CptS 350 project
#
# Appears to be working correctly to me, but my results are not what I expected.
# I believe the code to be correct, but something may be wrong. If there is something wrong
# with my results, please refer to my comment at computeRR2star() function definition.
################################################################

from pyeda.inter import *

def main():
    # step 3.1
    # create BDD's for R, [EVEN], and [PRIME]
    RR = computeRR()
    EVEN = computeEVEN()
    PRIME = computePRIME()

    # step 3.2
    # find the value of R composed R.
    RR2 = RComposeR(RR)

    # step 3.3
    # find the transitive closure of RR2, RR2star
    RR2star = computeRR2star(RR2)
    if RR2star.is_one():
        print("Since RR2star is a tautology, AKA, its true for every possible input combinations,\n"
              "Every node can reach every other node in an even number of steps!")
    elif RR2star.is_zero():
        print("Since RR2star is 0, there are no nodes that can reach each other in an even number of steps")
    else:
        print("Nodes that can reach each other in an even number of steps: {}".format(bdd2expr(RR2star)))


    return 0

# computes the EVEN BDD
def computeEVEN():
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

# computes the PRIME BDD
def computePRIME():
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

# computes the edges BDD
def computeRR():
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
            if (((x + 3) % 32 == y % 32) | ((x + 8) % 32 == y % 32)):
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
    print("RR: {}".format(boolExp))
    bdd = expr2bdd(boolExp)
    return bdd

## return R composed R
def RComposeR(RR):
    # declare domain
    X = bddvars('x', 5)
    Y = bddvars('y', 5)
    Z = bddvars('z', 5)

    # use compose to rename two new RR BDDs.
    RR_1 = RR.compose({X[0]: X[0], X[1]: X[1], X[2]: X[2], X[3]: X[3], X[4]: X[4],
                      Y[0]: Z[0], Y[1]: Z[1], Y[2]: Z[2], Y[3]: Z[3], Y[4]: Z[4]})

    RR_2 = RR.compose({X[0]: Z[0], X[1]: Z[1], X[2]: Z[2], X[3]: Z[3], X[4]: Z[4],
                      Y[0]: Y[0], Y[1]: Y[1], Y[2]: Y[2], Y[3]: Y[3], Y[4]: Y[4]})


    # print()
    # print(bdd2expr(RR_1))
    # print()
    # print(bdd2expr(RR_2))
    # print()

    # use smoothing on RR_1 & RR_2 to find all pairs of nodes, connected by two
    RR2 = (RR_1 & RR_2).smoothing(Z)
    print("RR2: {}".format(bdd2expr(RR2)))
    return RR2

# This computes RR2star according to our class notes
# I have verified RR2 is correct, by hand, so my composition function,
# compose(), does work. The code is written exactly along with the pseudo-code
# written in class. However, the result it gets says that all RR2star is a
# tautology. This means that all nodes can reach all other nodes in an even number
# of steps. This is a suprise to me, and I am not sure if it is correct.
def computeRR2star( RR2):
    # RR = bdd2expr(RR)
    # RR2 = bdd2expr(RR2)


    Hprime = RR2

    # first round of transitive closure
    H = Hprime | compose(Hprime, RR2)
    while Not(H.equivalent(Hprime)):
    #while H != Hprime:
        Hprime = H
        H = Hprime | compose(Hprime, RR2)

    print("RR2star: {}".format(bdd2expr(H)))

    return H

# return RR1 composed RR2
def compose(RR1, RR2):
    # declare domain
    # X = exprvars('x', 5)
    # Y = exprvars('y', 5)
    # Z = exprvars('z', 5)
    X = bddvars('x', 5)
    Y = bddvars('y', 5)
    Z = bddvars('z', 5)


    # use compose to rename two new RR BDDs.
    RR_1 = RR1.compose({X[0]: X[0], X[1]: X[1], X[2]: X[2], X[3]: X[3], X[4]: X[4],
                      Y[0]: Z[0], Y[1]: Z[1], Y[2]: Z[2], Y[3]: Z[3], Y[4]: Z[4]})

    RR_2 = RR2.compose({X[0]: Z[0], X[1]: Z[1], X[2]: Z[2], X[3]: Z[3], X[4]: Z[4],
                      Y[0]: Y[0], Y[1]: Y[1], Y[2]: Y[2], Y[3]: Y[3], Y[4]: Y[4]})


    # print()
    # print(bdd2expr(RR_1))
    # print()
    # print(bdd2expr(RR_2))
    # print()



    # use smoothing on RR_1 & RR_2 to find all pairs of nodes, connected by two
    composite = (RR_1 & RR_2).smoothing(Z)
    #print("Composite: {}".format(composite))
    return composite

if __name__ == "__main__":
    main()
