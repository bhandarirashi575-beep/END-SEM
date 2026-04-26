from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from agents.researcher import research_topic
from agents.extractor import extract_data
from agents.writer import write_brief

st.set_page_config(page_title="Environmental Impact Briefer")

st.title("🌱 Environmental Impact Briefer")

topic = st.text_input("Enter topic (e.g., Plastic Waste, Coal Mining):")

if st.button("Generate Brief"):
    if topic:
        with st.spinner("Researching..."):
            raw_data = research_topic(topic)

        with st.spinner("Extracting insights..."):
            structured = extract_data(raw_data)

        with st.spinner("Writing report..."):
            report = write_brief(structured, topic)

        st.subheader("📄 Final Report")
        st.write(report)

    else:
        st.warning("Please enter a topic")