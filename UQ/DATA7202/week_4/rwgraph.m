function rwgraph
P =   [ 0  1/2  1/2  0  0; ...
         1/3   0  1/3  1/3  0; ...
		 1/4  1/4  0  1/4  1/4; ...
         0  1/2  1/2  0  0; ...
         0   0  1  0  0];
     
    X = 1;
      
    ell = zeros(1,5);
    
    N = 100000;
    
    for i=1:N
        X = MakeStep(X,P);
        ell(X) = ell(X)+1;
    end
    ell = ell./N

    
end

function X = MakeStep(X,P)
    X = min(find(cumsum(P(X,:))> rand));
end