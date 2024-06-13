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
Cc = 0
num = 1
name = ''

st.set_page_config("ExamSave", layout ="centered")
st.header("ExamSave: Educating For Life")

#MAIN PAGE

name = st.text_input('Name:')
teacher = st.text_input('Input your unique code with at least 3 digits/alphabets.')
st.write(":zap:**This will also be your password**")
C = st.button('Log In!')

if C:
    st.subheader(f'Welcome, Teacher {name}!')
st.divider()


tab1, tab2 = st.tabs(["Imported Files", "Create New"])

with tab1:
        file = st.text_input('Search for File Name in Local Cache:')
        if file =='Pineapple.csv':
             st.subheader('Question: What is the probability that Maya can get a pineapple pizza?')
             chart_data = pd.DataFrame(np.random.randn(3, 3), 
             columns=["Pineapple", "Pepperoni", "Cheese"])
             st.bar_chart(chart_data)
        elif file == 'Local.csv':
            st.subheader(' Felix wants to open a (mostly legal) bird shop. Given the final receipt, what are the chances that they would overshoot the planned budget of $5000?')
            local = ['Sunbird','Snowy Owl','Hawk','Eagle','Vulture','Crow','Kingfisher', ' Pigeon','Nightingale','Woodpecker']
            index = ['$132','S4000','$15290','$12000','$20000','$56','$144','$10','$569','$210']

            series = pd.Series(local, index=index)
            series.iloc[1]='Red-crested Crane' #[num] is by the original index

            #Sort the series numerically using pandasAI
            sorted_series = pd.Series.sort_values(series, ascending=True)
            sorted_series


        else:
             st.subheader('*No sign of a file...try harder?*')
        #df = pd.read_csv([f'{file}.csv'])
        paper_name = str(file)
        #df.head()
        st.write('Is',paper_name,'this the correct paper?')
        yes = st.button('Yes')
        no = st.button('No.')
        if no:
             st.write('*Please search for the file again!*')
        if yes:
            Cc = st.checkbox("I agree and allow ExamSave to save and edit local files.")
        

with tab2:
        paper_name = st.text_input('Paper Title:')
        st.subheader('Number of Questions:')
        qns = st.text_input('0')
        num = (qns)
        i = 1
        st.warning('Please input whole numbers.')
        with st.form(f"Question {i}"):
                C = True
                question= st.text_input("Question Contents:")

                lang = st.radio('Question Type:',
                        [":rainbow[Open-Ended]", "**[MCQ]**", "Diagram & Charts"],
                        captions=["Standard.", "Easy way out:flower:", "Auto-generated/URL"]
                        )
                if lang == "Diagram & Charts":
                    st.write('Hereby a chart lol')
                    slider_val = st.slider("Number slider")
                elif lang == ":rainbow[Open-ended]":
                    open = st.text_input('Open-ended Question:')
                    checkbox_val = st.checkbox("Question has no direct answer.")
                elif lang == "**[MCQ]**" :
                    answer1 = st.text_input('2')
                    answer2 = st.image('2.jpg')
                    answer3 = st.balloons()
                    st.checkbox(f'{answer1}')
                    st.checkbox(f'{answer2}')
                    st.checkbox(f'{answer3}')
                

                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.write("Question:",question)
                    st.write('Answer is ',slider_val, checkbox_val,open )


    
      #  st.header("*Please allow ExamSave to use your files.*")

#IMPORT FROM FILES


#CREATE NEW

#password_generate = True
st.divider()
if not Cc:
    Cc = st.checkbox("I agree and allow ExamSave to save and edit local files.")
dates =''

if Cc:
    st.header(":zap: Exam Start:")
    d = st.date_input("Date of Exam", datetime.date(2025,6, 4))
    t = st.time_input("Starting", datetime.time(18,30))
    st.write(f"{paper_name}"+" is set to occur on", d, "at", t)

    #Password Idea #1: DayMonthYear(D/M/Y) of Paper, Teacher's Unique Code(Cc), Student_Register_No, CheckDigit [D/M/Y/Cc/No./Check]
    #Check Digit as in the student interface only needs to check that 1 digit lol to make life easier
    passcode = [f'{d}',f'{teacher}','Register_No._',str(random.randint(0,9))]
    final_passcode = ''

    st.header(' ')
    if teacher == '':
        st.warning('Login to get your user unique passcode.')
    st.divider()

    for i in passcode:
        final_passcode += i
        final_passcode += '_'
    st.subheader('Student Access Passcode:')
    st.write(f':blue-background[{final_passcode}]')
