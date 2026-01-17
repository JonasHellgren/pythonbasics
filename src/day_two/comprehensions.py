# =========================
# LIST COMPREHENSION DEMO
# =========================

# 1. Skapa en lista med tal 1–10
numbers = [i for i in range(1, 11)]
print("Alla tal:", numbers)


# 2. Filtrera ut jämna tal
even_numbers = [n for n in numbers if n % 2 == 0]
print("Jämna tal:", even_numbers)


# 3. Skapa en lista med kvadrater av talen
squares = [n * n for n in numbers]
print("Kvadrater:", squares)


# 4. Kvadrater av ENDAST jämna tal
even_squares = [n * n for n in numbers if n % 2 == 0]
print("Kvadrater av jämna tal:", even_squares)


# 5. Märk varje tal som jämn eller udda
labels = ["jämn" if n % 2 == 0 else "udda" for n in numbers]
print("Jämn/Udda:", labels)


# 6. Omvandla strängar till heltal
text_numbers = ["1", "2", "3", "4"]
int_numbers = [int(x) for x in text_numbers]
print("Sträng → int:", int_numbers)


# 7. Jobba med strängar
words = ["python", "är", "kul"]
lengths = [len(word) for word in words]
print("Ordlängder:", lengths)


# 8. Mini-exempel med input
age_list = [10, 15, 18, 25, 30]

status = ["vuxen" if age >= 18 else "barn" for age in age_list]
print("Åldersstatus:", status)
