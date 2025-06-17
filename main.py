# main.py

import streamlit as st
from agents.persona_agent import identify_persona
from agents.outreach_rag_agent import generate_outreach_insights
from agents.template_agent import create_templates
from agents.engagement_agent import recommend_engagement_strategy

st.set_page_config(page_title="Early Adopter Outreach Strategist", layout="wide")
st.title("🚀 Early Adopter Outreach Strategist")

startup_name = st.text_input("Enter your startup name:")
startup_description = st.text_area("Briefly describe your startup:")

if st.button("Generate Outreach Strategy"):
    with st.spinner("🔍 Mapping Persona..."):
        persona, communities = identify_persona(startup_description)

    with st.spinner("📚 Retrieving Outreach Styles..."):
        outreach_insights = generate_outreach_insights(startup_description)

    with st.spinner("📝 Generating Outreach Templates..."):
        templates = create_templates(persona, communities, outreach_insights)

    with st.spinner("📈 Recommending Engagement Strategy..."):
        engagement_plan = recommend_engagement_strategy(startup_description)

    st.subheader("🎯 Target Persona & Communities")
    st.write(f"**Persona:** {persona}")
    st.write("**Communities:**", communities)

    st.subheader("📬 Outreach Templates")
    for channel, template in templates.items():
        st.markdown(f"**{channel.capitalize()}**: {template}")

    st.subheader("📊 Engagement Strategy")
    st.write(engagement_plan)