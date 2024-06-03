import streamlit as st
import pickle

from is_duplicate import is_duplicate

st.header('Duplicate question detect')

qn1 = st.text_input('Enter first question')
qn2 = st.text_input('Enter second question')

if st.button('Submit', type="primary"):
    if(is_duplicate(qn1, qn2)):
        st.write('Questions are duplicate')
    else:
        st.write('Questions aren\'t duplicate')



