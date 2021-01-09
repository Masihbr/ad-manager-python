class BaseAdvertising:

    def __init__(self):
        _id = 0
        _clicks = 0
        _views = 0

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

    def describe_me(self):
        return "parent class for Ad and Advertiser class"
