from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet
import os
import pandas as pd

class ReportWriterAgent:
    def generate_report(self, top_jobs, top_skills, geo_distribution, countries, time_period):
        """
        Generates a PDF report with job trends, skills, and geographic distribution.
        Returns the path to the generated PDF.
        """
        report_path = "reports/MENA_AI_Jobs_Report.pdf"
        os.makedirs("reports", exist_ok=True)
        
        doc = SimpleDocTemplate(report_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        story.append(Paragraph("AI & ML Jobs Intelligence Report - MENA Region", styles["Title"]))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"Countries: {', '.join(countries)}", styles["Normal"]))
        story.append(Paragraph(f"Time Period: {time_period} months", styles["Normal"]))
        story.append(Spacer(1, 12))
        
        # Top 10 Jobs
        story.append(Paragraph("Top 10 AI/ML Job Titles", styles["Heading2"]))
        job_table_data = [["Job Title", "Count"]]
        for job, count in top_jobs.items():
            job_table_data.append([job, str(count)])
        job_table = Table(job_table_data)
        job_table.setStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])
        story.append(job_table)
        story.append(Spacer(1, 12))
        story.append(Image("reports/top_jobs.png", width=400, height=200))
        story.append(Spacer(1, 12))
        
        # Top Skills
        story.append(Paragraph("Top Required Skills", styles["Heading2"]))
        skills_table_data = [["Skill", "Frequency"]]
        for skill, count in top_skills.items():
            skills_table_data.append([skill, str(count)])
        skills_table = Table(skills_table_data)
        skills_table.setStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])
        story.append(skills_table)
        story.append(Spacer(1, 12))
        story.append(Image("reports/top_skills.png", width=400, height=200))
        story.append(Spacer(1, 12))
        
        # Geographic Distribution
        story.append(Paragraph("Geographic Distribution", styles["Heading2"]))
        geo_table_data = [["Country", "Count"]]
        for country, count in geo_distribution.items():
            geo_table_data.append([country, str(count)])
        geo_table = Table(geo_table_data)
        geo_table.setStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ])
        story.append(geo_table)
        story.append(Spacer(1, 12))
        story.append(Image("reports/geo_distribution.png", width=400, height=200))
        
        # Build PDF
        doc.build(story)
        return report_path