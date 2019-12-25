function [B,L,H] = readcsv_BLH( filepath, N)
[num, cellB] = xlsread( filepath,1,['f2:f',num2str(N+1)]);
[num, cellL] = xlsread( filepath,1,['g2:g',num2str(N+1)]);
H = xlsread( filepath,1,['h2:h',num2str(N+1)])+ xlsread( filepath,1,['i2:i',num2str(N+1)]);

B = zeros(N,1);
L = zeros(N,1);
for n = 1:N
    tmp1 = cellB(n);
    tmp2 = regexp(tmp1{1}, ':','split');
    dms_B = [str2double(tmp2{1}), str2double(tmp2{2}), str2double(tmp2{3})];
    B(n) = dms2degrees( dms_B );
    
    tmp1 = cellL(n);
    tmp2 = regexp(tmp1{1}, ':','split');
    dms_L = [str2double(tmp2{1}), str2double(tmp2{2}), str2double(tmp2{3})];
    L(n) = dms2degrees( dms_L ); 
end
    