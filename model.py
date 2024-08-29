import streamlit as st



st.set_page_config(
page_title = 'Forretningsmodel',
page_icon = '✅',
layout = 'wide'
)



st.logo("images.jpeg")



new_title = '<h5 style="font-family:sans-serif; color:#058ef7; font-size: 30px;">Forretningsmodel til Mer Innovasjon Norge</h5>'
st.markdown(new_title, unsafe_allow_html=True)



st.sidebar.title("DAMM-DATAANALYSE-MEDIA-MARKEDSFØRING")



tab1, tab2, tab3, tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11 = st.tabs(["KORT OM PROSJEKTET","KUNDESEGMENT", "VERDILØFTET", "KANALER","KUNDERELASJON","KJERNEAKTIVITETER","RESSURSER","NETTVERK/PARTNERE","INNTEKTSTRØM","KOSTNADER","SOWT-ANALYSE"])

with tab1:
   
   new_title1 = '<h5 style="font-family:sans-serif; color:#058ef7; font-size: 30px;">Hva dette prosjektet handler om?</h5>'
   st.markdown(new_title1, unsafe_allow_html=True)
   
   
   st.subheader(" Dette prosjektet betraktes som en praktisk anvendelse til en forskning inkubator der kan data analyse forskninger, deltar i den lokale utviklingen via å tilby de følgende tjenestene:")
   st.subheader("1- Dtat  analyse både til offentlige og private sektorer ") 
   st.image("data.jpeg",width=500)           
   st.subheader("2- Selv opplæring til indivder som er interessert i å lære seg data vitenskap og data analyse.")
   st.image("opplaring.jpeg",width=500) 
   
   new_title1_1 = '<h5 style="font-family:sans-serif; color:#058ef7; font-size: 30px;">FORRETNINGSIDEEN</h5>'
   st.text("__________________________________________________________________________________________________________________________________")
   st.markdown(new_title1_1, unsafe_allow_html=True)
   st.image("iddeen.png",width=700)
   
    
with tab2:
   new_title2 = '<h3 style="font-family:sans-serif; color:#058ef7; font-size: 30px;">Våre kunder grupperes i tre :</h3>'
   st.markdown(new_title2, unsafe_allow_html=True)
   
   st.subheader("1- OFFENTLIGE SEKTORER (KOMMUNER, ORGANISASJONER)")
   st.image("kommuner.png")
   st.subheader("2- PRIVATE SEKTORER (STORE OG SMÅ BEDRIFTER, ORGANISASJONER)")
   st.image("bedrifter.png",width=600)
   st.subheader("3- INDIVIDER")
   st.image("individ.jpeg",width=600)
  


with tab3:
   new_title3 = '<h3 style="font-family:sans-serif; color:#058ef7; font-size: 30px;">Hvilken verdi skaper produktet/tjenesten for kunden?</h3>'
   st.markdown(new_title3, unsafe_allow_html=True)
   
   
   st.subheader("PROSJEKT VERDIER")
   st.image("verdier.png",width=800)
  
   
   
   
   
   
   
with tab4:
    st.header("MERINNOVASJON-NORGE")
    

with tab5:
    st.header("MERINNOVASJON-NORGE")
    

with tab6:
    st.header("KJERNE AKTIVITETER")
    st.image("Activitetr.png")
    st.text("----------------------------------------------------------------------------------------------------")
    st.header("Noen eksampler")
    st.video("https://youtu.be/iGgECHx0_1c")
    st.video("https://youtu.be/1PGipYafSSk")
    st.video("https://youtu.be/Mi_JPmlr1sE")
    st.video("https://youtu.be/2UXUejawFeI")
    st.video("https://youtu.be/_LC_TdoI1Kk")
    st.video("https://youtu.be/5RpmVAtuzIo?feature=shared")


with tab7:
    st.header("RESSURSER")
    st.image("Ressurser.png")
    
with tab8:
    st.header("MERINNOVASJON-NORGE")
    
with tab9:
    st.header("INNTEKTSSTRØM-KILDER")
    st.image("inntekt.png")
    
    
    
with tab10:
    st.header("KOSTNADER")
    st.image("kostnader.png")
    
with tab11:
    st.header("SWOT ANALYSE")
    new_title3 = '<h3 style="font-family:sans-serif; color:#058ef7; font-size: 20px;">HVA SLAGS MULIGHETER DETTE PROSJEKTET HAR..? OG HVA SLAGS TRUSLER SOM KAN HINDRE PROSJEKT STRØMMEN..?</h3>'
    st.markdown(new_title3, unsafe_allow_html=True)
   
    st.subheader("SWOT ANALYSE")
    st.image("swot.png")
    
  
    
    
    