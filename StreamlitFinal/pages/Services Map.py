import folium
import streamlit as st
import pandas as pd
import re
from streamlit_extras.colored_header import colored_header
import webbrowser

from streamlit_folium import st_folium 
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





def format_phone_number(phone_number):
    phone_number = re.sub('[^0-9]+', '', phone_number)
    return '(' + phone_number[:3] + ') ' + phone_number[3:6] + '-' + phone_number[6:]


colored_header(
    label="Map",
    description=" ",
    color_name="violet-70",
)


df = pd.read_excel("StreamlitFinal\pages\CombinedSheetCleanedv3.xlsx", dtype=str)












@st.cache_resource(experimental_allow_widgets=True)
def mapcode():
    
    map_test = folium.Map(location=[48.949756125416, -57.9455439558197], zoom_start=14, tiles=None)
    folium.TileLayer('openstreetmap', name='Legend: ').add_to(map_test)

    MAX_WIDTH = 400

    fgKinesiology = folium.FeatureGroup(name='<i class="fa fa-wheelchair" style="color:rgb(70, 25, 70);"></i><FONT COLOR="(70, 25, 70)">Kinesiologist</FONT>')

    fgPharmacist = folium.FeatureGroup(name='<i class="fa fa-plus-circle" style="color:cadetblue;"></i>><FONT COLOR="cadetblue">Pharmacist</FONT>')

    fgSkilledNursing = folium.FeatureGroup(name='<i class="fa fa-heartbeat" style="color:#FF69B4;"></i><FONT COLOR="#FF69B4">Skilled Nursing Facilities</FONT>')

    fgPhysio = folium.FeatureGroup(name='<i class="fa fa-bed" style="color:#ADD8E6;"></i><FONT COLOR="#ADD8E6">Physiotherapist</FONT>')

    fgFinancial = folium.FeatureGroup(name='<i class="fa fa-credit-card" style="color:red;"></i><FONT COLOR="red">Financial aid</FONT>')

    fgOcuTherapy = folium.FeatureGroup(name='<i class="fa fa-user-md" style="color:#1e3518;"></i><FONT COLOR="#1e3518">Occupational Therapist</FONT>')

    fgSpeech = folium.FeatureGroup(name='<i class="fa fa-comments" style="color:pink;"></i>><FONT COLOR="pink">Speech Language Pathologist</FONT>')

    fgHomeRehab = folium.FeatureGroup(name='<i class="fa fa-home" style="color:grey;"></i><FONT COLOR="grey">Home-Based Rehabilitation</FONT>')

    fgSocial = folium.FeatureGroup(name='<i class="fa fa-child" style="color:green;"></i><FONT COLOR="green">Social Worker</FONT>')

    fgPsycho = folium.FeatureGroup(name='<i class="fa fa-id-badge" style="color:purple;"></i><FONT COLOR="purple">Psychologist/Psychiatrist</FONT>')

    fgFood = folium.FeatureGroup(name='<i class="fa fa-lemon-o" style="color:yellow;"></i><FONT COLOR="yellow">Food Subsides</FONT>')

    fgDiet = folium.FeatureGroup(name='<i class="fa fa-spoon" style="color:orange;"></i><FONT COLOR="orange">Community Dietician</FONT>')

    fgPeer = folium.FeatureGroup(name='<i class="fa fa-users" style="color:lime;"></i><FONT COLOR="lime">Peer Support Group</FONT>')

    fgInOut = folium.FeatureGroup(name='<i class="fa fa-medkit" style="color:blue;"></i><FONT COLOR="blue">In/Outpatient Rehabilitation</FONT>')

    fgFunny = folium.FeatureGroup(name='<i class="fa fa-heart" style="color:maroon;"></i><FONT COLOR="maroon">Sexologist</FONT>')




    for row in df.itertuples(index=False,name=None):
                    if pd.isna(row[13]) == True:
                        continue
                    elif row[1] == 'Kinesiologist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="darkpurple", icon="fa-wheelchair", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgKinesiology) # Kinesiology
                    elif row[1] == 'Pharmacist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgPharmacist) # Pharmacist
                    elif row[1] == 'Skilled nursing facilities':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgSkilledNursing) # Skilled nursing facilities
                    elif row[1] == 'Physiotherapist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="lightblue", icon="fa-bed", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgPhysio) # Physiotherapist
                    elif row[1] == 'Financial aid':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgFinancial) # Financial Aid
                    elif row[1] == 'Occupational Therapist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="darkgreen", icon="fa-user-md", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgOcuTherapy) # Occupational Therapist
                    elif row[1] == 'Speech Language Pathology':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="pink", icon="fa-comments", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgSpeech) # Speech Language Pathologist
                    elif row[1] == 'Home-based rehab':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="gray", icon="fa-home", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgHomeRehab) # Home-based rehab
                    elif row[1] == 'Social Worker':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="green", icon="fa-child", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgSocial) # Social Services
                    elif row[1] == 'Psychologist/Psychiatrist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="purple", icon="fa-user", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgPsycho) # Psychologist/Psychiatrist
                    elif row[1] == 'Food subsidies':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="beige", icon="fa-lemon-o", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgFood) # Food Subsides
                    elif row[1] == 'Community dietician':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="orange", icon="fa-spoon", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgDiet) # Community Dietician
                    elif row[1] == 'Peer support group':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="lightgreen", icon="fa-users", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgPeer) # Peer Support Group

                        
                        
                    elif row[1] == 'In/outpatient rehabilitation':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="blue", icon="fa-medkit", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgInOut) # In/Outpatient Rehabilitation
                    elif row[1] == 'Sexologist':
                        folium.Marker([row[13], row[14]], icon = folium.Icon(color="darkred", icon="fa-heart", prefix="fa"), popup=folium.Popup(f"""<font size='2.5'>
                                                                    {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                    <strong>Name:</strong> {row[0].title()}<br>
                                                                    <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                    <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                    <strong>Region: </strong> {row[6]}<br>
                                                                    {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                    {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                    {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isna(row[9]) is not True else ''}
                                                                    {f'<strong>Additional: </strong> {format_phone_number(row[10])}<br>' if pd.isna(row[10]) is not True else ''}
                                                                    {f'<strong>Email: </strong> {row[11]}<br>' if pd.isna(row[11]) is not True else ''}
                                                                    {f'<strong>Website: </strong> <a href="{row[12]}"  target="_blank">{row[12]}</a><br>' if pd.isna(row[12]) is not True else ''}
                                                                    {f'<strong>Info: </strong> {row[15].title()}<br>' if pd.isna(row[15]) is not True else ''}


                                                                    
                                                                    </font>
                                                                    """, max_width=MAX_WIDTH),
                                                                                        tooltip=f'{row[0].title()}').add_to(fgFunny) # Sexologist
    fgKinesiology.add_to(map_test)                   
    fgPharmacist.add_to(map_test)
    fgSkilledNursing.add_to(map_test)
    fgPhysio.add_to(map_test)
    fgFinancial.add_to(map_test)
    fgOcuTherapy.add_to(map_test)
    fgSpeech.add_to(map_test)
    fgHomeRehab.add_to(map_test)
    fgSocial.add_to(map_test)
    fgPsycho.add_to(map_test)
    fgFood.add_to(map_test)
    fgDiet.add_to(map_test)
    fgPeer.add_to(map_test)
    fgInOut.add_to(map_test)
    fgFunny.add_to(map_test)
            
           
            
          
            
            
            
            
            
            
    map_test.add_child(folium.LayerControl(collapsed=True))   
    return(map_test) 



 
