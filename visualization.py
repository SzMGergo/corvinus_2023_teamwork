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



def covar_visualization(valami):

    pass

#komment


