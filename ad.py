from baseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__()
        self._id = id
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    def inc_clicks(self):
        self._clicks += 1
        self._advertiser.inc_clicks()

    def inc_views(self):
        self._views += 1
        self._advertiser.inc_views()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, img_url):
        self._img_url = img_url

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def advertiser(self):
        return None

    @advertiser.setter
    def advertiser(self, advertiser):
        self._advertiser = advertiser

    def describe_me(self):
        return "Ad class: contains Ads' info and their stats"
