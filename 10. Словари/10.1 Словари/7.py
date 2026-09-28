for i, j in stock.items():
    c = "отсутствует" if j == 0 else f"остаток: {j} шт"
    print(f"Товар: {i}, {c}")