st_data = st_folium(mapcode(), width=710)
with st.expander('See Extra Info'):
    st.header('Social Workers')
    st.subheader('Stephanie Lawrence')
    st.text('Compassion Counselling\nCorner Brook, Newfoundland\n(709) 400-2763\n(709) 400-2763')
    st.markdown('''"I have a wealth of experience in working with individuals and families and I
            strive to help people learn healthy coping skills in order to improve their 
            mental health and wellness or to help overcome everyday life difficulties.
            I am registered Social Worker with a background in clinical counselling and
            advanced trainings in numerous therapeutic modalities and approches, all while
            maintaining the highest standards of professionalism and confidentiality."   
            - *Stephanie Lawrence*''')
    st.subheader('Suzanne Barry-Kroening')
    st.text('Stephenville, Newfoundland\n(709) 800-3879\n(709) 800-3880')
    st.markdown('''
                15 years of experience in counselling, crisis intervention, community development and building community partnerships.
                ''')
    st.subheader('Debbie A. Walsh')
    st.text('Stephenville, Newfoundland\n(709) 200-0406\n(709) 200-0407')
    st.markdown('''
In Person & Online Consults, offers 36 years of experience working with students ages 4 to 18 in the education system. has spent the last 10 years as a school counsellor. 
                 Has developed skills as an assessor in areas such as ADHD and learning disorders
                ''')
    st.subheader('Lance Jackson')
    st.text('Perpetual Evolution Counselling and Wellness\nSt. Georges, Newfoundland\n(709) 499-0444\n(709) 499-0445')
    st.markdown('''
Has over 2 decades working with people of all ages that suffer from past trauma, depression, anxiety, and interpersonal relationship issues  
[Website](https://pecounselling.com/)
''')
    st.subheader('Strength Counselling Services')
    st.text('Channel-Port-aux-Basques/Grand Bank, Newfoundland\n(709) 500-2599\n(709) 500-2599')
    st.markdown('''
Individual counselling, co-dependent recovering, couples and family therapy, life coaching.  
[Website](https://strengthcounselling.ca/)
''')
    st.subheader('Nichola Park')
    st.text('Meridian Holistic Health Center, 38 Brook Street, Newfoundland\n(709) 800-7021\n(709) 800-7022')
    st.markdown('''
With over five years experience working with individuals with mental health and addictions Nichola is skilled in individual therapy, and addiction assessments
''')
    st.subheader('Emma Chafe')
    st.text('Isle-aux-Morts, Newfoundland\n(709) 700-3774\n(709) 700-3775')
    st.markdown('''
As a trauma focused Art Therapist she uses movement, meditation, and art making to enable a different kind of relationship with difficult experiences. 
                Living with kindness and compassion requires strong clear boundaries and the skills to communicate them.  
                [Website](https://www.rowanwellness.com/)
''')
    st.subheader('Tammy Breen')
    st.text('Corner Brook, Newfoundland\n(709) 501-8399\n(709) 501-8400')
    st.markdown('''
Has experience in counselling individuals of all ages who are impacted by addictions, family issues, separation and divorce, anxiety and depression, eating disorders, trauma, and grief and loss.
''')
    st.subheader('Bonnie Hancock-Moore')
    st.text('Deer Lake, Newfoundland\n(709) 400-2801\n(709) 400-2802\nBhmcounselling@gmail.com')
    st.markdown('''
Has extensive knowledge of mental illness, addictions, child maltreatment, attachment, FASD, Trauma, etc. is an ally to LBGTQ+ Individuals and a provides a safe space for all  
                [Website](https://bhmcounselling.wixsite.com/website)
''')
    st.header('Psychologist/Psychiatrist')
    st.subheader('Cindy Russell')
    st.text('Stephenville, Newfoundland\n(709) 501-5126\n(709) 501-5127')
    st.markdown('Online Only, specialize in trauma, is EMDR trained and works with clients to help them process and let go of trauma while reducing it’s negative impact on their lives')
    st.subheader('The Serenity Space- Sarah Whelan')
    st.text('Corner Brook, Newfoundland\n(343) 453-2822\n(343) 453-2823')
    st.markdown('She incorporates a variety of therapeutic modalities including emotion focused therapy, parts work, mindfulness, DBT, and the Gottman method. She has experience working with trauma, ED/disordered eating, ADHD, BPD, anxiety/stress, relationship diffictulties and couples.')
    
    st.header('Peer Support Group')
    st.subheader('lifewiseNL')
    st.text('Opening Hours: 10:00 AM Mon-Fri\nClosing Hours: 12:00 AM Mon-Fri\n(855) 753-2560')
    st.markdown('''Online call center with virtual peer support services, At Lifewise, their purpose is to bring hope to, and reduce stigma for those individuals living with mental health and addictions issues.   
                [Website](https://lifewisenl.ca/)''')
    st.subheader('eMental health')
    st.text('Open 24/7')
    st.markdown('''Online call center, Self-help, mutual aid and support groups  
                [Website](https://www.ementalhealth.ca/Newfoundland-and-Labrador/Self-help-Mutual-Aid-and-Support-Groups/index.php?m=heading&ID=44)''')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
