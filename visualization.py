import utils as u
import matplotlib.pyplot as plt

d_weights = {'IEI': 0.6, 'VOO': 0.4}
pf_value = 10000
l_conf_levels = [0.99]
from_date = '2020-03-01'
to_date = '2020-04-01'
window_in_days = 250

df_var_hist = u.calc_var_for_period('hist',
                                               pf_value, d_weights, l_conf_levels,
                                               from_date, to_date, window_in_days)
df_var_hist.columns = ['hist']

df_var_simple = u.calc_var_for_period('simple',
                                               pf_value, d_weights, l_conf_levels,
                                               from_date, to_date, window_in_days)
df_var_simple.columns = ['simple']

df_var_covar = u.calc_var_for_period('covar',
                                               pf_value, d_weights, l_conf_levels,
                                               from_date, to_date, window_in_days)
df_var_covar.columns = ['covar']

ax = df_var_hist.plot()
df_var_simple.plot(ax=ax)
df_var_covar.plot(ax=ax)
plt.show()

def covar_visualization(valami):

    pass

#komment


