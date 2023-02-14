a = [1, 3, 4, 5, 7, 7, 11, 7, 11, 12, 12, 13, 14]
b, d = [], []
for i in range(len(a)):
    if len(a) > i+1:
        if a[i] - a[i+1] < 0:
            b.append(f"{(-1)*(a[i] - a[i+1])} ({a[i]} va {a[i+1]})")
        else:
            b.append(f"{a[i] - a[i+1]} ({a[i]} va {a[i+1]})")
for i in b:
    d.append(i.split()[0])

for i in b:
    if i.split()[0] == max(d):
        print(i, end=",  ")








