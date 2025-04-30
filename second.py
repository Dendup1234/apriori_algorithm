import math
from itertools import combinations

# Initialize data structures
dashbox = {}        # {frozenset: {'count': x, 'stop_number': y}}
dashcircle = {}     # {frozenset: {'count': x, 'stop_number': y}}
solid_box = []      # Frequent itemsets finalized
solid_circle = []   # Infrequent itemsets finalized

# Current stop number
current_stop_number = 0

# User input for min support percentage
num = int(input("Enter the percentage: "))  # e.g., 25
percentage = num / 100
print("Support %:", percentage)

# Dataset
data = {
    'T1': {'A': 1, 'B': 1, 'C': 0},
    'T2': {'A': 1, 'B': 0, 'C': 0},
    'T3': {'A': 0, 'B': 1, 'C': 1},
    'T4': {'A': 0, 'B': 0, 'C': 0}
}

# Get all unique items
all_items = set()
for record in data.values():
    all_items.update(record.keys())

# Initialize dashcircle with 1-itemsets (count=0, stop_number=0)
for item in all_items:
    dashcircle[frozenset([item])] = {'count': 0, 'stop_number': 0}

print("Initial dashcircle:", [set(x) for x in dashcircle.keys()])
# Calculate minimum support count
transaction_count = len(data)
min_support_count = math.ceil(transaction_count * percentage)
print("Min support count:", min_support_count)

# Helper function to format output
def print_itemset_dict(itemset_dict):
    return [(set(k), v) for k, v in itemset_dict.items()]

# Main DIC algorithm loop
while dashcircle:
    current_stop_number += 1
    print(f"\nIteration {current_stop_number} -----------------")

    # Process each transaction up to current stop point
    transactions_processed = 0
    for tid, record in data.items():
        transactions_processed += 1
        if transactions_processed > current_stop_number:
            break

        # Update counts for itemsets in dashcircle and dashbox couting for the candidate number
        for itemset in list(dashcircle.keys()) + list(dashbox.keys()):
            # Getting all the unique key from the data set
            #Itemset have all the unique value
            all_present = all(record.get(item, 0) == 1 for item in itemset)
            if all_present:
                if itemset in dashcircle:
                    dashcircle[itemset]['count'] += 1
                elif itemset in dashbox:
                    dashbox[itemset]['count'] += 1

    print("Dashcircle after counting:", print_itemset_dict(dashcircle))
    print("Dashbox after counting:", print_itemset_dict(dashbox))

    # Process dashcircle
    to_remove_from_dashcircle = []
    to_add_to_dashbox = []

    for itemset, info in list(dashcircle.items()):
        if info['count'] >= min_support_count:
            print(f"Itemset {set(itemset)} meets support (count={info['count']}), moving to dashbox")
            to_add_to_dashbox.append((itemset, info))
            to_remove_from_dashcircle.append(itemset)


        elif info['stop_number'] == current_stop_number:
            print(f"Itemset {set(itemset)} doesn't meet support and stop number reached, moving to solid circle")
            solid_circle.append(itemset)
            to_remove_from_dashcircle.append(itemset)

    # Move to dashbox with updated stop_number
    for itemset, info in to_add_to_dashbox:
        info['stop_number'] = current_stop_number
        dashbox[itemset] = info

    # Remove from dashcircle
    for itemset in to_remove_from_dashcircle:
        if itemset in dashcircle:
            del dashcircle[itemset]

    # To generate the candiate sets for the supersets
    dashbox_itemsets = list(dashbox.keys())
    new_candidates = set()
    for i in range(len(dashbox_itemsets)):
        for j in range(i+1,len(dashbox_itemsets)):
            itemset1 = dashbox_itemsets[i]
            itemset2 = dashbox_itemsets[j]
            union_set = itemset1.union(itemset2)

            # For generating the candidate set
            if len(union_set) == len(itemset1) +1:
                if (union_set not in dashcircle) and (union_set not in dashbox):
                    dashcircle[union_set] = {'count': 0, 'stop_number': current_stop_number}
                    print(f"Generated new candidate from dashbox: {set(union_set)}")

    # Process dashbox
    to_remove_from_dashbox = []
    for itemset, info in list(dashbox.items()):
        if info['stop_number'] == current_stop_number:
            print(f"Itemset {set(itemset)} in dashbox reached stop number, moving to solid box")
            solid_box.append(itemset)
            to_remove_from_dashbox.append(itemset)

    for itemset in to_remove_from_dashbox:
        del dashbox[itemset]

    print("Dashcircle after processing:", [set(x) for x in dashcircle.keys()])
    print("Dashbox after processing:", [set(x) for x in dashbox.keys()])
    print("Solid circle:", [set(x) for x in solid_circle])
    print("Solid box:", [set(x) for x in solid_box])

# Final output
print("\nFinal frequent itemsets in solid box:")
for itemset in solid_box:
    print(set(itemset))
