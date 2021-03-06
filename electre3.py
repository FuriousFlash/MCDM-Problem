import numpy as np
import dataloader as dt
import gui
import copy as cp

#T = [[50, 2, 9, 0.5], [30, 3, 8, 0.75], [40, 3, 8, 0.5], [30, 1, 7, 0.25]]
T = [[50, 3, 9, 0.5], [50, 3, 9, 0.5], [90, 10, 20, 1], [90, 10, 20, 1]]
W = [[0.25, 0, 0, 0], [0, 0.25, 0, 0], [0, 0, 0.25, 0], [0, 0, 0, 0.25]]

#filename = input()
print("Select Data Location")
T = dt.loadCsv(gui.openfile("DataFile"))
#filename = input()
print("Select Weight Location")
W = dt.loadCsv(gui.openfile("WeightFile"))

print("Select Preferrence Parameter Location")
PM = dt.loadCsv(gui.openfile("PreferrenceFile"))

print("Select Indifferrence Parameter Location")
QM = dt.loadCsv(gui.openfile("IndifferrenceFile"))
print("Matrix T = ")
print(np.array(T))
l1 = len(T)
l2 = len(T[0])
"""
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
"""
W = np.array(W)

#step 1 -> V = QW
#V = np.dot(Q, W)
#print("Matrix Q = ")
#print(Q)
print("Matrix W = ")
print(W)
#print("Matrix V = ")
#print(V)
#print(Q, W, V)
#step 2 -> Calculate C & D
# cij = {k | vik >= vjk}
# dij = {k | vik < vjk}
Cplus = []
Cpapp = Cplus.append
Ceq = []
Ceapp = Ceq.append
Cmin = []
Cmapp = Cmin.append
Cmat = []
Ctapp = Cmat.append

Dplus = []
Dpapp = Dplus.append
Deq = []
Deapp = Deq.append
Dmin = []
Dmapp = Dmin.append
Dmat = []
Dtapp = Dmat.append
C = []
Capp = C.append
Cp = []
Cplapp = Cp.append
Cm = []
Cmiapp = Cm.append
D = []
Dapp = D.append
S = []
Sapp = S.append
Dm = []
Dmiapp = Dm.append
Ci = {}
Di = {}

for i in range(l1):
	Cpapp([[] for j in range(l1)])
	Ceapp([[] for j in range(l1)])
	Cmapp([[] for j in range(l1)])
	Ctapp([[] for j in range(l1)])
	Dpapp([[] for j in range(l1)])
	Deapp([[] for j in range(l1)])
	Dmapp([[] for j in range(l1)])
	Dtapp([[] for j in range(l1)])
	Capp([0] * l1)
	Cplapp([0] * l1)
	Cmiapp([0] * l1)
	Dapp([0] * l1)
	Sapp([0] * l1)
	Dmiapp([0] * l1)
	#Dapp([0] * l1)
#print(D)
"""
for i in range(l1):
	for j in range(l1):
		if(i == j):
			continue
		for k in range(l2):
			#print(k, W)
			#print(W[0][0], Cmap, i, j)
			#print(Dmap)
			if(V[i][k] > V[j][k]):
				Cplus[i][j].append(W[k][k])
				Dmin[i][j].append(abs(V[i][k] - V[j][k]))
				Cmat[i][j].append(W[k][k])
				#Dmap[i][j].append(abs(V[i][k] - V[j][k]))
			elif(V[i][k] == V[j][k]):
				Ceq[i][j].append(W[k][k])
				Cmat[i][j].append(W[k][k])
				Deq[i][j].append(abs(V[i][k] - V[j][k]))
			else:
				Cmin[i][j].append(W[k][k])
				Dmat[i][j].append(abs(V[i][k] - V[j][k]))
				Dplus[i][j].append(abs(V[i][k] - V[j][k]))
				#Cmap[i][j].append(W[k][k])
"""
for j in range(l2):
	Ci[j] = cp.deepcopy(C)
	Di[j] = cp.deepcopy(D)

for i in range(l1):
	for j in range(l1):
		if(i == j):
			continue
		indiff = 0
		Th = 0
		pref = 0
		for k in range(l2):
			if(QM[1][k] == 0):
				indiff = QM[0][k]
				Th = QM[2][k]
			else:
				indiff = QM[0][k] * T[i][k]
				indiff /= 100
				Th = QM[2][k] * T[i][k]
				Th /= 100
			if(PM[1][k] == 0):
				pref = PM[0][k]
			else:
				pref = PM[0][k] * T[i][k]
				pref /= 100
			
			if(T[i][k] + indiff >= T[j][k]):
				Ci[k][i][j] = 1
			elif(T[i][k] + pref <= T[j][k]):
				Ci[k][i][j] = 0

			if(T[j][k] <= T[i][k] + pref):
				Di[k][i][j] = 0
			elif(T[j][k] >= T[i][k] + Th):
				Di[k][i][j] = 1


