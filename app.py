import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def get_data():
    return pd.read_csv("http://www.fa-technik.adfc.de/code/opengeodb/DE.tab", sep='\t', usecols=['lon', 'lat', 'name']).dropna().drop_duplicates().reset_index(drop=True)

df_all = get_data()
suffix = st.text_input("Endung (z.B. ow, in, ing, dorf, bach, hausen, heim, ...):", value='heim')
df = df_all[df_all['name'].str.lower().str.endswith(suffix.lower())]

fig = px.scatter_mapbox(df,
                        lon='lon', lat='lat',
                        hover_name='name',
                        title=f"Gemeinden, deren Name auf '{suffix}' endet:",
                        mapbox_style='carto-positron',
                        center={'lat': 51, 'lon':10.35}, zoom=4.8,
                        height=700, width=700)
st.write(fig)
st.caption("Datenquelle: http://www.fa-technik.adfc.de/code/opengeodb/DE.tab")
