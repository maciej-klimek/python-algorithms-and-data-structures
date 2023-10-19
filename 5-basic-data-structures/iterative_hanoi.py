
class Stack:
    def __init__(self, n, name):
        self.name = name
        self.size = n
        self.last_index = -1
        self.tbl = [0] * n

def create_stack(n, name, full):
    result = Stack(n, name)
    if full:
        result.last_index += 1
        for i in range(n):
            result.tbl[result.last_index] = n - i
            result.last_index += 1
        result.last_index -= 1
    return result


def move_disk(stack1, stack2):
    if stack1.last_index == -1 or (stack1.tbl[stack1.last_index] > stack2.tbl[stack2.last_index] and stack2.tbl[stack2.last_index] != 0):
        move_disk(stack2, stack1)
        return
    #print(f"Przekładam krążek {stack1.tbl[stack1.lastIndex]} z drążka {stack1.name} na drążek {stack2.name}")
    stack2.last_index += 1
    stack2.tbl[stack2.last_index] = stack1.tbl[stack1.last_index]
    stack1.tbl[stack1.last_index] = 0
    stack1.last_index -= 1


def solve(n, src, dest, buff):

    if n % 2 == 0:
        A = create_stack(n, src, True)
        B = create_stack(n, dest, False)
        C = create_stack(n, buff, False)
        conPole = C
    else:
        A = create_stack(n, src, True)
        B = create_stack(n, buff, False)
        C = create_stack(n, dest, False)
        conPole = B

    i = 1
    while (A.tbl[0] != 0 or conPole.tbl[0] != 0):
        if i % 3 == 1:
            move_disk(A, C)
        elif i % 3 == 2:
            move_disk(A, B)
        elif i % 3 == 0:
            move_disk(B, C)
        i += 1

    #print(f"Liczba kroków: {i-1}")


