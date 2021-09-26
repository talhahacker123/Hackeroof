import sys
import platform
from datetime import datetime
import streamlit as st
import os.path
import socket 
import subprocess
import requests
import os  
def home():
    #  st.markdown('''# Home
#   ('This is home page')''')
 st.markdown("<body><h1 style='text-align: center; '>Home</h1>'</body></html>", unsafe_allow_html=True)
 st.markdown("""# <h3>Hackeroof</h3>
<b>Hackeroof</b> is a web base framework for [Ethical Hackers](https://searchsecurity.techtarget.com/definition/ethical-hacker#:~:text=An%20ethical%20hacker%2C%20also%20referred,%2D%2D%20and%20with%20their%20authorization.) and [Pentesters](https://en.wikipedia.org/wiki/Penetration_test#:~:text=A%20penetration%20test%2C%20colloquially%20known,confused%20with%20a%20vulnerability%20assessment.). Developed by [Muhammad Talha Iqbal](). 
""",unsafe_allow_html=True)

def device():
 check_name=os.name
 check_platform=sys.platform
 if check_name=='posix' and check_platform=='linux':

    st.write('This is Linux OS')
    st.write('This is ',platform.platform())
    if st.button('detect'):
     '''st.write(os.system('lsusb -s 001:'))  
     p = subprocess.Popen(["lsusb",'-s 001:'], stdout=subprocess.PIPE)
     out,i=p.communicate()
 # out = p.stdout.read()
     st.success(out.decode('ascii'))'''
     p = subprocess.Popen(["lsblk",'/dev/sdb'], stdout=subprocess.PIPE)
     k,j=p.communicate()
# out = p.stdout.read()
     st.success(k.decode('UTF-8'))

     p = subprocess.Popen(["lsblk",'/dev/sdc'], stdout=subprocess.PIPE)
     k,j=p.communicate()
# out = p.stdout.read()
     st.success(k.decode('UTF-8'))
    

     

 elif check_name=='nt' and check_platform=="win32":

    st.write('This is Windows OS')

    
    
    
 

def subscanner():
 check_name=os.name
 if check_name=='nt':
   st.write('----This is windows----')
 else:
     st.write('not windows')  
 st.title('SubScanner')
# the domain to scan for subdomains
# domain = "google.com"
 domain=st.text_input('Enter target domain:')
# subdomai=['store','download','apps','mail']
# read all subdomains
 if st.button('click to scan'):

  file = open("sub.txt")
  # read all content
  content = file.read()
  print(content)
  # print(subdomains)
  # print(f'content {content}')
  # sub=content.splitlines()
  # subdomains.append(sub)
  # split by new lines
  subdomains = content.splitlines()
  #  st.write(f'subdomains {subdomains}')
  st.write('*'*10+'SCANNING'+'*'*10)
  # a list of discovered subdomains
  discovered_subdomains = []
  for subdomain in subdomains:
  # print(subdomain)
    # construct the url
    url = f"http://{subdomain}.{domain}"
  #    print(url)
  
    try:
  # if this raises an ERROR, that means the subdomain does not exist
          requests.get(url)

                  
          #  discovered_subdomains.append(url)
    # except requests.ConnectionError:
    except Exception as error:
          # st.write(str(error))
  # if the subdomain does not exist, just pass, print nothing
          # st.write('error occured')
        #   sleep(5)
          pass

    else:
          # print("[+] Discovered subdomain:", url)
          st.write(url)

  # append the discovered subdomain to our list
          discovered_subdomains.append(url)

def streamlit_tool():
    try:
     #  st.write('='*70)
     #  ascii_banner = pyfiglet.figlet_format('talha',font='computer')
     #  st.write(ascii_banner)
     #  st.markdown("<h3 style='font-size:16px; text-align:center;'>Created by Muhammad Talha Iqbal</h3>",unsafe_allow_html=True)
     #  st.write('='*70)
     #  st.write("-" * 50)
     

      host=st.text_input("Enter target host:")
      if st.button('Click to scan'):
       for port in range(20,1025):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.200)
        if s.connect_ex((host , port))==0:
         st.write("[+*+]port %d is open..." %(port))
         s.close()
        else:
          pass
          #  st.write("Port             %d              is            not             open" %(port))
  
    except KeyboardInterrupt:
     st.write('You pressed Ctrl+C')
 
'''st.title('PortScanner')
      st.write("Scanning started at:" + str(datetime.now()))
      st.write("-" * 50)
    
      DNS=st.text_input("Enter target host address(dns or ip): ")
      host = socket.gethostbyname(DNS)
    #   print("The IP of " +DNS+ " is" + " = " +ip)

    #   host=st.text_input("Enter target host:")
      y= st.text_input("Enter target port:")
      
      x=st.button('Scan')
      port=int(y)
      if x:
       try:  
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hi=s.connect_ex((host , port))
            if (hi==0):
             st.success("[+]Host %s  ->  %s is up" %(DNS,host))
             st.success("port %d is open..." %(port))
             st.balloons()
             print("[+]Host %s is up" %(host))
             print("port %d is open..." %(port))
             s.close()
            else:
              
             st.warning(("port %d is closed"%(port)))
        #  print("port %d is closed"%(port))
       except:
           print('')  
    except ValueError:
          st.stop()'''
