# 350Project
Nolen Young, 11517296

I think this whole project is working, the code seems correct to me.
However, The results form finding RR2star return a tautology, meaning
that every node can reach every other node in an even number of steps.
I do not think this is correct, but it is what I am getting, and I
cannot figure out what is wrong with my logic, as it follows the instructions
from class clearly, in my opinion. I hope if my solution gives undesired results,
you can at least see clearly that the logic is sound.

Below contains my answers to section 4 of the project

-----------------------------------------------------------------------------------

4\. To test the BDD, the function bdd.restrict() becomes very useful. Restric allows
us to get the results of a BDD, but only the results where the inputs are the
inputs specified in restrict. We can pass our results.restrict(u, v) to find out
if u, v exists in our result BDD.
 
(a). if u is 5, then v = 16 satisfies the condition, in relation to the graph.
It at u = 5, we can take the edge to 8, then we can take the dge to 16. This sequence
satisfies answer A.
I have written test code to test this specific case

(b). Check code for tests


