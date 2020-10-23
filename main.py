import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    response = requests.get(f'https://api.github.com/users/{username}/events')
    #print(response)    ->  <Response [200]>
    #need to access the repsonse.content using json
    print(response.json()[0]['created_at'])
    


