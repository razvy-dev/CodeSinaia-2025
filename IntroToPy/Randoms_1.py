import random
import math
import pandas
import matplotlib.pyplot as plt

# Read input parameters from the console
count = 100 # int(input("Number of values?> "))
min_value = 100 # int(input("Minimum value?> "))
max_value = 150 # int(input("Maximum value?> "))
print(f"Generating {count} randoms in the range [{min_value}, {max_value}]")

# Generate count values in the range [min_value, max_value] and store them in a the values map
# randoms_map - associates each random value to the zero-based index/iteration where it was generated
# <key=random_value, value=[index1, index2, index3, ...]> 
randoms_map = {}
for i in range(0, count):
    r = random.randint(min_value, max_value)
    #r = int(min_value + i) if i < 9 * count/10 else min_value + 1000 + i
    if r not in randoms_map:
        randoms_map[r] = []
    randoms_map[r].append(i)

# Write a text file "randoms_db.txt" with each random on a line, its value followed by the indexes where it occurred
with open("IntroToPy/randoms_improved_db.txt", "w") as data_file:
    for r in randoms_map.keys():
        data_file.write(f"{r} {randoms_map[r]}\n")

def unique_values(randoms_map):
    x = 0
    for num in randoms_map.keys():
        if len(randoms_map[num]) == 1:
            x = x + 1
    return x

print(f"Unique values: {unique_values(randoms_map)}")

all_nums = list(randoms_map.keys())

min_value = min(all_nums)
max_value = max(all_nums)

def get_median(randoms_map):
    if (len(all_nums) % 2 == 0):
        mid1 = all_nums[len(all_nums) // 2 - 1]
        mid2 = all_nums[len(all_nums) // 2]
        return (mid1 + mid2) / 2
    else:
        return all_nums[len(all_nums) // 2]

print(f"Min value: {min_value}, Max value: {max_value}, Median value: {get_median(randoms_map)}")
print(f"Average of the nums: {sum(all_nums) // len(all_nums)}")

df = pandas.DataFrame.from_dict(randoms_map, orient='index')
print(f"Standard deviation is: {df.std()}")

lengths_dict = {k: len(v) for k, v in randoms_map.items()}
print(lengths_dict)

def get_topN(topN):
    sorted = sorted(lengths_dict.items(), key=lambda item: item[1], reverse=True)
    for i in range(0, topN):
        print(f"Value: {sorted[i][0]}, Occurrences: {sorted[i][1]}")

get_topN(10)

def create_bar_chart():
    plt.bar(lengths_dict.keys(), lengths_dict.values())
    plt.xlabel('Random Values')
    plt.ylabel('Occurrences')




