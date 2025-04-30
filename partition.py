import math
from collections import defaultdict
from itertools import combinations

# Transaction data
"""

"""
transactions = [{1,5}, {2,4}, {4,5}, {2,3}, {5}, {2,3,4}]


maxLength = max(len(s) for s in transactions)

print("Min. support percentage: ")
minSupport = 0.2
print("No. of partitions: ")
noOfPartitions = 2
minSupportCount = math.ceil(len(transactions) * (minSupport))
print(f"\nminSupportCount: {minSupportCount}\n")
print("Transactions:")
for i, t in enumerate(transactions, 1):
    print(f"Transaction {i}: {t}")
print()

# Defining partition info
partitions = defaultdict(list)
partitionSize = math.ceil(len(transactions) / noOfPartitions)
localSupportCount = math.ceil(partitionSize * (minSupport))

def fillPartitions(transactions):
    for i, t in enumerate(transactions):
        partition_num = (i % noOfPartitions) + 1  # Cycles 1, 2, 1, 2, ...
        partitions[partition_num].append(t)

fillPartitions(transactions)

print(f"No. of partitions = {noOfPartitions}")
print(f"Local min. support count = {localSupportCount}")
for k in sorted(partitions.keys()):
    print(f"Partition {k}: {partitions[k]}")

def findLocalFreqSets(partitions, freqSetLength):
    localFreq = {}

    for partitionNum, transactionList in partitions.items():
        itemCount = defaultdict(int)
        # Count occurrences of items
        for t in transactionList:
            if len(t) >= freqSetLength:
                for item in combinations(sorted(t), freqSetLength):
                    itemCount[item] += 1

        # Filter items based on min. local support
        freqItems = set()
        for item, count in itemCount.items():
            if count >= localSupportCount:
                if freqSetLength == 1:
                    freqItems.add(item[0])
                else:
                    freqItems.add(item)
        localFreq[partitionNum] = freqItems

    return localFreq

print()

localFreqSets = {}
for i in range(1, maxLength + 1):
    localFreqSets[i] = findLocalFreqSets(partitions, i)
print("Local frequent sets:")
for p, i in sorted(localFreqSets.items()):
    print(f"{p}-frequent sets:")
    for part in sorted(i):
        print(f"  Partition {part}: {i[part]}")
    
def findGlobalFreqSets():
    # Count actual support across all transactions
    itemCount = defaultdict(int)
    all_items = set()
    
    # First collect all candidate items from local frequent sets
    for freqItems in localFreqSets.values():
        for partition, setList in freqItems.items():
            for i in setList:
                all_items.add(i)
    
    # Now count their actual support in the full database
    for t in transactions:
        t_sorted = sorted(t)
        for item in all_items:
            if isinstance(item, int):  # 1-itemset
                if item in t:
                    itemCount[item] += 1
            else:  # k-itemset (k > 1)
                if all(x in t_sorted for x in item):
                    itemCount[item] += 1
    
    globalFreqItems = set()
    for item, count in itemCount.items():
        if count >= minSupportCount:
            globalFreqItems.add(item)
    return globalFreqItems
    
print() 

print("Global frequent sets:")
global_freq = findGlobalFreqSets()
print(global_freq)
