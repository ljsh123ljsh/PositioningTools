import math
import numpy



def blh2enu(b, l):
    strb = (float(b) / 180) * math.pi
    strl = (float(l) / 180) * math.pi
    sinp = math.sin(strb)
    cosp = math.cos(strb)
    sinl = math.sin(strl)
    cosl = math.cos(strl)
    tranE = numpy.mat([
        [-sinl, cosl, 0],
        [-sinp * cosl, -sinp * sinl, cosp],
        [cosp * cosl, cosp * sinl, sinp]
    ])
    return tranE
