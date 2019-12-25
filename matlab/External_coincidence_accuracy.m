function tau = External_coincidence_accuracy(filepath, N,x0,y0,z0,B0,L0, tmpH)
% input:
% filepath : ����excel�ļ���·��
% N : ��������
% x0,y0,z0 : ��ȷECEF����
% B0, L0 : ��ȷ������꣨��γ�ȣ�

% ��ȡBLH���꣬B��L��H
[B,L,H] = readcsv_BLH( filepath, N);

% ��BLH����ת��ΪECEF����
[X,Y,Z] = blh2xyz(B,L,H);
% ���ECEF����ϵ�µ����
deltaX = X - x0;
deltaY = Y - y0;
deltaZ = Z - z0;
% �����ת����ENU����ϵ��
[deltaE,deltaN,deltaU] = xyz2enu(deltaX,deltaY,deltaZ,B0,L0);
% ��������Ͼ���
tau = sqrt( sum( deltaN.*deltaN + deltaE.*deltaE )/ N );
