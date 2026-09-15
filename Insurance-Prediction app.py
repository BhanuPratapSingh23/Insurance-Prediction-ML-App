# Step 1 = Load Imported Modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st

# This Streamlit is for web-based application project

# Web Page Code
st.title("HEALTH INSURANCE PREDICTION")

img_url = "https://cdn.zeebiz.com/sites/default/files/2026/03/09/401943-health-insurance.png"

st.image(img_url)

# LOAD DATA and ML MODEL PART

# Step 2: Load Insurance Data
url="https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df=pd.read_csv(url)

# Step 3: EDA: Exploratory Data Analysis
df.drop("Customer_ID",axis=1,inplace=True)

df["Previous_Insurance"]=df["Previous_Insurance"].map({"No":0,"Yes":1})
df["Insurance_Bought"]=df["Insurance_Bought"].map({"No":0,"Yes":1})

# Step 3: EDA: Exploratory Data Analysis
x = df.iloc[:,:-1]
print(x.shape)

y = df.iloc[:,-1]
print(y.shape)

# Step 5: Divide Data into Training & Testing Part
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
print(x_train.shape)
print(x_test.shape)

# Step 6: Train Model
model = LogisticRegression()
model.fit(x_train,y_train)

# show data sample
st.write(df.head())
# Create Side bar for user input form
st.sidebar.title("Fill Customer Details")
st.sidebar.image(img_url)


for index,col_name in enumerate(x.columns):
  min_v=x[col_name].min()
  max_v=x[col_name].max()
  if col_name != "Previous_Insurance":
    value =st.sidebar.slider(f"Select value for {col_name}",
                             min_value = min_v,
                             max_value = max_v)
  else:
    value=st.slidebar.number_input(f"Select value for {col_name}: ")
 all_ans.append(value)

ud={j:all_ans[i] for i,j in enumerate(x.columns)}
user_df = pd.DataFrame(ud,index = [1])
st.write(user_df)

#=========================Prediction================================
if st.button("Click to Predict: "):
  with st.spinner("Predicting.."):
    import time
    time.sleep(2)
  final_ans = model.predict([all_ans])[0]
  if final_ans == 0:
    st.info("❌ Customer will not Buy the Insurance ❌")
  else:
    st.success("✅ Customer will buy the Insurance ✅")
    
