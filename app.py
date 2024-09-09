from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)


model=pickle.load(open("FineTechmodel.pkl",'rb'))


car=pd.read_csv("clean.csv")


# @app.route('/',methods =['GET','POST'])
# def index():
#     Brand =sorted(car['Brand Name'].unique())
#     Fuel_type=sorted(car['Fuel type'].unique())
#     Aspiration=sorted(car['Aspiration'].unique())
#     Door_Panel=sorted(car['Door Panel'].unique())
#     Design=sorted(car['Design'].unique())
#     Wheel_Drive=sorted(car['Wheel Drive'].unique())
#     Engine_Location=sorted(car['Engine Location'].unique())
#     Engine_Type= sorted(car['Engine Type'].unique())
#     Cylinder_Count= sorted(car['Cylinder Count'].unique())
#     Fuel_System= sorted(car['Fuel System'].unique())

#     return render_template('index.html', Brand= Brand, Fuel_type= Fuel_type,Aspiration=Aspiration,Door_Panel=Door_Panel,Design=Design,Wheel_Drive=Wheel_Drive,Engine_Location=Engine_Location,Engine_Type=Engine_Type,Cylinder_Count=Cylinder_Count,Fuel_System=Fuel_System)

from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)


model=pickle.load(open("FineTechmodel.pkl",'rb'))


car=pd.read_csv("clean.csv")


@app.route('/')
def index():
    return render_template('index.html')

#     return render_template('index.html', Brand= Brand, Fuel_type= Fuel_type,Aspiration=Aspiration,Door_Panel=Door_Panel,Design=Design,Wheel_Drive=Wheel_Drive,Engine_Location=Engine_Location,Engine_Type=Engine_Type,Cylinder_Count=Cylinder_Count,Fuel_System=Fuel_System)

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    user = int(request.form.get('user'))  # Assuming 'user' is an integer
    dayofweek = int(request.form.get('week'))  # Assuming 'dayofweek' is an integer
    hour = int(request.form.get('hour'))  # Assuming 'hour' is an integer
    age = int(request.form.get('age'))  # Assuming 'age' is an integer
    numscreens = int(request.form.get('screen'))  # Assuming 'numscreens' is an integer
    minigame = int(request.form.get('game'))  # Assuming 'minigame' is an integer
    used_premium_feature = int(request.form.get('feature'))  # Assuming 'used_premium_feature' is an integer
    location = int(request.form.get('location'))  # Assuming 'location' is an integer

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'user': [user],
        'dayofweek': [dayofweek],
        'hour': [hour],
        'age': [age],
        'numscreens': [numscreens],
        'minigame': [minigame],
        'used_premium_feature': [used_premium_feature],
        'location': [location]
    })

    # Predict using the model
    prediction = model.predict(input_data)

    # Return the prediction
    return str(prediction[0])



if __name__=="__main__":
    app.run(debug=True)