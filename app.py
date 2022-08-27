import streamlit as st
import framework
import nmap

nav=st.sidebar.selectbox('Options',['Home','Subdomain Scanner','port scanner','Device Detector'])
st.markdown("<body style='background-color:black'><h1 style='text-align: center; font-size:50px; color: green;'>Hackeroof</h1>'</body></html>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size:16px; text-align:center;'>By Muhammad Talha Iqbal</h3>",unsafe_allow_html=True)
scanner=nmap.PortScanner()
st.write("result",scanner)

if nav=='Subdomain Scanner':
    framework.subscanner()
    #  scan.app()
    #  scan.app()
    #  domain=st.text_input('Enter target domain:')
    #  if st.button('enter'):
      
     
    #   scanner.func(domain)
     

elif nav=='port scanner':
    framework.streamlit_tool()
elif nav=='Home':
    framework.home()
elif nav=='Device Detector':
    framework.device()

    

