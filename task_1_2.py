from pprint import pprint


with open('recepies.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingridients_count = int(file.readline().strip())
        dish = []
        for _ in range(ingridients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dish.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = dish
pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                ingr = ingridient['ingredient_name']
                list_by_dishes[ingr] = {'measure': ingridient['measure'],
                                        'quantity': int(ingridient['quantity']) * person_count}
        else:
            print(f'Блюдо "{dish.capitalize()}" отсутствует в книге рецептов.')
            continue
    pprint(list_by_dishes)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Яблочный пирог'], 2)
