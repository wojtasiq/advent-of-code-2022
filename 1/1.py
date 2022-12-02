task = "1"
f = open(f"{task}/{task}.in", "r")

result_array = []
tmp_array = []

for line in f:
    if line != "\n":
        tmp_array.append(int(line))
    else:
        result_array.append(sum(tmp_array))
        tmp_array = []

f.close()

res_number = 0
res_order = 0

i = 1
for x in result_array:
    if x > res_number:
        res_number = x
        res_order = i
    i += 1

print(res_number)
