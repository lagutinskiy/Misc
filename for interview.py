new_list = [i for i in range(15) if i % 2 == 0]
print(new_list)

for _ in range(10):
    print("**")

print((lambda x, y: x**y) (2,16))