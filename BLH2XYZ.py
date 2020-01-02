import math
def change(coordinate, direction):
    cor_list = coordinate.split(':')
    cor_loat = float(cor_list[0]) + (float(cor_list[1]) + float(cor_list[2])/60)/60
    if direction == 'N' or direction == 'W':
        return cor_loat*(-1)
    elif direction == 'S' or direction == 'E':
        return cor_loat
    else:
        return 0



def blh2xyz(b ,l, h):
    b = change(b, 'N')
    l = change(l, 'E')
    h = float(h)
    strb = (b/180)*math.pi
    strl = (l/180)*math.pi
    sinp = math.sin(strb)
    cosp = math.cos(strb)
    sinl = math.sin(strl)
    cosl = math.cos(strl)
    e2 = (1.0 / 298.257223563) * (2.0 - (1.0 / 298.257223563))
    v = 6378137.0 / math.sqrt(1.0 - e2 * sinp * sinp)
    r = [0, 0, 0]
    if str(((v + h) * cosp * cosl)) == '6378137.0' or str(((v + h) * cosp * cosl)) == 'NaN':
        r[0] = 0
    else:
        r[0] = (v + h) * cosp * cosl
    if str(((v + h) * cosp * sinl)) == 'NaN':
        r[1] = 0
    else:
        r[1] = (v + h) * cosp * sinl
    if str(((v * (1.0 - e2) + h) * sinp)) == 'NaN':
        r[2] = 0
    else:
        r[2] = -(v * (1.0 - e2) + h) * sinp
    return r


if __name__ == '__main__':
    r = blh2xyz(' 031:14:40.842963976092214',' 121:35:32.85703129974859', '35.009688250083016')

    print(r)