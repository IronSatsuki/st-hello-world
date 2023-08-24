import streamlit as st
from streamlit_extras.colored_header import colored_header
import webbrowser

colored_header(
    label="Information",
    description=" ",
    color_name="violet-70",
)

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

url = "https://www.heartandstroke.ca/how-you-can-help/volunteer/join-us/newfoundland-and-labrador"
st.info("This project was made for the [Heart and Stroke Foundation](%s)" % url)



st.text("There are ways to know if you are having a stroke:")

st.image("fast.png")

colored_header(
    label="Risks",
    description="There is many risks that are in your control to stop.",
    color_name="violet-70",
)

st.subheader("If you have a unhealthy diet")
st.text("The types of food affect your health. Learning how to eat healthy can make your\nhealth better and decrease the risk.")
st.subheader("If you are physically inactive")
st.text("The more active you are, the less likely you are to have a risk of a stroke. You\nalso have an increased risk of diabetes, cancer and dementia.")
st.subheader("If you are in a unhealthy weight")
st.text("Having a lot of weight can lead to high blood pressure, high cholesterol,\ndiabetes and sleep apnea. Being obese can double the risk of a stroke.")
st.subheader("If you are a smoker")
st.text("Smoking triples the risk of a stroke. Quitting is the best thing you can do\nto prevent heart disease and strokes.")
st.subheader("If you are stressed")
st.text("Stress is something that everyone has. People who have high levels of stress or\nprolonged stress have higher blood pressure and cholesterol.")
st.subheader("If you use excessive amounts of alcohol and drugs")
st.text("Heavy drinking is a big risk factor for high blood pressure and strokes. If you do\ndrink, limit yourself to small amounts, and drink lots of water at the same time.")
st.text("Drugs such as amphetamines, cannabis, cocaine, ecstacy, heroin, and LSD increases\nthe risk of strokes and heart disease. When a stroke does occur, it usually happens\nwithin hours of drug use.")
st.subheader("Birth control and HRT")
st.text("Any type of medication that includes estrogen increases the risk of herat attacks,\nstrokes and mini-strokes.")

colored_header(
    label="Preventions",
    description="There are ways you can prevent the risks.",
    color_name="violet-70",
)
st.subheader("Eating healthy")
st.text("Eating lots of vegetables, cooking at home, limiting your processed foods, are\nall ways to help prevent the risk of strokes.")
st.subheader("Staying active")
st.text("Start to walk more, rake some leaves, start to play a sport. All and any of these\nare great ways to keep staying acive and decrease the risk.")
st.subheader("Reduce stress")
st.text("The best way to deal with your stress is to find out what your stressors are. This\ncan be done by taking a stress test and see what triggers your stress symptoms.\nYou can then start to manage to remove this stress.")
st.subheader("Maintaining a healthy weight")
st.text("You should eat healthy foods, choose protein from food sources, avoid highly\nprocessed foods such as processed meats, fried foods, frozen meals, and snack\nfoods. Drink lots of water. Make portions of foods a reasonable size. Eat 3 meals\nand 2 healthy snacks per day.")

colored_header(
    label="Risks that you cannot control",
    description="These are risks that are out of your control.",
    color_name="violet-70",
)

st.subheader("Sex")
st.text("The risk of heart disease and strokes will increase after menopause.")
st.subheader("Age")
st.text("The older you get, the higher the risk you are of a stroke.")
st.subheader("Medical history")
st.text("If you have close relative that has had a stroke, you are at risk.")
st.subheader("Personal circumstances")
st.text("Personal circumstances and environmental factors will have a toll on your health.")

st.header("Donate")
if st.button('Click to donate to the foundation'):
    webbrowser.open("https://www.heartandstroke.ca/how-you-can-help/ways-to-give")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
