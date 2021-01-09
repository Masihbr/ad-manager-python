from baseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__()
        self._id = id
        self.__title = title
        self.__img_url = imgUrl
        self.__link = link
        self.__advertiser = advertiser

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_img_url(self):
        return self.__img_url

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser

    def describe_me(self):
        return "Ad class: contains Ads' info and their stats"

    def inc_clicks(self):
        self._clicks += 1
        self.__advertiser.inc_clicks()

    def inc_views(self):
        self._views += 1
        self.__advertiser.inc_views()
