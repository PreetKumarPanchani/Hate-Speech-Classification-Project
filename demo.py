'''
from hateSpeechIdentification.logger import logging

logging.info("Starting the project...")
'''

'''
from hateSpeechIdentification.exception import CustomException
import sys


try:
    a = 7 / '6'
except Exception as e:
    raise CustomException(e, sys ) from e

'''

'''
from hateSpeechIdentification.configuration import gcloud_syncer

gcloud_syn = gcloud_syncer()

gcp_bucket_url = ''
filepath =   ''
filename =  ''
destination = ''

gcloud_syn.sync_folder_to_gcloud( gcp_bucket_url, filepath, filename)

gcloud_syn.sync_folder_from_gcloud( gcp_bucket_url, filename, destination)

'''



