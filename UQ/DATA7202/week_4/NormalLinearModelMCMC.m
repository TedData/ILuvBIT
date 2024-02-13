%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NormalLinearModelMCMC.m                                               %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
rng(12345);
% artificial data generation
n = 500;
dim = 2;
X = [ones(n,1)];
for i=1:dim
    X = [X rand(n,1)];
end
beta_real = [3;4;-5];
sigma2_real = 2;
y = X*beta_real + randn(n,1).*sqrt(sigma2_real);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% prior
alpha0 = 3; beta0 = 2;
mu0 = zeros(dim+1,1); 
sigma0_inv = eye(dim+1)/100;

N = 10000;
burnin = 1000;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% initialize the chain
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
beta = X\y;
sig2 = var(y-X*beta);

ell = zeros(N,dim+1+1);

for i=1:N+burnin
    % sample sig2 from inverse gamma
    alpha1 = alpha0 + n/2;
    tmp = y-X*beta;
    beta1 = beta0 + 0.5*tmp'*tmp;
    sig2 =  igrnd(alpha1,beta1);
    
    % sample beta from multi var norm
    Sigma1 = inv(sig2^-1 * X'*X + sigma0_inv);
    mu1 = Sigma1 * (sig2^-1 * (X'*y)  + sigma0_inv*mu0);
    
    beta = mvnormalrnd(mu1,Sigma1);
        
    if(i>burnin)
        ell(i-burnin,:) = [beta',sig2];
    end
end

fprintf("beta_hat, sigma_hat, %d,%d,%d, | %d \n",  mean(ell));
% credible intervalse
for i=1:size(ell,2)
    arr = ell(:,i);
    fprintf("(%d,%d)\n", quantile(arr,0.05/2), quantile(arr,1-(0.05/2)));
end

