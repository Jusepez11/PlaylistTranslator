import googleapiclient.discovery
import googleapiclient.errors
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib3 import request

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    # Define the scopes you need
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    #flow = InstalledAppFlow.from_client_secrets_file('secrets.json', SCOPES)
    API_KEY = json.load(open('API_KEY.json'))["API_KEY"]
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId="PLrCCqE1vWhlxeIdKkB-J5LXJZiVpdyFiw",
        maxResults=50
    )
    response = request.execute()

# For testing to check that we are getting what we need, title and link
    #TODO get artist name 
    for item in response["items"]:
        title = item["snippet"]["title"]
        video_id = item["snippet"]["resourceId"]["videoId"]
        print(f"{title} - https://www.youtube.com/watch?v={video_id}")

if __name__ == "__main__":
    main()
