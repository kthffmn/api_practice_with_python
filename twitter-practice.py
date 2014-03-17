import twitter

# Twitter OAuth Keys and Secrets
consumer_key = 'L6WB7nEiKupG4i6yjfHhCw'
consumer_secret = '3Yq1Mrm295ZiSmyxalui7ORhXhdW14UIRwPrhdJ570'
access_token = '394988283-HtD6jPUfvV46a5VQtUdVkTb4yOfA9l6L5YJzYsLm'
access_token_secret = 'a7CC8M5bWy2OldkmhnDhtqf9cm2sFC5zlBzxYW8INCLV4'

# from https://github.com/requests/requests-oauthlib
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# see if it worked:
# print api.VerifyCredentials()

# print Mary Charlene's status updates
# user = 'IamEnidColeslaw'
# statuses = api.GetUserTimeline(screen_name=user)
# print [s.text for s in statuses]

# print my friends
# user = 'kt_hffmn'
# users = api.GetFriends(screen_name=user)
# print [u.name for u in users]

# print the number of my friends
# print(len(users))