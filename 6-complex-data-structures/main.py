import time as t
import random as r
from tree import node


class root_tbl:
    def __init__(self, root_vals):
        self.roots = []
        for val in root_vals:
            self.roots.append(node(val))

    def INSERT(self, val):
        val = round(val, 2)
        i = 0
        while i < len(self.roots):
            if val < self.roots[i].data + 0.5 and val >= self.roots[i].data - 0.5:
                self.roots[i].add_node(val)
                # print(f"Added {val} to root: {self.roots[i].data}")
                return
            i += 1

    def MINIMUM(self, root_val):
        for root in self.roots:
            if root.data == root_val:
                # print(root.getMinNode())
                return
        # print("No root in structure")

    def MAXIMUM(self, root_val):
        for root in self.roots:
            if root.data == root_val:
                # print(root.getMinNode())
                return
        # print("No root in structure")

    def SEARCH(self, val):
        val = round(val, 2)
        for root in self.roots:
            if root.check_if_exists(val):
                return True
        return False

    def PRINT(self):
        for root in self.roots:
            root.print_tree()


def measure(num_of_roots, num_of_elements, times):
    insert_time = []
    min_time = []
    max_time = []
    search_time = []

    for i in range(times):
        roots = []
        elements = []
        for i in range(num_of_roots):
            roots.append(i + 1)
            roots.append(i + 1.5)

        for i in range(num_of_elements):
            elements.append(r.uniform(0, roots[-1]))

        struct = root_tbl(roots)
        for val in elements:
            struct.INSERT(val)

        time1 = t.time()
        struct.INSERT(r.uniform(0, roots[-1]))
        time1 = t.time() - time1

        time2 = t.time()
        struct.MINIMUM(r.choice(roots))
        time2 = t.time() - time2

        time3 = t.time()
        struct.MAXIMUM(r.choice(roots))
        time3 = t.time() - time3

        time4 = t.time()
        struct.SEARCH(r.choice(elements))
        time4 = t.time() - time4

        insert_time.append(time1)
        min_time.append(time2)
        max_time.append(time3)
        search_time.append(time4)

    print(f"Average time for  {num_of_elements} elements")
    print(f"INSERT: {sum(insert_time)/len(insert_time)}")
    print(f"MINIMUM: {sum(min_time)/len(min_time)}")
    print(f"MAXIMUM: {sum(max_time)/len(max_time)}")
    print(f"SEARCH: {sum(search_time)/len(search_time)}")


if __name__ == "__main__":
    example_roots = [1.5, 3.5, 4.5, 7.5, 9.5]
    example_vals = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]

    example_struct = root_tbl(example_roots)
    for val in example_vals:
        example_struct.INSERT(val)

    example_struct.PRINT()
    example_struct.MAXIMUM(7.5)
    example_struct.MINIMUM(7.5)
    example_struct.SEARCH(4.99)

    measure(10, 25, 100)
    print()
    measure(20, 50, 100)
    print()
    measure(40, 100, 100)
    print()
    measure(400, 1000, 10)
