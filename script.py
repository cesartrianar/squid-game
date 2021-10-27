# Marbles Game

import random

muertes_ali = 0
muertes_sang = 0
turno = random.randint(0, 1)

for i in range(1000):
  canicas1 = 19 # Canicas de Ali >> p1 >> Player 1
  canicas2 = 1 # Canicas de Sang >> p2 >> Player 2
  while canicas1 > 0 and canicas2 > 0:
    if turno == 0:
      p1 = random.randint(1, 2)
      p2 = random.randint(1, 2)
      if p1 == p2:
        canicas1 += 1
        canicas2 -= 1
        turno = 1
      else:
        canicas1 -= 1
        canicas2 += 1
        turno = 1
    else:
      p1 = random.randint(1, 2)
      p2 = random.randint(1, 2)
      if p1 == p2:
        canicas2 += 1
        canicas1 -= 1
        turno = 0
      else:
        canicas2 -= 1
        canicas1 += 1
        turno = 0
  else:
    if canicas1 == 0:
      muertes_ali += 1
    elif canicas2 == 0:
      muertes_sang += 1

print(f'ALI muere {muertes_ali} veces. Muere el {(muertes_ali / (i + 1)) * 100 :.2f}% de las veces.')
print(f'SANG muere {muertes_sang} veces. Muere el {(muertes_sang / (i + 1)) * 100 :.2f}% de las veces.')
