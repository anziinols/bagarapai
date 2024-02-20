import time
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import requests
import socket
import ftplib

def get_public_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        if response.status_code == 200:
            return response.json()['origin']
        else:
            print("Failed to retrieve public IP address:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

public_ip = get_public_ip()
#st.write("Your public IP address is:", public_ip)


# Get the IP address
#ip_address = socket.gethostbyname(socket.gethostname())
#get AI response 
ai_response = ""

ip_address = public_ip

# Display the IP address using Streamlit
st.write(f"Your IP address is: {ip_address}")




def write_ip_address(ip_address,user_input,ai_response):
    
    # Open a file for writing
    file = open("ip_addresses.txt", "a")

    ip_address = ip_address or ""
    user_input = user_input or ""
    ai_response = ai_response or ""
    # Write some text to the file
    file.write(ip_address+","+user_input+","+ai_response+"\n")
    #file.write("This is an example text file.\n")

    # Close the file
    file.close()    

# Display IP  
#st.write("Your IP Address is: ", ip_address)


# Custom HTML for the banner
custom_html = """
<div style="display: flex; align-items: center; justify-content: center;">
    <h1 style="text-align: center;">Bagarap AI</h1>
    
</div>
<h4 style="text-align: center;">Only Sarcastic Responses</h4>
<p style="text-align: center;">By Bata Nols</p>
"""
hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
header {visibility:hidden;}
#aitopia {visibility:hidden;}

</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)

# Display the custom HTML

#st.image("sarcastic-logo.png",caption=None,width=50)
st.markdown(custom_html, unsafe_allow_html=True)


#st.title('Bagarap AI')

#st.subheader('Sarcastic Responses')  


openai_api_key = st.secrets["OPENAI_API_KEY"]

chat = ChatOpenAI(temperature=1, openai_api_key=openai_api_key)

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
intro_message = SystemMessage(
    #content="You're an unhelpful AI bot that makes jokes at whatever the user says. Your name is Sacastic AI"
    content="You're a helpful AI bot that answers the user in a dirthy flirty way. Your name is Sarcastic AI"
)

st.session_state['chat_history'].append(intro_message)

def clear_chat():
    st.empty()

def get_response():
     with st.spinner("Bagarapim tintin..."):
        time.sleep(2)
        
        # Hide chat history
        clear_chat() 
        
        human_message = HumanMessage(content=user_input)
        st.session_state['chat_history'].append(human_message)

        response = chat(st.session_state['chat_history'])
        st.session_state['chat_history'].append(response)
        #ai_response = response.content
       
        
user_input = st.chat_input("Say something... ", key="input")  

if user_input:
    get_response()
    
for i, message in enumerate(st.session_state['chat_history']):
    
    if isinstance(message, HumanMessage):
        with st.chat_message("User"):
            st.info(message.content)
            
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):  
            #st.image("sarcastic-logo.png",caption=None,width=20)
            ai_response = message.content
            st.success(message.content)
            

write_ip_address(ip_address,user_input,ai_response)

# Custom HTML for the footer
custom_footer = """
<style>
footer {
  position: fixed;
  bottom: 0;
  left: 10%;
  width: 100%;
}
</style>
<footer>Developed by <b>Bata Nols</b> </footer>
"""    
st.markdown(custom_footer, unsafe_allow_html=True)


# Write to file 
# Connect to the FTP Server
#    try:
ftp = ftplib.FTP('sg1-ts2.a2hosting.com')
ftp.login(user='dakoiim1', passwd='72lS6Qoju7)(XX')

# List Files
print("\nListing Contents:\n")
ftp.dir()

# Disconnect after finishing work
ftp.quit()
#    except Exception as e:
#        print(f"An error occurred while connecting to the FTP server: {e}")

