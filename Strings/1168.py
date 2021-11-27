leds = {
    '1' : 2, '2' : 5, '3' : 5,
    '4' : 4, '5' : 5, '6' : 6,
    '7' : 3, '8' : 7, '9' : 6,
    '0' : 6    
}
n_termos = int(input())
for i in range(n_termos):
    entrada = str(input())
    total_leds = 0
    for numero in entrada:
        if numero in leds:
            total_leds += leds[numero]
    print(f'{total_leds} leds')
