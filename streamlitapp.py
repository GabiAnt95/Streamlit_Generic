import streamlit as st
import pandas as pd


def load_data(n, c):
    r = pd.DataFrame(list(zip([n], [n**2], [n*3.5])))
    for col in range(1, c):
        r = pd.concat([r,pd.DataFrame(list(zip([n+col], [(n+col)**2], [(n+col)*3.5])))], axis = 0).reset_index(drop =True)
    
    return r


def filter_uploaded_file(df, col):
    globals()['filtered_df'] = df[col]
    return filtered_df
    
filtered_df = pd.DataFrame()

st.title('Uber pickups in NYC')

date = st.date_input('Update Date: ')
option_dev = st.selectbox('Development type?',('Desarrollo', 'Correctivo', 'Soporte'))
option_tec = st.selectbox('Tecnology Dev?',('JAVA', 'PYTHON', 'SAP'))
option_input_def = st.slider('INPUT DATAFRAME', 0, 100)
columns_input = st.number_input('COLUMNS INPUT', 0, 100)

#photo = st.camera_input('Take photo')

st.write('Development Type:', option_dev)
st.write('Tecnology Dev:', option_tec)

uploaded_file = st.file_uploader('Upoload File', accept_multiple_files=False)

if uploaded_file is None:
    st.write("There is no File uploaded")
else:    
    dataframe = pd.read_excel(uploaded_file)
    st.table(dataframe)
    
st.button('Filter Uploaded File', on_click = lambda: filter_uploaded_file(dataframe, 'nombre'))

st.write(filtered_df)

st.table(load_data(option_input_def, columns_input))

