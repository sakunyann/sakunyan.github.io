import streamlit as st

# set page config
st.set_page_config(page_title="Sakunyann's Data Science Portfolio",
                   page_icon=":bar_chart:",
                   layout='centered',
                   initial_sidebar_state="auto")

# Display the title of the web app
st.title(":bar_chart: WELCOME TO SAKUNYANN'S DATA SCIENCE PORTFOLIO!")
# Display a header that briefly describes the web apps, with a rocket emoji
st.write('')
st.subheader(":rocket: An Unofficial Platform For Custom Web Applications Hosted By Streamlit")
# Display a subheader that indicates the author of the web apps, with a sunglasses emoji
st.write(':memo: By Sakura Koffron')

st.write('')
st.write('')
# Display a markdown bullet point with a emoji and a link to "AQI_Prediction" app
url = "./AQI_Prediction"
git_url = "https://github.com/sakunyann/sakunyan.github.io/tree/main"
st.subheader(":wind_blowing_face: [AQI Prediction App](%s)" % url,
             help = "Learn more about this app at my [github repository](%s)" % git_url)
# Display a markdown bullet point with a computer emoji and a link to app 2
#st.markdown('- **[:computer: App 2](./App_2)**')

# Display an empty line
st.text('')
# Display an image from the 'assets' folder named 'cover-page.gif'
#st.image('assets/cover-page.gif')
