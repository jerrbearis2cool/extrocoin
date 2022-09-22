import math
from math import sqrt, pi, sin, cos #mmm yes import

user_dict = {"jerrbear" : {"coords":[10, 10], "last_ten_coords":[[1.001,1],[1, 1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],]}}

def measure(lat1, lon1, lat2, lon2):
    R = 6378.137
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000

class user_data:
    def __init__(self, user):
        user_data.user = user
        user_data.coords = user_dict.get(user).get("coords")
        user_data.last_ten_coords = user_dict.get(user).get("last_ten_coords")

    def last_ten_coords(self):
        return user_data.last_ten_coords
    def coords(self):
        return user_data.coords

def check_spoof(user):
    length = []
    location_list = user_data.last_ten_coords
    for i in range(0, 8):
        x1, y1 = location_list[i] #compares the distance between two points using pyagorean theorum
        x2, y2 = location_list[i + 1]
        length.append(measure(x1, y1, x2, y2))
    '''for i in range(0, 8):
        if length[i] == length[i + 1]:
            results = {"status": "FAIL", "reason": "DUPLICATE_LENGTH"}
            break
        else:'''
    return sum(length)

print(check_spoof("jerrbear"))
