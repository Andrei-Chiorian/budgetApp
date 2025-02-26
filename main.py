from category import Category, create_spend_chart

food = Category('food')
tobaco = Category('tobaco')
coche = Category('coche')
dentista = Category('dentista')

tobaco.deposit(100, 'deposito')
tobaco.withdraw(5.40, 'marlboro 23/10')
tobaco.withdraw(5.25, 'Camel 22/10')
tobaco.withdraw(5.40, 'marlboro 21/10')
tobaco.withdraw(5.25, 'Camel 20/10')
tobaco.withdraw(6.50, 'marlboro 24 17/10')

food.deposit(1000, 'deposito')
food.withdraw(250, 'galletas')
food.withdraw(250, 'carne')

coche.deposit(2000, 'deposito')
coche.withdraw(1200, 'embrague')
coche.withdraw(560, 'cambio de aceite y filtros')

dentista.deposit(100, 'deposito')
dentista.withdraw(50, 'muela')

print(food)
print()
print(tobaco)
print()
print(coche)
print()
print(dentista)
print()
print(create_spend_chart([food, tobaco, coche, dentista]))
