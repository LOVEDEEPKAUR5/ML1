import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("/content/drive/My Drive/decision_model.pkl","rb")
model=pickle.load(pickle_in)
dataset= pd.read_csv('/content/drive/My Drive/Classification Dataset2.csv')
X = dataset.iloc[:, [2, 3]].values
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
def predict_note_authentication( Gender,Glucose,BP, BMI,Age,Outcome):
  output= model.predict(sc.transform([[Age,Outcome]]))
  print("Purchased", output)
  if output==[1]:
    prediction="person will have that diseases"
  else:
    prediction="person will not have that diseases"
  print(prediction)
  return prediction
def main():
    st.title("Person Diseases")
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Person Diseases</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender","Type Here")
    Glucose = st.text_input("Glucose","Type Here")
    BP = st.text_input("BP","Type Here")
    BMI = st.text_input("BMI","Type Here")
    Age = st.text_input("Age","Type Here")
    Outcome = st.text_input("Outcome","Type Here")
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication( Gender,Glucose,BP, BMI,Age,Outcome)
      st.success('Model has predicted {}'.format(result))
    if st.button("About"):
      st.text("Developed by Lovedeep kaur")
      st.text("Student , Department of Computer Engineering")

if __name__=='__main__':
  main()
   