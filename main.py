print('''__      __   _  _____      _      
\ \    / /  | |/ ____|    | |     
 \ \  / /__ | | |     __ _| | ___ 
  \ \/ / _ \| | |    / _` | |/ __|
   \  / (_) | | |___| (_| | | (__ 
    \/ \___/|_|\_____\__,_|_|\___|\n''')

print('-'*50)
print('----- List of Objects that VolCalc can Calculate;')
print('[1] cube')
print('[2] cylinder')
print('[3] Cone')
print('[4] Semi-Cone')
print('[5] sphere')
print('-'*50)

volume_total = []
while True:
    select_object = int(input('Type the number in the left of the object to calculate: '))
    if select_object == 1:
        comp = float(input('Length: '))
        larg = float(input('Width: '))
        altu = float(input('Height: '))
        volume = comp*larg*altu
        print(f'Volume: {volume:.2f} m³ ')
        volume_total.append(volume)
        break
    if select_object == 2: 
        dim = float(input('Diameter: '))
        altu = float(input('Height: '))
        raio_quadrado = (dim/2)**2
        pi = 3.1415
        volume = pi * raio_quadrado * altu
        print(f'Volume: {volume:.2f} m³')
        volume_total.append(volume)
        break
    if select_object == 3:
        altu  = float(input('Height: '))
        dim = float(input('Diameter: '))
        pi = 3.1415
        raio_quadrado = (dim/2)**2
        volume = pi * raio_quadrado * (altu/3)
        print(f'Volume: {volume:.2f} m³')
        volume_total.append(volume)
        break
    if select_object == 4:
        raio_me = float(input('Smaller radius: '))
        raio_ma = float(input('Larger radius: '))
        altura =float(input('Cone trunk height: '))
        pi = 3.141592654
        volume = ((pi*altura)/3) * ((raio_ma**2)+(raio_ma*raio_me)+(raio_me**2))
        print(f'Volume: {volume:.2f} m³')
        volume_total.append(volume)
        break
    if select_object == 5:
        diameter = float(input('Type the diameter: '))
        raio = diameter/2
        pi = 3.141592654
        volume = (4/3)*(pi)*(raio**3)
        print(f'Volume: {volume:.2f} m³')
        volume_total.append(volume)
    else:
        print('Option not avaliable...\n Please try again.')

