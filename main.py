import pickle
import argparse
from crawl import get_title
from hackmdcolab import HackMDColab

if __name__ == '__main__':
    dict = {'1': 'hi'}
    file_name = 'test.pickle'
    # Read pickle file from file
    try:
        with open(file_name, 'rb') as f:
            dict = pickle.load(f)
    # If file not found
    except FileNotFoundError:
        with open(file_name, 'wb') as f:
            pickle.dump(file_name, f)
    except EOFError:
        print(EOFError)
    #colab = hackmdcolab(dict)

