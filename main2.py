import streamlit as st
from scraper import scrape_reviews
from ai_analysis import analyze_reviews
from generator import save_csv, save_pdf, create_chart
import os

st.set_page_config(layout="wide")
st.title("AI Customer Review Analyzer")

url = st.text_input("Enter Product Page URL")
max_reviews = st.slider("Number of Reviews", 5, 50, 10)
manual_reviews = st.text_area("Or paste reviews manually (one per line)")

if st.button("Analyze"):
    reviews = []
    if manual_reviews:
        reviews = manual_reviews.strip().split("\n")
    elif url:
        with st.spinner("Scraping reviews..."):
            reviews = scrape_reviews(url, max_reviews)

    if len(reviews) == 0:
        st.error("No reviews found")
        st.stop()

    st.success(f"{len(reviews)} reviews collected")

    st.subheader("Sample Reviews")
    for r in reviews[:5]:
        st.write("-", r)

    with st.spinner("AI analyzing..."):
        analysis = analyze_reviews(reviews)

    st.subheader("AI Insights")
    st.text(analysis)

    csv_file = save_csv(reviews)
    pdf_file = save_pdf(analysis)
    chart_file = create_chart(reviews)

    st.image(chart_file, caption="Reviews Analysis Chart")

    if os.path.exists(csv_file) and os.path.exists(pdf_file):
        st.success("Files are ready for download")
        with open(csv_file, "rb") as f:
            st.download_button("Download Reviews CSV", f.read(), file_name="reviews.csv", mime="text/csv")
        with open(pdf_file, "rb") as f:
            st.download_button("Download AI Report PDF", f.read(), file_name="analysis.pdf", mime="application/pdf")