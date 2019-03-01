from nico_client.html_page import HtmlPage
from nico_client.video import Video
from utils import html2json


class DailyTrending(HtmlPage):
    def to_json(self):
        json_array = []
        items = list(filter(lambda line: '<div class="itemData">' in line, self.html_string.split('\n')))
        for item in items:
            json_object = html2json.HTMLtoJSONParser.to_json(item)
            json_array.append(json_object)
        return json_array

    def __get_video(self, json_element):
        href = None
        likes = None
        views = None

        bullet_points = json_element['div']['ul']['li']
        for bullet_point in bullet_points:
            if bullet_point['#class'] == 'count mylist':
                hyperlink = bullet_point['span']['a']
                href = hyperlink['#href']
                likes = hyperlink['']
            elif bullet_point['#class'] == 'count view':
                views = bullet_point['span']['']

        if href:
            video_id = href.split('/')[-1]
            views = int(views.replace(',', ''))
            likes = int(likes.replace(',', ''))
            return Video(video_id=video_id, views=views, likes=likes)

        return None

    def get_videos(self):
        videos = []
        for element in self.to_json():
            video = self.__get_video(element)
            if video is not None:
                videos.append(video)
        return videos
