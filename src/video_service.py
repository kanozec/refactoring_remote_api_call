import json
import os

import googleapiclient.discovery
import googleapiclient.errors
from datetime import date, timedelta
from dateutil import parser

API_KEY = "YOUR_API_KEY"

dir_path = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.join(dir_path, 'videos.json')


class VideoService:
    def video_list(self):
        with open(json_path) as json_file:
            videos_list = json.load(json_file)
        ids = [x['youtubeID'] for x in videos_list]

        youtube = googleapiclient.discovery.build(
            "youtube", "v3", developerKey=API_KEY)
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(ids)
        )

        response = request.execute()

        for video in videos_list:
            youtube_record = [x for x in response['items'] if x['id'] == video['youtubeID']][0]
            video['views'] = int(youtube_record['statistics']['viewCount'])
            today = date.today()
            published_day = parser.parse(youtube_record['snippet']['publishedAt']).date()
            days_available = today - published_day
            video['monthlyViews'] = video['views'] * 365.0 / days_available.days / 12
        return json.dumps(videos_list)
