# Streamlit app for PPCI travel times in Kent and Medway
# 11/03/2024 GU
# Page 5 for conclusions on optimal new site configurations 

##############################################################################
#
#                  Package imports and initial data sources
#
##############################################################################

#import geopandas as gpd
#import matplotlib.pyplot as plt
#import pandas as pd
#from bokeh.plotting import ColumnDataSource, figure, output_file, show, output_notebook
#from bokeh.models import LinearInterpolator
#from shapely import wkt
#from shapely.geometry import Point
#import seaborn as sbn
#import numpy as np
#import itertools
import streamlit as st
#import time
from PIL import Image
import os

st.title('Conclusions')

#st.write('Here we show optimal configurations for 1 or 2 sites')
site_count = st.radio('Select number of additional sites to see '+
                      'optimal configuration',
                      ('One', 'Two'),
                      horizontal = True)

if site_count == 'One' :
    st.markdown('### The optimal configuration with 1 additional site is '+
                'the addition of RWF03: The Maidstone Hospital')
                
    st.markdown('* Median travel time for Kent and Medway patients reduced '+
                'from 34 to 21 minutes.')
    
    rwf03_kde = Image.open(os.getcwd()+'/RWF03_kde.png')
    st.image(rwf03_kde)
    
    rwf03_times = Image.open(os.getcwd()+'/RWF03_times.png')
    st.image(rwf03_times)
    
    st.markdown('* Travel times would be reduced for 53% of the Kent and '+
                'Medway patients, based on historic activity.')
    
    rwf03_impact = Image.open(os.getcwd()+'/RWF03_impact.png')
    st.image(rwf03_impact)
    
    st.markdown('* Travel times would be reduced to less than the national '+
                'median for 23% of the Kent and Medway patients, '+
                'based on historic activity.')
    
    rwf03_threshold = Image.open(os.getcwd()+'/RWF03_threshold.png')
    st.image(rwf03_threshold)
    
    st.markdown('* Mean travel time reduction would be 15 minutes.')
    
    st.markdown('* Total travel distance (1 way) reduction would be 28,673 '+
                'km for the period of actuals considered.')
    st.markdown('* The new maximum travel time would be 56 minutes.')
    
if site_count == 'Two' :
    st.markdown('### The optimal configuration with 2 additional sites is '+
                'the addition of RWF03: The Maidstone Hospital and RVVKC: '+
                'Kent & Canterbury Hospital')
                
    st.markdown('* Median travel time for Kent and Medway patients reduced '+
             'from 34 to 17 minutes.')
    
    RWF03_RVVKC_kde = Image.open(os.getcwd()+'/RWF03-RVVKC_kde.png')
    st.image(RWF03_RVVKC_kde)
    
    RWF03_RVVKC_times = Image.open(os.getcwd()+'/RWF03-RVVKC_times.png')
    st.image(RWF03_RVVKC_times)
    
    st.markdown('* Travel times would be reduced for 80% of the Kent and '+
                'Medway patients, based on historic activity.')
    
    RWF03_RVVKC_impact = Image.open(os.getcwd()+'/RWF03-RVVKC_impact.png')
    st.image(RWF03_RVVKC_impact)
    
    st.markdown('* Travel times would be reduced to less than the national '+
                'median for 35% of the Kent and Medway patients, '+
                'based on historic activity.')
    
    RWF03_RVVKC_threshold = Image.open(os.getcwd()+'/RWF03-RVVKC_threshold.png')
    st.image(RWF03_RVVKC_threshold)
    
    st.markdown('* Mean travel time reduction would be 20 minutes.')
    
    st.markdown('* Total travel distance (1 way) reduction would be 38,927 '+
                'km for the period of actuals considered.')
    st.markdown('* The new maximum travel time would be 35 minutes.')
