#Primind această listă de numere:
#
#numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17],
#
#Si lista de persoane:
#
#people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]
#Creati o functie care returnează: o lista de dicționare, care arată astfel:
#
#result = { "name": "Codrin", "age": 30, "of_age": True}
#
#Pentru fiecare persoană, alegeți un număr random din lista de numere.
#Unde of_age este true doar daca numărul ales este mai mare de 18
#
#import random
#picked = random.choice(numbers)

#Creati o altă funcție care filtrează toate persoanele și returnează doar persoanele of_age.
#Creați oldest_person, o funcție care returnează cea mai bătrână persoană
#La fel și pentru youngest_person, cea mai tânără
#
#Printați acel rezultat.

import random

numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]

# Functia 1: genereaza lista de dictionare
def generate_people(people, numbers):
    result = []
    for person in people:
        age = random.choice(numbers)
        result.append({
            "name": person,
            "age": age,
            "of_age": age > 18
        })
    return result

# Functia 2: filtreaza doar persoanele of_age
def filter_of_age(people_list):
    return [p for p in people_list if p["of_age"]]

# Functia 3: cea mai batrana persoana
def oldest_person(people_list):
    return max(people_list, key=lambda p: p["age"])

# Functia 4: cea mai tanara persoana
def youngest_person(people_list):
    return min(people_list, key=lambda p: p["age"])


# --- Rulam tot ---
people_list = generate_people(people, numbers)

print("=== Lista completa ===")
for p in people_list:
    print(p)

print("\n=== Persoane of_age ===")
for p in filter_of_age(people_list):
    print(p)

print("\n=== Cea mai batrana persoana ===")
print(oldest_person(people_list))

print("\n=== Cea mai tanara persoana ===")
print(youngest_person(people_list))