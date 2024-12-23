from pickle import load
import streamlit as st
import os


# Ruta al archivo del modelo
model_path = ("/opt/render/project/src/models/modelo_adaboost_optimizado (3).pkl", "rb")


# Diccionario de clases
class_dict = {
    "0": "Diabético",
    "1": "No Diabético",
}

# Título de la aplicación
st.title("Predicción de Diabetes")

# Sliders para ingresar los valores del formulario
val1 = st.slider("Embarazos", min_value=0, max_value=20, step=1)
val2 = st.slider("Glucosa", min_value=0, max_value=200, step=1)
val3 = st.slider("Insulina", min_value=0, max_value=800, step=1)
val4 = st.slider("Índice de Masa Corporal (BMI)", min_value=0.0, max_value=70.0, step=0.1)
val5 = st.slider("Función de Diabetes", min_value=0.0, max_value=3.0, step=0.1)
val6 = st.slider("Edad", min_value=0, max_value=100, step=1)

# Botón de predicción
if st.button("Predecir Diabetes"):
    data = [[val1, val2, val3, val4, val5, val6]]
    prediction = str(model.predict(data)[0])
    pred_class = class_dict[prediction]
    st.write("Predicción:", pred_class)

