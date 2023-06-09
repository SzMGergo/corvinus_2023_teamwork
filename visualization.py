import utils as u
import matplotlib.pyplot as plt


def plot_multiple_vars_for_one_conf(
    d_weights, pf_value, conf_level,
    from_date, to_date, window_in_days,
    show=True):

    l_conf_levels = [conf_level]

    df_var_hist = u.calc_var_for_period('hist',
                pf_value, d_weights, l_conf_levels,
                from_date, to_date, window_in_days)
    df_var_hist.columns = ['hist']

    df_var_covar = u.calc_var_for_period('covar',
        pf_value, d_weights, l_conf_levels,
        from_date, to_date, window_in_days)
    df_var_covar.columns = ['covar']

    ax = df_var_hist.plot()
    df_var_covar.plot(ax=ax)
    plt.title('VaR values for ' + str(conf_level))

    if show:
        plt.show()

def plot_one_var_for_multiple_conf_level(
    d_weights, pf_value, vartype, l_conf_levels,
    from_date, to_date, window_in_days,
    show=True):


    df_var = u.calc_var_for_period(vartype, pf_value,
                                       d_weights, l_conf_levels,
                                       from_date, to_date, window_in_days)

    df_var.plot()
    plt.title(vartype + ' VaR values, with weights:' + str(d_weights))
    plt.ylabel('VaR in USD')
    if show:
        plt.show()


# d_weights = {'IEI': 0.6, 'VOO': 0.4}
# pf_value = 10000
# conf_level = 0.99
# from_date = '2020-03-01'
# to_date = '2020-04-01'
# window_in_days = 250
# vartype='simple'
# l_conf_levels = [0.95, 0.99]
#
# plot_multiple_vars_for_one_conf(d_weights, pf_value, conf_level,
#     from_date, to_date, window_in_days,
#     show=True)
#
# plot_one_var_for_multiple_conf_level(
#     d_weights, pf_value, vartype, l_conf_levels,
#     from_date, to_date, window_in_days,
#     show=True)




