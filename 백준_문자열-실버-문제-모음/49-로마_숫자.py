#https://jrc-park.tistory.com/248
order_lst = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
value_lst = [1, 5, 10, 50, 100, 500, 1000]

alhpa_to_value = {i:j for i,j in  zip(order_lst, value_lst)}
value_to_alpha = {i:j for i,j in  zip(value_lst, order_lst)}

a = input().strip()
b = input().strip()


value = 0
for v in [a,b]:
    value += alhpa_to_value[v[-1]]
    for i in range(len(v)-1):
        if alhpa_to_value[v[i]] < alhpa_to_value[v[i+1]]:
            value -= alhpa_to_value[v[i]]
        else:
            value += alhpa_to_value[v[i]]

print(value)

for v in value_lst[::-1]:
    while value>=v:
        if str(value)[0] == "4":
            value -= 4*v 
            print(value_to_alpha[v], end="")
            print(value_to_alpha[v*5], end="")
        elif str(value)[0] == "9":
            v //= 5
            value -= 9*v 
            print(value_to_alpha[v], end="")
            print(value_to_alpha[v*10], end="")
        else:
            value-=v
            print(value_to_alpha[v], end="")
