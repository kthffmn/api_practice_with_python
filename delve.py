import twitter
import requests
import time

CONSUMER_KEY = 'L6WB7nEiKupG4i6yjfHhCw'
CONSUMER_SECRET = '3Yq1Mrm295ZiSmyxalui7ORhXhdW14UIRwPrhdJ570'
ACCESS_TOKEN = '394988283-HtD6jPUfvV46a5VQtUdVkTb4yOfA9l6L5YJzYsLm'
ACCESS_TOKEN_SECRET = 'a7CC8M5bWy2OldkmhnDhtqf9cm2sFC5zlBzxYW8INCLV4'

DELVE_URL = http://delvenews.com/api/matador/?format=json

def retrieve_tweets(handle, start, end):
  api = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token_key=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET)
  tweets = api.GetUserTimeline(screen_name=handle, count=100)
  filtered_tweets = []
  for tweet in tweets:
    filtered_tweets.appened(filter_tweets(tweet, start, end))
  return filtered_tweets

def filter_tweets(tweet, start, end):
  date = tweet.created_at
  if date >= start and date <= end:             # date stuff unfinished
    return tweet
  else:
    return None

def get_domain(url):
  domain = url_parse(url).domain                # unclear
  get_redirect(url)

def get_redirect(url):
  header = request.get(header)(url)             # unclear
  if status == 301 or status == 302:
    return location
  else:
    return url

def main:
  delve_json = request.get(url).json
  start = delve_json['begin_date']              # "2014-02-20"
  end = delve_json['end_date']                  # "2014-03-05"
  match_num = delve_json['match_criteria']

  handle_dict = {}
  for handle in delve_json['twitter_handles']:
    tweets = get_tweets(handle, start, end)
    domain_dict = {}
    for tweet in tweets:
      urls = re.findall(regex, tweet)
      for url in urls:
        domain = get_domain(url)
        if domain not in domain_dict:
          domain_dict[domain] = 0
        domain_dict[domain] += 1
    handle_dict[handle] = domain_dict
    time.sleep(0.5)
 
  name_list = sorted(handle_dict)
  final_dict = {}
  for i in range(len(name_list)):
    for j in range(i+1, len(name_list)):
      i_name = name_list[i]
      j_name = name_list[j]
      i_domain = handle_dict[i_name]
      j_domain = handle_dict[j_name]
      common_domain_dict = {}
      for domain in i_domain
        if i_domain[domain] >= match_num and j_domain.get(domain, 0) >= match_num:
          common_domain_dict[domain] = True
      if i_name not in final_dict:
        final_dict[i_name] = {}
      final_dict[i_name][j_name] = common_domain_dict

  return common_domain_dict







