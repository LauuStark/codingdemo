candy_list = ["Palanquetas","Glorias","Ate","Mueganos","Cocada"]



allowance = 5

candy_cart = []





for x in range(len(candy_list)):
    print("[" + str(x) + "] " + candy_list[x])


for x in range(allowance):
    candy = input("Which candy would you like? ")

    candy_cart.append(candy_list[int(candy)])

for candy in candy_cart:
    print(candy)


