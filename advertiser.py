from baseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    __allAdvertisers = []

    def __init__(self, id, name):
        super().__init__()
        self._id = id
        self.__name = name
        Advertiser.__allAdvertisers.append(self)
