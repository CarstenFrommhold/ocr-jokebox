from soco import SoCo, discover

for zone in discover():
	print(zone.player_name)

zone_list = list(discover())

print(zone_list)