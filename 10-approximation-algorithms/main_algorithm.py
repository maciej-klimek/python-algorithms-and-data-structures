import numpy as np
from tabulate import tabulate
import time as t


def read_data(file_path):
    items = []
    num_of_items = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]

        for line in lines:
            line = line.strip()
            data = line.split(',')
            item = {
                'id': int(data[0]),
                'width': int(data[1]),
                'height': int(data[2]),
                'value': int(data[3]),
                'density': int(data[3])/(int(data[1])*int(data[2]))
            }
            items.append(item)
            num_of_items += 1

    return items


def place_item(id_val, width, height, capacity, backpack):
    for x in range(capacity - width + 1):
        if x + width > capacity + 1:
            break
        for y in range(capacity - height + 1):
            if y + height > capacity + 1:
                break

            if np.all(backpack[y: y+height, x: x+width] == 0):
                backpack[y: y+height, x: x+width,] = id_val
                return True
    return False


def fill_backpack(items, capacity):
    backpack_value = 0
    backpack = np.zeros((capacity, capacity))
    sorted_items = sorted(
        items, key=lambda item: item["density"], reverse=True)
    for item in sorted_items:
        # print(sorted_items.index(item), item)
        item_id = item["id"]
        item_width = item["width"]
        item_height = item["height"]
        item_value = item["value"]

        if place_item(item_id, item_width, item_height, capacity, backpack):
            # print(sorted_items.index(item))
            backpack_value += item_value

        elif place_item(item_id, item_height, item_width, capacity, backpack):
            # print(sorted_items.index(item))
            backpack_value += item_value

    return backpack, backpack_value


if __name__ == "__main__":
    packages = ['packages/packages20.txt', 'packages/packages100.txt',
                'packages/packages500.txt',  'packages/packages1000.txt']
    sizes = [10, 20, 50, 100, 500, 1000]

    stime = t.time()
    filled_backpack, backpack_value = fill_backpack(
        read_data(packages[0]), sizes[1])
    print(t.time()-stime)
    print("Backpack content:")
    print(tabulate(filled_backpack, tablefmt="fancy_grid"))
    print(
        f"Backpack value: {backpack_value}")
