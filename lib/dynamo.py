from uuid import uuid1
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('')

def create_site(event,context): 
    """
    :param dict site:{"name": "foo.com", "url": "https://foo.com"}
		Put Site Data in DynamoDB
    """
    site["id"] = uuid1()
		
    sites.append(site)


def get_sites(event,context): 
    """
		Get Site Data in DynamoDB
		"""

		return sites


def remove_site(event,context):
    """
		Remove Site Data in DynamoDB		
		"""
		
		pass


def update_site_state(event,context):
    """	
		Update Site Data
		"""

		pass
