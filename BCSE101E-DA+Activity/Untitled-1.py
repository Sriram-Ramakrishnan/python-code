
total = int(input())
step = int(input())
people = []
for i in range(total):
    people.append(i+1)
index = 0
while len(people) >= 2:
    index = (index + step-1) % len(people)
    print(people.pop(index))

for i in people:
    print("\n",i)
            