
import streamlit as st
import pandas as pd

def cargar_datos():
    return pd.read_excel("estrategia_postflop.xlsx")

def main():
    st.title("Estrategia Postflop - José Luis Sernaque")

    df = cargar_datos()

    posicion_hero = st.selectbox("Tu posición", sorted(df["Tu posición"].dropna().unique()))
    posicion_villano = st.selectbox("Posición del Villano", sorted(df["Posición del Villano"].dropna().unique()))
    tipo_rival = st.selectbox("Tipo de Rival", sorted(df["Tipo de Rival"].dropna().unique()))
    tipo_mano = st.selectbox("Tipo de Mano", sorted(df["Tipo de Mano"].dropna().unique()))
    textura = st.selectbox("Textura del Board", sorted(df["Textura Board"].dropna().unique()))
    situacion = st.selectbox("Situación Preflop", sorted(df["Situación Preflop"].dropna().unique()))

    resultado = df[
        (df["Tu posición"] == posicion_hero) &
        (df["Posición del Villano"] == posicion_villano) &
        (df["Tipo de Rival"] == tipo_rival) &
        (df["Tipo de Mano"] == tipo_mano) &
        (df["Textura Board"] == textura) &
        (df["Situación Preflop"] == situacion)
    ]

    st.markdown("### 🎯 Estrategia Recomendada")

    if not resultado.empty:
        for col in resultado.columns:
            if col not in ["Tu posición", "Posición del Villano", "Tipo de Rival", "Tipo de Mano", "Textura Board", "Situación Preflop"]:
                st.markdown(f"**{col}**: {resultado[col].values[0]}")
    else:
        st.warning("No se encontraron recomendaciones para esta combinación.")

if __name__ == "__main__":
    main()
