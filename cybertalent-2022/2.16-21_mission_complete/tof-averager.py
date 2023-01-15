from math import sin, cos, sqrt, atan2, pi
import geopy.distance

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000 # radius of Earth in meters
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def ecef_vector_to_lat_lon(x,y,z):

    lon = atan2(y, x)
    hyp = sqrt(x ** 2 + y ** 2)
    lat = atan2(z, hyp)

    lon = lon * 180 / pi
    lat = lat * 180 / pi

    return lat, lon


## 
## Remove coment on the sub ur testing and comment the 4 others out.
##
vect = []
# Sub 1
vect.append([1080.00, 3965173.80,   -8172.61, 4986679.35, "ill-buzz"])
vect.append([1080.00, 3877218.23, -128524.04, 5053741.33, "tan-city"])
vect.append([1080.00, 3788140.78, -148481.80, 5120310.89, "any-fang"])
vect.append([1080.00, 3793400.39, -197697.20, 5114750.27, "six-crop"])
vect.append([1080.00, 3761259.92, -101682.56, 5141228.01, "few-darn"])
vect.append([1200.00, 3565283.98, -265059.37, 5273341.89, "its-folk"])
vect.append([1200.00, 3561474.41, -199048.12, 5278818.14, "wry-cook"])
vect.append([1000.00, 3798982.34,  -97495.01, 5113498.70, "few-area"])
vect.append([1080.00, 3780277.58, -415086.43, 5111442.62, "bad-dime"])
vect.append([1100.00, 3904518.71,  292813.87, 5025796.92, "day-acid"])
vect.append([ 500.00, 4517609.64,  -45797.26, 4492076.00, "bad-dory"])
vect.append([1300.00, 3931251.08,  515136.93, 4986936.93, "her-chin"])
vect.append([ 900.00, 4840420.30, -313337.46, 4130592.21, "the-clue"])
vect.append([1080.00, 3978633.52,  306311.28, 4966516.86, "sly-chug"])
vect.append([1500.00, 3771037.60,  898732.45, 5055808.19, "one-epee"])
vect.append([1200.00, 4629467.70, 1026020.23, 4254991.45, "top-game"])
# Sub 2
# vect.append([2000.00, 2871529.36, 1335712.45, 5528094.82, "fat-blow"])
# vect.append([1400.00, 3916904.74,  305684.71, 5015381.85, "coy-drug"])
# vect.append([1100.00, 3506335.17,  781724.52, 5261574.05, "new-bore"])
# vect.append([1300.00, 4187571.65,  171778.44, 4798372.31, "top-draw"])
# vect.append([2000.00, 4073672.03, 1196123.56, 4750171.12, "hot-blow"])
# vect.append([1800.00, 3642005.91, 1399313.87, 5036601.50, "sea-axis"])
# vect.append([1100.00, 3727617.22,  656855.67, 5124748.92, "ten-bank"])
# vect.append([2100.00, 4068863.73, 1404219.05, 4697037.13, "new-epic"])
# vect.append([2000.00, 4776300.55,  179647.34, 4212400.85, "icy-beat"])
# vect.append([1800.00, 4165201.60,  853184.42, 4744766.90, "odd-cyst"])
# vect.append([1500.00, 3089215.84, 1007518.11, 5480081.55, "own-axis"])
# vect.append([1600.00, 4038925.22,  616753.05, 4888388.26, "fat-dirt"])
# vect.append([1300.00, 3137883.12,  596195.86, 5512520.39, "six-fill"])
# vect.append([2000.00, 3960132.01, 1018155.11, 4885729.80, "two-comb"])
# vect.append([1600.00, 4144099.14,  669960.54, 4792414.44, "own-chop"])
# vect.append([2000.00, 3824498.89, 1172080.09, 4958737.49, "raw-coke"])
# Sub 3
# vect.append([1500.00, 4410958.41,  713514.00, 4541363.75, "odd-fine"])
# vect.append([1300.00, 4299765.90, 1853546.05, 4320419.11, "the-fact"])
# vect.append([1900.00, 3985471.63,  486043.26, 4946657.34, "fat-dawn"])
# vect.append([ 600.00, 4669514.06, 1190727.92, 4167426.84, "sly-foal"])
# vect.append([1900.00, 3874979.79,  332003.34, 5046181.37, "bad-clef"])
# vect.append([1600.00, 4616563.98,  433955.07, 4369057.23, "wee-beet"])
# vect.append([1000.00, 4446250.49,  604524.44, 4522725.70, "one-dirt"])
# vect.append([1700.00, 3845603.32, 1395471.42, 4884018.39, "icy-bias"])
# vect.append([1700.00, 4918271.64,  -32190.47, 4049593.66, "sea-cafe"])
# vect.append([1000.00, 4269110.60, 1221452.38, 4568631.07, "tan-burn"])
# vect.append([2000.00, 5034046.16, -528572.99, 3868931.49, "cut-cyst"])
# vect.append([1800.00, 4759979.88,  -73754.64, 4234004.35, "few-case"])
# vect.append([1700.00, 3718215.79, 1313565.45, 5003904.29, "wee-boss"])
# vect.append([1080.00, 4085093.56, 2000940.11, 4460705.13, "two-fork"])
# vect.append([1900.00, 3961278.75,  471185.24, 4967483.89, "all-area"])
# vect.append([ 600.00, 4876635.39, 1158780.74, 3932593.98, "shy-chip"])
# Sub 4
# vect.append([2200.00, 4597051.62, 2020600.46, 3920960.49, "hot-beat"])
# vect.append([2000.00, 3171884.46, 1419189.87, 5339914.80, "all-colt"])
# vect.append([1600.00, 3887682.95,  851924.98, 4974915.69, "fun-babe"])
# vect.append([1700.00, 3329463.78,  706154.41, 5385690.11, "new-bear"])
# vect.append([1300.00, 4611888.79,  116255.99, 4393928.46, "the-copy"])
# vect.append([1100.00, 3865581.56,  -76231.47, 5063705.07, "old-bass"])
# vect.append([1400.00, 4570639.43,  584655.32, 4399667.53, "low-diet"])
# vect.append([1100.00, 3670172.41, -380922.31, 5193685.94, "few-babe"])
# vect.append([1500.00, 3940686.48,  484402.33, 4982568.16, "due-edge"])
# vect.append([1600.00, 5091632.09, -393567.62, 3809203.09, "icy-alto"])
# vect.append([2000.00, 3330020.22, 1572646.72, 5198787.23, "wee-gene"])
# vect.append([1550.00, 3782049.34,  585606.67, 5093408.35, "two-fate"])
# vect.append([1600.00, 4496095.57,  707789.04, 4458004.07, "hot-coin"])
# vect.append([1600.00, 3890478.06,  951077.25, 4954722.35, "red-chef"])
# vect.append([1500.00, 4907473.21, -789505.95, 3985351.69, "key-debt"])
# vect.append([1750.00, 3718324.97, 1131497.77, 5048109.87, "key-geek"])
# Sub 5
# vect.append([2000.00, 3833839.73,  657618.26, 5045676.58, "big-bone"])
# vect.append([1300.00, 4428743.04,  374560.24, 4564600.82, "bad-chug"])
# vect.append([1700.00, 4063995.57,  794515.12, 4841727.66, "few-beam"])
# vect.append([1600.00, 3944256.52,  467894.59, 4981320.73, "due-coat"])
# vect.append([2000.00, 3516587.05, 1186080.23, 5178462.15, "her-cash"])
# vect.append([2000.00, 4062712.85, 1250376.84, 4745583.53, "icy-fate"])
# vect.append([1100.00, 5019970.12,  -99074.77, 3921699.27, "sad-bend"])
# vect.append([2200.00, 2941903.82, 1356458.76, 5485878.47, "two-fill"])
# vect.append([1100.00, 4905851.41,  227075.15, 4058411.00, "coy-boat"])
# vect.append([1800.00, 3674173.23,  953834.06, 5116668.12, "dry-epic"])
# vect.append([1400.00, 4455748.78,  894105.71, 4465032.90, "its-bulb"])
# vect.append([ 600.00, 4898728.76, -809920.21, 3992007.87, "mad-bulb"])
# vect.append([1800.00, 3989809.15, 1190414.03, 4822237.90, "shy-cock"])
# vect.append([1200.00, 5437633.32,-1356240.55, 3030246.93, "the-boot"])
# vect.append([1500.00, 4511619.77,  898015.45, 4407776.80, "cut-fuel"])
# vect.append([1600.00, 4367306.66,  953423.03, 4539521.79, "one-boom"])

msAvg = 0

for cord in vect:
  
  lat, lng = ecef_vector_to_lat_lon(cord[1], cord[2], cord[3])
  dist = geopy.distance.geodesic((45,-5), (lat,lng)).m
  ms = dist / cord[0]
  print(f"{cord[4]} - dist {round(dist/1000)}km - {round(ms)}m/s")
  msAvg += ms

msAvg = msAvg / 16

print(f"{round(msAvg)}m/s i snitt over 16 missiler")

## 
## Remove coment on the sub ur testing and comment the 4 others out.
##
ourLoc=(45,-5) # Sub 1
# ourLoc=(60,-10) # Sub 2
# ourLoc=(37,19) # Sub 3
# ourLoc=(50,-20) # Sub 4
# ourLoc=(40,-15) # Sub 5




distToSafe = geopy.distance.geodesic(ourLoc, (24.1851, -43.3704)).m
print(f"{round(distToSafe/1000)}km to safe zone")
print(f"{round(distToSafe/msAvg)}s TOF to safe zone")