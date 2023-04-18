import unittest
import utils as u

class Sajat(unittest.TestCase):

    def test_calc_historical_var(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        pf_value = 100000
        l_conf_levels = [0.95, 0.99]
        last_day_of_interval = '2020-03-01'
        window_in_days = 250
        df_var, df_var_amount = u.calc_historical_var(pf_value, d_weights, l_conf_levels,
                              last_day_of_interval, window_in_days)
        self.assertAlmostEqual(df_var.values[0][0], -0.00429, 4)
        self.assertAlmostEqual(df_var.values[0][1], -0.01039, 4)
    ''''
    def test_get_portfolio_return_btw_dates(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        df = u.get_portfolio_return_btw_dates(
            d_weights, '2020-03-01', '2020-04-15')
        self.assertEqual(len(df.index), 32)
        self.assertAlmostEqual(32.1111, 32.1112, 3)
    '''
    def test_subtract_trading_date(self):
        result = u.subtract_trading_date('2023-03-28', 2)
        self.assertEqual(result, '2023-03-24')

    def test_calc_simple_var(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        pf_value = 100000
        l_conf_levels = [0.95, 0.99]
        last_day_of_interval = '2020-03-01'
        window_in_days = 250
        df_var, df_var_amount = u.calc_simple_var(pf_value, d_weights, l_conf_levels,
                              last_day_of_interval, window_in_days)
        self.assertAlmostEqual(df_var.values[0][0], -0.00429, 4)
        self.assertAlmostEqual(df_var.values[0][1], -0.01039, 4)



    def test_calc_covar_var(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        pf_value = 100000
        l_conf_levels = [0.95, 0.99]
        last_day_of_interval = '2020-03-01'
        window_in_days = 250
        df_var, df_var_amount = u.calc_covar_var(pf_value, d_weights, l_conf_levels,
                              last_day_of_interval, window_in_days)
        self.assertAlmostEqual(df_var.values[0][0], -0.00429, 4)
        self.assertAlmostEqual(df_var.values[0][1], -0.01039, 4)

    def test_calc_historical_var_for_period(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        pf_value = 100000
        l_conf_levels = [0.95, 0.99]
        from_date = '2020-03-01'
        to_date = '2020-04-01'
        window_in_days = 250
        df_var, df_var_amount = u.calc_historical_var_for_period(pf_value, d_weights, l_conf_levels,
                              from_date, to_date, window_in_days)
        self.assertAlmostEqual(df_var.values[0][0], -0.00429, 4)
        self.assertAlmostEqual(df_var.values[0][1], -0.01039, 4)

    def test_calc_var_for_period(self):
        d_weights = {'IEI': 0.6, 'VOO': 0.4}
        pf_value = 100000
        l_conf_levels = [0.95, 0.99]
        from_date = '2020-03-01'
        to_date = '2020-04-01'
        window_in_days = 250
        df_var, df_var_amount = u.calc_var_for_period('hist', pf_value, d_weights, l_conf_levels, from_date, to_date, window_in_days)
        self.assertAlmostEqual(df_var.values[0][0], -0.00429, 4)
        self.assertAlmostEqual(df_var.values[0][1], -0.01039, 4)
