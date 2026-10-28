n = 4

guess = input("Predict: how many item in the list fpr n = 4")
points= list(range(1,n+1))
print("your guess:", guess, "List:",points,"items:", len(points))

input("proddict: what happens to list size as n grows? presse enter ")
for size in [4,10,100,1000]:
    print(f"n = {size:<5}, list uses {size:>5} items in memory")