def close_to(p1,p2):
    """ Determines if p1 and p2 are close to each other """
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2)**2 + (y1 - y2)**2 < 1600
