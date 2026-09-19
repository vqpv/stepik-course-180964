names = set(input().split())

for name in list(names):
    if name.startswith("Р"):
        names.discard(name)

names.add("Алон")
names.add("Эйли")

print(sorted(names))
