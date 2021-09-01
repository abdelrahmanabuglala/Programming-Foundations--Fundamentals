def favorite_city(name):
    if name == 1 :
        print("one of my favorite cities is Damietta")

    if name == 2 :
        print("one of my favorite cities is Alexandria")

    if name == 3 :
        print("one of my favorite cities is Beni Suef")

x = input("enter a number from 1 to 3 : \n")
if x == '1' :
    favorite_city(1)

if x == '2' :
    favorite_city(2)
    
if x == '3' :
    favorite_city(3)




