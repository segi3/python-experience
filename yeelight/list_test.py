
colors = [
    ['red', 255, 0, 0],
    ['blue', 0, 255, 0]
]

print(colors[0][1])
inp = 'red'
if any(inp in color for color in colors):
    p = next(c for c in colors if c[0] == inp)
    print(p)
else:
    print('tidak ada')
