from baseAdvertising import BaseAdvertising
from ad import Ad
from advertiser import Advertiser

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
print(baseAdvertising.describe_me())
print(ad2.describe_me())
print(advertiser1.describe_me())
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
print(advertiser2.name)
advertiser2.name = "new name"
print(advertiser2.name)
print(ad1.clicks)
print(advertiser2.clicks)
print(Advertiser.get_total_clicks())
print(Advertiser.help())