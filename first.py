#for the possible combination
from itertools import combinations
import math

def get_itemsets(partition,support_percentage):
    items = []
    transactions = list(partition.values())
    total_transaction = len(transactions)
    #Calculation of min support count
    min_support = math.ceil(total_transaction*support_percentage)

    #Getting the unique item
    items = set(item for trans in transactions for item in trans)

    # For one item set
    one_itemsets = []
    for item in items:
        support = sum(1 for trans in transactions if item in trans)
        if support >= min_support:
            one_itemsets.append({item})

    # For two item set
    two_itemsets = []
    for pair in combinations(items,2):
        support = sum(1 for trans in transactions if pair[0] in trans and pair[1] in trans)
        if support >= min_support:
            two_itemsets.append(set(pair))

    return one_itemsets,two_itemsets

    
# For the partition of the dictionary
def partition_dict(data,size):
    key = list(data.keys())
    partition = []

    for i in range(0,len(key),size):
        chunck_key = key[i:i+size]
        chunck_dict = {k:data[k] for k in chunck_key}
        partition.append(chunck_dict)
    return partition

# Given transactional data
data = {
    "T1": ['i1','i5'],
    "T2": ['i2','i4'],
    "T3": ['i4','i5'],
    "T4": ['i2','i3'],
    "T5": ['i5'],
    "T6":  ['i2','i3','i4'],
}

# Getting the input from the user
n = int(input("Enter the number of partition:"))
support = int(input("Enter the given support:"))
# Calculation of the min support count
support_percentage = support/100

#For the global min support count
transaction = len(data.values())

result = partition_dict(data,n)

# for printing the partition
Partition_lists = []
for i, partition in enumerate(result, start=1):
    one_itemsets,two_itemsets = get_itemsets(partition,support_percentage)
    print(f"\nPartition {i}:")
    for x in one_itemsets:
        print(x)
        
    for x in two_itemsets:
        print(x)

print("Min_support_count:",math.ceil(transaction*support_percentage))

#For the union of the 2 partitions







