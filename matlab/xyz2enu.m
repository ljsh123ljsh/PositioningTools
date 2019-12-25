function [E,N,U] = xyz2enu(X,Y,Z,B0,L0)
Npoints = length(X);
E = zeros(Npoints,1);
N = zeros(Npoints,1);
U = zeros(Npoints,1);

sinp = sin(B0);  cosp = cos(B0);
sinl = sin(L0);  cosl = cos(L0);
tranE = zeros(3,3);
tranE(1,1:3) = [-sinl, cosl, 0.0];
tranE(2,1:3) = [-sinp*cosl, -sinp*sinl, cosp];
tranE(3,1:3) = [cosp*cosl, cosp*sinl,sinp];
    
for n = 1:Npoints
    tmp = tranE * [X(n); Y(n); Z(n)];
    E(n) = tmp(1);
    N(n) = tmp(2);
    U(n) = tmp(3);
end
    
    