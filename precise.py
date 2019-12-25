from pandas import read_csv
from numpy import array, square, average, sqrt
from pandas import DataFrame
PRE_LOCATION_BLH = {
    'B': '31:14:40.84330',
    'L': '121:35:32.85687',
    'H': '34.8738'
}
PRE_LOCATION_XYZ = {
    'X': '-2859303.0243',
    'Y': '4649101.4526',
    'Z': '3289134.8596'
}

def openfile(address):
    coding_list = ['utf-8', "gbk", 'ANSI']
    for code in coding_list:
        try:
            df = read_csv(address, encoding=code)
        except:
            continue
    return df

def Calculation_1(lis, location):
    '''
    :param lis: 输入列表
    :param location: 输入绝对位置
    :return: 返回列表与位置的差值平方再取平均数，再开方
    '''
    res_lis = array([square(li-location) for li in lis])
    average_lis = average(res_lis)
    sqrt_lis = sqrt(average_lis)
    return sqrt_lis

def XYZ2precise(address):
    df = openfile(address)
    df_X = df['空间直角X']
    df_Y = df['空间直角Y']
    df_Z = df['空间直角Z']
    np_X = array(df_X)
    np_Y = array(df_Y)
    np_Z = array(df_Z)
    sq_X1 = Calculation_1(np_X, float(PRE_LOCATION_XYZ['X']))
    sq_Y1 = Calculation_1(np_Y, float(PRE_LOCATION_XYZ['Y']))
    sq_Z1 = Calculation_1(np_Z, float(PRE_LOCATION_XYZ['Z']))
    # result = DataFrame(data={"偏差X": str(sq_X1),
    #                          "偏差Y": str(sq_Y1),
    #                          "偏差Z": str(sq_Z1),
    #                          "平均偏差": str((sq_X1+sq_Y1+sq_Z1)/3)}, index=[0])
    print("偏差X：{}；偏差Y：{}；偏差Z：{}；平均偏差：{}".format(sq_X1, sq_Y1, sq_Z1, (sq_X1+sq_Y1+sq_Z1)/3))
    result = '{},{},{},{}'.format(sq_X1, sq_Y1, sq_Z1, (sq_X1+sq_Y1+sq_Z1)/3)
    return result

def BLH2precise(address):
    df = openfile(address)
    df_B = df['B']
    df_L = df['L']
    df_H = df['H']
    print(df_B)

if __name__ == '__main__':
    print(XYZ2precise('1225/csv_1225千寻1243_1.csv'))
    # BLH2precise('1225/csv_1225千寻1243_1.csv')





