from nico_client import populate_details
from nico_client.model.video import Video
from tests import IntegrationTest


class TestVideoInfoHandler(IntegrationTest):
    def test_video_attribute_population_nicopy(self):
        video = Video(id='sm34734479')
        self.assertIsNone(video.views)
        populate_details(video, 'nicopy')
        self.assertEqual(type(video.views), int, "video.views is expected to be an integer")

    def test_date_parser(self):
        video = Video(id='sm34734479')
        populate_details(video, 'nicopy')
        upload_time_nicopy = video.upload_time
        populate_details(video, 'html_parser')
        upload_time_html = video.upload_time
        self.assertEqual(upload_time_nicopy, upload_time_html)
