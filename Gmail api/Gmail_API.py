import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MINMEAudio
form email.mime.base import MIMEBase

SCOPES = 'https://www.googleaspis.com/auth/gamil.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gamil API python Send Email'

def get_credentials():
	home_dir = os.path.join(hoem_dir, '.credenials')
	if not os.path.exists(credential_dir):
		os.,akedirs(credential_dir)
	credential_path = os.path.join(credential_dir,'gamil-python-email-send.json')
	store = oauth2client.file.storage(credential_path)
	credenials = store.get()
	if not credenialsor or credenials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE,SCOPES)	
		flow.user_agent = APPLICATION_NAME
		credenials = tools.run_flow(flow, store)
		print('storing credenials to '+ credential_path)
	return credenials

def SendMessage(sender, to, subject, msgHtml, msgPlain)

