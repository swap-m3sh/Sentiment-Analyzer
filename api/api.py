import os
from googleapiclient.discovery import build

def main():
    # only for development
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get('DEV_KEY')

    youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        order="relevance",
        textFormat="html",
        videoId="E16WhXcIghM"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()