%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% disaster_model.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% disaster model

disastersarray = [4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6, ...
         3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5, ...
         2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0, ...
         1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1, ...
         0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2, ...
         3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4, ...
         0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1];
                     
n = length(disastersarray);

%plot(disastersarray,'*')
%return

N = 100000;
burnin = 10000;

% init chain
s  = 2;
r1 = 4;
r2 = 4;

ac_rate = 0;
ell = zeros(N,3);
%MCMC
for i=1:N+burnin
    % sample 
    s_ = ceil(rand*n);
    r1_ = rand*4;
    r2_ = rand*2;
    accept = min(1, ...
      exp(target(s_,r1_,r2_,disastersarray)-target(s,r1,r2,disastersarray)));
    if(rand<=accept)
        s = s_;
        r1 = r1_;
        r2 = r2_;
        ac_rate = ac_rate +1;
    end
    if(i>burnin)
       ell(i- burnin,:) = [s,r1,r2];
    end
end

%fprintf("acceptence rate = %d\n",ac_rate/(N+burnin));
fprintf("s =  %d, 5 percent  CI = (%d,%d) \n",mean(ell(:,1)), ...
                    quantile(ell(:,1),[0.025,0.975]));

fprintf("r_1 =  %d, 5 percent  CI = (%d,%d) \n",mean(ell(:,2)), ...
                    quantile(ell(:,2),[0.025,0.975]));

fprintf("r_2 =  %d, 5 percent  CI = (%d,%d) \n",mean(ell(:,3)), ...
                    quantile(ell(:,3),[0.025,0.975]));


figure(1)
histogram(ell(:,1))
figure(2)
histogram(ell(:,2))
figure(3)
histogram(ell(:,3))


function logres = target(s,r1,r2,disastersarray)
    [d1,d2] = DataPartition(s,disastersarray);
    s1 = length(d1);
    s2 = length(d2); 
    logres = sum(d1)*log(r1) + sum(d2)*log(r2) - (s1+1)*r1 - (s2+1)*r2; 
end

function [d1,d2] = DataPartition(s,disastersarray)
    n = length(disastersarray);
    if(s==1)
       d1 = [];
       d2 = disastersarray;
    elseif(s==n)
        d1 = disastersarray;
        d2 = [];
    else
        d1 = disastersarray(1:s);
        d2 = disastersarray(s:length(disastersarray));
    end
end