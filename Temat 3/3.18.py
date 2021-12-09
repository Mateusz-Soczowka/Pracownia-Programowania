init_amount = int(input('Enter the amount in PLN: '))
amount = init_amount

five = amount // 5
amount //= 5

two = amount // 2
amount //= 2

one = amount

print(f"The amount of PLN {init_amount} in coins:")
print(f'5 zł - {five}')
print(f'2 zł - {two}')
print(f'1 zł - {one}')