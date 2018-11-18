import numpy as np
import dataloader as dt
import gui

#T = [[50, 2, 9, 0.5], [30, 3, 8, 0.75], [40, 3, 8, 0.5], [30, 1, 7, 0.25]]
T = [[50, 3, 9, 0.5], [50, 3, 9, 0.5], [90, 10, 20, 1], [90, 10, 20, 1]]
W = [[0.25, 0, 0, 0], [0, 0.25, 0, 0], [0, 0, 0.25, 0], [0, 0, 0, 0.25]]
#filename = input()
print("Select Data Location")
T = dt.loadCsv(gui.openfile("DataFile"))
#filename = input()
print("Select Weight Location")
W = dt.loadCsv(gui.openfile("WeightFile"))
print("Matrix T = ")
print(np.array(T))
l1 = len(T)
l2 = len(T[0])

Q = []
Qapp = Q.append

for i in range(l1):
	Qapp([0] * l2)

for i in range(l2):
	mean = [(T[j][i] ** 2) for j in range(l1)]
	mean = sum(mean)
	mean = pow(mean, 0.5)

	for j in range(l1):
		Q[j][i] = T[j][i] / mean
		#print(T[j][i], mean, Q[j][i])

Q = np.array(Q)
W = np.array(W)

#step 1 -> V = QW
V = np.dot(Q, W)
print("Matrix Q = ")
print(Q)
print("Matrix W = ")
print(W)
print("Matrix V = ")
print(V)
#print(Q, W, V)
#step 2 -> Calculate C & D
# cij = {k | vik >= vjk}
# dij = {k | vik < vjk}
Cmap = []
Cmapp = Cmap.append
Dmap = []
Dmapp = Dmap.append
C = []
Capp = C.append
D = []
Dapp = D.append

for i in range(l1):
	Cmapp([[] for j in range(l1)])
	Dmapp([[] for j in range(l1)])
	Capp([0] * l1)
	Dapp([0] * l1)

for i in range(l1):
	for j in range(l1):
		if(i == j):
			continue
		for k in range(l2):
			#print(k, W)
			#print(W[0][0], Cmap, i, j)
			#print(Dmap)
			if(V[i][k] >= V[j][k]):
				Cmap[i][j].append(W[k][k])
				#Dmap[i][j].append(abs(V[i][k] - V[j][k]))
			else:
				Dmap[i][j].append(abs(V[i][k] - V[j][k]))
				#Cmap[i][j].append(W[k][k])

for i in range(l1):
	D[i][i] = -1
	C[i][i] = -1
	for j in range(l1):
		if(i == j):
			continue
		arr = [abs(V[i][k] - V[j][k]) for k in range(l2)]
		maxt = max(arr)

		try:
			maxd = max(Dmap[i][j])
			#print(maxd, maxt)
			if(maxt == 0):
				raise ValueError
			t = maxd / maxt
			#print(t)
			D[i][j] = t
		except ValueError:
			D[i][j] = -1
			pass

		try:
			sumc = sum(Cmap[i][j])
			C[i][j] = sumc
		except ValueError:
			C[i][j] = -1
			pass
		
		
		"""

		try:
			maxd = max(Dmap[j][i])
			if(maxt == 0):
				raise ValueError
			D[j][i] = maxd / maxt
		except ValueError:
			D[j][i] = -1
			pass
		
		try:
			sumc = sum(Cmap[j][i])
			C[j][i] = sumc
		except ValueError:
			C[j][i] = -1
			pass
		"""
		


C = np.array(C)
D = np.array(D)
I = np.ones([l1, l1])
print("Matrix C = ")
print(C)
print("Matrix D = ")
print(D)
D_dash = np.subtract(I, D)
print("Matrix D' = ")
print(D_dash)
A = np.multiply(C, D_dash)
print("Matrix A = ")
print(A)
E_dash = A
for i in range(l1):
	for j in range(l1):
		if(A[i][j] > 0):
			E_dash[i][j] = 1


s = [i for i in range(l1)]
s = set(s)
print("Matrix E' = ")
print(E_dash)
for i in range(l1):
	for j in range(l1):
		if(E_dash[i][j] == 1 and E_dash[j][i] != 1):
			print("A" + str(i), ">>", "A" + str(j))
			try:
				s.remove(j)
			except KeyError:
				pass

s = list(s)
print("best alternatives are", s)
#print(s)