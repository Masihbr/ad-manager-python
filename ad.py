from baseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__()
        self._id = id
        self._title = title
        self._img_url = imgUrl
        self._link = link
        self._advertiser = advertiser

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def img_url(self):
        return self._img_url

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    def __setattr__(self, key, value):
        if key == 'advertiser':
            self._advertiser = value
        
    def describe_me(self):
        return "Ad class: contains Ads' info and their stats"

    def inc_clicks(self):
        self._clicks += 1
        self._advertiser.inc_clicks()

    def inc_views(self):
        self._views += 1
        self._advertiser.inc_views()
