import tweepy

#tweepy authorization setup
ckey = 'YHhJ1A5aQMhRDVXjj3TBMjR6m'
csecret = '2mTVsZSJyHgHoKetVscWFDPxgg3P7uQyfLobkQcTToZEbpao1h'
atoken = '2308889702-KHnyBbDfEhPo51RRSr87e55xVYHLhCelJgrUjdk'
asecret = 'ND8GvPhxP02htZgIb0AgF47QMYqrO6ZWiwjAEFBFOotIF'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#define listener class
class myStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        if '"country_code":"US"' in data:
            print(data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

if __name__ == '__main__':
    listener = myStreamListener()
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['trump', 'clinton', 'sanders', 'cruz', 'kasich']) 

    """"Potential alternate streaming filters
    stream.filter(locations=[-125,25,-65,48])
    stream.filter(track=['"country_code":"US"'])
    """
