import streamlit as st

st.set_page_config(layout="wide", page_title="Contact Me", page_icon="📧")
st.header("Contact Me")

# Define the links to your social media accounts
github_link = "https://github.com/harshpreet14"
linkedin_link = "https://www.linkedin.com/in/harshpreetkaur14/"
portfolio_link = "https://rxresu.me/ms21103/harshpreet-kaur-/build"
resume_link = "https://rxresu.me/ms21103/harshpreet-kaur-/build"

# Define your email and phone number
email = "kaurharshpt6@gmail.com"
phone_number = "+91-70871-93693"

# Create three columns to display the links
col1, col2, col3 = st.columns(3)

# Add the GitHub and LinkedIn links to the first column with icons
with col1:
    st.write("[![GitHub icon](https://img.icons8.com/fluency/48/000000/github.png)](" + github_link + ") "
             "GitHub")

    st.write("")  # Add an empty line for spacing

    st.write("[![LinkedIn icon](https://img.icons8.com/fluency/48/000000/linkedin.png)](" + linkedin_link + ") "
             "LinkedIn")

# Add the Portfolio and Resume links to the second column with icons
with col2:
    st.write("[![Portfolio icon](https://img.icons8.com/fluency/48/000000/domain.png)](" + portfolio_link + ") "
             "Portfolio")

    st.write("")  # Add an empty line for spacing

    st.write("[![Resume icon](https://img.icons8.com/fluency/48/000000/document.png)](" + resume_link + ") "
             "Resume")

# Add the email and phone number to the third column with icons
with col3:
    st.write("[![Email icon](https://img.icons8.com/fluency/48/000000/email.png)](mailto:" + email + ") "
             "Email")

    st.write("")  # Add an empty line for spacing

    st.write("[![Phone icon](https://img.icons8.com/fluency/48/000000/phone.png)](tel:" + phone_number + ") "
             "Phone")

st.write("")

st.markdown("**Click on the icons to visit my profiles on GitHub, LinkedIn, and other sites. You can also find my email and phone number for further contact.**")