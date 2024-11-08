import googleapiclient.discovery
import googleapiclient.errors
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib3 import request

# Define the scopes you need
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file('secrets.json', SCOPES)
API_KEY = json.load(open('API_KEY.json'))["API_KEY"]
youtube = build('youtube', 'v3', developerKey=API_KEY)

request = youtube.Search().list(


)