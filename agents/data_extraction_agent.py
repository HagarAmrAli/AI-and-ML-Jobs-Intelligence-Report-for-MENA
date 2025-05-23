import pandas as pd

class DataExtractionAgent:
    def extract_data(self, job_listings):
        """
        Extracts structured data from job listings.
        Returns a pandas DataFrame with job title, skills, and country.
        """
        data = {
            "title": [],
            "skills": [],
            "country": []
        }
        
        for job in job_listings:
            data["title"].append(job["title"])
            data["skills"].append(", ".join(job["skills"]))
            data["country"].append(job["country"])
        
        return pd.DataFrame(data)