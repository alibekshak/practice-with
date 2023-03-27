n = int(input("Enter number for matrix: "))
triangle = []

for i in range(n+1):
    triangle.append([1] + [0]*n) 



for i in range(1, n+1): # lines
    for j in range(1, i+1): # column
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]  #pascal triangle formula


# draw a triangle
for i in range(0, n+1):
    for j in range(0, n+1):
        print(triangle[i][j], end=" ")
    print() # line wrapping