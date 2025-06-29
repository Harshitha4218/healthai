import os
from dotenv import load_dotenv

print("🧪 Running test_env.py...")

# Point directly to the .env file in the root folder
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
print(f"Loading .env from: {dotenv_path}")

load_dotenv(dotenv_path)

# Fetch and print variables
apikey = os.getenv("WATSONX_APIKEY")
url = os.getenv("WATSONX_URL")
project_id = os.getenv("PROJECT_ID")

print("WATSONX_APIKEY =", apikey)
print("WATSONX_URL =", url)
print("PROJECT_ID =", project_id)
