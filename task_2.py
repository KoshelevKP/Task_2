cook_book = {}

with open('cook book.txt') as f:

    for line in f:

        name = line.strip()
        cook_book[name] = list()

        number_ingredients = int(f.readline().strip())
        number = 0
        while number < number_ingredients:
            number += 1

            ingredients = f.readline().strip().split('|')
            cook_book[name].append({'ingridient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]})

        f.readline().strip()
 
        
def get_shop_list_by_dishes(dishes, person_count):

  shop_list = {}

  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingridient_name'] not in shop_list:
        shop_list[ingredient['ingridient_name']] = {'measure': ingredient['measure'], 'quantity': 0}
      shop_list[ingredient['ingridient_name']]['quantity'] += ingredient['quantity'] * person_count
  return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

for key, value in shop_list.items():
  print(key, value)
