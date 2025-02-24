import os
import streamlit as st
import joblib
from sklearn.ensemble import AdaBoostClassifier

# Ruta al archivo del modelo (en la raíz del repositorio)
model_path = "modelo_adaboost_optimizado_corrido.pkl"

# Verificar si el archivo del modelo existe
if not os.path.exists(model_path):
    st.error(f"El archivo del modelo no se encuentra en la ruta: {model_path}")
    st.stop()

# Cargar el modelo utilizando joblib
model = joblib.load(model_path)

# Verificar que el modelo es un objeto AdaBoostClassifier
if not isinstance(model, AdaBoostClassifier):
    st.error("El modelo cargado no es un objeto de tipo AdaBoostClassifier.")
    st.stop()

# Diccionario de clases para interpretar la predicción
class_dict = {
    "0": "Diabético",
    "1": "No Diabético",
}

# Título de la aplicación
st.title("Predicción de Diabetes con AdaBoost")

# Creación de los controles (sliders) para la entrada de datos
val1 = st.slider("Número de Embarazos", min_value=0, max_value=20, step=1)
val2 = st.slider("Nivel de Glucosa", min_value=0, max_value=200, step=1)
val3 = st.slider("Nivel de Insulina", min_value=0, max_value=800, step=1)
val4 = st.slider("Índice de Masa Corporal (BMI)", min_value=0.0, max_value=70.0, step=0.1)
val5 = st.slider("Función de Diabetes", min_value=0.0, max_value=3.0, step=0.1)
val6 = st.slider("Edad", min_value=0, max_value=100, step=1)

# Botón para realizar la predicción
if st.button("Predecir Diabetes"):
    # Preparar los datos en el formato esperado por el modelo
    data = [[val1, val2, val3, val4, val5, val6]]
    
    # Realizar la predicción
    prediction = model.predict(data)[0]
    pred_class = class_dict.get(str(prediction), "Clase desconocida")
    
    # Mostrar el resultado en la interfaz
    st.success(f"Predicción: {pred_class}")
