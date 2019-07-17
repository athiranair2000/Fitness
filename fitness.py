from telegram.ext import Updater,InlineQueryHandler,CommandHandler
import requests


def get_url():
	contents=requests.get('https://www.googleapis.com/fitness/v1/users/me/dataSources?key=AIzaSyDIltHT3f1XqwpnBY50NQhozdzIRT1gic8').json()
	url=contents['url']
	return url

def main():
	updater=Updater('789004155:AAHJVdomi3-JQ0qcl_6WiBAmu_VLgRZqhak',use_context=True)
	dp=updater.dispatcher
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	main()
	
	
