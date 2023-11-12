import json
from prettytable import PrettyTable
import os.path

def saveCache(cache) -> None:
    with open('cache.json', 'w') as file:
        file.write(json.dumps(cache))
        
def getChange(newFollowers):
    if not os.path.isfile('cache.json'):
        return list(newFollowers)
    
    file = open('cache.json', 'r')
    cache = json.loads(file.read())
    oldFollowers = cache['followers'].split(', ')
    
    old = set(oldFollowers)
    new = set(newFollowers)
    
    diff_followers = list(new.symmetric_difference(old))
    
    return diff_followers

def show(newFollowers, data) -> None:
    if len(data) == 0:
        print("Your recent follower count hasn't changed")
        return
    
    table = PrettyTable(['User', 'URL'])
    
    for user in data:
        table.add_row([user, f'https://github.com/{user}'])
    
    print(
        f'Current followers: {len(newFollowers)}\n' +
        'The person who unfollowed/followed you recently:'
    )
    print(table)