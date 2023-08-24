import streamlit as st
import requests
import webbrowser
api_key = "fbef48545e72b7183786f15c0ab091e4"

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'
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


def getweather(city):
    result = requests.get(url.format(city, api_key))     
    if result:
        json = result.json()
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humid = json['main']['humidity'] - 273.15
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        res = [country, round(temp,1),round(temp_feels,1),
                humid,lon,lat,icon,des]
        return res , json
    else:
        print("error in search !")

def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start,api_key))
    data = res.json()
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)     
    return data , temp


st.header('Whats the weather?')   

col1, col2 = st.columns(2)

with col1:
    city_name = st.text_input("Enter a city name")
with col2:  
		if city_name:
		        res , json = getweather(city_name)
		        st.success('Current: ' + str(round(res[1],2)))
		        st.info('Feels Like: ' + str(round(res[2],2)))
		        st.subheader('Status: ' + res[7])
		        web_str = "![Alt Text]"+"(http://openweathermap.org/img/wn/"+str(res[6])+"@2x.png)"
		        st.markdown(web_str)  

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
