name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts = dict()
handle = open(name)
for line in handle:
    if not line.startswith('From '):
        continue
    mail = line.strip().split()[1]
    counts[mail] = counts.get(mail, 0) + 1

biggest = -1
person = None
for k, v in counts.items():
    if v > biggest:
        biggest = v
        person = k
        
print(person, biggest)
