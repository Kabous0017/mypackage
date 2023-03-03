def top_n (items,n):
    """Return the top n items in an array in descending order.
    
    Arg:
        items(array): list or array like object
        n (int): number of items to return
    
    Return:
        array: top n items in descending order
    
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """

    items.sort()
    topn= items[-n:]
    
    return topn[::-1]