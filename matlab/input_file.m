%%------- input -----------------------------------------------------------
su_filepath = 'C:\Users\LXY\Desktop\20191224waifuhe\csv data\csv_122416__sy.csv';
qx_filepath = 'C:\Users\LXY\Desktop\20191224waifuhe\csv data\csv_122417__qx.csv';

%------------- ¾«È·×ø±ê(CGCS2000) -----------------------------------------
x0 = -2838720.6127;
y0 = 4654331.1310;
z0 = 3299441.7983;
B0 = dms2degrees([31 21 12.898986]);
L0 = dms2degrees([121 22 45.877409]);
H0 = 14.5582;

N = 1516;
su_tau = External_coincidence_accuracy(su_filepath, N,x0,y0,z0,B0,L0);

N = 623;
qx_tau = External_coincidence_accuracy(qx_filepath, N,x0,y0,z0,B0,L0);

