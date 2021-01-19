input_list = (input('Enter values: ')).split()
output_list = []
for k in input_list:
    if int(k) % 2 == 0:
        output_list.append(int(k))
print(output_list)
