Px = abs(int(sum(x for x, y in processed) * 10_000))
Py = abs(int(sum(y for x, y in processed) * 10_000))

Q1 = abs(int(min(dist(cl1, cl2) for cl1 in processed for cl2 in processed if cl1 != cl2) * 10_000))
Q2 = abs(int(max(dist(cl1, cl2) for cl1 in processed for cl2 in processed if cl1 != cl2) * 10_000))

print(Px, Py)
print(Q1, Q2)