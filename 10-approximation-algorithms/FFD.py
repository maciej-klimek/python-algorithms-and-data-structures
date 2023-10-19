import numpy as np
from tabulate import tabulate

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
                'density': int(data[3]) / (int(data[1]) * int(data[2]))
            }
            items.append(item)
            num_of_items += 1

    return items

def place_item(id_val, width, height, capacity, bins):
    for bin in bins:
        if bin['width'] >= width and bin['height'] >= height:
            bin['items'].append(id_val)
            bin['width'] -= width
            bin['height'] -= height
            return True
    return False

def fill_backpack_ffd(items, capacity):
    backpack_value = 0
    bins = [{'width': capacity, 'height': capacity, 'items': []}]
    sorted_items = sorted(items, key=lambda item: item["density"], reverse=True)

    for item in sorted_items:
        item_id = item["id"]
        item_width = item["width"]
        item_height = item["height"]
        item_value = item["value"]

        if not place_item(item_id, item_width, item_height, capacity, bins):
            bins.append({'width': capacity - item_width, 'height': capacity, 'items': [item_id]})
        
    for bin in bins:
        backpack_value += sum(item['value'] for item in sorted_items if item['id'] in bin['items'])

    # Create backpack grid representation
    backpack = np.zeros((capacity, capacity))
    for bin in bins:
        for item_id in bin['items']:
            item = next((item for item in sorted_items if item['id'] == item_id), None)
            if item:
                item_width = item['width']
                item_height = item['height']
                for x in range(capacity - item_width + 1):
                    if x + item_width > capacity + 1:
                        break
                    for y in range(capacity - item_height + 1):
                        if y + item_height > capacity + 1:
                            break
                        if np.all(backpack[y: y+item_height, x: x+item_width] == 0):
                            backpack[y: y+item_height, x: x+item_width] = item_id
                            break

    return backpack, backpack_value


if __name__ == "__main__":
    packages = ['packages/packages20.txt', 'packages/packages100.txt', 'packages/packages500.txt',  'packages/packages1000.txt']
    sizes = [10, 20, 50, 100, 500, 1000]

    filled_backpack, backpack_value = fill_backpack_ffd(read_data(packages[0]), sizes[1])
    print("Backpack content:")
    print(tabulate(filled_backpack, tablefmt="fancy_grid"))
    print(f"Total value of 20x20 backpack filled with items from packages20: {backpack_value}")
