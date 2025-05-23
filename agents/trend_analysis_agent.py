import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class TrendAnalysisAgent:
    def analyze_trends(self, job_data):
        """
        Analyzes job data to extract top jobs, skills, and geographic distribution.
        Returns top 10 jobs, top skills, and geographic distribution.
        """
        # Create reports directory if it doesn't exist
        os.makedirs("reports", exist_ok=True)
        
        # Top 10 job titles
        top_jobs = job_data["title"].value_counts().head(10)
        
        # Top skills
        all_skills = job_data["skills"].str.split(", ", expand=True).stack()
        top_skills = all_skills.value_counts().head(10)
        
        # Geographic distribution
        geo_distribution = job_data["country"].value_counts()
        
        # Generate visualizations
        self._plot_top_jobs(top_jobs)
        self._plot_top_skills(top_skills)
        self._plot_geo_distribution(geo_distribution)
        
        return top_jobs, top_skills, geo_distribution
    
    def _plot_top_jobs(self, top_jobs):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="Blues_d")
        plt.title("Top 10 AI/ML Job Titles in MENA")
        plt.xlabel("Number of Listings")
        plt.ylabel("Job Title")
        plt.tight_layout()
        plt.savefig("reports/top_jobs.png")
        plt.close()
    
    def _plot_top_skills(self, top_skills):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_skills.values, y=top_skills.index, palette="Greens_d")
        plt.title("Top 10 Required Skills for AI/ML Jobs")
        plt.xlabel("Frequency")
        plt.ylabel("Skill")
        plt.tight_layout()
        plt.savefig("reports/top_skills.png")
        plt.close()
    
    def _plot_geo_distribution(self, geo_distribution):
        plt.figure(figsize=(10, 6))
        sns.barplot(x=geo_distribution.values, y=geo_distribution.index, palette="Oranges_d")
        plt.title("Geographic Distribution of AI/ML Jobs")
        plt.xlabel("Number of Listings")
        plt.ylabel("Country")
        plt.tight_layout()
        plt.savefig("reports/geo_distribution.png")
        plt.close()