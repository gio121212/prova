even_squares = {x: x*x for x in range(11) if x%2 == 0}
print(even_squares.items())
for i in even_squares:
  print(even_squares[i])
print(even_squares.values())