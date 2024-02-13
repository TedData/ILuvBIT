%latent_t_dist.m
% generate t-distributioned numbers
rng(12345);
N = 1000;
mu = 8;
sigma = 2;
v = 8;

Z = trnd(8,N,1);
T = Z*sigma + mu;

% latent variable
lambda = 1./gamrnd((v/2),1/(v/2),N,1);
T2 = normrnd(mu,(lambda.^0.5)*sigma);

% histogram(T,100);
% hold on
% histogram(T2,100);

cdfplot(T)
hold on
cdfplot(T2)


