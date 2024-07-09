from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'jackie_welles': {
        'бокал рокс / олд фэшнд со льдом, шт': 1,
        'водка, мл.': 50,
        'имбирное пиво, мл': 75,
        'сок лайма, мл': 15,
        'капелька любви': 1,
    },
    'python': {
        'ром светлый, мл': 50,
        'мятный ликер, мл' : 30,
        'ананас сок, мл': 30,
        'сок лимона, мл': 35,
        'спрайт или 7up, мл': 55,
    }
    # можете добавить свои рецепты ;)
}

def recipes(request, dish):
    if dish in DATA:
        servings = request.GET.get('servings', '1')
        if servings.isdigit():
            servings = int(servings)
        else:
            servings = 1
        target_dish = DATA[dish].copy()
        for key in target_dish:
            target_dish[key] = target_dish[key] * servings

        context = {
            'recipe': target_dish,
            'name': dish
            }

    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
