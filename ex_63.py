print('Farenheit\t Celsius')
print('------------------------')


for celsius in range(0, 110,10):
    farenheit = 9 / 5 * celsius + 32
    print(format(farenheit, '.1f'), '\t\t', celsius)