for i in range(l1):
	for j in range(l1):
		if(i == j):
			C[i][j] = -1
			continue
		temp = 0
		for k in range(l2):
			temp += (Ci[k][i][j] * W[k][k])
		C[i][j] = temp
C = np.array(C)
print("Concordace Matrix C = ")
print(C)
for i in range(l1):
	for j in range(l1):
		if(i == j):
			S[i][j] = -1
			continue
		f1 = 1
		f2 = 1
		for k in range(l2):
			if(Di[k][i][j] > C[i][j]):
				f2 *= ((1 - Di[k][i][j]) / (1 - Ci[k][i][j]))
				f1 = 0
		S[i][j] = C[i][j]
		if(f1 == 0):
			S[i][j] *= f2
S = np.array(S)
print("Credibility Matrix S = ")
print(S)
s = [j for j in range(l1)]
s = set(s)
for i in range(l1):
	for j in range(i + 1, l1):
		if(S[i][j] > S[j][i]):
			if(abs(S[i][j] - S[j][i]) <= 0.0):
				print("A" + str(i), "= A" + str(j))
				try:
					s.remove(j)
				except KeyError:
					pass
			else:
				try:
					s.remove(j)
				except KeyError:
					pass
				print("A" + str(i), "> A" + str(j))
		elif(S[i][j] == S[j][i]):
			try:
				s.remove(j)
			except KeyError:
				pass
			print("A" + str(i), "= A" + str(j))
		else:
			if(abs(S[i][j] - S[j][i]) <= 0.0):
				print("A" + str(i), "= A" + str(j))
				try:
					s.remove(j)
				except KeyError:
					pass
			else:
				try:
					s.remove(i)
				except KeyError:
					pass
				print("A" + str(i), "< A" + str(j))

print("Best alternatives are:", s)
"""


for i in range(l1):
	D[i][i] = -1
	C[i][i] = -1
	for j in range(l1):
		if(i == j):
			continue
		arr = [abs(V[i][k] - V[j][k]) for k in range(l2)]
		maxt = max(arr)

		try:
			maxd = max(Dmat[i][j])
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
			sumc = sum(Cmat[i][j])
			C[i][j] = sumc
		except ValueError:
			C[i][j] = -1
			pass
		
		try:
			maxd = max(Dmin[i][j])
			#print(maxd, maxt)
			if(maxt == 0):
				raise ValueError
			t = maxd / maxt
			#print(t)
			Dm[i][j] = t
		except ValueError:
			Dm[i][j] = -1
			pass

		try:
			sumc = sum(Cmin[i][j])
			Cm[i][j] = sumc
		except ValueError:
			Cm[i][j] = -1
			pass

		try:
			maxd = max(Dplus[i][j])
			#print(maxd, maxt)
			if(maxt == 0):
				raise ValueError
			t = maxd / maxt
			#print(t)
			Dp[i][j] = t
		except ValueError:
			Dp[i][j] = -1
			pass

		try:
			sumc = sum(Cplus[i][j])
			Cp[i][j] = sumc
		except ValueError:
			Cp[i][j] = -1
			pass
		

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
		
"""
#Cp[1][0] = 1
#Cp[1]
C = np.array(C)
#Cm = np.array(Cm)
#Cp = np.array(Cp)
D = np.array(D)
#Dm = np.array(Dm)
#Dp = np.array(Dp)
#I = np.ones([l1, l1])
print("Matrix C = ")
print(C)
#print("Matrix C- = ")
#print(Cm)
#print("Matrix C* = ")
#print(Cp)
print("Matrix D = ")
print(D)
#print("Matrix D- = ")
#print(Dm)
#print("Matrix D* = ")
#print(Dp)
"""
"""
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
"""
"""
s = [i for i in range(l1)]
s = set(s)
for i in range(l1):
	for j in range(l1):
		if(C[i][j] >= Cp[i][j] and D[i][j] <= Dp[i][j] and C[i][j] >= C[j][i]):
			print("A" + str(i), ">>", "A" + str(j))
			try:
				s.remove(j)
			except KeyError:
				pass
		elif(C[i][j] >= Cm[i][j] and D[i][j] <= Dm[i][j] and C[i][j] >= C[j][i]):
			print("A" + str(i), ">", "A" + str(j))
			try:
				s.remove(j)
			except KeyError:
				pass

s = list(s)
print("best alternatives are", s)
#print(s
"""