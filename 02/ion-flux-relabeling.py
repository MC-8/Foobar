"""Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of her
LAMBCHOP doomsday device has backfired spectacularly. She had been improving
the structure of the ion flux converter tree, but something went terribly wrong
and the flux chains exploded. Some of the ion flux converters survived the
explosion intact, but others had their position labels blasted off. She's
having her henchmen rebuild the ion flux converter tree by hand, but you think
you can do it much more quickly - quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion
flux converters to form one. To label them, she performed a post-order
traversal of the tree of converters and labeled each converter with the order
of that converter in the traversal, starting at 1. For example, a tree of 7
converters would look like the following:

   7
 3   6
1 2 4 5

Write a function solution(h, q) - where h is the height of the perfect tree of
converters and q is a list of positive integers representing different flux
converters - which returns a list of integers p where each element in p is the
label of the converter that sits on top of the respective converter in q, or -1
if there is no such converter. For example, solution(3, [1, 4, 7]) would return
the converters above the converters at indexes 1, 4, and 7 in a perfect binary
tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect
binary tree containing only the root, h = 2 represents a perfect binary tree
with the root and two leaf nodes, h = 3 represents a perfect binary tree with
the root, two internal nodes and four leaf nodes (like the example above), and
so forth. The lists q and p contain at least one but no more than 10000
distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(5, {19, 14, 28})
Output:
    21,15,29

Input:
Solution.solution(3, {7, 3, 5, 1})
Output:
    -1,7,6,3

-- Python cases --
Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3

Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29

Use verify [file] to test your solution and see how it does. When you are
finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
"""


class Node(object):
    
    def __init__(self, value=0):
        assert(isinstance(value, int))
        self.value    = value
        self.left     = None
        self.right    = None

    def add_left(self, node):
        assert(None==node or isinstance(node, Node))
        self.left = node
    
    def add_right(self, node):
        assert(None==node or isinstance(node, Node))
        self.right = node

    def set_value(self, value):
        assert(isinstance(value, int))
        self.value = value


class Tree(object):
    
    def __init__(self, height):
        assert(isinstance(height, int))
        self.nodes = 0
        self.root = self.build(height)

    def build(self, height):
        """ Recursive build of perfect binary tree.
        """
        if height==0:
            return None
        N = Node()
        N.add_left(self.build(height-1))
        N.add_right(self.build(height-1))
        self.nodes+=1
        N.set_value(self.nodes)
        return N

    def get_node_parents_value(self, value):
        """ Find node with given value, return parent's node value.
        Being a perfect binary tree, and that all provided values will be 
        between 1 and 2^h-1, we are guaranteed to find the node.
        """
        assert(isinstance(value, int))
        current_node = self.root
        if value==current_node.value:
            # Node is root
            return -1
        while True:
            if value==current_node.left.value or value==current_node.right.value:
                return current_node.value
            elif value < current_node.left.value:
                current_node = current_node.left
            elif value < current_node.right.value:
                current_node = current_node.right


def solution(h, q):
    myTree = Tree(h)
    return [myTree.get_node_parents_value(v) for v in q]


if __name__=="__main__":
    t1_sol = [-1,7,6,3]
    t2_sol = [21,15,29]
    t1_res = solution(3, [7, 3, 5, 1])
    t2_res = solution(5, [19, 14, 28])
    print 'Test 1 passed' if (t1_sol==t1_res) else 'Test 1 failed. Expected: {}, actual {}'.format(t1_sol, t1_res)
    print 'Test 2 passed' if (t2_sol==t2_res) else 'Test 2 failed. Expected: {}, actual {}'.format(t2_sol, t2_res)
