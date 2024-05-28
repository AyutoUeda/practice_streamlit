import streamlit as st
import pandas as pd
import numpy as np

st.title('My firs')
st.caption("this is the caption")
st.subheader("subheader")

python_code = '''
print("aaa")
'''

st.code(python_code, language="python")


st.write(1235)

df = pd.DataFrame(
    [1,2,3],
    [4,5,6]
)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.markdown('''
            - a
            - b
            
            '''
            )
st.caption("abc")

with st.form(key="profile_form"):
    # text box
    name = st.text_input("name")
    address = st.text_input("address")
    
    # select box
    age_category = st.selectbox(
        "age category",
        ("under 18", "over 18")
    )
    
    hobby = st.multiselect(
        "hobby",
        ("sport", "reading", "cooking", "shopping")
    )

    # btn
    submit_btn = st.form_submit_button("submit")
    cancel_btn = st.form_submit_button("cancel")
    # print(f"submit_btn:{submit_btn}")
    # print(f"cancel_btn:{cancel_btn}")
    
    # print(type(hobby))

    if submit_btn:
        st.text("ようこそ, {}!{}に書類を発送しました".format(name, address))
        st.text("your age category is {}".format(age_category))
        st.text(", ".join(hobby))
        
