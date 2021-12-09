height=input('Height(cm): ')
height=int(height)
cm_in_inches = 0.3937008
inches = height * cm_in_inches
feet=int(inches/12)
inches=inches-(feet*12)
print(f'I am {height}cm tall, {feet} feet and {inches} inches.')