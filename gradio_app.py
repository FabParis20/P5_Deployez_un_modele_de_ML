import gradio as gr
import pandas as pd
from app.models.load_pipeline import load_pipeline
from app.models.dummy_data import DUMMY_DATA

pipeline = load_pipeline()
input_cols = list(DUMMY_DATA.keys())

def predict_from_inputs(**kwargs):
    df = pd.DataFrame([kwargs])
    pred = pipeline.predict(df)
    return f"⚠️ Risque de démission : {'OUI' if pred[0] == 1 else 'NON'}"

# Interface Gradio (à compléter ensuite)
import gradio as gr

# Génération dynamique des champs à partir de DUMMY_DATA
inputs = [
    gr.Textbox(label=key, value=str(val))
    for key, val in DUMMY_DATA.items()
]

# Interface Gradio
interface = gr.Interface(
    fn=predict_from_inputs,
    inputs=inputs,
    outputs=gr.Textbox(label="Résultat"),
    title="Prédicteur de démission",
    description="Entrez les caractéristiques d’un employé pour prédire son risque de démission.",
)

# Lancement de l’interface
if __name__ == "__main__":
    interface.launch()
