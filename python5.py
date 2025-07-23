while True:
    temperature = input('If you want to convert from Fahrenheit to Celsius type F, otherwise type C: ')
    if temperature.upper() == 'F':
        fah = input('Temperature in Fahrenheit: ')
        temp = int(fah)
        cel = (temp - 32) * (5/9)
        print(f'Temperature in Celsius: {cel:.2f}')
        break  # exit the loop after a valid conversion
    elif temperature.upper() == 'C':
        cels = input('Temperature in Celsius: ')
        temps = int(cels)
        fahr = (temps * (9/5)) + 32
        print(f'Temperature in Fahrenheit: {fahr:.2f}')
        break  # exit the loop after a valid conversion
    else:
        print('Invalid input. Please type F or C.')