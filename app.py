import streamlit as st
import pickle

from is_duplicate import is_duplicate

st.title('AskAlign', anchor=False)
st.text("'Quora - Duplicate question detection'")


qn1 = st.text_input('Enter first question')
qn2 = st.text_input('Enter second question')

if st.button('Check', type="primary"):
    if(is_duplicate(qn1, qn2)):
        st.markdown('### Questions are duplicate' )
    else:
        st.markdown('### Questions aren\'t duplicate')



