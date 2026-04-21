import streamlit as st
import plotly.express as px
from models import get_kpi_data, get_shipment_data

# 1. Configuration de la page
st.set_page_config(
    page_title="Bénin Logistics Dash",
    page_icon="",
    layout="wide"
)

# 2. Titre et Design
st.title(" Pilotage Logistique : Port de Cotonou <> GDIZ")
st.markdown("---")

# 3. Affichage des KPIs (En-tête)
kpis = get_kpi_data()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Performance Globale", kpis["perf"]["val"], kpis["perf"]["delta"])
with col2:
    st.metric("Flux GDIZ (24h)", kpis["gdiz"]["val"], kpis["gdiz"]["delta"])
with col3:
    st.metric("Taux d'Occupation", kpis["stocks"]["val"], kpis["stocks"]["delta"])
with col4:
    st.metric("Taux de Service", kpis["service"]["val"], kpis["service"]["delta"])

st.write("") # Espacement

# 4. Graphique des Flux (Corps)
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader(" Intensité des Flux Logistiques")
    # Création d'un graphique simple pour illustrer les flux
    df_flux = px.data.iris() # Données temporaires pour le test
    fig = px.line(df_flux, y="sepal_width", 
                  title="Activité en temps réel (Cotonou - Glo-Djigbé)",
                  template="plotly_dark", 
                  color_discrete_sequence=["#00FFC8"])
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("⚠️ Alertes Critiques")
    st.error("Retard : Convoi n°402 (Axe Parakou)")
    st.warning("Congestion : Entrée Nord GDIZ")
    st.info("Info : 3 navires en attente au Port")

# 5. Tableau des Expéditions (Bas)
st.subheader("📦 Suivi des Expéditions Nationales")
df_exp = get_shipment_data()
st.dataframe(df_exp, use_container_width=True)

st.markdown("---")
st.caption("Application de monitoring développée pour la logistique du Bénin.")
  
