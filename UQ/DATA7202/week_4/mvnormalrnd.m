%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% mvnormalrnd.m                                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
function X = mvnormalrnd(mu, Sigma)
    C = chol(Sigma,'lower');
    X = mu +C*randn(length(Sigma),1);
end
