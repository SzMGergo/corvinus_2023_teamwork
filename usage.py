import portfolio as p

d_weights = {'IEI': 0.6, 'VOO': 0.4}
pf_value = 100000
p1 = p.Portfolio(d_weights, pf_value)
print(p1.d_weights)