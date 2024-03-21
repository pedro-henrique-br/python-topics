num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print("{:.1f}".format(divisao))
print(f"{divisao:.2f}")

name = "Pedro Henrique"

print(f"{name:.10s}")
print(len(name))
print(f"{name:@<15}")

name_format = "{:@<15}".format(name)

print(name_format)

num_3 = 1000

num_3 = int(num_3)

print(f"{num_3:d}")
print(f"{num_3:0>10}")
print(f"{num_3:0>10.2f}")

n1 = "{n1:@<15}gmail.com".format(n1 = name)

print(n1)

name = "Pedro"
last_name = "Henrique"

last_name_format = "{1}".format(name, last_name)

print(last_name_format)

