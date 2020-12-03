"""
Ejercicio 3. programa que compruebe si una variable esta vacia y si esta vacia,
rellenaria con texto en minuscular y mostrarlo en mayusculas
"""

texto=""

if len(texto.strip())<=0:
    texto = "hola soy maria"
    print(texto.upper())
else:
    print(f"la variable tiene contenido {texto}")