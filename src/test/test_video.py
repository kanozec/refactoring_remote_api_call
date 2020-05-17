import json
import unittest
from datetime import datetime
from unittest import mock

from src.video_service import VideoService


class MyTestCase(unittest.TestCase):
    def fack(self, ids):
        with open("youtube-video-list.json") as test_file:
            fake_response = json.load(test_file)
        return fake_response

    def mocked_today(self):
        return datetime(2020, 5, 19).date()

    @mock.patch.object(VideoService, 'get_today', mocked_today)
    @mock.patch.object(VideoService, 'call_youtube', fack)
    def test_video_list(self):
        vs = VideoService()
        videos = json.loads(vs.video_list())
        video1 = [x for x in videos if x['youtubeID'] == '9hyV27g9YFk'][0]
        video2 = [x for x in videos if x['youtubeID'] == 'C2WCbHTTB-4'][0]
        video3 = [x for x in videos if x['youtubeID'] == 'l-pWz9p7AvU'][0]

        self.assertEqual(191120, video1['views'])
        self.assertEqual(3767755, video2['views'])
        self.assertEqual(235127, video3['views'])


if __name__ == '__main__':
    unittest.main()
