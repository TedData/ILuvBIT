import random
def toss():
    """ Simulate the toss of a coin to obtain a head or tail
    Parameters:
        No input arguments
    Return:
        str: 'head' or 'tail'
    """
    if random.randint(0,1) == 0:
        return 'head'
    else:
        return 'tail'
def move(pos,coin_toss_result):
    """ Return the new position of the pirate given the current position
    and the result of a coin toss
    Parameters:
        pos(int): the position along the plank
        coin_toss_result(str): 'head' or 'tail'
    Return:
        int: the new position along the plank 
    """
    if coin_toss_result == 'head':   # head
        pos=pos+1
    # tail
    elif pos == 0:
        pos=0
    else:
        pos=pos-1
    #print(pos)
    return pos
def trial(size):
    """Run the game and
    return the number of coin tosses for the pirate to fall into the water.
    Parameters:
        size(int): the size of the plank
    Return:
        int: the number of coin tosses before the pirate falls into drink
    """
    pos=0
    count=0
    while pos < size:
        pos=move(pos,toss())
        count +=1
    return count
def getaverage(total_trials,size):
    """Return the average number of coin tosses for a given number of trials
    and plank length
    Parameters:
        total_trials(int): no of trials used to determine average
        size(int): size of the plank
    Return:
        float: average number of coin tosses 
    """
    num_trials = 0
    total_count = 0
    while num_trials < total_trials:
        total_count = total_count + trial(size)
        num_trials +=1
    return total_count/total_trials
