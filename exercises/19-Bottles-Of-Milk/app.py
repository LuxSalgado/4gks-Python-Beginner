def number_of_bottles():
    t = 99
    for i in range(0,100):
        if t == 2:
            print(str(t)+" bottles of milk on the wall, "+str(t)+" bottles of milk.")
            t = t-1
            print("Take one down and pass it around, "+str(t)+" bottle of milk on the wall.")
        elif t == 1:
            print(str(t)+" bottle of milk on the wall, "+str(t)+" bottle of milk.")
            t = t-1
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        elif t == 0:
            print("No more bottles of milk on the wall, no more bottles of milk.")
            t = 99
            print("Go to the store and buy some more, "+str(t)+" bottles of milk on the wall.")
        else:
            print(str(t)+" bottles of milk on the wall, "+str(t)+" bottles of milk.")
            t = t-1
            print("Take one down and pass it around, "+str(t)+" bottles of milk on the wall.")
    
number_of_bottles()