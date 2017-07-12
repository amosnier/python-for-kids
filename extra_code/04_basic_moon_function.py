#earth_weight = 50
#factor = 0.165
#for year in range(1, 16):
#    moon_weight = earth_weight * factor
#    print('year %s: moon weight is %s kg' % (year, moon_weight))
#    earth_weight += 1

factor = 0.165

def moon_weight(earth_weight, weight_increase):
    for year in range(1, 16):
        moon_weight = earth_weight * factor
        print('year %s: moon weight is %s kg' % (year, moon_weight))
        earth_weight += weight_increase

moon_weight(30, 0.25)
