products = [{'name': 'Bike', 'price': 100},
            {'name': 'TV', 'price': 200},
            {'name': 'Album', 'price': 10},
            {'name': 'Book', 'price': 5},
            {'name': 'Phone', 'price': 500},
            {'name': 'Computer', 'price': 1000} ]

prices = []
allprices = 0
remainprice = 0

for j in range(len(products)):
    prices.append(products[j]['price'])
    
for k in range(len(products)):
    if products[k]['price'] == min(prices):
        print("Cheap products: ", products[k]['name'], "price: ", products[k]['price'])
       
for l in range(len(products)):
    if products[l]['price'] == max(prices):
        print("expensive products: ", products[l]['name'], "price: ", products[l]['price'])
        
for m in range(len(products)):
    allprices += products[m]['price']

for n in range(len(products)):
    if products[n]['price'] > 10:
        remainprice += products[m]['price']
    
print('sum of all prices = ', allprices)
print('sum of all prices greater than 10 dollar = ', remainprice)

