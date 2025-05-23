import pandas as pd
import random

class WebSearchAgent:
    def search_jobs(self, countries, time_period):
        """
        Simulates fetching job listings for AI/ML roles in the MENA region.
        Returns a list of job listings (dictionaries).
        """
        # Mock job titles and skills
        job_titles = [
            "AI Engineer", "Machine Learning Engineer", "Data Scientist",
            "Deep Learning Specialist", "NLP Engineer", "Computer Vision Engineer",
            "AI Research Scientist", "Data Engineer", "MLOps Engineer", "AI Consultant"
        ]
        skills = [
            "Python", "TensorFlow", "PyTorch", "SQL", "R", "AWS", "Azure",
            "Deep Learning", "NLP", "Computer Vision", "Scikit-learn", "Spark"
        ]

        # Generate mock job listings
        job_listings = []
        for _ in range(100):  # Simulate 100 job listings
            job = {
                "title": random.choice(job_titles),
                "skills": random.sample(skills, random.randint(2, 5)),
                "country": random.choice(countries),
                "description": "Sample job description for AI/ML role."
            }
            job_listings.append(job)
        
        return job_listings