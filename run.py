#python cron job to run the neccessary jobs
import os
import time


def cron():
    while True:
	#print "Started new job"
        time.sleep(300)
        os.popen("/root/.nvm/versions/node/v9.7.1/bin/node scripts/sync.js index update")
        os.popen("/root/.nvm/versions/node/v9.7.1/bin/node scripts/peers.js")
    
    
if __name__=="__main__":
    cron()
