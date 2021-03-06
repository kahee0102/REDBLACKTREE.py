class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = NullNode()
        self.right = NullNode()
        self.parent = None
        self.color = 'RED'

class NullNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = "BLACK"


class RBT:
    def __init__(self):
        self.root = None

    def search(self, tree, val):
        if self.root is None:
            print("That RedBlack Tree do not have any Node")
            return None
        if tree.val is None:
            print(val, "is not in the RedBlackTree")
            return None
        if tree.val > val:
            return self.search(tree.left, val)
        elif tree.val < val:
            return self.search(tree.right, val)
        else:
            return tree

    def findMinimum(self, tree):
        if tree.left.val is None:
            return tree
        else:
            return self.findMinimum(tree.left)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def insert(self, tree, n):
        y = None
        x = self.root


        while x is not None and x.val is not None:
            y = x
            if n.val < x.val:
                x = x.left
            else:
                x = x.right

        n.parent = y
        if y is None:
            self.root = n
        elif n.val < y.val:
            y.left = n
        else:
            y.right = n

        self.RBT_Insert_Fixup(self, n)

    def RBT_Insert_Fixup(self, tree, n):
        while n.parent is not None and n.parent.parent is not None and n.parent.color is 'RED':
            if n.parent == n.parent.parent.left:
                y = n.parent.parent.right
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.right:
                        n = n.parent
                        self.Left_Rotate(tree, n)
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Right_Rotate(tree, n.parent.parent)
            else:
                y = n.parent.parent.left
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.left:
                        n = n.parent
                        self.Right_Rotate(tree, n)
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Left_Rotate(tree, n.parent.parent)
        self.root.color = "BLACK"

    def delete(self, tree, n):
        delTree = self.search(tree, n)
        if delTree is None:
            return

        y = delTree
        yOrgColor = y.color

        if delTree.left.val == None:
            x = delTree.right
            self.transplant(delTree, delTree.right)

        elif delTree.right.val == None:
            x = delTree.left
            self.transplant(delTree, delTree.left)

        else:
            y = self.findMinimum(delTree.right)
            yOrgColor = y.color
            x = y.right

            if y.parent is delTree:
                x.parent = delTree.right
            else:

                self.transplant(y, y.right)
                y.right = delTree.right
                y.right.parent = y

            self.transplant(delTree, y)

            y.left = delTree.left
            y.left.parent = y
            y.color = delTree.color

        if yOrgColor == "BLACK":
            self.RBT_Delete_Fixup(self, x)

    def RBT_Delete_Fixup(self, tree, x):
        while x is not tree.root and x.color == "BLACK":

            if x == x.parent.left:

                w = x.parent.right

                # Case 1
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.Left_Rotate(tree, x.parent)

                    w = x.parent.right

                # Case 2
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent

                # Case 3
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.Right_Rotate(tree, w)
                        w = x.parent.right

                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.Left_Rotate(tree, x.parent)
                    x = tree.root

            else:

                w = x.parent.left

                # Case 1
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.Right_Rotate(tree, x.parent)

                    w = x.parent.left

                # Case 2
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent

                # Case 3
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.Left_Rotate(tree, w)
                        w = x.parent.left

                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.Right_Rotate(tree, x.parent)
                    x = tree.root
        if x is not None:
            x.color = "BLACK"

    def Left_Rotate(self, tree, x):

        y = x.right


        x.right = y.left
        if y.left is not None:
            y.left.parent = x


        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def Right_Rotate(self, tree, x):

        y = x.left


        x.left = y.right
        if y.right is not None:
            y.right.parent = x


        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y


        y.right = x
        x.parent = y

    def print(self, tree, level):
        if tree.right.val is not None:
            self.print(tree.right, level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val, tree.color)
        if tree.left.val is not None:
            self.print(tree.left, level + 1)

    def nodeCount(self, tree, n=0):
        if tree.val is None:
            return 0
        else:
            return self.nodeCount(tree.left) + self.nodeCount(tree.right) + 1

    def printNodeCount(self, tree):
        print(self.nodeCount(tree))

    def blackNodeCount(self, tree):
        if tree.val is None:
            return 0
        elif tree.color == "BLACK":
            return self.blackNodeCount(tree.left) + self.blackNodeCount(tree.right) + 1
        else:
            return self.blackNodeCount(tree.left) + self.blackNodeCount(tree.right)

    def printBlackNodeCount(self, tree):
        print(self.blackNodeCount(tree))

    def blackHeight(self, tree, n=0):
        if tree.val is None:
            return 0
        elif tree.color == "BLACK":
            return self.blackHeight(tree.left) + 1
        else:
            return self.blackHeight(tree.left)

    def printBlackHeight(self, tree, n=0):
        print(self.blackHeight(tree, n))

    def inOrderTraversal(self, tree):
        if tree.left.val is not None:
            self.inOrderTraversal(tree.left)
        print(tree.val, end=" ")
        if tree.right.val is not None:
            self.inOrderTraversal(tree.right)

def getFileData(name = "input.txt"):
    data = []

    f = open(name, 'r')
    lines = f.readlines()

    for line in lines:
        data.append(int(line.strip("\n")))

    f.close()

    return data

def main():
    data = getFileData()
    rbt = RBT()

    for i in data:
        if i > 0:
            rbt.insert(rbt.root, Node(i))
        elif i < 0:
            rbt.delete(rbt.root, -i)
        else:
            break

    print("Number of Total Node")
    rbt.printNodeCount(rbt.root)

    print("Number of Black Node")
    rbt.printBlackNodeCount(rbt.root)

    print("Black Height")
    rbt.printBlackHeight(rbt.root)

    print("Inorder Traversal")
    rbt.inOrderTraversal(rbt.root)

main()