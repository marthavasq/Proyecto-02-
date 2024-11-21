import streamlit as st 
import streamlit as st 
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt 

# Usar Markdown con HTML y CSS para el diseño en cuadrícula
st.markdown("""
<style>
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Tres columnas de ancho igual */
    gap: 20px; /* Espaciado entre los elementos */
    padding: 20px;
}
.kpi-card {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra para destacar los KPIs */
}
.kpi-title {
    font-size: 20px;
    font-weight: bold;
    color: #333333;
    margin-bottom: 10px;
}
.kpi-value {
    font-size: 36px;
    font-weight: bold;
    color: #007BFF; /* Color azul para los valores */
}
.kpi-delta {
    font-size: 16px;
    color: green; /* Positivo en verde */
    margin-top: 5px;
}
</style>

<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-title">Acceso a internet</div>
        <div class="kpi-value">+02%</div>
        <div class="kpi-delta">cada 100 hogares</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Fibra Óptica</div>
        <div class="kpi-value">13.39%</div>
        <div class="kpi-delta" style="color: green;">Incremento nacional</div> <!-- Negativo en rojo -->
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Cablemodem</div>
        <div class="kpi-value">-1.99%</div>
        <div class="kpi-delta">Trimestre 2 (2024)</div>
    </div>
</div>
""", unsafe_allow_html=True)




#Botones debajo de los kpis
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Acceso a internet"):
        st.write("*Calculo: KPI = ((nuevo acceso - acceso actual) / acceso actual)* 100*")

with col2:
    if st.button("Fibra Óptica"):
        st.write("% = total de accesos con Fibra optica en el pais/total de accesos de todas las tecnologias en el pais x 100")

with col3:
    if st.button("Cablemodem"):
        st.write("Accesos cablemodem actual - accesos Cablemodem anterior / accesos cablemodem anterior x 100")






st.title("KPI1:")
st.markdown(" **Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia.** ")
st.markdown(" **Objetivo:** Medir el incremento en la penetracion de accesos a internet por cada 100 hogares.")



