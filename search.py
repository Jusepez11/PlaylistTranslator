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

def main():
    #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Create an OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file('secrets.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

    request = youtube.search().list(
        part='id',
        q="Feid - Feliz Cumpleaños Ferxxo",
        type='video',
        maxResults=1
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
'''
 async function getVideoIdsForSongs(songNames) {
  const videoIds = [];

  for (const songName of songNames) {
    const response = await fetch(
      `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(
        songName
      )}&type=video&maxResults=1&key=YOUR_API_KEY`
    ); 

    const data = await response.json();

    if (data.items && data.items.length > 0) {
      videoIds.push(data.items[0].id.videoId);
    } else {
      // Handle case where no video is found for the song
      videoIds.push(null); 
    }
  }

  return videoIds;
}'''