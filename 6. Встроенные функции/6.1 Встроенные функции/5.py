print(f'''Название: {data[0]}
Количество: {sum(map(int, data[1]))}
Описание товара: {", ".join(data[2])}
Средняя цена: {round(sum(map(float, data[3])) / len(data[3]))}
Отзыв: {data[4]}''')
