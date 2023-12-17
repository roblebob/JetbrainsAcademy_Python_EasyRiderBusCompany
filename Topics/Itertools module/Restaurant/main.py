import itertools


zip_main = zip(main_courses, price_main_courses)
zip_desserts = zip(desserts, price_desserts)
zip_drinks = zip(drinks, price_drinks)

for _main, _dessert, _drinks  in itertools.product(zip_main, zip_desserts, zip_drinks):
    _sum = sum([_main[1], _dessert[1], _drinks[1]])
    if _sum <= 30:
        print(f'{_main[0]} {_dessert[0]} {_drinks[0]} {_sum}')
