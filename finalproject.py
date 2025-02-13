import requests
from bs4 import BeautifulSoup
import re
import json
import time
import uuid
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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

        # Parse salary range
        salary_range = data["salary_range"].strip()
        if "-" in salary_range:
            salary_min, salary_max = map(int, re.split(r"\s*-\s*", salary_range))
        else:
            salary_min = int(salary_range)
            salary_max = 999999  # Set a very high maximum value if only one value is provided

        if salary_min > salary_max:
            raise ValueError("Invalid salary range! The first value should be less than the second.")

        # Update preferences with parsed salary range
        self.preferences["salary_range"] = f"{salary_min}-{salary_max}"


class JobScraper:
    """Scrapes job listings from a website."""

    def __init__(self, url):
        self.url = url
        self.jobs = []

    def scrape_jobs(self):
        """Fetches job listings from the given job portal."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            job_cards = soup.find_all("div", class_="job-card")
            for job in job_cards:
                title = job.find("h2").text.strip()
                company = job.find("h3").text.strip()
                location = job.find("p", class_="location").text.strip()
                salary = job.find("span", class_="salary").text.strip() if job.find("span", class_="salary") else "Not specified"
                description = job.find("p", class_="description").text.strip()

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
            print(f"Error scraping jobs: {e}")
        return self.jobs


class JobFilter:
    """Filters jobs based on user preferences."""

    def __init__(self, jobs, preferences):
        self.jobs = jobs
        self.preferences = preferences

    def filter_jobs(self):
        """Filters jobs based on user-defined keywords and salary range."""
        filtered_jobs = []
        salary_min, salary_max = map(int, self.preferences["salary_range"].split("-"))

        for job in self.jobs:
            if (self.preferences["job_title"].lower() in job["title"].lower() and
                self.preferences["location"].lower() in job["location"].lower() and
                job["salary"] != "Not specified"):

                # Handle salary parsing (remove non-numeric characters)
                salary = int(re.sub(r"[^\d]", "", job["salary"]))
                if salary_min <= salary <= salary_max:
                    filtered_jobs.append(job)

        return filtered_jobs


class JobManager:
    """Handles storing and logging job details."""

    @staticmethod
    def store_jobs(jobs):
        """Stores filtered jobs in a text file."""
        with open("jobs.txt", "w") as f:
            json.dump(jobs, f, indent=4)

    @staticmethod
    def log_activity(activity):
        """Logs scraping and automation activity."""
        with open("job_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {activity}\n")


class JobAutomation:
    """Automates the job application process."""

    def __init__(self, jobs):
        self.jobs = jobs

    def apply_jobs(self):
        """Uses Selenium to automate job applications."""
        options = Options()
        options.headless = True
        service = Service("chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

        try:
            jobs_to_apply = random.sample(self.jobs, min(3, len(self.jobs)))
            for job in jobs_to_apply:
                driver.get("https://www.example-job-portal.com")  
                time.sleep(2)

                search_box = driver.find_element(By.NAME, "search")
                search_box.send_keys(job["title"])
                search_box.send_keys(Keys.RETURN)
                time.sleep(2)

                apply_button = driver.find_element(By.CLASS_NAME, "apply-now")
                apply_button.click()
                time.sleep(1)

                name_input = driver.find_element(By.NAME, "name")
                email_input = driver.find_element(By.NAME, "email")
                resume_upload = driver.find_element(By.NAME, "resume")

                name_input.send_keys("John Doe")
                email_input.send_keys("john.doe@example.com")
                resume_upload.send_keys("/path/to/resume.pdf")  

                submit_button = driver.find_element(By.NAME, "submit")
                submit_button.click()
                time.sleep(1)

                JobManager.log_activity(f"Applied for {job['title']} at {job['company']}")

        except Exception as e:
            print(f"Error in automation: {e}")
        finally:
            driver.quit()


if __name__ == "__main__":
    job_assistant = JobAssistant()
    preferences = job_assistant.get_user_preferences()
    try:
        job_assistant.validate_input(preferences)
    except ValueError as e:
        print(f"Validation Error: {e}")
        exit(1)

    scraper = JobScraper("https://www.example-job-portal.com")  
    jobs = scraper.scrape_jobs()
    job_filter = JobFilter(jobs, preferences)
    filtered_jobs = job_filter.filter_jobs()
    JobManager.store_jobs(filtered_jobs)

    automation = JobAutomation(filtered_jobs)
    automation.apply_jobs()