from pprint import pprint

array = []
maximum = 0
summary = []

arr = [[1, 8, 5, 9], [0, 4, 5, 8], [5, 4, 2, 0], [0, 6, 1, 2]]

for a in arr:
    for b in a:
        if b == max(a):
            summary.append(b)
while len(summary) > 0:
    a = summary.pop(0)
    arr[maximum][maximum] = a
    maximum += 1

pprint(arr)
