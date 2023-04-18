import portfolio as p

d_weights = {'IEI': 0.6, 'VOO': 0.4}
pf_value = 100000
p1 = p.Portfolio(d_weights, pf_value)
print(p1.d_weights)

vartype = 'hist'
from_date = '2020-03-01'
to_date = '2021-03-01'
l_conf_levels = [0.95, 0.99]
window_in_days = 250


# print(p1.get_pf_returns(from_date, to_date))
# print(p1.get_returns_of_etfs(from_date, to_date))

print(p1.calculate_var(
    vartype, l_conf_levels,
    from_date, to_date, window_in_days))