
# multi35 = []

# for x in range(1,1000):
#     if x % 3 == 0 or x % 5 == 0:
#         multi35.append(x)


# print(len(multi35))
# print(multi35)

# multi35 = []
multi35 = 0

for x in range(1,1000):
    if x % 3 == 0:
        multi35 +=x
    elif x % 5 == 0:
        multi35 +=x

print(multi35)
