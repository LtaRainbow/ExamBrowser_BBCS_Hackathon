import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from streamlit_lottie import st_lottie
import random
import pytz

page = 0
paper_name = 'Cool_Nameless_file :sunglasses:'
password_generate = False

st.set_page_config("ExamSave: *Teacher Interface*", layout ="centered")
st.header("ExamSave: Educating For Life")

#MAIN PAGE
if page == 0:
    files = st.button("Import Locally:")
    newwwwww = st.button("Create New:")
    Cc = st.checkbox("I agree and allow ExamSave to save and edit local files.")
    if files and Cc:
        page = 10
    elif newwwwww and Cc:
        page = 20
    else:
        st.header("*Please allow ExamSave to use your files.*")

if page == 10 and Cc:
    st.header("Hey uh, work still in progress^^")
#IMPORT FROM FILES
#(while page == 10:
    #paper_name = st.text_input("CSV File Name")
   # @st.cache_data
    #def convert_df(df):
    #Cache conversion to prevent computation on every rerun
     #   return df.to_csv().encode("utf-8")

    #csv = convert_df(f'{paper_name}.csv')#need file )

    #st.download_button(
     #   label="Download data as CSV",
      #  data=csv,
       # file_name=f"{paper_name}.csv",
        #mime="text/csv",
     #)



#CREATE NEW
if page == 20 and Cc:
 paper_name = 'Biology End_of_Year Paper 1'
 #password_generate = True
     
st.divider()

    #password_generate = True
st.header(":zap: Exam Start:")
d = st.date_input("Date of Exam", datetime.date(2025,6, 4))
t = st.time_input("Starting", datetime.time(18,30))
st.write(f"{paper_name}"+" is set to occur on", d, "at", t)

teacher = st.text_input('Input your unique code within 5 digits/alphabets.')
#Password Idea #1: DayMonthYear(D/M/Y) of Paper, Teacher's Unique Code(Cc), Student_Register_No, CheckDigit [D/M/Y/Cc/No./Check]
#Check Digit as in the student interface only needs to check that 1 digit lol to make life easier
passcode = f"{d}_{teacher}_Register_No._{random.randint(0, 9)}"

st.divider()


st.subheader('Student Access Passcode:')
st.write(f':blue-background[{passcode}]')

def write_variable(variable):
    with open('variable.txt', 'w') as file:
        file.write(variable)

write_variable(passcode)
