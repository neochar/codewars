
# x - chickens
# y - cows

# legs = 2*x + 4*y
# heads = x + y

# x = (legs - 4*y) / 2 (1)
# x = heads - y

# (legs - 4*y) / 2 = heads - y
# (legs - 4*y) = 2*heads - 2*y
# 2*y = legs - 2*heads
# y = legs / 2 - heads (2)

heads = 72
legs = 200

cows = legs // 2 - heads
chickens = (legs - 4 * cows) // 2
chickens = (4 * heads - legs) // 2

print("Cows: {}\nChickens: {}".format(
    cows,
    chickens
    ))
