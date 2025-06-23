from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import MODEL_VERSION , predict_output
from schema.prediction_response import PredictionResponse
app = FastAPI()

# Home API
@app.get('/')
def home():
    return {"messag":"Insurance PremiumPrediction"}

# machine readable :AWS service elastic net or kubernet check here 
# Health Check APi (when using AWS service, Help)
@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'version': MODEL_VERSION
    }

## API for model
# @app.post('/predict')
# def predict_premium(data: UserInput):
#     #single row inside this one dictionary
#     input_df = pd.DataFrame([{
#         'bmi': data.bmi,
#         'age_group': data.age_group,
#         'lifestyle_risk': data.lifestyle_risk,
#         'city_tier': data.city_tier,
#         'income_lpa': data.income_lpa,
#         'occupation': data.occupation
#     }])


@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):
    #single row inside this one dictionary
    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))



