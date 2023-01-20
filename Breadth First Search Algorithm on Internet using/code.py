import queue
import requests
from bs4 import BeautifulSoup

visited = {}
q = queue.Queue()

token = 0
start_url = input("Enter the starting URL: ")
q.put(start_url)

while not q.empty():
    current_url = q.get()
    print(token, current_url)
    visited[current_url] = token
    token += 1

    try:
        res = requests.get(current_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            if link.get('href') and link.get('href') not in visited:
                q.put(link.get('href'))

    except:
        pass
