import pandas as pd
import re
import ast

from bs4 import BeautifulSoup
import requests

def load_and_filter_data(file_path, relevant_columns):
    data = pd.read_csv(file_path)
    return data[relevant_columns]

def extract_names_simple(data_str):
    try:
        return ", ".join(re.findall(r'"name":\s?"(.*?)"', data_str)) if data_str else None
    except Exception:
        return None

def process_skills(skills_str):
    try:
        skills_list = ast.literal_eval(skills_str)
        return ", ".join(skills_list) if isinstance(skills_list, list) else skills_str
    except (ValueError, SyntaxError):
        return None

def preprocess_columns_simple(df):
    df['education'] = df['education'].apply(extract_names_simple)
    df['work_history'] = df['work_history'].apply(extract_names_simple)
    df['skills'] = df['skills'].apply(process_skills)
    return df

def scrape_and_summarize_domain(url):
    try:
        # Fetch the webpage
        response = requests.get("https://" + url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and clean up the text content
        paragraphs = soup.find_all('p')
        clean_text = [p.get_text(strip=True) for p in paragraphs]
        combined_text = ' '.join(clean_text)

        # Truncate or summarize the combined text to fit
        summary = combined_text[:1000]  # Example: truncate to 1000 characters
        return summary
    except Exception as e:
        return f"Error fetching or summarizing content from {url}: {str(e)}"

def enrich_advertiser_data_with_domain(df):
    df['domain_info'] = df['company_domain'].apply(scrape_and_summarize_domain)
    return df
