# day1 är en TUPLE
# → används för en fast, oföränderlig samling värden (en dags mätningar)
day1 = (8.5, 12.3, 10.1)

# measurements är en LIST
# → används för en samling av flera dagar som kan växa och ändras
measurements = []

# Vi lägger till day1 (tuple) i listan measurements
measurements.append(day1)

# Vi kan även lägga till fler tuples direkt
measurements.append((7.9, 11.4, 9.6))
measurements.append((6.8, 10.2, 8.7))

# Skriv ut alla mätningar
print(measurements)

# Åtkomst:
# measurements[0] → första dagen (tuple)
# measurements[0][1] → andra temperaturvärdet första dagen
print(measurements[0])
print(measurements[0][1])
