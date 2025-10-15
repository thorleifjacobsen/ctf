from sage.all import *
from random import randint
from hemmelig import flagg

p = 39761755302725183918693591729206126391094688519137850931996389197052105934335057950945885109127019315116708698582684135940731

a = 37470413545164594923241940723449977961814431955261347161951289533994732796785078955994373335971437954627235171462939970255523
b = 33862474237826219764283873646917712191796653587975971730267794592641857158089029148517141460472220490573591617494610494543421 

gf = GF(p)

E = EllipticCurve(gf, [a, b])

G = E.gen(0)
print(f"G = {G.xy()}")

offentlig_nøkkel = [randint(1, p) * G for _ in flagg]
print(f"offentlig_nøkkel = {[P.xy() for P in offentlig_nøkkel]}")

hemmelighet = [ord(c) for c in flagg]

error = randint(-1000, 1000) * G

resultat = sum(o * h for o, h in zip(offentlig_nøkkel, hemmelighet)) + error
print(f"resultat = {resultat.xy()}")
