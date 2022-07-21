n,m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
s = 0
x = -1
y = 0
ry = n
rx = m+1
k = 1
while s < n*m:

#вправо
 rx -= 1
 for _ in range(rx):
  x += 1
  s += 1
  matrix[y][x] = str(s).ljust(3)
  
#низ 
 ry -= 1
 for _ in range(ry):
  y += 1
  s += 1
  matrix[y][x] = str(s).ljust(3)
  
 if s < n * m:
#влево
  rx -= 1
  for _ in range(rx):
   x -= 1
   s += 1
   matrix[y][x] = str(s).ljust(3)
   
#вверх
  ry -= 1
  for _ in range(ry):
   y -= 1
   s += 1
   matrix[y][x] = str(s).ljust(3)

 
for i in matrix:
  print(*i)