class BaseAdvertising:

    def __init__(self):
        _id = 0
        _clicks = 0
        _views = 0

    def getClicks(self):
        return self._clicks

    def getViews(self):
        return self._views

    def incClicks(self):
        self._clicks += 1

    def incViews(self):
        self._views += 1

    def describeMe(self):
        return "parent class for Ad and Advertiser class"
