# =========================
# LAMBDA DEMO
# =========================

# 1. Enkel lambda
square = lambda x: x * x
print("Kvadrat av 5:", square(5))


# 2. Lambda med två argument
add = lambda a, b: a + b
print("3 + 4 =", add(3, 4))


# 3. Lambda i list comprehension
numbers = [1, 2, 3, 4, 5]

squares = [(lambda x: x * x)(n) for n in numbers]
print("Kvadrater:", squares)


# 4. Lambda + filter (viktig kombination)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Jämna tal:", evens)


# 5. Lambda + map
doubles = list(map(lambda x: x * 2, numbers))
print("Dubbla tal:", doubles)


# 6. Lambda för sortering
names = ["Jonas", "Anna", "Bo"]

sorted_names = sorted(names, key=lambda name: len(name))
print("Sorterade efter längd:", sorted_names)


# 7. Lambda med if/else
check_age = lambda age: "vuxen" if age >= 18 else "barn"
print("Ålder 15:", check_age(15))
print("Ålder 25:", check_age(25))
