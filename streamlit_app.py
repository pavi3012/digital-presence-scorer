import streamlit as st
import requests, pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Digital Presence Scorer", layout="wide")
st.title("Small Business Digital Presence Scorer")
st.caption("Pavi Creations · Data Analytics Internship · June 2026")

with st.form("audit_form"):
    col1, col2 = st.columns(2)
    with col1:
        name     = st.text_input("Business name *")
        category = st.selectbox("Category", ["Restaurant","Salon","Retail","Tutor","Mechanic","Other"])
        city     = st.text_input("City", "Madurai")
        ig_handle = st.text_input("Instagram handle")
        ig_followers = st.number_input("Instagram followers", 0, step=10)
        ig_ppw = st.number_input("Posts per week", 0.0, step=0.5)
        ig_er  = st.number_input("Engagement rate (%)", 0.0, step=0.1)
        ig_bio = st.checkbox("Bio is complete")
    with col2:
        gm_listed  = st.checkbox("Listed on Google Maps")
        gm_rating  = st.number_input("Google Maps rating", 0.0, 5.0, step=0.1)
        gm_reviews = st.number_input("Number of reviews", 0, step=1)
        gm_photos  = st.number_input("Photos uploaded", 0, step=1)
        gm_hours   = st.checkbox("Business hours set")
        has_web    = st.checkbox("Has a website")
        web_mobile = st.checkbox("Mobile-friendly website")
        web_fast   = st.checkbox("Fast loading website")
        web_contact= st.checkbox("Contact info on homepage")
        same_name  = st.checkbox("Same name across platforms")
        same_logo  = st.checkbox("Same logo across platforms")
        same_color = st.checkbox("Consistent brand colors")
        replies    = st.checkbox("Replies to reviews")
        wa_biz     = st.checkbox("WhatsApp Business active")
        response_h = st.number_input("Avg. response time (hours)", 0.0, value=24.0)

    submitted = st.form_submit_button("Generate Score", type="primary")

if submitted and name:
    payload = dict(
        name=name, category=category, city=city,
        instagram_handle=ig_handle, instagram_followers=ig_followers,
        instagram_posts_per_week=ig_ppw, instagram_engagement_rate=ig_er,
        instagram_bio_complete=ig_bio, google_maps_listed=gm_listed,
        google_maps_rating=gm_rating, google_maps_reviews=gm_reviews,
        google_maps_photos=gm_photos, google_maps_hours_set=gm_hours,
        has_website=has_web, website_mobile_friendly=web_mobile,
        website_load_fast=web_fast, website_contact_visible=web_contact,
        same_name_across_platforms=same_name,
        same_logo_across_platforms=same_logo, consistent_colors=same_color,
        replies_to_reviews=replies, whatsapp_business_active=wa_biz,
        average_response_time_hours=response_h,
    )
    try:
        r = requests.post("http://localhost:8000/api/score", json=payload)
        data = r.json()

        col_score, col_rating = st.columns([1, 2])
        with col_score:
            color = {"Excellent":"green","Good":"orange","Average":"red","Poor":"darkred"}[data["rating"]]
            st.metric("Digital Health Score", f"{data['total_score']}/100")
            st.markdown(f"**Rating:** :{color}[{data['rating']}]")

        with col_rating:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=data["total_score"],
                gauge={"axis":{"range":[0,100]},
                       "bar":{"color":color},
                       "steps":[{"range":[0,40],"color":"#fee2e2"},
                                {"range":[40,60],"color":"#fef3c7"},
                                {"range":[60,80],"color":"#d1fae5"},
                                {"range":[80,100],"color":"#a7f3d0"}]},
            ))
            st.plotly_chart(fig, use_container_width=True)

        # Radar chart
        labels = ["Instagram","Google Maps","Website","Brand","Engagement"]
        scores = [data["instagram_score"]/25*100, data["google_maps_score"]/25*100,
                  data["website_score"]/20*100, data["brand_consistency_score"]/15*100,
                  data["customer_engagement_score"]/15*100]
        fig2 = go.Figure(go.Scatterpolar(r=scores+[scores[0]], theta=labels+[labels[0]],
                                          fill="toself", fillcolor="rgba(37,99,235,0.15)",
                                          line_color="#2563eb"))
        fig2.update_layout(polar=dict(radialaxis=dict(range=[0,100])), showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

        # Recommendations
        st.subheader("Your action plan")
        for pillar, tips in data["recommendations"].items():
            with st.expander(pillar.replace("_", " ").title()):
                for tip in tips:
                    st.markdown(f"- {tip}")
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")