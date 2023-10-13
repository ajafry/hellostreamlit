import streamlit as st
import os
import msal

client_id = os.environ.get('CLIENT_ID', '***NO CLIENT ID***')
client_secret = os.environ.get('CLIENT_SECRET', '***NO CLIENT SECRET***')
scopes=["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(
    "77e2f8e5-5b78-47c5-abc1-fbb6006e1633", authority="https://login.microsoftonline.com/fd58167c-8662-4cd9-8797-550a074ef51d",
    client_credential="480a3cdd-7eea-42ed-b991-29feb2863ab2",
    # token_cache=...  # Default cache is in memory only.
                       # You can learn how to use SerializableTokenCache from
                       # https://msal-python.readthedocs.io/en/latest/#msal.SerializableTokenCache
    )
accounts = app.get_accounts()
your_account = None
if (accounts):
    your_account = accounts[0]

result = app.acquire_token_silent(scopes, account=your_account)

st.set_page_config(page_title="Hello streamlit", page_icon=":ninja", layout="wide")

if result:
    if "access_token" in result:
        st.write(result["access_token"])
    else:
        st.write(result.get("error"))
        st.write(result.get("error_description"))
        st.write(result.get("correlation_id"))  # You may need this when reporting a bug
else:
    st.markdown(":red[=-=-=- NO RESULT FROM SILENT TOKEN ACQUISITION =-=-=-]")

# ---- Header Section -----
with st.container():
    st.subheader("Hi, I am a simple app :wave:")
    st.title("Streamlit is fun")
    st.write("Streamlit enables you to create a website quickly")
    st.write("[Learn more about Streamlit >](https://streamlit.io/)")