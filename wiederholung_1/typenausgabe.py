t_1 = type(42)
print(f" 42 hat den Typ {t_1}")
t_2 = type(4.2)
print(f" 4.2 hat den Typ {t_2}")
t_3 = type("42")
print(f'"42" hat den Typ {t_3}')
# Produziert einen Fehler, da mit 4, 2 zwei Argumente übergeben werden.
# type erlaubt aber nur ein Argument
# t_4 = type(4, 2)
# Besser:
t_4 = type((4, 2))
print(f'(4, 2) hat den Typ {t_4}')
