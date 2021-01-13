class BaseAdvertising:

    def __init__(self):
        self._id = 0
        self._clicks = 0
        self._views = 0

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

    @property
    def clicks(self):
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        self._clicks = clicks

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self):
        return self._views
    
    def describe_me(self):
        return "parent class for Ad and Advertiser class"
