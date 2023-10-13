import streamlit as st
import os
import msal

st.set_page_config(page_title="You are authenticated!!!!", page_icon=":ninja:", layout="wide")

client_id = os.environ.get('CLIENT_ID', '***NO CLIENT ID***')
client_secret = os.environ.get('CLIENT_SECRET', '***NO CLIENT SECRET***')
authority = os.environ.get('AUTHORITY', '***NO AUTHORITY***')

st.markdown(f":green[*** Authority is: {authority} ***]")
scopes=["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(
    client_id, authority=authority,
    client_credential=client_secret,
    # token_cache=...  # Default cache is in memory only.
                       # You can learn how to use SerializableTokenCache from
                       # https://msal-python.readthedocs.io/en/latest/#msal.SerializableTokenCache
    )
accounts = app.get_accounts()
your_account = None
if (accounts):
    your_account = accounts[0]
    st.write(your_account)
else:
    st.markdown(":red[=-=-=- NO ACCOUNT FOUND =-=-=-]")

result = app.acquire_token_silent(scopes, account=your_account)

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