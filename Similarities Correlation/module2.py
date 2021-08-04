from scipy.stats import pearsonr
from math import sqrt


def squared(x):
    '''
    A function that takes in a list of integers and squares them one by one.
    
    Parameter:
    x - List of integers.
    '''
    
#     return the square of the values passed into the function 
    return sqrt(sum([a*a for a in x]))


def euclidean_similarity(dictionary, id1, id2):
    '''
    A function to calculate the euclidean distance between two variables.
    
    Parameters:
    dictionary - a dictionary object that stores the parameters (either a single data or list of data) to be used
    in calculating the euclidean similarity between 2 data points.
    id1 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id2.
    id2 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id1.
    '''
    
    #     get the features associated with the id to be used for calculating the similarity
    first = dictionary[id1]
    second = dictionary[id2]
    
    #     remove string values found in the features
    x = [x for x in first if not isinstance(x, str)]
    y = [x for x in second if not isinstance(x, str)]
    
    #     calculate and return the euclidean similarity as shown in the mathematical notation
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
    
def cosine_similarity(dictionary, id1, id2):
    '''
    A function to calculate the cosine distance between two variables.
    
    Parameters:
    dictionary - a dictionary object that stores the parameters (either a single data or list of data) to be used
    in calculating the cosine similarity between 2 data points.
    id1 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id2.
    id2 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id1.
    '''
    
    #     get the features associated with the id to be used for calculating the similarity
    first = dictionary[id1]
    second = dictionary[id2]
    
    #     remove string values found in the features
    x = [x for x in first if not isinstance(x, str)]
    y = [x for x in second if not isinstance(x, str)]
    
    #     calculate and return the cosine similarity as shown in the mathematical notation
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = squared(x)*squared(y)
    return (numerator/float(denominator))


def pearson_similarity(dictionary, id1, id2):
    '''
    A function to calculate the pearson correlation between two variables.
    
    Parameters:
    dictionary - a dictionary object that stores the parameters (either a single data or list of data) to be used
    in calculating the pearson similarity between 2 data points.
    id1 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id2.
    id2 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id1.
    '''
    
    #     get the features associated with the id to be used for calculating the similarity
    first = dictionary[id1]
    second = dictionary[id2]
    
    #     remove string values found in the features
    x = [x for x in first if not isinstance(x, str)]
    y = [x for x in second if not isinstance(x, str)]
    
    #   return the pearson similarity as shown in the mathematical notation using a predefined class
    return pearsonr(x,y)[0]
  
    
def jaccard_similarity(dictionary, id1, id2):
    '''
    A function to calculate the jaccard distance between two variables.
    
    Parameters:
    dictionary - a dictionary object that stores the parameters (either a single data or list of data) to be used
    in calculating the jaccard similarity between 2 data points.
    id1 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id2.
    id2 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id1.
    '''
    
    #     get the features associated with the id to be used for calculating the similarity
    first = dictionary[id1]
    second = dictionary[id2]
    
    #     remove string values found in the features
    x = [x for x in first if not isinstance(x, str)]
    y = [x for x in second if not isinstance(x, str)]
    
    #     calculate and return the jaccard similarity as shown in the mathematical notation
    numerator = len(set.intersection(*[set(x), set(y)]))
    denominator = len(set.union(*[set(x), set(y)]))
    return numerator/float(denominator)


def manhattan_similarity(dictionary, id1, id2):
    '''
    A function to calculate the manhattan distance between two variables.
    
    Parameters:
    dictionary - a dictionary object that stores the parameters (either a single data or list of data) to be used
    in calculating the manhattan similarity between 2 data points.
    id1 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id2.
    id2 -  A key to a specific data in the dictionary (either a single data or list of data) whose values are to be compared against id1.
    '''
    
    #     get the features associated with the id to be used for calculating the similarity
    first = dictionary[id1]
    second = dictionary[id2]
    
    #     remove string values found in the features
    x = [x for x in first if not isinstance(x, str)]
    y = [x for x in second if not isinstance(x, str)]
    
    #     calculate and return the manhattan similarity as shown in the mathematical notation
    return sum(abs(a-b) for a,b in zip(x,y))


# data1 = music_features(specific_columns)
# data2 = artist_music(specific_columns)

# pearson_similarity(data1, '6KbQ3uYMLKb5jDxLF7wYDD', '6N6tiFZ9vLTSOIxkj8qKrd')


# pearson_similarity(data2, 400, 23104)
# cosine_similarity(data2, 400, 23104)