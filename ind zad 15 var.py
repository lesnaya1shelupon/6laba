print("Введите сколько команда забила в каждом из 26 матчей 1 сезона:")
a = tuple(map(int, input().split()))
print("Введите сколько команда забила в каждом из 26 матчей 2 сезона:")
b = tuple(map(int, input().split()))
sum = 0

if len(a) != 26 and len(b) != 26:
    print("Неверный размер списка", file=sys.stderr)
    exit(1)

for i in a:
    sum += i

for l in b:
    sum += l

print("Общее количество голов в двух сезонах: ", sum)
