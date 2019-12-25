function tau = External_coincidence_accuracy(filepath, N,x0,y0,z0,B0,L0, tmpH)
% input:
% filepath : 读入excel文件的路径
% N : 数据条数
% x0,y0,z0 : 精确ECEF坐标
% B0, L0 : 精确大地坐标（经纬度）

% 读取BLH坐标，B、L、H
[B,L,H] = readcsv_BLH( filepath, N);

% 将BLH坐标转换为ECEF坐标
[X,Y,Z] = blh2xyz(B,L,H);
% 算出ECEF坐标系下的误差
deltaX = X - x0;
deltaY = Y - y0;
deltaZ = Z - z0;
% 将误差转换到ENU坐标系下
[deltaE,deltaN,deltaU] = xyz2enu(deltaX,deltaY,deltaZ,B0,L0);
% 计算外符合精度
tau = sqrt( sum( deltaN.*deltaN + deltaE.*deltaE )/ N );
