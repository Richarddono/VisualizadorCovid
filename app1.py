from numpy.lib.function_base import rot90
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('darkgrid')

st.title("holi")
st.markdown("## Bienvenido al visualizador")
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")

## st.dataframe(df.head(10))

col1,col2=st.columns(2)


with col1:
    region = st.radio("region", df.Region.unique())
    st.markdown("Su seleccion es: "+region)
with col2:
    categoria = st.radio ("Categoria", df.Categoria.unique())
    st.markdown("Su seleccion es: " +categoria)

##region = st.radio("region", df.Region.unique())
##st.markdown("Su seleccion es: "+region)
##categoria = st.radio("Categoria",df.Categoria.unique())

##st.table(df.iloc[:,2:-1])

super_filtro = df[(df.Region==region)&(df.Categoria==categoria)]
st.dataframe(super_filtro)
fig,ax= plt.subplots()
to_plot=(super_filtro.iloc[:,2:-1])
ax.plot(to_plot.T)

ax.set_title(region)
ax.set_ylabel("casos")
ax.set_xlabel("Fecha")

ejeX=np.arange(0,super_filtro.shape[1]-2,38)
plt.xticks(ejeX,rotation=90)


st.pyplot(fig)


