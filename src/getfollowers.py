import requests

def getFollowers(username):
    page = 1
    followers = []
    try:
        while True:
            url = f'https://api.github.com/users/{username}/followers?page={page}&per_page=100'
            response = requests.get(url=url)
            data = response.json()
            if len(data) == 0:
                break
            page += 1
            followers.extend([follower['login'] for follower in data])
    except:
        print('An exception occurred')
    return followers