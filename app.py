from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import sqlite3
import os
import google.generativeai as genai

#configure api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google gemini model and provide sqlquery as response

def get_gemini_response(que,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],que])
    return response.text

#function to retrieve query  from sql db

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#define your prompt

prompt = [  
    """  
    You are an expert in converting English questions to SQL queries.  
    The SQL database is named STUDENT, and its columns are: NAME, CLASS, SECTION, and MARKS.  
    \n\nHere are some examples to guide you:\n  
    Example 1:   
    Question: "How many entries of records are there?"  
    SQL Command: SELECT COUNT(*) FROM STUDENT;  
    
    Example 2:  
    Question: "Tell me all the students studying in Data Science class."  
    SQL Command: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';  
    
    \nPlease ensure that:\n  
    1. The generated SQL queries are syntactically correct.  
    2. There are no extraneous characters (like ''' or the word 'sql') at the beginning or end of the SQL output.  
    3. You respect the data types of the columns (e.g., strings should be enclosed in single quotes).  
    \n  
    Now, convert the following questions into SQL queries:  
    """  
]  

##streamlit App

st.set_page_config(page_title="I can retrive any sql query")
st.header("Gemini app to retrieve sql data")
que=st.text_input("Input: ",key="input")
submit = st.button("Ask the Question")

#if submit is clicked

if submit:
    response=get_gemini_response(que,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is: ")
    for row in data:
        print(row)
        st.header(row)