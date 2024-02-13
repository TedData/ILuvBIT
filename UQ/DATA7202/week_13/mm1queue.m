%mm1queue.m
clc
clear
T = 10000;  % simulation time
 
lambda = 2; % arrival 2 customers per unit time on average
mu = 3;     % service 3 customer per unit time  on average
 
% get analytical results
rho = lambda/mu;
L = rho/(1-rho);
L_q = rho^2/(1-rho);
W_q = rho^2/(lambda*(1-rho));
W = W_q + 1/mu;
fprintf('ANALYTICAL RESULTS \n');
fprintf('______________________________________________ \n');
fprintf('the average proportion of time for which the server is utilized is %d \n',round(rho,3));
fprintf('the average number of customers in the queue is %d \n',L_q);
fprintf('the average number of customers in the system is %d \n',L);
fprintf('the average wait time the queue is %d \n',W_q);
fprintf('the average wait time the system is %d \n',W);
fprintf('______________________________________________ \n');


% physical queue
waiting_queue = CQueue;
% main simulation priority queue
event_q = PriorityQueue(false);

t = 0;

% create first arrival
t = t + exprnd(1/lambda);
client = CreatClientObject();
client.t_arrive = t;
client.event_type = 'A';
event_q.insert(t, client);

% create first state
state_obj = CreatStateObject();
state_obj.time   = 0;
state_obj.W      = 0;
state_obj.X_busy = 0;

% for output analysis
client_arr = [];
statespace_arr = [state_obj];

serverBusyFlag = 0;

% main DES procedure
while(t<T)        

    [t, client] = event_q.pop;
    % Determine event type
    if(client.event_type == 'A')     % handle arrival 
          % create next arrival
          nextClient =  CreatClientObject();
          nextClient.event_type = 'A';
          nextClient.t_arrive = t + exprnd(1/lambda);
          event_q.insert( nextClient.t_arrive,nextClient);
          
          % handle current arrival        
          if(0==serverBusyFlag)
               client.t_serv1start = t;
               client.t_serv1end = t + exprnd(1/mu);
               client.event_type = 'D';
               event_q.insert(client.t_serv1end,client);
               serverBusyFlag = 1;
          else
               % push to physical queue
               waiting_queue.push(client);
          end
          
          state_obj = CreatStateObject();
          state_obj.time   = t;
          state_obj.W      = waiting_queue.size();
          state_obj.X_busy = serverBusyFlag;
          
          statespace_arr = [statespace_arr; state_obj]; 
          
    elseif(client.event_type == 'D')  % handle dearture         
             client_arr = [client_arr; client];
             
             if(waiting_queue.isempty())
                 serverBusyFlag = 0;
             else
                 next_cust = waiting_queue.pop; 
                 next_cust.t_serv1start = t;
                 next_cust.t_serv1end = t + exprnd(1/mu);
                 next_cust.event_type = 'D';
                 event_q.insert(next_cust.t_serv1end,next_cust); 
             end    
        
          state_obj = CreatStateObject();
          state_obj.time   = t;
          state_obj.W      = waiting_queue.size();
          state_obj.X_busy = serverBusyFlag;
          
          statespace_arr = [statespace_arr; state_obj]; 
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% statistical analysis in steady state
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
N = 50; % batches
burnin_percentage = 0.5;

state_mat = cell2mat(struct2cell(statespace_arr))';
client_mat = [client_arr.t_arrive; client_arr.t_serv1start; ...
              client_arr.t_serv1end]';

% calculate the step length of the step function
delta_time =  state_mat(2:end,1) - state_mat(1:end-1,1);
state_mat = state_mat(1:end-1,:);

% steady-state estimation   
fprintf('STEADY STATE SIMULATION RESULTS \n');


% step function estimation

% calculate the step length of the step function
delta_time =  state_mat(2:end,1) - state_mat(1:end-1,1);
state_mat = state_mat(1:end-1,:);

[hatell, ci1, ci2] =  BatchMeanForStep(burnin_percentage, N, state_mat(:,3), delta_time);
fprintf('average proportion of time for which the server is utilized %d CI=(%d, %d)\n'...
            ,hatell, ci1, ci2);

[hatell, ci1, ci2] =  BatchMeanForStep(burnin_percentage, N, state_mat(:,2), delta_time);
fprintf('average number of customers in the queue %d CI=(%d, %d)\n'...
            ,hatell, ci1, ci2);        

[hatell, ci1, ci2] =  BatchMeanForStep(burnin_percentage, N,  state_mat(:,2)+state_mat(:,3), delta_time);
fprintf('average number of customers in the system %d CI=(%d, %d)\n'...
            ,hatell, ci1, ci2);        
 

ell = client_mat(:,2)-client_mat(:,1);
[hatell, ci1, ci2] =  BatchMean(burnin_percentage,N,ell);
fprintf('average wait time in the queue %d CI=(%d, %d) \n', hatell, ci1, ci2);

ell = client_mat(:,3)-client_mat(:,1);
[hatell, ci1, ci2] =  BatchMean(burnin_percentage,N,ell);
fprintf('average wait time in the system %d CI=(%d, %d) \n', hatell, ci1, ci2);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% output analysis
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
function [mu, CI_l, CI_r] = BatchMeanForStep(burnin_percentage,N,ell, step)
    K = floor(burnin_percentage*length(ell));
    ell_steady = ell(K+1:end);
    step_steady = step(K+1:end);
    batch_sz = floor(length(ell_steady)/N);
    ell_batch_mean = zeros(N,1);
    for i=1:N
        ell_tmp = ell_steady((i-1)*batch_sz + 1:i*batch_sz);
        step_tmp = step_steady((i-1)*batch_sz + 1:i*batch_sz);
        ell_batch_mean(i) = GetStepFunctionIntegral(ell_tmp, step_tmp)/sum(step_tmp);
    end
    [mu, CI_l, CI_r] = GetCI(ell_batch_mean)      ;
end

function [mu, CI_l, CI_r] = BatchMean(burnin_percentage,N,ell)
    K = floor(burnin_percentage*length(ell));
    ell_steady = ell(K+1:end);
    batch_sz = floor(length(ell_steady)/N);
    ell_batch_mean = zeros(N,1);
    for i=1:N
        ell_tmp = ell_steady((i-1)*batch_sz + 1:i*batch_sz);
        ell_batch_mean(i) = mean(ell_tmp);
    end
    [mu, CI_l, CI_r] = GetCI(ell_batch_mean)      ;
end

function res = GetStepFunctionIntegral(values, steps)
    res = sum(values.*steps);
end

function [mu, CI_l, CI_r] = GetCI(ell)
    n = length(ell);
    mu = mean(ell);
    S = std(ell);
    CI = [mu-1.96*S/sqrt(n),mu+1.96*S/sqrt(n)];
    CI_l = CI(1);
    CI_r = CI(2);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% data storing object
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function state_obj = CreatStateObject()
    state_obj.time   = -1;
    state_obj.W      = -1;
    state_obj.X_busy = -1;
end

function client_obj = CreatClientObject()
     client_obj.event_type = '';
     client_obj.t_arrive = -1;
     client_obj.t_serv1start = -1;
     client_obj.t_serv1end = -1;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%