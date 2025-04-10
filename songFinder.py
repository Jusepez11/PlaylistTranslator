import googleapiclient.discovery
import googleapiclient.errors
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib3 import request

from search import playlistId

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

class YouTube:

    def __init__(self, playlistId):
        self.SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
        self.API_KEY = json.load(open('API_KEY.json'))["API_KEY"]
        self.playlistId = playlistId
        self.flow = InstalledAppFlow.from_client_secrets_file('secrets.json', self.SCOPES)

    def auth(self):
        self.credentials = self.flow.run_local_server(port=0)


    def readPlaylist(self):
        #flow = InstalledAppFlow.from_client_secrets_file('secrets.json', SCOPES)
        youtube = build('youtube', 'v3', developerKey=self.API_KEY)

        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId="",
            maxResults=50
        )
        response = request.execute()

    # For testing to check that we are getting what we need, title and link
        #TODO get artist name
        for item in response["items"]:
            title = item["snippet"]["title"]
            video_id = item["snippet"]["resourceId"]["videoId"]
            print(f"{title} - https://www.youtube.com/watch?v={video_id}")


    def insertSong(self, songID, playlistID):
        youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=self.credentials)

        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlistID,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": songID
                    }
                }
            }

        )
        response = request.execute()

        print(response)

    def searchSong(self, songName):
        youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=self.credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=songName,
        )
        response = request.execute()

        self.searched_channel_title = response['items'][0]['snippet']['channelTitle']
        self.searched_title = response['items'][0]['snippet']['title']
        self.searched_video_id = response['items'][0]['id']['videoId']

class Spotify:
    def __init__(self):
        pass

    def readPlaylist(self):
        pass

    def insertSong(self):
        pass

    def searchSong(self):
        pass


playlistId = "PLrCCqE1vWhlxeIdKkB-J5LXJZiVpdyFiw"
videoId = "JI9kNg6wDMY"

test = YouTube(playlistId)
if __name__ == "__main__":
    '''
    test.auth()
    test.searchSong("Passionfruit Drake")
    test.insertSong(test.searched_video_id, playlistId)'''
