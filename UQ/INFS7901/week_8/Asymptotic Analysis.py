#!/usr/bin/env python
# coding: utf-8

# # Asymptotic analysis
# 
# Asymptotic analysis is analyzing what happens to the run time (or other performance metric) as the input size $n$ goes to infinity. The word comes from “asymptote”, which is where you look at the limiting behavior of a function as something goes to infinity. This gives a solid mathematical way to capture the intuition of emphasizing scalable performance. It also makes the analysis a lot simpler!

# ## Motivating Example -The Fibonacci series
# Asymptotic analysis is often used to compare the performance of different algorithms. Let's compare the runtime of two algorithms that find the nth value of the Fibonacci series. A reminder that the Fibonacci series is the series of numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., where the next number is found by adding up the two numbers before it.
# 

# In[1]:


def Fib1(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return Fib1(n-1) + Fib1(n-2);
    
def Fib2(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


# In[2]:


import timeit
import random
import matplotlib.pyplot as plt
import math
get_ipython().run_line_magic('matplotlib', 'inline')

def visual_runtime_Fib(N):
    current_N= []
    Fib1_runtime=[]
    Fib2_runtime=[]
    for i in range(1, N):
        current_N.append(i)
                        
        #Fib1
        startTime1 = timeit.default_timer()
        Fib1(i)
        stopTime1 = timeit.default_timer()
        Fib1_runtime.append(stopTime1-startTime1)
        
        #Fib2
        startTime2 = timeit.default_timer()
        Fib2(i)
        stopTime2 = timeit.default_timer()
        Fib2_runtime.append(stopTime2-startTime2)
    
        
    plt.plot(current_N, Fib1_runtime, label="Fib1 runtime")
    plt.plot(current_N, Fib2_runtime, label="Fib2 runtime")

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_Fib(30) 


# ## Big O notation
# 
# Big O notation is a notation used when talking about growth rates. It formalizes the notion that two functions "grow at the same rate," or one function "grows faster than the other," and such. 
# 
# ### Meet The Big-O Classes
# In this part we will be comparing functions with differnt Big O complexities

# ### Constant Time $O(1)$
# Algorithms always complete in a fixed time irrespective of the size of the input.

# In[3]:


def const_time_function(n):
    return 

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    for i in range(10,N,10000000000000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
            
        
    plt.plot(current_N, const_time, label="const_time")

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(1000000000000000) 


# ### Logarithmic time -  Divide and Conquer $O(log n)$
# These algorithms never have to look at all the input. They often halve inputs at each stage and thus have inverse the performance of exponentiation

# In[4]:


def logn_time_function(n):
    while n>2:
        n = n/2
    return 


def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    for i in range(10,N,10000000000000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(1000000000000000) 


# ### Linear Time - Blind Search - $O(N)$
# The linear algorithm scales directly proportional to the input. This is commonly the case because we often have to access an item at least once.

# In[5]:


def linear_time_function(n):
    for i in range(n):
        a = 5
    return 

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    linear_time=[]
    for i in range(10,N,10000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
        
        #Linear Time
        startTime = timeit.default_timer()
        linear_time_function(i)
        stopTime = timeit.default_timer()
        linear_time.append(stopTime-startTime)        
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")
    plt.plot(current_N, linear_time, label="linear_time")    

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(1000000) 


# ### log-linear time - Sorting O- $O(N$ $LOG$ $N)$
# Efficient general sorting algorithms work in $O(N$ $LOG$ $N)$ time, and many algorithms that use sorting as a subroutine also have this time complexity. It can be shown that algorithms that need to compare elements cannot sort faster than this.

# In[6]:


def log_linear_time_function(n):
    for i in range(n):
         while n>2:
            n = n/2
    return 

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    linear_time=[]
    log_linear_time=[]
    for i in range(10,N,10000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
        
        #Linear Time
        startTime = timeit.default_timer()
        linear_time_function(i)
        stopTime = timeit.default_timer()
        linear_time.append(stopTime-startTime)        

        #Log-Linear Time
        startTime = timeit.default_timer()
        log_linear_time_function(i)
        stopTime = timeit.default_timer()
        log_linear_time.append(stopTime-startTime)        
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")
    plt.plot(current_N, linear_time, label="linear_time")    
    plt.plot(current_N, log_linear_time, label="log-linear_time")        

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(500000) 


# ### Quadratic Time - $O(N^2)$
# The number of steps taken to accomplish a task is square of n, often in the form of two nested loops each having a linear time run time.

# In[ ]:


def quadratic_time_function(n):
    for i in range(n):
        for j in range(n):
            #do something
            a = i * j
    return 

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    linear_time=[]
    log_linear_time=[]
    quadratic_time=[]

    for i in range(10,N,1000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
        
        #Linear Time
        startTime = timeit.default_timer()
        linear_time_function(i)
        stopTime = timeit.default_timer()
        linear_time.append(stopTime-startTime)        

        #Log-Linear Time
        startTime = timeit.default_timer()
        log_linear_time_function(i)
        stopTime = timeit.default_timer()
        log_linear_time.append(stopTime-startTime)  
        
        #quadratic time
        startTime = timeit.default_timer()
        quadratic_time_function(i)
        stopTime = timeit.default_timer()
        quadratic_time.append(stopTime-startTime)  
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")
    plt.plot(current_N, linear_time, label="linear_time")    
    plt.plot(current_N, log_linear_time, label="log-linear_time")        
    plt.plot(current_N, quadratic_time, label="quadratic_time")        

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(10000) 


# ### Polynomial time - $O(N^k)$
# An algorithm is said to be of polynomial time if its running time is upper bounded by a polynomial expression in the size of the input for the algorithm, for some positive constant $k$.

# In[ ]:


def polynomial_time_function(n):
    for i in range(n):
        for j in range(n):
            for k in range (n):
                #do something
                a = i * j*k
    return 

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    linear_time=[]
    log_linear_time=[]
    quadratic_time=[]
    polynomial_time=[]

    for i in range(10,N,1000):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
        
        #Linear Time
        startTime = timeit.default_timer()
        linear_time_function(i)
        stopTime = timeit.default_timer()
        linear_time.append(stopTime-startTime)        

        #Log-Linear Time
        startTime = timeit.default_timer()
        log_linear_time_function(i)
        stopTime = timeit.default_timer()
        log_linear_time.append(stopTime-startTime)  
        
        #quadratic time
        startTime = timeit.default_timer()
        quadratic_time_function(i)
        stopTime = timeit.default_timer()
        quadratic_time.append(stopTime-startTime)  
        
        #polynomial time
        startTime = timeit.default_timer()
        polynomial_time_function(i)
        stopTime = timeit.default_timer()
        polynomial_time.append(stopTime-startTime) 
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")
    plt.plot(current_N, linear_time, label="linear_time")    
    plt.plot(current_N, log_linear_time, label="quadratic_time")        
    plt.plot(current_N, quadratic_time, label="polynomial_time")        

    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(10000) 


# ### Exponential time - $O(C^N)$
# Exponential algorithms execution time grows much faster than that of polynomial ones and are often interactable.

# In[ ]:


def exponential_time_function(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return Fib1(n-1) + Fib1(n-2);

def visual_runtime_classes(N):
    current_N= []
    const_time =[]
    logn_time=[]
    linear_time=[]
    log_linear_time=[]
    quadratic_time=[]
    polynomial_time=[]
    exponential_time = []

    for i in range(10,N,1):
        current_N.append(i)
                        
        #Constant Time
        startTime = timeit.default_timer()
        const_time_function(i)
        stopTime = timeit.default_timer()
        const_time.append(stopTime-startTime)
        
        #Log n Time
        startTime = timeit.default_timer()
        logn_time_function(i)
        stopTime = timeit.default_timer()
        logn_time.append(stopTime-startTime)
        
        #Linear Time
        startTime = timeit.default_timer()
        linear_time_function(i)
        stopTime = timeit.default_timer()
        linear_time.append(stopTime-startTime)        

        #Log-Linear Time
        startTime = timeit.default_timer()
        log_linear_time_function(i)
        stopTime = timeit.default_timer()
        log_linear_time.append(stopTime-startTime)  
        
        #quadratic time
        startTime = timeit.default_timer()
        quadratic_time_function(i)
        stopTime = timeit.default_timer()
        quadratic_time.append(stopTime-startTime)  
        
        #polynomial time
        startTime = timeit.default_timer()
        polynomial_time_function(i)
        stopTime = timeit.default_timer()
        polynomial_time.append(stopTime-startTime) 
        
        #exponential time
        startTime = timeit.default_timer()
        exponential_time_function(i)
        stopTime = timeit.default_timer()
        exponential_time.append(stopTime-startTime) 
    
        
    plt.plot(current_N, const_time, label="const_time")
    plt.plot(current_N, logn_time, label="logn_time")
    plt.plot(current_N, linear_time, label="linear_time")    
    plt.plot(current_N, log_linear_time, label="quadratic_time")        
    plt.plot(current_N, quadratic_time, label="polynomial_time")        
    plt.plot(current_N, quadratic_time, label="exponential_time")        


    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    legend = plt.legend(loc='upper center', bbox_to_anchor=(1, 0.5))
    plt.show()

visual_runtime_classes(40) 


# In[ ]:




