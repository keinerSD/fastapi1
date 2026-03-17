import joblib
import numpy as np
import pandas as pd

model = joblib.load("data/disease_model.pkl")
symptoms = joblib.load("data/symptoms.pkl")

def predict_disease(symptom_list):

    input_vector = np.zeros(len(symptoms))

    for symptom in symptom_list:
        if symptom in symptoms:
            index = symptoms.index(symptom)
            input_vector[index] = 1

    input_df = pd.DataFrame([input_vector], columns=symptoms)

    probabilities = model.predict_proba(input_df)[0]

    top_indices = probabilities.argsort()[-5:][::-1]

    results = []

    for i in top_indices:
        disease = model.classes_[i]
        prob = float(probabilities[i] * 100)

        results.append({
            "disease": disease,
            "probability": round(prob, 2)
        })

    return results