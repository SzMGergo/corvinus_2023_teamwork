import pandas as pd
import utils as u
import numpy as np

class Portfolio():

    def __init__(self, d_weights, pf_value):
        self.d_weights = d_weights
        self.pf_value = pf_value


    # parameters: from date to date
    def get_pf_returns(self, from_date, to_date):
        pf_return = u.get_portfolio_return_btw_dates(self.d_weights, from_date, to_date)
        return pf_return

    # parameters: from date to date
    def get_returns_of_etfs(self, d_weights, from_date, to_date):
        filtered_df=u.get_joined_returns(d_weights, from_date=None, to_date=None)
        return filtered_df


    def calculate_var(self):
        pass
