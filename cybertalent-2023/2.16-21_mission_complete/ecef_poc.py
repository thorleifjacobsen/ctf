import math

def ecef_vector_to_lat_lon(vector):

    [[x], [y], [z]] = vector
    lon = math.atan2(y, x)
    hyp = math.sqrt(x ** 2 + y ** 2)
    lat = math.atan2(z, hyp)

    lon = lon * 180 / math.pi
    lat = lat * 180 / math.pi

    return lat, lon

vector = [[4517609.64],  [-45797.26], [4492076.00]]

lat, lon = ecef_vector_to_lat_lon(vector)
print("ECEF x: ",vector[0][0])
print("ECEF y: ",vector[1][0])
print("ECEF z: ",vector[2][0])
print(f"Resolves to: {lat},{lon}") # Bordeaux PERFEKT

def lat_lon_to_ecef_vector(lat, lon):
    lat_rad = lat * math.pi / 180
    lon_rad = lon * math.pi / 180

    x = 6371000 * math.cos(lat_rad) * math.cos(lon_rad)
    y = 6371000 * math.cos(lat_rad) * math.sin(lon_rad)
    z = 6371000 * math.sin(lat_rad)

    return [[x], [y], [z]]


lat = 44.83615102544574
lon = -0.5808159707777749
vector = lat_lon_to_ecef_vector(lat, lon)
print("")
print("Backwards:")
print("ECEF x: ",vector[0][0])
print("ECEF y: ",vector[1][0])
print("ECEF z: ",vector[2][0])
