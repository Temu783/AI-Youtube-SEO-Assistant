import streamlit as st
from chains.seo_chain import generate_seo_content

st.set_page_config(page_title="YouTube SEO Assistant", layout="centered")
st.title("🎥 AI-Powered YouTube SEO Assistant")

topic = st.text_input("Enter your video topic")

if st.button("Generate SEO Content"):
    with st.spinner("Generating..."):
        result = generate_seo_content(topic)

        st.subheader("📌 Title")
        st.write(result['title'])

        st.subheader("📝 Description")
        st.write(result['description'])

        st.subheader("🏷️ Tags")
        st.write(", ".join(result['tags']))

        st.subheader("💡 Content Ideas")
        st.write("\n".join(result['ideas']))

st.markdown("## 📽️ How to Use This App")
st.video("https://www.loom.com/share/664b96ba93e64fee899ca010a7fccd1a?sid=e72ae2bf-da7e-46dc-b9af-98c3a486d406")
