import pickle
from crawl import get_title
class HackMDColab():
    def __init__(self, file_name="./data.pickle"):
        # Read pickle file from file
        try:
            with open(file_name, 'rb') as f:
                self.main_dict = pickle.load(f)
        # If file not found
        except FileNotFoundError:
            self.main_dict = {}
            print(FileNotFoundError)
        # If file found but nothing in it
        except EOFError:
            self.main_dict = {}
            print(EOFError)
    def __del__(self):
        with open(file_name, 'wb') as f:
            pickle.dump(file_name, f)
        print("Process Exit.")
    def add(self, url):
        # URL preprocess
        if not check_url_legal(url):
            return "URL illegal."
        if "?" in url:
            url = url.split("?")[0]

        # If URL duplicated?
        if url in main_dict:
            pass

        # Try to get the title of the input URL
        try:
            title = get_title(url)  # TODO There might be some problems
        # TODO Exception handling
        except Exception:
            print(Exception)

        # If key exist but title different
        if url in main_dict:
            change_title(title)

        main_dict[url] = title
    
    # TODO
    def delete(self, string):
        pass
    # TODO
    # Check if:
    #       1. hackmd.io is in URL
    #       2. after hackmd.io/, there is 22 char
    def check_url_legal(self, url):
        if "hackmd.io" in url and len(url.split('?')[0].split('/')[-1]) == 22:
            return True
        return False
    def change_title(new_title):
        main_dict[url] = new_title

    def store(self, data, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(data, f)

class Links():
    def __init__(self, url, title, colaborators):
        ''' url => str
            title => str
            colaborators => list
        '''
        self.url = url
        self.title = title
        self.colaborators = colaborators
    
    def __new__(self, ):
        
    def add_colaborator(self, id):
        colaborators.append(id)
    
    def del_colaborator(self, id):
        if id in colaborators:
            colaborators.remove(id)

class Person():
    def __init__(self, id):
        self.id = id
        self.Links = {]}
    
    def add_link(self, Link):
