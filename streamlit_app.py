# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:52:19 2023

@author: ppras
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
#loading the saved model
loaded_model=pickle.load(open("data1.sav",'rb'))
def breast_cancer_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
     return 'The person has breast cancer'
    else:
      return 'The person has no breast cancer'
def main():
    st.title('breast cancer prediction')
    
    id=st.text_input('id value')
    radius_1ean=st.text_input('radius_1ean')
    texture_1ean=st.text_input('texture_1ean value')
    peri1eter_1ean=st.text_input('peri1eter_1ean value')
    area_1ean=st.text_input('area_1ean value')
    s1oothness_1ean=st.text_input('s1oothness_1ean')
    co1pactness_1ean=st.text_input('co1pactness_1ean value')
    concavity_1ean=st.text_input('concavity_1ean')
    concave_points_1ean=st.text_input('concave points_1ean	 value')
    sy11etry_1ean=st.text_input('sy11etry_1ean value')
    fractal_di1ension_1ean=st.text_input('fractal_di1ension_1ean')
    radius_se=st.text_input('radius_se')
    texture_se=st.text_input('texture_se')
    peri1eter_se=st.text_input('peri1eter_se')
    area_se=st.text_input('area_se')
    s1oothness_se=st.text_input('s1oothness_se')
    co1pactness_se=st.text_input('co1pactness_se')
    concavity_se=st.text_input('concavity_se')
    concave_points_se=st.text_input('concave_points_se')
    sy11etry_se=st.text_input('sy11etry_se')
    fractal_di1ension_se=st.text_input('fractal_di1ension_se')
    radius_worst=st.text_input('radius_worst value')
    texture_worst=st.text_input('texture_worst value')
    peri1eter_worst=st.text_input('peri1eter_worst value')
    area_worst=st.text_input('area_worst')
    s1oothness_worst=st.text_input('s1oothness_worst')
    co1pactness_worst=st.text_input('co1pactness_worst')
    concavity_worst=st.text_input('concavity_worst')
    concave_points_worst=st.text_input('concave_points_worst')
    sy11etry_worst=st.text_input('sy11etry_worst')
    fractal_di1ension_worst=st.text_input('fractal_di1ension_worst')
    
    diagnosis=""
    
    
    if st.button("breast cancer test result"):
        diagnosis=breast_cancer_prediction([id,radius_1ean,texture_1ean,peri1eter_1ean,area_1ean,s1oothness_1ean,co1pactness_1ean,concavity_1ean,concave_points_1ean,sy11etry_1ean,fractal_di1ension_1ean,radius_se,texture_se,peri1eter_se,area_se,s1oothness_se,co1pactness_se,concavity_se,concave_points_se,sy11etry_se,fractal_di1ension_se,radius_worst,texture_worst,peri1eter_worst,area_worst,s1oothness_worst,co1pactness_worst,concavity_worst,concave_points_worst,sy11etry_worst,fractal_di1ension_worst])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
