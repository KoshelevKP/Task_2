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
            cook_book[name].append({'ingridient_name': ingredients[0].replace(" ", ""),
                                    'quantity': int(ingredients[1].replace(" ", "")),
                                    'measure': ingredients[2].replace(" ", "")})

        f.readline()
 
        
def get_shop_list_by_dishes(cook_book, dishes, person_count):

  shop_list = {}

  for dish in dishes:
    for ingredient in cook_book[dish]:
      ingridient_name = ingredient['ingridient_name']
      if ingridient_name not in shop_list:
        shop_list[ingridient_name] = {'measure': ingredient['measure'], 'quantity': 0}
      shop_list[ingridient_name]['quantity'] += ingredient['quantity'] * person_count
  return shop_list

shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)

for key, value in shop_list.items():
  print(key, value)