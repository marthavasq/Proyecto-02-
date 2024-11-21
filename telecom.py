import streamlit as st 
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.graph_objects as go



st.title("TELECOMUNICACIONES")
st.markdown("Análisis de comportamiento de accesos a internet y KPIs")
#kpis 


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
    background-color: #A7C7E7; /* Fondo azul pastel */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra para destacar los KPIs */
    color: white; /* Texto blanco */
}
.kpi-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}
.kpi-value {
    font-size: 36px;
    font-weight: bold;
    color: #FFFFFF; /* Color blanco para los valores */
}
.kpi-delta {
    font-size: 16px;
    color: #FFFFFF; /* Color blanco para el texto */
    margin-top: 5px;
}
</style>
<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-title">Acceso a internet</div>  
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Nuevas tecnologias</div>   
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Infraestructura</div> 
    </div>
</div>
""", unsafe_allow_html=True)


# Filtramos la hoja de ingresos
df_ingresos_internet = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\ingresos_internet.csv")
df_ingresos_filtrado = df_ingresos_internet[(df_ingresos_internet['Año'] >= 2014) & (df_ingresos_internet['Año'] <= 2024)] 

# Agrupar por Año y sumar los ingresos
ingresos_por_año = df_ingresos_filtrado.groupby('Año')['Ingresos (miles de pesos)'].sum().reset_index()

# Gráfico interactivo en tonos azules
fig_ingresos = px.bar(
    ingresos_por_año,
    x='Año',
    y='Ingresos (miles de pesos)',
    title="Aumento de ingresos a través de los años (2014-2024)",
    labels={'Ingresos (miles de pesos)': 'Ingresos (miles de pesos)', 'Año': 'Año'},
    color='Año',  # Opcional: agregar color por año
    color_continuous_scale='Blues'  # Paleta de colores en tonos azules
)

# Personalizar el diseño del gráfico
fig_ingresos.update_layout(
    title_font_size=14,
    xaxis_title="Año",
    yaxis_title="Ingresos (miles de pesos)",
    xaxis_tickangle=-45,
    template="plotly_dark"  # Usar un tema oscuro
)

# Filtramos la hoja de Dial-BAf
df_dial_baf = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\totales_dial_baf.csv")
df_filtrado = df_dial_baf[df_dial_baf["Trimestre"].isin([1, 2])]

# Agrupar los datos por año y sumar los accesos para Banda Ancha Fija y Dial-Up
df_agrupado = df_filtrado.groupby("Año")[["Banda ancha fija", "Dial up"]].sum().reset_index()

# Gráfico interactivo usando Plotly
fig = go.Figure()

# Añadir la línea para Banda Ancha Fija
fig.add_trace(go.Scatter(
    x=df_agrupado["Año"], 
    y=df_agrupado["Banda ancha fija"],
    mode='lines+markers', 
    name="Banda Ancha Fija", 
    line=dict(color='royalblue', width=3), 
    marker=dict(symbol='circle', size=8)
))

# Añadir la línea para Dial-Up
fig.add_trace(go.Scatter(
    x=df_agrupado["Año"], 
    y=df_agrupado["Dial up"],
    mode='lines+markers', 
    name="Dial-Up", 
    line=dict(color='lightblue', width=3), 
    marker=dict(symbol='circle', size=8)
))

# Personalizar el diseño del gráfico
fig.update_layout(
    title="Comparación Dial-BAf Enero-Julio (2014-2024)",
    title_x=0.5,
    title_font_size=14,
    xaxis_title="Año",
    yaxis_title="Accesos",
    xaxis=dict(tickmode='array', tickvals=df_agrupado["Año"], tickangle=45),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    legend_title="Tecnología",
    template="plotly_dark",  # Tema oscuro
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
    hovermode="x unified"  # Mostrar valores de ambos ejes al pasar el ratón sobre cualquier punto
)

# Mostrar los gráficos en dos columnas
col1, col2 = st.columns(2)  # Dividir la pantalla en dos columnas

with col1:
    st.markdown('### Análisis de Ingresos de Internet (2014-2024)')
    st.plotly_chart(fig_ingresos)

with col2:
    st.markdown('### Comparación de Tecnologías (Dial-BAf)')
    st.plotly_chart(fig)






#----------------------------------------------------------
#grafico velocidades 

# Cargar el DataFrame (asegurarse de que df_dict ya esté cargado)
df_rangos = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\totales_accesos_rangos.csv")


# Filtrar los datos para los primeros dos trimestres
df_filtrado = df_rangos[df_rangos["Trimestre"].isin([1, 2])]

# Agrupar por año y sumar los accesos por rango de velocidad
rangos_velocidad = [
    'Hasta 512 kbps',
    'Entre 512 Kbps y 1 Mbps',
    'Entre 1 Mbps y 6 Mbps',
    'Entre 6 Mbps y 10 Mbps',
    'Entre 10 Mbps y 20 Mbps',
    'Entre 20 Mbps y 30 Mbps',
    'Más de 30 Mbps',
    'OTROS'
]

df_rangos = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\totales_accesos_rangos.csv")
df_agrupado = df_rangos.groupby("Año")[rangos_velocidad].sum().reset_index()

# Crear un gráfico de barras agrupadas usando Plotly
fig = go.Figure()

# Añadir barras para cada rango de velocidad
colors = ['#add8e6', '#87cefa', '#4682b4', '#4169e1', '#1e90ff', '#00bfff', '#0000ff', '#5f9ea0']
for i, rango in enumerate(rangos_velocidad):
    fig.add_trace(go.Bar(
        x=df_agrupado["Año"],
        y=df_agrupado[rango],
        name=rango,
        marker=dict(color=colors[i]),
        width=0.1,
        offsetgroup=i  # Asegura que las barras estén agrupadas por año
    ))

# Personalizar el diseño del gráfico
fig.update_layout(
    title="Distribución de Accesos por Velocidad, primer semestre (2014-2020)",
    title_x=0.5,
    title_font_size=16,
    xaxis_title="Año",
    yaxis_title="Total de Accesos",
    xaxis=dict(tickmode='array', tickvals=df_agrupado["Año"], tickangle=45),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    barmode='group',  # Las barras estarán agrupadas por año
    legend_title="Velocidades",
    template="plotly_dark",  # Usar un tema oscuro
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
    hovermode="x unified"  # Mostrar valores de ambos ejes al pasar el ratón sobre cualquier barra
)

# Mostrar el gráfico en Streamlit
st.title("Distribución de Accesos por Velocidad")
st.plotly_chart(fig)


#-----------------------------------------------------------




# Extraer la hoja 'Totales Accesos Por Tecnología'
df_tecnologia = pd.read_csv(r"C:\Users\pc\Desktop\HENRY LABS\STREAMLIT\documentos csv\totales_accesos_tecnologia.csv")


# Filtrar los datos para los primeros dos trimestres
df_filtrado = df_tecnologia[df_tecnologia["Trimestre"].isin([1, 2])]

# Tecnologías que queremos analizar
tecnologias = ['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros']

# Agrupar por año y sumar los accesos por tecnología
df_agrupado = df_filtrado.groupby("Año")[tecnologias].sum().reset_index()

# Crear el gráfico de barras agrupadas con Plotly
fig = go.Figure()

# Definir los colores para cada tecnología
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Añadir barras para cada tecnología
for i, tecnologia in enumerate(tecnologias):
    fig.add_trace(go.Bar(
        x=df_agrupado["Año"],
        y=df_agrupado[tecnologia],
        name=tecnologia,
        marker=dict(color=colores[i]),
        width=0.15,
        offsetgroup=i  # Agrupar las barras por año
    ))

# Personalizar el diseño del gráfico
fig.update_layout(
    title="Distribución de accesos por Tecnología (primer semestre, 2014-2024)",
    title_x=0.5,
    title_font_size=16,
    xaxis_title="Año",
    yaxis_title="Total de Accesos",
    xaxis=dict(tickmode='array', tickvals=df_agrupado["Año"], tickangle=45),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    barmode='group',  # Agrupar las barras por año
    legend_title="Tecnología",
    template="plotly_dark",  # Tema oscuro
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
    hovermode="x unified"  # Mostrar los valores de cada barra cuando se pase el ratón
)

# Mostrar el gráfico en Streamlit
st.title("Distribución de Accesos por Tecnología")
st.plotly_chart(fig)








