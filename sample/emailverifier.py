from boto3 import client
from dotenv import load_dotenv

load_dotenv()

ses = client('ses')
response = ses.verify_domain_identity(
    Domain='DOMAIN_NAME'
)

print(response)