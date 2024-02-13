%empiricalcdf.m
N = 1000;
mu = 10;
X = exprnd(mu,N,1);
x = linspace(0,max(X),100);
y = expcdf(x,mu);
plot(x,y);
hold on
ecdf(X);
legend('Theoretical CDF','Empirical CDF','Location','best')
hold off