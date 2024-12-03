import streamlit as st
import time 
st.title('hello')
st.write('what you want')
name = st.text_input('say something: ')
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
btn = st.button('oke')
btn1 = st.button('no')
btn2 = st.button('yes')
if btn:
    st.write('no')
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
      time.sleep(0.01)
      my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

elif btn1:
    st.write('yes')

elif btn2:
    st.write('no')
    progress_text = "đợi xíu"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
      time.sleep(0.01)
      my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.image('yo.gif', caption="bear")
st.button('rerun')

