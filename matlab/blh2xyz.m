function [X,Y,Z] = blh2xyz(B,L,H)
a = 6378137.0; % 地球长轴
%f = 1/298.257223563; % 扁率 = (a-b)/a
f = 1/298.257222101;
b = a - a*f; %地球短轴

B = deg2rad(B);
L = deg2rad(L);

e2 = (a^2 - b^2)/(a^2);
W = sqrt( 1 - e2 * ( sin(B).^2 ));
N = a./W;
X = (N + H).*cos(B).*cos(L);
Y = (N + H).*cos(B).*sin(L);
Z = (N*(1-e2) + H).*sin(B);