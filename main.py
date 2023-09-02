from src.getfollowers import getFollowers
from src.utils import saveCache, getChange, show

username = input('Please input your username: ')

followers = getFollowers(username=username)
if len(followers) > 0:
    change = getChange(newFollowers=followers)
    show(newFollowers=followers, data=change)
    saveCache({
        'followers': ', '.join(followers)
    })
else:
    print('Empty followers')