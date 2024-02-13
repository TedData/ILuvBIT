%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NormalModelMCMC.m                                                      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
rng(12345);
% generae dataset
n = 100;
mu = 3;
sig2 = 0.15;
y = randn(n,1)*sig2^0.5 + mu;

% set prior
mu0 = -1; sig20 = 100;     % normal
alpha0 = 3; beta0 = 0.5;   % inverse gamma

% simulation parameters
N = 10000;
burnin = 1000;

% array for theta recording
ell = zeros(N,2);

% initial values
mu = 0; sigma2 = 10;

% Main MCMC loop
for i = 1:N + burnin
    % sample mu
    sigma_post = (1/sig20 + n/sigma2)^-1;
    mu_post = (n*mean(y)/sigma2 + mu0/sig20)*sigma_post;
    mu = mvnormalrnd(mu_post,sigma_post);
    
    % sample sigmna2
    alpha = 0.5*n + alpha0;
    betta =  (beta0 + 0.5*sum((y-mu).^2)) ;
    sigma2 = igrnd(alpha,betta);
    
    if(i>burnin)
        ell(i-burnin,:) = [mu,sigma2];        
    end
end
fprintf("posterior (mu,sigma^2) is (%d, %d) \n",mean(ell));

ci_1 = quantile(ell,0.05/2,1);
ci_2 = quantile(ell,1-0.05/2,1);

fprintf("CI for mu is (%d, %d) \n",ci_1(1),ci_2(1));
fprintf("CI for sigma^2 is (%d, %d) \n",ci_1(2),ci_2(2));


