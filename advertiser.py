from baseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    _allAdvertisers = []

    def __init__(self, id, name):
        super().__init__()
        self._id = id
        self._name = name
        Advertiser._allAdvertisers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def help():
        return """Advertiser{
             String name: contains name of the Advertiser
             int id: a unique number to identify Advertiser
             int clicks: contains number of clicks that Advertiser has received
             int views: contains number of clicks that Advertiser has received
} """

    @staticmethod
    def get_total_clicks():
        total_clicks = 0
        for advertiser in Advertiser._allAdvertisers:
            total_clicks += advertiser.clicks
        return total_clicks

    def describe_me(self):
        return "Advertiser class: contains advertisers' info and their stats"
