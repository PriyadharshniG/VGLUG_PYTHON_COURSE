# set_membership.py
# Membership checking and subset/superset

A = {1, 2, 3, 4}
B = {2, 3}

print("Is 3 in A?", 3 in A)
print("Is 5 not in A?", 5 not in A)

# Subset and Superset
print("Is B a subset of A?", B.issubset(A))
print("Is A a superset of B?", A.issuperset(B))
