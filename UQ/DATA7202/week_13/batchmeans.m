%batchmeans.m
M = 10000; % # of samples
K = 1000;  % discard
N = 50;    % # of batches
% sample from N(5,9)
ell = randn(M,1)*3 + 5;

T = floor((M-K)/N);
ell = ell(K+1:length(ell));
batch_ell = zeros(N,1);

for i=1:N
   startid =T*(i-1)+1; 
   endid = startid + T-1; 
   tmp = ell(startid:endid); 
   batch_ell(i) = mean(tmp);
end

mu = mean(batch_ell);
S = std(batch_ell);
CI = [mu-1.96*S/sqrt(N),mu+1.96*S/sqrt(N)];
fprintf("batch means 0.95 CI for mu is (%d, %d)\n",CI(1),CI(2));