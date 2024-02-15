# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:39:00 2024

@author: chris
"""

import streamlit as st
from scipy.optimize import root

# custom packages
import default_probability_calculator as dpc

# Main page title
st.title("Default Probability Calculator")

# Sidebar streamlit
st.sidebar.title("Parameters")

# user inputs on sidebar
coupon_rate = st.sidebar.slider('Coupon Rate (in %)', value=5, 
                                min_value=0, max_value=30)

coupon_rate = coupon_rate / 100

risk_free = st.sidebar.slider('Risk Free Rate (in %)', value=5, 
                      min_value=0, max_value=20)

risk_free = risk_free / 100

T = st.sidebar.slider('Maturity in years', value=5, 
                      min_value=1, max_value=50)

par_value = st.sidebar.number_input('Enter the par value of the bond', 100)
st.write('The par value chosen is ', par_value)

market_price = st.sidebar.number_input('Enter the market price of the bond', 
                                       100)

st.write('The market price chosen is ', market_price)


result = root(fun=dpc.find_default_probability,
              x0=0.05,
              args=(coupon_rate, risk_free, T, par_value, False, market_price)
              )

table_cf = dpc.calculate_bond_value(distress_prob=result.x[0],
                                    coupon_rate=coupon_rate,
                                    risk_free_rate=risk_free,
                                    maturity=T,
                                    par_value=par_value,
                                    display_cf=True)

# back to main body
st.header("*Default probability calculator based on bond market price*")
st.markdown("Full table of bond cash flows")
st.dataframe(table_cf)

# display calculated values
st.markdown("Implied default rate obtained")
st.write("Default Probability: ", round(result.x[0], 4))

