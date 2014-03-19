import tldextract
import requests
import twitter
import time


DELVE_URL = 'http://delvenews.com/api/matador/?format=json'

def main():
  delve_json = requests.get(DELVE_URL).json()
  start = datetime.strptime(delve_json['begin_date'], '%Y-%m-%d')
  end = datetime.strptime(delve_json['end_date'], '%Y-%m-%d')
  match_num = delve_json['match_criteria']

  handle_dict = {}
  for handle in delve_json['twitter_handles']:
    tweets = get_tweets(handle, start, end)
    domain_dict = {}
    for tweet in tweets:
      urls = re.findall(r'http:\/\/\S*', tweet)
      for url in urls:
        domain = get_domain(url)
        if domain not in domain_dict:
          domain_dict[domain] = 0
        domain_dict[domain] += 1
    handle_dict[handle] = domain_dict
 
  name_list = sorted(handle_dict)
  final_dict = {}
  for i in range(len(name_list)):
    i_name = name_list[i]
    i_domain = handle_dict[i_name]
    for j in range(i+1, len(name_list)):
      j_name = name_list[j]
      j_domain = handle_dict[j_name]
      common_domain_dict = {}
      for domain in i_domain:
        if i_domain[domain] >= match_num and j_domain.get(domain, 0) >= match_num:
          common_domain_dict[domain] = True
      if common_domain_dict:
        if i_name not in final_dict:
          final_dict[i_name] = {}
        final_dict[i_name][j_name] = common_domain_dict

  return common_domain_dict

def get_tweets(handle, start, end):
  API = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token_key=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET)
  # rate limiting is 15 requests/15 minutes
  time.sleep(60)
  tweets = API.GetUserTimeline(screen_name=handle, count=200)
  last_tweet_id = tweet[-1].id
  for _ in range(15):
    time.sleep(60)
    new_tweets = API.GetUserTimeline(screen_name=handle, since_id=last_tweet_id, count=200)
    if not new_tweets:
      break
    tweets += new_tweets
    last_tweet_id = tweets[-1].id
  filtered_tweets = []
  for tweet in tweets:
    if filter_tweet(tweet, start, end):
      filtered_tweets.append(tweet)
  return filtered_tweets

def filter_tweet(tweet, start, end):
  date = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
  return date >= start and date <= end

def get_domain(url):
  response = requests.head(url)
  if response.status_code in (301, 302):
    url = response.headers['location']
  return find_domain(url)

def find_domain(url):
  extracted = tldextract.extract(url)
  return "{}.{}".format(extracted.domain, extracted.tld)
