import twitter
import time

# Twitter OAuth Keys and Secrets

# Mine:
consumer_key = 'L6WB7nEiKupG4i6yjfHhCw'
consumer_secret = '3Yq1Mrm295ZiSmyxalui7ORhXhdW14UIRwPrhdJ570'
access_token = '394988283-HtD6jPUfvV46a5VQtUdVkTb4yOfA9l6L5YJzYsLm'
access_token_secret = 'a7CC8M5bWy2OldkmhnDhtqf9cm2sFC5zlBzxYW8INCLV4'

# Harold's:
# consumer_key = 'Y3S0XTEzicvGeXfIylnWg'
# consumer_secret = 'AgDaE7lTnSYyNrY2N73U4Cg2sR6kYGzJZY3yXyzQK8'
# access_token = '22175229-sgeyVQnTOdnJ5351CK0WFCytvCOMFO7ShvV2RMAOS'
# access_token_secret ='frFIe2FRW4cttuo6LtYPKkchyjFoWpqDIYLgqrz9EbNxQ'

# from https://github.com/requests/requests-oauthlib
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# see if it worked:
# print api.VerifyCredentials()

# print Mary Charlene's status updates
user = 'IamEnidColeslaw'
statuses = api.GetUserTimeline(screen_name=user)
print(len(statuses))
for status in statuses:
  print('{}: {}'.format(status.text, status.created_at))

# print [s.text for s in statuses]

# print the number of my friends
# print(len(users))

# print the top ten people that the people that I follow follow without Harold's tweaks :) 
# user = 'kt_hffmn'
# my_users = api.GetFriends(screen_name=user)
# all_user_dict = {}
# for my_user in my_users:
#   time.sleep(0.5)
#   their_users = api.GetFriends(screen_name=my_user.screen_name)
#   for their_user in their_users:
#     name = their_user.screen_name
#     if name in all_user_dict:
#       all_user_dict[name] += 1
#     else:
#       all_user_dict[name] = 1
# all_user_list = []
# for screen_name in all_user_dict:
#   all_user_list.append((all_user_dict[screen_name], screen_name))
# all_users_list.sort(reverse=True)
# for user in all_user_list[0:10]:
#   print(user[1])


# # HAROLD'S TWEAKS!!!! :))) triple chin
# user = 'kt_hffmn'
# my_users = api.GetFriends(screen_name=user)

# all_user_dict = {}
# for my_user in my_users:
#   time.sleep(0.5)
#   their_users = api.GetFriends(screen_name=my_user.screen_name)
#   for their_user in their_users:
#     name = their_user.screen_name
#     if name not in all_user_dict:
#       all_user_dict[name] = 0
#     all_user_dict[name] += 1

# all_user_list = []
# for screen_name,count in all_user_dict.items():
#   all_user_list.append((count, screen_name))
# all_users_list.sort(reverse=True)

# for user in all_user_list[0:10]:
#   print(user[1])

# # HAROLD'S MOOOOORE TWEAKS!!!! :)))} triple chin + beard
# user = 'kt_hffmn'
# my_users = api.GetFriends(screen_name=user)

# all_user_dict = {}
# for my_user in my_users:
#   time.sleep(0.5)
#   their_users = api.GetFriends(screen_name=my_user.screen_name)
#   for their_user in their_users:
#     name = their_user.screen_name
#     if name not in all_user_dict:
#       all_user_dict[name] = 0
#     all_user_dict[name] += 1

# all_user_list = [(count, screen_name) for screen_name,count in all_user_dict.items()]
# all_users_list.sort(reverse=True)

# for count, screen_name in all_user_list[0:10]:
#   print('{}: {}'.format(screen_name, count))
