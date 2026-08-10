import random
from django.http import HttpResponse

names = ["Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana", "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai", "Diana", "Radu", "Laura", "Cristian", "Raluca", "Bianca"]

numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]


# View 1 - Nume ordonate alfabetic
def ordered_names(request):
    sorted_names = sorted(names)
    return HttpResponse(", ".join(sorted_names))


# View 2 - Numere ordonate descrescator
def ordered_numbers(request):
    sorted_numbers = sorted(numbers, reverse=True)
    return HttpResponse(str(sorted_numbers))


# View 3 - Perechi nume + count random
def paired_names(request):
    paired = []
    for name in names:
        paired.append({
            "name": name,
            "count": random.choice(numbers)
        })
    return HttpResponse(str(paired))