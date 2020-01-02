from pandas import read_csv
from numpy import array, square, average, sqrt, dot, mat
from pandas import DataFrame
from BLH2ENU import blh2enu
from BLH2XYZ import change
from BLH2XYZ import blh2xyz

def openfile(address):
    coding_list = ['utf-8', "gbk", 'ANSI']
    for code in coding_list:
        try:
            df = read_csv(address, encoding=code)
            break
        except:
            continue
    return df


def BLH2precise_neu(address):
    df = openfile(address)
    np_B = array(df['B'])
    np_L = array(df['L'])
    B2 = array([float(i.split(":")[2]) for i in np_B])
    L2 = array([float(i.split(":")[2]) for i in np_L])
    b_ave = average(B2)
    l_ave = average(L2)
    np_H = array(df['H'])
    h_ave = average(np_H)
    print(b_ave, l_ave, h_ave)
if __name__ == '__main__':
    address = '1225/csv_1227_1.csv'
    BLH2precise_neu(address)