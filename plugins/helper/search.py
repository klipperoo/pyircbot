#!/usr/bin/python

from apiclient.discovery import build
import secrets


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = secrets.GOOGLEDEVELOPERKEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
         q=query,
        part="id,snippet"
    ).execute()

    # Return the data for the first json object
    return search_response.get("items")[0]