def go_buy(fruit_name, store_name='Walmart'):
    print('Going to ' + store_name)
    print('Buying ' + fruit_name)
    print('Going back home\n')


go_buy('Apple')
go_buy('Banana', 'Fortinos')
r = go_buy('Orange', 'Food Basics')
# print(r)  is none


def add(x, y):
    return x+y


total = add(10, 3)
print(total)
