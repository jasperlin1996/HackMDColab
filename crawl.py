from requests_html import HTMLSession

def get_title(url):
    sess = HTMLSession()
    req = sess.get(url)
    return req.html.text.title().split('\n')[0]


if __name__ == '__main__':
    url = 'https://hackmd.io/RdTVR5lMRZWHONRoMOGvzw?view#Deep-NN'
    print(get_title(url))