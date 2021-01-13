from baseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__()
        self._id = id
        self._title = title
        self._img_url = imgUrl
        self._link = link
        self._advertiser = advertiser

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_img_url(self):
        return self._img_url

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def set_advertiser(self, advertiser):
        self._advertiser = advertiser

    def describe_me(self):
        return "Ad class: contains Ads' info and their stats"

    def inc_clicks(self):
        self._clicks += 1
        self._advertiser.inc_clicks()

    def inc_views(self):
        self._views += 1
        self._advertiser.inc_views()
