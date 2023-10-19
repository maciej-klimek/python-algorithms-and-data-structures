import numpy as np
import time
import random
import multiprocessing
import matplotlib.pyplot as plt

coords = []

class Backpack:
    def __init__(self,height,width): 
        self.width = int(width)
        self.height = int(height) 
        self.field = np.zeros((self.width,self.height))
        self.value = 0 
    def add_item(self,item):
        item_width,item_height = item.height,item.width
        for w in range(self.width- item_width+1):
            if w+item_width> self.width + 1 :
                break
            for h in range(self.height - item_height+1):
                if h + item_height > self.height +1 :
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        #rotation
        item_width,item_height = item_height,item_width
        for w in range(self.width- item_width +1):
            if w+item_width> self.width :
                break
            for h in range(self.height - item_height+1 ):
                if h + item_height > self.height +1 :
                    break
                if np.all(self.field[w: w + item_width, h: h + item_height] == 0):
                    self.field[w: w + item_width, h: h + item_height] = item._id
                    self.value += item.value
                    return True
        return False
    def add_items(self,items):
        for item in items:
            self.add_item(item)
    def display_backpack(self):
        print(self.field)
    def get_value_of_backpack(self):
        return self.value
            

class Item:
    def __init__(self,_id,width,height,value):
        self._id = _id
        self.width= int(width)
        self.height = int(height) 
        self.value = int(value)
        self.density = self.value/(self.width*self.height)

def greedy_algorithm(backpack,items):
    temp_items = items
    temp_items.sort(key=lambda item: item.density,reverse = True)
    for item in temp_items:
        backpack.add_item(item) 

def eval(backpack,gene):
    if isinstance(gene[-1],int):
        return 0
    temp_backpack = Backpack(backpack.height,backpack.width)
    for item in gene: 
        temp_backpack.add_item(item)
    return temp_backpack.get_value_of_backpack()

def population_algorithm(backpack_arg,items,debug=False):
    p = 100 # population size
    pc = 0.2 # elite percentage
    pm = 0.01 # mutations
    ps = 0.05 # mutation severity
    iterations = 50
    data_for_chart = []
    population = []
    counter = 0
    while counter < iterations:
        counter += 1
        # generate random population
        for i in range(p-len(population)):
            population.append((backpack_arg,random.sample(items,k=len(items))))


        # multicore eval
        pool = multiprocessing.Pool()
        result = pool.starmap(eval,population)
        for i in range(len(population)):
            if not isinstance(population[i][1][-1], int):
                population[i][1].append(result[i])

        # sort according to perceived value 
        population.sort(key=lambda g: -g[1][-1])
        if counter == iterations:
            value = population[0][1][-1]
            data_for_chart.append(value)
            if debug:
                print(counter, value)
            del population[0][1][-1] 
            return (population[0][1],value,data_for_chart)
        data_for_chart.append(population[0][1][-1])
        if debug == True:
            print(counter, population[0][1][-1])

        # breed
        for i in range(round(p - 2 * pc * p)):
            b = random.randint(0, pc * p - 1)
            c = random.randint(pc * p, p - 2)
            bc = []
            iter_b = 0
            iter_c = 0
            for j in range(len(items)):
                # randomize gene mixing
                mixer = random.randint(0,1)
                if mixer:
                    while population[b][1][iter_b] in bc:
                        iter_b += 1

                    if iter_b <= len(items):
                        copy = population[b][1][iter_b]
                        bc.append(copy)
                    else:
                        copy = population[c][1][iter_c]
                        bc.append(copy)
                    
                else:
                    while population[c][1][iter_c] in bc:
                        iter_c += 1

                    if iter_c <= len(items):
                        copy = population[c][1][iter_c]
                        bc.append(copy)
                    else:
                        copy = population[b][1][iter_b]
                        bc.append(copy)

            population.append((backpack_arg,bc))
            
        del population[round(pc * p):p]

        # mutate
        for i in range(round(pm * len(population))):
            # pick entity to mutate
            m = random.randint(0, len(population) - 1)
            for j in range(round(ps * len(items))):
                # pick two genes to swap
                m1 = random.randint(0, len(items) - 1)
                m2 = random.randint(0, len(items) - 1)
                
                temp = population[m][1][m1]
                population[m][1][m1] = population[m][1][m2]
                population[m][1][m2] = temp
                if isinstance(population[m][1][-1], int):
                    del population[m][1][-1]

def display_chart(data): 
    iterations = list(range(1,51))
    print(iterations)  
    print(data)

    plt.plot(iterations,data) 
    plt.xlabel("Iterations")
    plt.ylabel("Values") 
    plt.title("Population Algorithm Values and Iterations Chart")
    plt.show() 

if __name__ =="__main__":
    with open("packages/packages20.txt",'r') as file:
        for line in file:
            line = line.strip().split('\n') 
            coords.append(line[0].split(','))


    coords.pop(0)
    coords.pop(0) 
    items = []

    for cord in coords:
        items.append(Item(cord[0],cord[1],cord[2],cord[3]))

    backpack1 = Backpack(20,20)

    start_time = time.time()
    greedy_algorithm(backpack1,items)  
    end_time = time.time()
    print("Greedy Algorithm time to execute: " + str(end_time-start_time)) 
    print("Greedy Algorithm Value: " + str(backpack1.get_value_of_backpack()))
    print("Greedy Algorithm Backpack Content:")
    backpack1.display_backpack()

    backpack2 = Backpack(20,20)

    start_time = time.time()
    optimal_set_of_items,value,data_for_chart = population_algorithm(backpack2,items) 
    end_time = time.time()
    print("Population Algorithm time to execute: " + str(end_time-start_time)) 
    print("Population Algorithm Value: " + str(value))
    print("Population Algorithm Backpack Content: ")
    backpack2.add_items(optimal_set_of_items)
    backpack2.display_backpack() 
    display_chart(data_for_chart)
    
    backpack3 = Backpack(100,100)
    coords = [] 
    items = []
    with open("packages/packages100.txt",'r') as file:
        for line in file:
            line = line.strip().split('\n') 
            coords.append(line[0].split(','))
    coords.pop(0)
    coords.pop(0)
    for cord in coords:
        items.append(Item(cord[0],cord[1],cord[2],cord[3]))
    start_time = time.time()
    optimal_set_of_items,value,data_for_chart = population_algorithm(backpack3,items,True) 
    end_time = time.time()
    print("Population Algorithm time to execute for 100 elements: " + str(end_time-start_time)) 
    print("Population Algorithm Value for 100 elements: " + str(value))
    print("Population Algorithm Backpack Content for 100 elements: ")
    backpack3.add_items(optimal_set_of_items) 
    backpack3.display_backpack()  
    display_chart(data_for_chart)