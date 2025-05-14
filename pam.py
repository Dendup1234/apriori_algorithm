#Imports of the libraries in the python
import random

#Function for calculating the distance
def mahattan_distance(p1,p2):
    return sum(abs(a-b) for a,b in zip(p1,p2))

#Function for finding the total cost in the selected and non_selected
def culstering_cost(non_selected,selected):
    total_cost = 0
    for point in non_selected:
        #finding the minimum distance from the point to any mediod 
        min_dist = float('inf')
        for mediod in selected:
            dist = mahattan_distance(point,mediod)
            if dist < min_dist:
                min_dist = dist
        total_cost = total_cost + min_dist
    return total_cost

# Function for swaping the best mediod for the given cost
def pam_swap_step(Data,selected,non_selected):
    current_cost = culstering_cost(Data,selected)
    best_cost = current_cost
    best_swap = None

    # finding the best swap
    for i,Oi in enumerate(selected):
        for h,Oh in enumerate(non_selected):
            temp_selected = selected.copy()
            temp_selected[i] = Oh # simulated swap
            temp_cost = culstering_cost(Data,temp_selected)

            delta = temp_cost - current_cost

            if delta < 0 and temp_cost < best_cost:
                best_cost = temp_cost
                best_swap = (i,h)
    return best_swap,best_cost

#Intialzation of the x and y coordinates of the data
Data = [(7,6),(2,6),(3,8),(8,5),(7,4),(4,7),(6,2),(7,3),(6,4),(3,4)]

#intialization of cluster 1 and cluster 2
c1 = []
c2 = [] 

#Printing the coordinates for the databases
for i in Data:
    print(i)

# Defining the cluster used in the PAM algorithm
k = 2

# Randomly selecting the kmed in the data based on the cluster
kmed = random.sample(Data,k)
#For testing the kmed
#kmed = [(4,7),(7,4)]

# Marking the kmed as the selected and others as non selected
selected = kmed
non_selected = []
for obj in Data:
    if (obj not in selected):
        non_selected.append(obj)
print("seleted:", selected)
print("Non-selected:",non_selected)

#Test run of the mahattan distance
"""
D1 = [(1,2)]
D2 = [(3,4)]
result = mahattan_distance(D1[0],D2[0])
print(result)
"""
#Calculating the total cost of the given selected and the non_selected
#For testing if the total cost is working or not
result = culstering_cost(non_selected,selected)
print("intial_total_cost:",result)

# Swaping function working for finding the best swap and best cost

swap, cost = pam_swap_step(Data,selected,non_selected)
print("Best swap:",swap," best_cost:",cost)

# For finding the new medoid and the new cost basis on the function and the swap
if swap is None:
    print("No better swap found.")
    print("Final medoids:", selected)
else:
    i, h = swap
    old_medoid = selected[i]
    new_medoid = non_selected[h]
    
    print(f"Best swap: Replace medoid {old_medoid} with {new_medoid}")
    
    # simulation of the updated medoid list
    updated_medoids = selected.copy()
    updated_medoids[i] = new_medoid
    print("New medoid list after swap:", updated_medoids)

# Based on the updated medoid finding the clusters
for x in Data:
    if (culstering_cost([x],[updated_medoids[0]]) < culstering_cost([x],[updated_medoids[1]])):
        c1.append(x)
    else:
        c2.append(x)

print("Cluster1:",c1)
print("Cluster2:",c2)
















