from pandas import read_csv
from numpy import array, square, average, sqrt, dot, mat
from pandas import DataFrame
from BLH2ENU import blh2enu
from BLH2XYZ import change
from BLH2XYZ import blh2xyz



PRE_LOCATION_BLH = {
    'B': '31:14:40.84328192734967',
    'L': '121:35:32.857075737083406',
    'H': '35.00690099 '
}
PRE_LOCATION_XYZ = {
    'X': '-2859303.11731802',
    'Y': '4649101.22957921',
    'Z': '3289135.34910245'
}

def openfile(address):
    coding_list = ['utf-8', "gbk", 'ANSI']
    for code in coding_list:
        try:
            df = read_csv(address, encoding=code)
            break
        except:
            continue
    return df

def Calculation_1(lis, location):
    '''
    :param lis: 输入列表
    :param location: 输入绝对位置
    :return: 返回列表与位置的差值平方，再取平均数，再开方
    '''
    res_lis = array([square(li-location) for li in lis])
    average_lis = average(res_lis)
    sqrt_lis = sqrt(average_lis)
    return sqrt_lis

def XYZ2precise_xyz(address):
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
    print("‘{}’组————偏差X：{}；偏差Y：{}；偏差Z：{}；平均偏差：{}".format(address, sq_X1, sq_Y1, sq_Z1, (sq_X1+sq_Y1+sq_Z1)/3))
    result = '{},{},{},{}'.format(sq_X1, sq_Y1, sq_Z1, (sq_X1+sq_Y1+sq_Z1)/3)
    return result

def BLH2precise_neu(address):
    df = openfile(address)
    np_B = array(df['B'])
    np_L = array(df['L'])
    np_H = array(df['H'])
    np_x = []
    np_y = []
    np_z = []
    for i in range(len(np_B)):
        xyz = blh2xyz(np_B[i], np_L[i], np_H[i])
        np_x.append(xyz[0])
        np_y.append(xyz[1])
        np_z.append(xyz[2])
    np_x = array(np_x)
    np_y = array(np_y)
    np_z = array(np_z)
    gap_x = array([i - float(PRE_LOCATION_XYZ['X']) for i in np_x])
    gap_y = array([i - float(PRE_LOCATION_XYZ['Y']) for i in np_y])
    gap_z = array([i - float(PRE_LOCATION_XYZ['Z']) for i in np_z])
    tranE = blh2enu(float(change(PRE_LOCATION_BLH['B'], 'N')), float(change(PRE_LOCATION_BLH['L'], 'E')))
    matrix = []
    for i in range(len(gap_x)):
        ar = mat([[gap_x[i]], [gap_y[i]], [gap_z[i]]])
        # print(ar)
        ma = dot(tranE, ar).T.tolist()[0]
        # print(ma)
        matrix.append(ma)
    matrix = mat(matrix).T.tolist()
    # print(matrix)
    e = array(matrix[0])
    m = array(matrix[1])
    e2 = e * e
    m2 = m * m
    em2 = e2 + m2
    print(sqrt(average(em2)))

    # result_list = []
    # for lis in matrix:
    #     res = Calculation_1(lis, 0)
    #     result_list.append(res)
    # print("‘{}’组————水平误差:{}；各方位结果：{}".format(address, sqrt(square(result_list[0])+square(result_list[1])), result_list))


def method2(address):
    df = openfile(address)
    np_B = array(df['B']).tolist()
    np_L = array(df['L']).tolist()
    # np_H = array(df['H']).tolist()
    B0 = [float(str(c).split(':')[2]) * 30 for c in np_B]
    L0 = [float(str(c).split(':')[2]) * 30 for c in np_L]
    # H0 = [float(str(c).split(':')[2]) * 30 for c in np_H]
    res_b = Calculation_1(B0, float(PRE_LOCATION_BLH['B'].split(':')[2])*30)
    res_l = Calculation_1(L0, float(PRE_LOCATION_BLH['L'].split(':')[2])*30)
    print("‘{}’组————b误差:{}；l误差：{}".format(address, res_b, res_l))


# def gga_method2(address):
#     df = read_csv(address, encoding='ANSI', index_col=[i for i in range(10)])
#
#     print(df)
#     np_B = array(df[2]).tolist()
#     np_L = array(df[4]).tolist()
#     print(np_B)


if __name__ == '__main__':
    method2('csv_010218abc.csv')
    XYZ2precise_xyz('csv_010218abc.csv')

    method2('csv_0102sy__10自.csv')
    XYZ2precise_xyz('csv_0102sy__10自.csv')