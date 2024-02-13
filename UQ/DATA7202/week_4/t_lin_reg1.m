% t_lin_reg1.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% generate custom dataset
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n = 500;
sigma_sqr = 0.2;
v = 5;

beta_original = [1,1.5,-3,2]';
X = [ones(n,1) -1 + 2*rand(n,3)];
y = X*beta_original + trnd(v,n,1)*sigma_sqr^0.5;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% prior for sigma
alpha0 = 3;
beta0 = 2;

% prior for betta
mu0 = zeros(4,1);
sigma0_inv = eye(4)/100;

N = 10000;
burnin = 5000;
%  array to store \beta and sigma squared
ell = zeros(N,5);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
beta = (X'*X)\(X'*y);
sigma_sq = var(X*beta - y);

for r=1:N+burnin
    %  sample lambda from inverse gamma
    igparams = ((X*beta - y)).^2/sigma_sq;
    lambda = 1./gamrnd(((v+1)/2),1./(0.5*(v+igparams))); 
    
    %  sample beta from multi-variate normal
    LAMBDA = diag(lambda.^-1);
    sigLAMBDA = LAMBDA/sigma_sq;
    SIG = (X'*sigLAMBDA*X + sigma0_inv)^-1;
    mu = SIG*(X'*sigLAMBDA*y + sigma0_inv*mu0 );
    beta = mvnrnd(mu,SIG)';
    
    % sample sigma
    sigma_sq = 1./gamrnd(alpha0 + n/2, 1/(beta0 + 0.5*(y-X*beta)'* ...
        LAMBDA*(y-X*beta))); 
    
    if(r>=burnin+1)
        ell(r-burnin,1:4) = beta;
        ell(r-burnin,5) = sigma_sq;
    end        
end

disp("original paraneters")
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
fprintf("beta = [%d,%d,%d,%d], sigma = %d \n",beta_original,sigma_sqr)
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

averages = mean(ell,1);
disp("estimated parameters")
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
fprintf("beta_hat = [%d,%d,%d,%d], sigma_sqr_hat = %d \n",averages(1:4),averages(5))
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


disp("credible intervals")
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
ci_1 = quantile(ell,0.05/2,1);
ci_2 = quantile(ell,1-0.05/2,1);

for i=1:5
    fprintf("(%d,%d)\n",ci_1(i),ci_2(i));
end

