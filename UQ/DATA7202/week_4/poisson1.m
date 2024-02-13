function poisson1
    lambda =1.5;
    T = 15;
    t = 0; n = 0;
    tt = [t];
    
    while t < T
        t = t - log(rand)/lambda;
        tt = [tt,t];
    end
    n = size(tt,2)-1;
    nn = 0:n;
    for i =1:n
        line([tt(i),tt(i+1)],[nn(i),nn(i)],'Linewidth',2);
    end    
end