import time
import json
import uuid
import random
import datetime
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class JobAssistant:
    """Handles user preferences and input validation."""

    def __init__(self):
        self.preferences = {}

    def get_user_preferences(self):
        """Accepts user input for job title, location, and salary range."""
        self.preferences["job_title"] = input("Enter job title: ").strip()
        self.preferences["location"] = input("Enter job location: ").strip()
        self.preferences["salary_range"] = input("Enter salary range (e.g., 50000 or 50000-80000): ").strip()
        return self.preferences

    def validate_input(self, data):
        """Validates user input using regular expressions."""
        job_title_pattern = r"^[a-zA-Z0-9\s]+$"
        location_pattern = r"^[a-zA-Z\s]+$"
        salary_pattern = r"^\s*(\d{1,6})\s*(-\s*(\d{1,6})\s*)?$"

        if not re.match(job_title_pattern, data.get("job_title", "")):
            raise ValueError("Invalid job title format! Only letters, numbers, and spaces are allowed.")
        if not re.match(location_pattern, data.get("location", "")):
            raise ValueError("Invalid location format! Only letters and spaces are allowed.")
        if not re.match(salary_pattern, data.get("salary_range", "")):
            raise ValueError("Invalid salary range format! Expected format: e.g., 50000 or 50000-80000.")

        salary_range = data["salary_range"].strip()
        if "-" in salary_range:
            salary_min, salary_max = map(int, re.split(r"\s*-\s*", salary_range))
        else:
            salary_min = int(salary_range)
            salary_max = 999999

        if salary_min > salary_max:
            raise ValueError("Invalid salary range! The first value should be less than the second.")
        self.preferences["salary_range"] = f"{salary_min}-{salary_max}"

class JobScraper:
    """Scrapes job listings dynamically using Selenium."""

    def __init__(self, url, preferences):
        self.url = url
        self.preferences = preferences
        self.jobs = []

    def scrape_jobs(self):
        """Fetches job listings dynamically using Selenium."""
        options = Options()
        options.headless = False  
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(self.url)
            time.sleep(3)  

            
            job_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "job_title"))  
            )
            job_input.send_keys(self.preferences["job_title"])

            
            location_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "location"))
            )
            location_input.send_keys(self.preferences["location"])

            
            salary_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "salary"))  
            )
            salary_input.send_keys(self.preferences["salary_range"])
            salary_input.send_keys(Keys.RETURN)

            time.sleep(3)  

            
            job_cards = driver.find_elements(By.CLASS_NAME, "job-card")  
            for job in job_cards:
                try:
                    title = job.find_element(By.TAG_NAME, "h2").text.strip()
                    company = job.find_element(By.TAG_NAME, "h3").text.strip()
                    location = job.find_element(By.CLASS_NAME, "location").text.strip()
                    salary = job.find_element(By.CLASS_NAME, "salary").text.strip() if job.find_elements(By.CLASS_NAME, "salary") else "Not specified"
                    description = job.find_element(By.CLASS_NAME, "description").text.strip()

                    job_data = {
                        "id": str(uuid.uuid4()),
                        "title": title,
                        "company": company,
                        "location": location,
                        "salary": salary,
                        "description": description
                    }
                    self.jobs.append(job_data)
                except Exception as e:
                    print(f"Error extracting job details: {e}")

        except Exception as e:
            print(f"Error scraping jobs: {e}")
        finally:
            driver.quit()

        return self.jobs

class JobManager:
    """Handles storing and logging job details."""

    @staticmethod
    def store_jobs(jobs):
        """Stores filtered jobs in a JSON file."""
        with open("jobs.json", "w") as f:
            json.dump(jobs, f, indent=4)

    @staticmethod
    def log_activity(activity):
        """Logs scraping and automation activity."""
        with open("job_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {activity}\n")

if __name__ == "__main__":
    job_assistant = JobAssistant()
    preferences = job_assistant.get_user_preferences()

    try:
        job_assistant.validate_input(preferences)
    except ValueError as e:
        print(f"Validation Error: {e}")
        exit(1)

    scraper = JobScraper("https://www.jobs-hunter.com/", preferences)
    jobs = scraper.scrape_jobs()

    if jobs:
        JobManager.store_jobs(jobs)
        print(f"Scraped and saved {len(jobs)} jobs.")
    else:
        print("No jobs found.")
