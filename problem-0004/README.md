I'm not happy with the solution for this one, but I want to move on to other
problems. I know there are much simpler and quicker algorithms out there, but
I'm trying to answer these problems in creative and interesting ways, where
possible.

My solution is based on the fact that if you find all possible combinations of
numbers with a certain number of digits (in this case 3) and then find their
products in largest-first order, the first palindrome will by definition be the
largest.

Unfortunately this is quite slow. A better approach would be to generate the
products in order, in which case you wouldn't need to sort them, but without
an algorithm to do that I'm just going to leave this, for now...
