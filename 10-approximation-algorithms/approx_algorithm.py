import numpy as np
import random as r
from tabulate import tabulate
from main_algorithm import read_data, place_item
import time as t


def fill_backpack(shuffled_items, items, capacity):
    backpack = np.zeros((capacity, capacity))
    backpack_value = 0
    genome = [0]*len(items)
    for item in shuffled_items:
        item_id = item["id"]
        item_width = item["width"]
        item_height = item["height"]
        item_value = item["value"]

        if place_item(item_id, item_width, item_height, capacity, backpack):
            genome[items.index(item)] = 1
            backpack_value += item_value

        elif place_item(item_id, item_height, item_width, capacity, backpack):
            genome[items.index(item)] = 1
            backpack_value += item_value

    return backpack, backpack_value, genome


def get_first_generation(size, items, capacity):
    generation = []
    for i in range(size):

        shuffled_items = items.copy()
        r.shuffle(shuffled_items)
        backpack, value, genome = fill_backpack(
            shuffled_items, items, capacity)
        generation.append([value, genome])

    return generation


def decode(genome, items, capacity):
    item_list = []

    for item in items:
        if genome[item["id"]-1] == 1:
            item_list.append(item)

    r.shuffle(item_list)

    for item in items:
        if item not in item_list:
            item_list.append(item)

    backpack, value, genome = fill_backpack(item_list, items, capacity)
    return [value, genome, backpack]


def crossover(parents):
    genome1 = parents[0][1]
    genome2 = parents[1][1]
    length = len(parents[0][1])

    crossover_point = r.randint(1, length - 1)
    child1 = genome1[:crossover_point] + genome2[crossover_point:]
    child2 = genome2[:crossover_point] + genome1[crossover_point:]

    return child1, child2


def mutate(genom, mutation_rate, mutation_chance):
    indexes_to_mutate = r.sample(range(len(genom)), mutation_rate)
    for i in indexes_to_mutate:
        if r.uniform(0, 1) > mutation_chance:
            genom[i] = abs(genom[i] - 1)

    return genom


def genetic_approx(items, capacity, generation_num, population_size, elite_size=2, mutation_rate=2, mutation_chance=0.5):
    stime = t.time()
    generation = get_first_generation(population_size-1, items, capacity)
    greedy_backpack, greedy_value, greedy_genome = fill_backpack(
        sorted(items, key=lambda item: item["density"], reverse=True), items, capacity)
    generation.append([greedy_value, greedy_genome, greedy_backpack])
    generation = sorted(generation, reverse=True)

    for i in range(generation_num):
        print(f"Generation {i+1} completed.")
        temp_generation = []

        for i in range(elite_size):
            temp_generation.append(generation[i])

        while len(temp_generation) < population_size + 1:
            probabilities = [1 / (i + 10) for i in range(len(generation))]
            new_parents = r.choices(generation, probabilities, k=2)
            children = crossover(new_parents)

            for child in children:
                child = mutate(child, mutation_rate, mutation_chance)
                temp_generation.append(decode(child, items, capacity))

        generation = sorted(temp_generation, key=lambda x: x[0], reverse=True)

    best_genome = generation[0][1]
    best_backpack = generation[0][2]
    best_item_list = []
    best_ids_list = []

    for item in items:
        if best_genome[item["id"]-1] == 1:
            best_item_list.append(item)
            best_ids_list.append(item["id"])

    for item in items:
        if item not in best_item_list:
            best_item_list.append(item)
            best_ids_list.append(item["id"])

    print()
    print(f"Time of execution: {t.time()-stime}")
    print()
    print(f"RESULTS FOR {generation_num} GENERATIONS, POPULATION SIZE: {population_size}, ELITE SIZE: {elite_size}, MUTATION RATE: {mutation_rate}, MUTATION CHANCE: {mutation_chance}")
    print()
    print(f"Best genom: {best_genome}")
    print(f"Item list for this genom: {best_ids_list}")
    print()
    print("Backpack content:")
    print(tabulate(best_backpack, tablefmt="fancy_grid"))
    print(f"Backpack value: {generation[0][0]}")


if __name__ == "__main__":
    packages = ['packages/packages20.txt', 'packages/packages100.txt',
                'packages/packages500.txt',  'packages/packages1000.txt']
    sizes = [10, 20, 50, 100, 500, 1000]
    package = read_data(packages[0])
    genetic_approx(package, 20, 50, 100)
