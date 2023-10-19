import numpy as np
def read_data_from_file(file_path):
    items = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]
        
        for line in lines:
            line = line.strip()
            item_data = line.split(',')
            item = {
                'id': int(item_data[0]),
                'width': int(item_data[1]),
                'height': int(item_data[2]),
                'value': int(item_data[3])
            }
            items.append(item)
    
    return items

def backpack_greedy(packages, capacity):
    backpack = np.zeros((capacity, capacity))
    sorted_packages = sorted(packages, key=lambda x: x['value']/(x['height'] * x['width']), reverse = True)
    for item in sorted_packages:
        print(sorted_packages.index(item), item)
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        item_value = item['value']
        inserted = False
        
        if not inserted:
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if h + item_height > capacity +1:
                        break

                    if np.all(backpack[w: w + item_width, h: h + item_height] == 0):
                        backpack[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
        if not inserted:
            item_width, item_height = item_height, item_width
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if  + item_height > capacity +1:
                        break

                    if np.all(backpack[w: w + item_width, h: h + item_height] == 0):
                        backpack[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
    value = calculate_backpack_value(backpack, packages)

    return backpack, value

def calculate_backpack_value(backpack, packages):
    total_value = 0
    counted_ids = {}  

    for row in backpack:
        for item_id in row:
            if item_id != 0 and item_id not in counted_ids:
                counted_ids[item_id] = True  
                item = next((item for item in packages if item['id'] == item_id), None)
                if item:
                    total_value += item['value']
    
    return total_value


packages20path = 'packages/packages20.txt'
packages100path = 'packages/packages100.txt'
packages500path = 'packages/packages500.txt'
packages1000path = 'packages/packages1000.txt'

matrix100 = read_data_from_file(packages100path)

backpack, value = backpack_greedy(matrix100, 100)
print(value)
print(backpack)