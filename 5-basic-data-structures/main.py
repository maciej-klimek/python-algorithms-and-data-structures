import time as t
import iterative_hanoi as iterative
import recursive_hanoi as recursive


def avg(lst):
    return sum(lst) / len(lst)

def test(x, n, src, dest, buff):
    rec_times = []
    iter_times = []
    for i in range(x):
        s1 = t.time()
        recursive.solve(n, src, dest, buff)
        e1 = t.time() - s1

        s2 = t.time()
        iterative.solve(n, src, dest, buff)
        e2 = t.time() - s2    
        rec_times.append(e1)
        iter_times.append(e2)
    print(f"Średni czas rekurencyjnie: {avg(rec_times)}")
    print(f"Średni czas iteracyjnie: {avg(iter_times)}")
    



cont = True
while cont:
    n = int(input("Podaj liczbę krążków: "))
    s = int(input("Podaj liczbę wywołań: "))

    test(s, n, "A", "B", "C")
    cont = bool(input("Kontynuować? "))