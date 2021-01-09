from baseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    __allAdvertisers = []

    def __init__(self, id, name):
        super().__init__()
        self._id = id
        self.__name = name
        Advertiser.__allAdvertisers.append(self)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

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
        n = len(Advertiser.__allAdvertisers)
        sum = 0
        for i in range(0, n):
            sum += Advertiser.__allAdvertisers[i].get_clicks()
        return sum

    def describe_me(self):
        return "Advertiser class: contains advertisers' info and their stats"
