def makeSandwiches(name,*other_items, color="red",size=16):
    print(f"Making a {color} {name.title()} {size} inch-sized sandwich with the following toppings:")
    for toppings in other_items:
        print(f"[-] {toppings}")
makeSandwiches("Cake","green","onions","potash",color="Yellow",size=12)