# Cargar el DataFrame
df_penetracion_totales = pd.read_csv (r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\penetracion_totales.csv")
df_penetracion_kpi = df_penetracion_totales

# Calcular los nuevos accesos y el KPI
df_penetracion_kpi['Nuevo acceso'] = df_penetracion_kpi['Accesos por cada 100 hogares'] * 1.02
df_penetracion_kpi['KPI (%)'] = ((df_penetracion_kpi['Nuevo acceso'] - df_penetracion_kpi['Accesos por cada 100 hogares']) / 
                                  df_penetracion_kpi['Accesos por cada 100 hogares']) * 100

# Crear gráfico interactivo con Plotly Express
fig = px.bar(
    df_penetracion_kpi,
    x='Trimestre',
    y=['Accesos por cada 100 hogares', 'Nuevo acceso'],
    color='Año',
    barmode='group',
    title='Proyección de Accesos por cada 100 Hogares y KPI',
    labels={
        'value': 'Accesos por cada 100 hogares',
        'Trimestre': 'Trimestre',
        'variable': 'Indicador'
    },
    text_auto='.2f',
)

# Personalizar diseño
fig.update_layout(
    xaxis_title='Trimestre',
    yaxis_title='Accesos por cada 100 hogares',
    legend_title='Indicador',
    title_font_size=16,
    template='plotly_white'
)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

# Mostrar tabla adicional con KPI
st.write("### Resumen de KPI:")
st.dataframe(df_penetracion_kpi[['Año', 'Trimestre', 'Accesos por cada 100 hogares', 'Nuevo acceso', 'KPI (%)']])


st.title("KPI: 2")
st.markdown(" **Participación de Fibra Óptica en el mercado total de accesos.** ")
st.markdown("**Objetivo:** cuantificar qué porcentaje de los accesos totales en un país utiliza la tecnología de Fibra Óptica, en comparación con otras tecnologías")

#DF FIBRA OPTICA 

accesos_por_tecnologia = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\accesos_por_tecnologia.csv")

tecnologias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']
totales_tecnologias = accesos_por_tecnologia[tecnologias].sum()

# Crear un DataFrame para la gráfica
data = pd.DataFrame({
    'Tecnología': tecnologias,
    'Accesos Totales': totales_tecnologias
})

# Crear gráfica de pastel interactiva
fig = px.pie(
    data,
    values='Accesos Totales',
    names='Tecnología',
    title='Distribución de Accesos por Tecnología',
    color_discrete_sequence=px.colors.qualitative.Pastel,
    hole=0.4  # Hace el gráfico un pastel tipo "donut"
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)




# Mostrar la participación nacional de Fibra Óptica como texto
total_fibra = accesos_por_tecnologia['Fibra óptica'].sum()
total_accesos = accesos_por_tecnologia['Total'].sum()
participacion_fibra = (total_fibra / total_accesos) * 100
st.write(f"**Participación nacional de Fibra Óptica:** {participacion_fibra:.2f}%")# Calcular el porcentaje de accesos por "Fibra óptica" respecto al total por provincia
accesos_por_tecnologia['Porcentaje_Fibra'] = (accesos_por_tecnologia['Fibra óptica'] / accesos_por_tecnologia['Total']) * 100

# Agrupar por provincia y calcular el promedio del porcentaje
porcentaje_fibra_provincia = accesos_por_tecnologia.groupby('Provincia')['Porcentaje_Fibra'].mean()

# Ordenar y seleccionar el top 5
top_5_provincias_fibra = porcentaje_fibra_provincia.sort_values(ascending=False).head(5).reset_index()

# Crear un gráfico interactivo con Plotly Express
fig = px.bar(
    top_5_provincias_fibra,
    x='Provincia',
    y='Porcentaje_Fibra',
    title='Top 5 Provincias con Mejor Porcentaje de Acceso a Internet (Fibra Óptica)',
    labels={'Porcentaje_Fibra': 'Porcentaje (%)', 'Provincia': 'Provincia'},
    text='Porcentaje_Fibra',
    color='Porcentaje_Fibra',
    color_continuous_scale='viridis'
)

# Personalizar el diseño del gráfico
fig.update_layout(
    xaxis_title="Provincia",
    yaxis_title="Porcentaje (%)",
    title_font_size=16,
    xaxis_tickangle=-45,
    template="simple_white",
)

# Mostrar el gráfico interactivo en Streamlit
st.plotly_chart(fig, use_container_width=True)












st.title("KPI: 3")
st.markdown(" **Crecimiento trimestral de accesos a cablemodem en comparación con Fibra Óptica y ADSL** ")
st.markdown("**Objetivo:** Identifica el crecimiento de Cablemodem en comparacion a otras tecnologías trimestralmente.")
# DF CABLEMODEM 

totales_accesos_tecnologia = pd.read_csv(r'C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\totales_accesos_tecnologia.csv')
totales_accesos_tecnologia = totales_accesos_tecnologia.dropna()
totales_accesos_tecnologia = totales_accesos_tecnologia.sort_values(by=['Año', 'Trimestre'])

# Calcular el crecimiento trimestral para Cablemodem
totales_accesos_tecnologia['Crecimiento_Cablemodem'] = (
    totales_accesos_tecnologia['Cablemodem'].pct_change() * 100
)

#grafico interactivo cablemodem
# Crear un gráfico interactivo con Plotly
fig = px.line(
    totales_accesos_tecnologia,
    x='Trimestre',
    y='Crecimiento_Cablemodem',
    color='Año',
    title="Crecimiento Trimestral de Cablemodem",
    markers=True,
    labels={'Crecimiento_Cablemodem': 'Crecimiento (%)'}
)

# Añadir interactividad
fig.update_traces(mode="lines+markers")
fig.update_layout(
    xaxis_title="Trimestres",
    yaxis_title="Crecimiento (%)",
    hovermode="x unified"
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Crear una checkbox para mostrar/ocultar la tabla cablemodem 
mostrar_datos = st.checkbox("Mostrar crecimiento trimestral del acceso por Cablemodem")

# Si la checkbox está marcada, mostrar la tabla
if mostrar_datos:
    st.write("Crecimiento trimestral del acceso por Cablemodem:", 
             totales_accesos_tecnologia[['Año', 'Trimestre', 'Crecimiento_Cablemodem']])








  # Conclusión en Markdown con colores personalizados
st.markdown("""
### <span style="color: black;">Conclusión:</span>
La fibra óptica está revolucionando el acceso a internet con su alta capacidad de banda ancha, 
mientras que el **cablemodem** sigue siendo una opción viable y más accesible en áreas sin infraestructura de fibra óptica. 
No obstante, la fibra óptica se está posicionando como el estándar debido a su capacidad para soportar el aumento 
de la demanda de datos y la digitalización.
""", unsafe_allow_html=True)

# Lista de ideas
ideas = [
    "Incrementar el porcentaje de penetración en accesos a internet en provincias con baja incidencia.",
    "Invertir en infraestructura para fibra óptica y nuevas tecnologías.",
    "Aprovechar la infraestructura existente de Cablemodem para diversificar el servicio ofreciendo TV por suscripción.",
]

# Mostrar la lista de ideas con color negro
st.markdown("### <span style='color: black;'>Ideas para mejorar el servicio:</span>", unsafe_allow_html=True)
for i, idea in enumerate(ideas):
    st.markdown(f"<p style='font-size: 16px; color: black;'>{i+1}. {idea}</p>", unsafe_allow_html=True)






