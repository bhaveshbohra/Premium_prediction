import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# here we create manaul but actul will come from mlflow (model registery)
MODEL_VERSION ='1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist() # high, medium, low 

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(input_df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }