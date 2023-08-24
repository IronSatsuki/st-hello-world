import streamlit as st
import webbrowser
from PIL import Image
from streamlit_extras.colored_header import colored_header

st.title("Heart and Stroke Foundation")
st.write("Phone: 1-888-473-4636 | Email: donorinfo@heartandstroke.ca")
colored_header(
    label="",
    description="",
    color_name="red-80",
)
st.info("Welcome to the Heart and Stroke website. You can navigate different pages through the pull bar on the left hand side.")
st.divider()
st.subheader("About Us")
st.text("The Heart and Stroke Foundation is a national, voluntary,")
st.text("non-profit organization whose mission is to improve the ")
st.text("health of Canadians by preventing and reducing disability ")        
st.text("and death from heart disease and stroke through research,")
st.text(" health promotion and advocacy.")

url2 = "https://app-hsfdonation.heartandstroke.ca/?pagename=DMDonationForm&s_locale=en_CA&s_fT=cont&s_pres=hsweb&s_cscid=hsweb_nav"
url3 = "https://www.heartandstroke.ca/stroke/what-is-stroke"
url4 = "https://www.heartandstroke.ca/heart-disease/what-is-heart-disease"
st.sidebar.title("Links")

if st.sidebar.button('Donate'):
    webbrowser.open_new_tab(url2)
if st.sidebar.button('Stroke Infomation'):
    webbrowser.open_new_tab(url3)
if st.sidebar.button('Heart disease Infomation'):
    webbrowser.open_new_tab(url4)

st.divider()
st.subheader("True Stories and Articles")

story1 = "https://www.heartandstroke.ca/articles/using-data-to-save-more-women"
story2 = "https://www.heartandstroke.ca/articles/i-am-here-for-a-reason"
story3 = "https://www.heartandstroke.ca/articles/saving-baby-nora"

tab1, tab2, tab3 = st.tabs(["1", "2", "3"])
with tab1:  
    if st.button('Using data to save more women'):
        webbrowser.open_new_tab(story1)
with tab2:
    if st.button('I am here for a reason'):
         webbrowser.open_new_tab(story2)
with tab3:
    if st.button('Saving baby Nora'):
         webbrowser.open_new_tab(story3)
colored_header(
    label="",
    description=" ",
    color_name="red-80",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)