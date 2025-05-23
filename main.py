import streamlit as st
import pandas as pd
import os
from agents.web_search_agent import WebSearchAgent
from agents.data_extraction_agent import DataExtractionAgent
from agents.trend_analysis_agent import TrendAnalysisAgent
from agents.report_writer_agent import ReportWriterAgent

# Set up Streamlit interface
st.title("AI & ML Jobs Intelligence Report for MENA Region")
st.write("A multi-agent system to analyze job trends and generate a customized report")

# User inputs
countries = st.multiselect(
    "Select Countries:",
    ["Egypt", "Saudi Arabia", "UAE", "Qatar", "Jordan", "Lebanon", "Morocco"],
    default=["Egypt", "Saudi Arabia", "UAE"]
)
time_period = st.slider("Select Time Period (months):", 1, 12, 6)

# Button to start analysis
if st.button("Start Analysis"):
    with st.spinner("Collecting job data..."):
        # Initialize agents
        web_agent = WebSearchAgent()
        extraction_agent = DataExtractionAgent()
        analysis_agent = TrendAnalysisAgent()
        report_agent = ReportWriterAgent()

        # Step 1: Collect job data
        st.write("Fetching job listings...")
        job_listings = web_agent.search_jobs(countries, time_period)

        # Step 2: Extract structured data
        st.write("Extracting job details...")
        job_data = extraction_agent.extract_data(job_listings)

        # Step 3: Analyze trends
        st.write("Analyzing job trends...")
        top_jobs, top_skills, geo_distribution = analysis_agent.analyze_trends(job_data)

        # Step 4: Generate report
        st.write("Generating PDF report...")
        report_path = report_agent.generate_report(top_jobs, top_skills, geo_distribution, countries, time_period)

        # Display download button
        with open(report_path, "rb") as file:
            st.download_button(
                label="Download Report",
                data=file,
                file_name="MENA_AI_Jobs_Report.pdf",
                mime="application/pdf"
            )
        st.success("Report generated successfully!")

# Optional CLI mode
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        countries = ["Egypt", "Saudi Arabia", "UAE"]
        time_period = 6
        web_agent = WebSearchAgent()
        extraction_agent = DataExtractionAgent()
        analysis_agent = TrendAnalysisAgent()
        report_agent = ReportWriterAgent()
        job_listings = web_agent.search_jobs(countries, time_period)
        job_data = extraction_agent.extract_data(job_listings)
        top_jobs, top_skills, geo_distribution = analysis_agent.analyze_trends(job_data)
        report_path = report_agent.generate_report(top_jobs, top_skills, geo_distribution, countries, time_period)
        print(f"Report generated at: {report_path}")
# Run the Streamlit app
