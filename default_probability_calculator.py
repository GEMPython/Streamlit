# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:07:43 2024

@author: chris
"""

import numpy as np
import pandas as pd

def calculate_bond_value(distress_prob,
                         coupon_rate,
                         risk_free_rate,
                         maturity,
                         par_value,
                         display_cf):
    
    cf_array = np.ones(maturity)
    
    maturity_array = np.arange(start=1,
                               stop=maturity+1,
                               step=1
                               )

    cf_array = cf_array * par_value * coupon_rate
    cf_array[-1] += par_value
    
    cf_prob_array = cf_array * (1 - distress_prob) ** maturity_array

    cf_present_value = cf_prob_array / (1 + risk_free_rate) ** maturity_array
    
    if display_cf:
        
        results = pd.DataFrame({'Cash Flows': cf_array,
                                'Probabilistic Cash Flows': cf_prob_array,
                                'Discounted cash flows': cf_present_value},
                               index=np.arange(start=1, stop=maturity+1)
                               )
        results.index.name = 'Year'
        
    else:
        
        results = np.sum(cf_present_value)
        
    return results


def find_default_probability(distress_prob,
                             coupon_rate,
                             risk_free_rate,
                             maturity,
                             par_value,
                             display_cf,
                             market_price):
    
    bond_price = calculate_bond_value(distress_prob, 
                                      coupon_rate, 
                                      risk_free_rate, 
                                      maturity, 
                                      par_value,
                                      display_cf)
    
    return bond_price - market_price
    