import streamlit as st
import time as t

# title
st.title('Welcome to nsti dehradun')

# header
st.header('Machine Learning')

# subheader
st.subheader('Linear Regression')

# to give information
st.info('Information Details of a user')

# warning message
st.warning('This is a warning messsage')

# write 
st.write('Employee Name')
st.write("range(50)")
st.write(range(50))

# error message
st.error('This is a Error Message')

# success message
st.success('Congrats you have got A grade')

# markdown 
st.markdown('This is a markdown')
st.markdown('# This is a markdown')
st.markdown('## This is a markdown')
st.markdown('### This is a markdown')
st.markdown('#### This is a markdown')
st.markdown('##### This is a markdown')
st.markdown('###### This is a markdown')
st.markdown(':moon:')

# text
st.text('This is a text')

# caption
st.caption('This is a caption')

# to display a mathematical equation
st.latex(r'''a+b x^2+c''')

# image
st.image('streamlit.png')

# widgets


# checkbox
st.checkbox('Login')

# button
st.button('Click')

# radiobutton
st.radio('Select Your Gender:',['Male','Female','Other'])

# selectbox
st.selectbox('Select Your Course:',['ML','IT','ADIT','IBM'])

# multiselect
st.multiselect('Choose the dept:',['Content','Sales','Marketing'])

# selectslider
st.select_slider("Age", options=list(range(1,9)), value=(3,6), key='my_key')
st.select_slider('Rating',['Bad','Good','Excellent','Outstanding'])

# slider
st.slider('Enter your number:',0,30)

# number_input
st.number_input('Pick a number:',0,30)

# text_input
st.text_input('Enter your email:')

# date_input
st.date_input('Opening Ceremony:')

# time_input
st.time_input('Hey whats the timing:')

# text_area
st.text_area('Welcome to the nsti dehradun:')

# upload_file
st.file_uploader('Upload your file:')

# color_picker
st.color_picker('Choose your color:')

# progress
st.progress(80)

# spinner
with st.spinner('Just wait'):
    t.sleep(2)

# balloons
st.balloons()

# sidebar
st.sidebar.title('Welcome to nsti dehradun')
st.sidebar.text_input('Enter your mail:')
st.sidebar.text_input('Password:')
st.sidebar.button('Submit')
st.sidebar.radio('Professional Expert:',['Student','Working','Others'])

# data visualization
import pandas as pd
import numpy as np
st.title('Bar Chart')
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)

st.title('Line Chart')
st.line_chart(data)

st.title('Area Chart')
st.area_chart(data)




