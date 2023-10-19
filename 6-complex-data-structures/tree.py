import random as r
import math as m


class node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.data = num

    def add_node(self, num):
        if num < self.data:
            if self.left is None:
                self.left = node(num)
            else:
                self.left.add_node(num)

        if num > self.data:
            if self.right == None:
                self.right = node(num)
            else:
                self.right.add_node(num)

    def get_min_node(self):
        min_node = self
        while min_node.left is not None:
            min_node = min_node.left
        return min_node.data

    def get_max_node(self):
        max_node = self
        while max_node.right is not None:
            max_node = max_node.right
        return max_node.data

    def check_if_exists(self, num):
        if num == self.data:
            return True

        if num < self.data:
            if self.left == None:
                return False
            return self.left.check_if_exists(num)

        if self.right == None:
            return False
        return self.right.check_if_exists(num)

    def print_tree(self, depth=0):
        print((depth) * "-" + f"{self.data}", end="")
        if len(str(self.data)) < 4:
            print(" ", end="")
        depth += 1
        if self.left != None:
            self.left.print_tree(depth)
        else:
            print("")
        if self.right != None:
            padding = 0
            for i in range(depth):
                padding += i + 4
            print((padding) * " ", end="")
            self.right.print_tree(depth)


if __name__ == "__main__":
    root = node(2.5)
    for i in range(1000):
        root.add_node(round(r.uniform(2, 3), 2))

    root.print_tree()
    print(root.check_if_exists(2.60), root.get_min_node(), root.get_max_node())
