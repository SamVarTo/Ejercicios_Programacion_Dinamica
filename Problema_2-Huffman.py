# Palabras y frecuencias
frecuencias = {
    "INFO": 120,
    "DEBUG": 80,
    "ERROR": 45,
    "WARN": 30,
    "TRACE": 15
}

# Códigos dados (según árbol construido)
codigos = {
    "INFO": "0",
    "DEBUG": "10",
    "ERROR": "110",
    "WARN": "1110",
    "TRACE": "1111"
}

# Longitud de cada palabra (para ASCII)
longitudes = {
    "INFO": 4,
    "DEBUG": 5,
    "ERROR": 5,
    "WARN": 4,
    "TRACE": 5
}

# ===== SIN COMPRESIÓN =====
sin_compresion = 0

for palabra in frecuencias:
    bits = longitudes[palabra] * 8 * frecuencias[palabra]
    sin_compresion += bits

print("Bits sin compresión:", sin_compresion)

# ===== CON HUFFMAN =====
con_huffman = 0

for palabra in frecuencias:
    bits = len(codigos[palabra]) * frecuencias[palabra]
    con_huffman += bits

print("Bits con Huffman:", con_huffman)

# ===== AHORRO =====
ahorro = (sin_compresion - con_huffman) / sin_compresion * 100

print("Ahorro (%):", round(ahorro, 2))