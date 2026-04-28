def greedy_cajero(monto, billetes):
    resultado = []

    for b in billetes:
        while monto >= b:
            resultado.append(b)
            monto -= b

    return resultado, monto


# Ejecución
billetes = [50000, 20000, 10000, 5000, 1000]
monto = 87500

res, restante = greedy_cajero(monto, billetes)

print("Billetes usados:", res)
print("Restante:", restante)