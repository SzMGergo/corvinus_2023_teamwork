import pandas as pd
import utils as u

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
    def get_returns_of_etfs(self):

        pass


    def calculate_var(self):
        pass
