import sys
import tweepy
from serial import Serial
from time import sleep

microbitPort = '/dev/tty.usbmodem1412' # USB port address for the micro:bit /dev/ttyACM0 or /dev/tty.usbmodem40132 or similar
microbitBaud = '115200' # Baud for serial communication

consumer_key        = 'your code'
consumer_secret     = 'your code'
access_key          = 'your code'
access_secret       = 'your code'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#api = tweepy.API(auth, wait_on_rate_limit=True)

ser = Serial(microbitPort, microbitBaud, timeout=3)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
#        user = api.me()
        if 'norway' in status.text.lower():
            print("norway " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("norway" + "\n"))
            
        if 'rainbow' in status.text.lower():
            print("rainbow " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("rainbow" + "\n"))
           
        if 'sweden' in status.text.lower():
            print("sweden " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("sweden" + "\n"))
            
        if 'trump' in status.text.lower():
            print("trump " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("usa" + "\n"))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-27.9,32.7,63.3,73.6]) # make area and numbers on http://boundingbox.klokantech.com/

