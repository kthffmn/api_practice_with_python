import time
import requests

FRIENDS_URL = 'https://graph.facebook.com/{}/friends'
TOKEN = 'CAACEdEose0cBAEJTNfrt1yniNZBcu9sU5uRQZA3ZACTwW1TRrHbA11gNteZBmDq30udaokw42eUOvisRZCcahk0idKFCgHNFZAHzBYmZBD99FFDdewZC7omlEHi6FzHuPlPOjfPonBe8wLwHgFMSG7wZCpxdvLq88WghpJeyyozBB7A5ZCTOh82IZAiI9VOQOCxFvrZAmFUlYZAaUAgZDZD'

url = FRIENDS_URL.format('katie.a.hoffman')
data = requests.get(url, params={'access_token': TOKEN}).json()

# getting length of data
# print(len(data['data']))

# url_two = data['paging']['next']
# data_two = requests.get(url_two).json()
# print(len(data_two['data']))

# get friend with lowest id
# print(data['data'][0]['name'])

# sort and find friends with lowest id numbers
# my_friends = data['data']
# def get_id(user):
#   return int(user['id'])
# my_friends.sort(key=get_id)
# print('Your friends with the oldest FB accounts are:')
# for i, friend in enumerate(my_friends[0:10]):
#   print('{}. {}'.format(i+1,friend['name']))

# get harold's id
# harolds = [x for x in data['data'] if x['name'] == 'Harold Cooper']
# print(harolds)

# get the name of the friend with the most mutual friends
my_friends = data['data']
my_friend_ids = {f['id'] for f in my_friends}
friend_id_and_overlapping_friends = []
for my_friend in my_friends:
  print(my_friend)
  time.sleep(0.5)
  friend_url = FRIENDS_URL.format(my_friend['id'])
  print friend_url
  friend_data = requests.get(friend_url, params={'access_token': TOKEN}).json()
  print friend_data
  if 'data' in friend_data:
    their_friends = friend_data['data']
    their_friend_ids = {f['id'] for f in their_friends}
    counter = len(my_friend_ids & their_friend_ids)
    # counter = 0
    # for their_friend in their_friends:
    #   for f in my_friends:
    #     if their_friend['id'] == f['id']:
    #       counter += 1
    friend_id_and_overlapping_friends.append((counter, my_friend['id']))

print(friend_id_and_overlapping_friends)
f_w_most_mutual = max(friend_id_and_overlapping_friends)
yay = [x for x in data['data'] if x['id'] == f_w_most_mutual[1]]
print(yay)

