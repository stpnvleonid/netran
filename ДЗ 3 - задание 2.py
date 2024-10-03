boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
res = list(zip(sorted(boys),sorted(girls)))
for para in res:
    print(para[0],'и',para[1])