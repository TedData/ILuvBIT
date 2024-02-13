%finitehorizon.m
N = 10000; % # of samples

% sample from N(5,9)
ell = randn(N,1)*3 + 5;

mu = mean(ell);
S = std(ell);
CI = [mu-1.96*S/sqrt(N),mu+1.96*S/sqrt(N)];
fprintf("0.95 CI for mu is (%d, %d)\n",CI(1),CI(2));