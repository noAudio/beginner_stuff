some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

some_list.sort()

repeated_items = []

previous_item = ''

for item in some_list:
    if item == previous_item:
        repeated_items.append(item)
    previous_item = item

print(repeated_items)