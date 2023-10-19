import random
import math

def get_random_path(cords):
    num_of_cities = len(cords)
    path = list(range(1, num_of_cities))  
    random.shuffle(path)  
    path = [1] + path + [1] 

    return path

def get_distance(city_cords, path):
    total_distance = 0.0
    num_of_cities = len(path)

    for i in range(num_of_cities):
        curretn_city = path[i]
        next_city = path[(i + 1) % num_of_cities]

        x1, y1 = city_cords[curretn_city]
        x2, y2 = city_cords[next_city]

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_distance += distance

    return total_distance

def get_distance_nearest_neighbour(cords):
    num_of_cities = len(cords)

    visited = [False] * num_of_cities

    starting_city = 1
    visited[starting_city - 1] = True

    path = [starting_city]

    current_city = starting_city
    while len(path) < num_of_cities:
        min_distance = math.inf
        nearest_city = None

        for city_id, coords in cords.items():
            if not visited[city_id - 1]:
                x1, y1 = cords[current_city]
                x2, y2 = coords
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city_id

        path.append(nearest_city)
        visited[nearest_city - 1] = True
        current_city = nearest_city

    path.append(starting_city)

    distance = get_distance(cords, path)

    return path, distance


city_cords = {}
cords_file = open("TSP.txt", "r")
data = cords_file.read().splitlines()
for line in data:
    line = line.split()
    city_id = int(line[0])
    x = float(line[1])
    y = float(line[2])
    city_cords[city_id] = (x, y)


random_path = get_random_path(city_cords)
print("Dystans dla losowej ścieżki: ", end="")
print(get_distance(city_cords, random_path))
print()

path = [i for i in range(1,101)]
distance = get_distance(city_cords, path)
better_path, better_distance = get_distance_nearest_neighbour(city_cords)

print(f"Dystans policzony naiwnie: {distance}")
print()
print(f"Dystans policzony przez znajdowanie \nnajbliższego sąsiedniego miasta: {better_distance}")
