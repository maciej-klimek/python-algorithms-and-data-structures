count = 0

def solve(n, src, dest, buff):
    global count
    if n == 1:
        #print(f"Przekładam krążek {n} z drążka {src} na drążek {dest}.")
        count+=1
        return
    solve(n-1, src, buff, dest)
    #print(f"Przekładam krążek {n} z drążka {src} na drążek {dest}.")
    count+=1
    solve(n-1, buff, dest, src)


