import tweepy
import time

#setup tweepy Oauth
auth = tweepy.OAuthHandler(
    'YMaRCwObPMfcEvcqDSMaEza4x', 
    'qmawQuA8p6Rxvp9rrLREUkaLVRLRWpUdOE9GaI2BLpxntq8iat'
)
auth.set_access_token(
    '961387368463781888-6NYJVeWtVhbXVU12qvRno4kuq43492N',
    '5DsU7UfhghntczyLNsijssrfZVpcsOe8Rbo24Ighjnzwo'
)
api=tweepy.API(auth)

#Extract from ids
def ids_to_txt(id_txt, output):
    with open(id_txt, 'r') as in_file:
        print("***************************************************************")
        print(id_txt)
        print("***************************************************************")
        with open(output, 'w') as out_file:
            count=0
            ids=[]
            for line in in_file:
                ids.append(int(line))
                if len(ids)>=100:
                    try:
                        status=api.statuses_lookup(ids, False, True, False)
                    except tweepy.RateLimitError:
                        time.sleep(15 * 60 + 5)
                        print("Waiting for API Rate Limit to Reset")
                        print(count+" tweets collected")
                        status=api.statuses_lookup(ids, False, True, False)
                    count+=len(status)
                    for s in status:
                        out_file.write(s.text.encode('ascii', 'ignore').replace('\r', '').replace('\n',' ')+"\n")
                    ids=[]
#ISCRAM18 datasets
out=[
    "tweets_ISCRAM18_Harvey.txt",
    "tweets_ISCRAM18_Irma.txt",
    "tweets_ISCRAM18_Maria.txt"
]
files=[
    'tweets/ISCRAM18_datasets/Harvey_tweet_ids.txt',
    'tweets/ISCRAM18_datasets/Irma_tweet_ids.txt',
    'tweets/ISCRAM18_datasets/Maria_tweet_ids.txt'
]
for i, f in enumerate(files):
    ids_to_txt(files[i], out[i])