import json
import os

from oauth2client.service_account import ServiceAccountCredentials
import time

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes you need
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

#Playlist and individual song to test
playlistId = "PLrCCqE1vWhlxeIdKkB-J5LXJZiVpdyFiw" #Chill
#videoId = "ljRAR8LXo1k" //previous one
#videoId = "KN8nJFLu1Rk" #IS IT TRUE TAME IMPALA
#videoId = 'Ej8RhiSv2-4' #falling behind by laufey
vId2 = 'PppNloWCMXg' #Human doddie
videoId = 'H7-7TXXnw8I' #TURiSTA bad bunny

def main():
    flow = InstalledAppFlow.from_client_secrets_file('secrets.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlistId,
                "position": 0,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": videoId
                }
            }
        }

    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()