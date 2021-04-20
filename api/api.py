import os
import sys
import json
import pandas as pd
from googleapiclient.discovery import build

def fetchComments(url):
    # only for development
    url_list = url.split(sep="=")
    video_url = url_list[-1]

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get('DEV_KEY')

    youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        order="relevance",
        maxResults=50,
        textFormat="html",
        videoId= video_url
    )
    response = request.execute()
    data = []
    for v in response['items']:
        data.append(v['snippet']['topLevelComment']['snippet']['textOriginal'])    
    comments = pd.Series(data)
    return comments

if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    print(fetchComments(arg))