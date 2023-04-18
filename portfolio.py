import pandas as pd
import utils as u
import numpy as np

class Portfolio():

    def __init__(self, d_weights, pf_value):
        self.d_weights = d_weights
        self.pf_value = pf_value


    # parameters: from date to date
    def get_pf_returns(self, from_date, to_date):
        df_joined = u.get_joined_returns(self.d_weights, from_date, to_date)
        df_weighted_returns = df_joined * pd.Series(self.d_weights)
        s_portfolio_return = df_weighted_returns.sum(axis=1)
        return pd.DataFrame(s_portfolio_return, columns=['pf'])

    # parameters: from date to date
    def get_returns_of_etfs(etf_name,
                        return_type='log', fieldname='Adj Close'):

        df = u.read_etf_file(etf_name)
        df = df[[fieldname]]

        df['shifted'] = df.shift(1)
        if return_type == 'log':
            df['return'] = np.log(df[fieldname] / df['shifted'])
        if return_type == 'simple':
            df['return'] = df[fieldname] / df['shifted'] - 1

        # restrict df to result col
        df = df[['return']]
        # rename column
        df.columns = [etf_name]
        # df = df.rename(by=col, {'return': etf_name})
        return df


    def calculate_var(self):
        pass
