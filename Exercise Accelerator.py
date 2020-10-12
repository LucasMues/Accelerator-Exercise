print("Task 1: Add 2+2")
print("2+2=?")

def add():
  return 2+2

result = add()
print("result:")
print(result)

print("Task 2: Multiplication of two 3x3 Matrices")

X=[[3,4,7],
   [6,4,9],
   [11,4,2]]
Y=[[9,6,3],
   [3,3,4],
   [2,12,7]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]
print("Matrix 1:")
for r in X:
    print(r)
print("Matrix 2:")
for r in Y:
    print(r)
print("results [X x Y:")
for r in result:
    print(r)
