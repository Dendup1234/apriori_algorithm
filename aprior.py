import math
# Intiliazation
min_support = 2
k = 0
unique_items = set()
count = []
#Transaction data
data = {
    'T1': {'1','2','5'},
    'T2': {'1','4'},
    'T3': {'2','3'},
    'T4': {'1','2','4'},
    'T5': {'1','3'},
    'T6': {'2','3'},
    'T7': {'1','3'},
    'T8': {'1','2','3'},
    'T9': {'1','2','3'},
}

print(min_support)
for k,v in data.items():
    for i in v:
        unique_items.add(int(v[i]))
print(unique_items)







# Algorithm



