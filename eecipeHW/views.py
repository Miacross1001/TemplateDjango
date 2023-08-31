from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    servings = int(request.GET.get('servings', 1))
    ing = list(DATA['omlet'].keys())
    val = list(DATA['omlet'].values())
    result = []
    if servings > 1:
        for e in val:
            result.append(e * servings)
    else:
        result = val

    context = {
        'recipe': dict(zip(ing, result)),
        'servings': servings,
    }

    return render(request, 'index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))
    ing = list(DATA['pasta'].keys())
    val = list(DATA['pasta'].values())
    result = []
    if servings > 1:
        for e in val:
            result.append(e * servings)
    else:
        result = val

    context = {
        'recipe': dict(zip(ing, result)),
        'servings': servings,
    }

    return render(request, 'index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))
    ing = list(DATA['buter'].keys())
    val = list(DATA['buter'].values())
    result = []
    if servings > 1:
        for e in val:
            result.append(e * servings)
    else:
        result = val

    context = {
        'recipe': dict(zip(ing, result)),
        'servings': servings,
    }

    return render(request, 'index.html', context)