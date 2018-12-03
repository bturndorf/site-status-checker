import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

#read .env file with Twilio API keys
#docs at https://github.com/theskumar/python-dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

urls = ['https://www.ushgnyc.com',
		'https://www.bluesmoke.com',
		'https://www.caffemarchio.com/',
		'https://www.dailyprovisionsnyc.com/',
		'https://www.gramercytavern.com/',
		'https://www.manhattarestaurant.com/',
		'https://www.martamanhattan.com/',
		'https://www.martinapizzeria.com/',
		'https://www.themodernnyc.com/',
		'https://www.porchlightbar.com/',
		'https://www.heytacocina.com/',
		'https://www.unionsquarecafe.com/',
		'https://www.untitledatthewhitney.com/',
		'https://www.vinifritti.com/']

def get_status_code(url):
	response = requests.get(url)
	return response.status_code

def send_site_down_text(urls):
	message = client.messages \
		.create(
			body='{} down - not returning 200 status.'.format(', '.join(urls)),
			from_='+16467986006',
			to='+19088124615'
			)
	print(message.sid)

status_codes = {}
for url in urls:
	status_codes[url] = get_status_code(url)

#array of site domains (no "https", etc) for sites that aren't returning 200 status code
non_responding_sites = [site[12:-5] for site, status in status_codes.items() if status !=200]

if non_responding_sites:
	send_site_down_text(non_responding_sites)