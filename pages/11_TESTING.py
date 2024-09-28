# Streamlit app for PPCI travel times in Kent and Medway
# 22/02/2024 GU
# Page 1 for national PPCI activity and travel times

##############################################################################
#
#                  Package imports and initial data sources
#
##############################################################################

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.plotting import ColumnDataSource, figure, output_file, show, output_notebook
from bokeh.models import LinearInterpolator
from shapely import wkt
from shapely.geometry import Point
import seaborn as sbn
import numpy as np
import itertools
import streamlit as st
import time
import fiona 
# for time test
start_full = time.time()

##############################################################################
#
#              Functions for processing national activity data
#
##############################################################################

# Read zipfile containing ICB shapefile and .csv with population values, and merge for expanded shapefile
st.cache_data()
def get_icb_gdf(filename_geo, filename_pop):
    
    # Read ICB shapefile
    icb_gdf = gpd.read_file(filename_geo, crs='EPSG:27700')
    icb_gdf['ICB22NM'] = icb_gdf['ICB22NM'].str.replace('Integrated Care Board', 'ICB')
    
    # Read ICB population file
    icb_pop = pd.read_csv(filename_pop)
    icb_pop['Integrated Care Board'] = icb_pop['Integrated Care Board'].str.replace(' Of ',' of ')
    icb_pop['Integrated Care Board'] = icb_pop['Integrated Care Board'].str.replace(' The ',' the ')
    
    # Merge in population values
    icb_gdf = icb_gdf.merge(icb_pop, left_on='ICB22NM', right_on='Integrated Care Board')
    
    # Select columns and rename
    cols_to_keep = ['ICB22','ICB22NM','geometry','Projected population 2022/23','Region']
    icb_gdf = icb_gdf[cols_to_keep]
    icb_gdf.rename(columns={'ICB22':'ICB_code','ICB22NM':'ICB_name','Projected population 2022/23':'Population'}, inplace=True)
    
    # Calcualte area and population density for each ICB from the (multi)polygon
    icb_gdf['Area'] = icb_gdf['geometry'].area
    icb_gdf['Population_per_sq_km'] = 10**6 * icb_gdf['Population'] / icb_gdf['Area']
    
    return icb_gdf


##############################################################################
#
#               Inputs and creation of objects for output
#
##############################################################################

filename_geo = 'zip://./ICB_JUL_2022_EN_BGC_V3_-1460063858159520993.zip'
filename_pop = 'ICB_population.csv'
#icb_gdf = get_icb_gdf(filename_geo, filename_pop)

# TESTING
#icb_gdf = gpd.read_file(filename_geo)
st.write('Geopandas version ')
gpd.__version__

st.write('Fiona version')
fiona.__version__

#st.write(icb_gdf.head())

#@st.cache_data()
#def get_data():
#    df_raw = gpd.read_file(filename_geo)
#    df_raw = df_raw[df_raw['ICB22CD'] != 0]
#    return df_raw
#st.write(get_data())
# Works here, not in Streamlit



#filename_activity = 'output_national_ppci_2223.csv'
#filename_routino = 'actuals_from_to_routino.csv'
#activity_time_dist_df = get_activity_time_dist_df(filename_activity, filename_routino)
#icb_time_df = get_national_activity_icb(filename_activity, filename_routino)
#prov_gdf_filename = 'provider_locations.csv'
#prov_gdf = get_prov_gdf(prov_gdf_filename)
#national_activity_prov = get_national_activity_prov(filename_activity)
#national_activity_prov.set_index('Provider_Site_Code', inplace=True)
#icb_to_plot, prov_to_plot = national_activity_to_plot(national_activity_prov, icb_time_df, icb_gdf, prov_gdf, threshold=50)
##nat_median = get_national_median(filename_routino)
#icb_density_times_gdf = national_activity_to_plot(national_activity_prov, icb_time_df, icb_gdf, prov_gdf, threshold=50)[1].copy()
#icb_density_times_rank_df = get_density_times_icb_rank_df(icb_density_times_gdf).sort_values(by=['Travel_time_rank_asc'], ascending=False)
##sites_orig = ['RVV01', 'RVV09', 'RJ122', 'RJZ01']
#km_prov_filename = 'KM_Sites_Geog.csv'
#km_prov_gdf = get_prov_gdf(km_prov_filename)
#dict_sitecode_sitename = get_dict_sitecode_sitename(km_prov_gdf)
#km_lsoa_filename = 'km_lsoa_shapefile.csv'
#km_lsoa_gdf = get_lsoa_gdf(km_lsoa_filename)
#km_actuals_time_dist_df = get_km_actuals_time_dist_df(filename_activity, filename_routino)
#km_all_journeys_df = get_km_all_journeys_df(km_actuals_time_dist_df, km_lsoa_gdf)

##############################################################################
#
#                           Streamlit content
#
##############################################################################

st.title("Travel Times For PPCI in Kent and Medway")

st.markdown("We take as our base activity data all spells coded to the  "+
            "specialised service code NCBPS13F Adult Specialist Cardiac "+
            "Services: PPCI for ST-Elevation Myocardial Infarction in   "+
            "the year 2022/23 in England.")

#st.write("Nationally, based on Routino data, we see a mean travel time of "+
#         f"{activity_time_dist_df['time_min'].mean():.0f} minutes "+
#         f"and a median of {activity_time_dist_df['time_min'].median():.0f} minutes.")

#time_elapsed = time.time()
# st.write('Time elapsed '+str(round(time_elapsed - start_full,1)) + ' seconds')
# Display summary of traval times
#st.dataframe(activity_time_dist_df.describe([0, 0.25, 0.5, 0.75, 0.95]).round().astype(int))

#st.markdown("We map the travel times based on Routino data for the patient "+
 #           "home LSOA and the provider site postcode, showing the mean "+
 #           "travel time for each ICB")

#time_elapsed = time.time()
# st.write('Time elapsed '+str(round(time_elapsed - start_full,1)) + ' seconds')
# Plot the national map
#fig, ax = plot_national_icb_prov(icb_to_plot, prov_to_plot)
#st.pyplot(fig)

#st.write("Looking at travel times by ICB, we note a negative "+
#         "correlation between population density and mean travel time. "+
#         "")
#df_rank_to_show = icb_density_times_rank_df[['ICB_name',
#                                            'time_min',
#                                            'Travel_time_rank_asc',
#                                            'Pop_density_rank',
#                                            'Population_per_sq_km',
#                                            'Population'
#                                            ]].copy()
#df_rank_to_show[['time_min',
#                 'Travel_time_rank_asc',
#                 'Pop_density_rank',
#                 'Population_per_sq_km',
#                 'Population']
#                 ] = icb_density_times_rank_df[['time_min',
#                                                'Travel_time_rank_asc',
#                                                'Pop_density_rank',
#                                                'Population_per_sq_km',
#                                                'Population']
#                                                ].round().astype(int).copy()

#with st.expander("Ranked travel time and population density by ICB",
#                 expanded=False) :
#    st.dataframe(df_rank_to_show)
#time_elapsed = time.time()
# st.write('Time elapsed '+str(round(time_elapsed - start_full,1)) + ' seconds')
# Plot scatter plot for correaltion of population density and mean travel times
#fig = plot_density_times(icb_density_times_gdf)
#st.bokeh_chart(fig, use_container_width=True)

#st.write("We observe that Kent and Medway ICB ranks 37 out of 42 for PPCI travel times. "+
#         "Thus there is a case for considering a possible site or sites for new PPCI service "+
#         "in this area.") 



#end_full = time.time()
# st.write('Total time to run '+str(round(end_full - start_full,1)) + ' seconds')
