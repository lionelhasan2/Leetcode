# Use bin() to see what's happening
a = 5
b = 3
print(f"{a} = {bin(a)}")     # 5 = 0b101
print(f"{b} = {bin(b)}")     # 3 = 0b11
print(f"{a & b} = {bin(a & b)}")  # 1 = 0b1
print(f"{a | b} = {bin(a | b)}")  # 7 = 0b111
print(f"{a ^ b} = {bin(a ^ b)}")  # 6 = 0b110