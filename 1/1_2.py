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

result_array.sort(reverse=True)


# 210367
print(sum(result_array[0:3]))
