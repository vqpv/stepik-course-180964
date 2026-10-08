filtered_persons = filter(lambda x: x['rating'] >= 4.5, persons)

sorted_persons = sorted(filtered_persons, key=lambda x: x['name'])

for i in sorted_persons:
    print(i['name'])
