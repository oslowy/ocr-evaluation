from itertools import groupby

with open("image_names_list.txt") as image_names_file:
    image_names = [line.rstrip() for line in image_names_file]

    outer_index = lambda name: name[:2]
    inner_index = lambda name: name[3:5]

    sorted_names = [name
                    for _, group in groupby(sorted(image_names, key=outer_index), key=outer_index)
                    for name in sorted(group, key=inner_index)]

    for name in sorted_names:
        print(name)


