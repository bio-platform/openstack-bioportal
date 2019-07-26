from glanceclient import Client as GlanceClient
from auth_api import sess

glance_client = GlanceClient('2', session=sess)
"""
for image in glance.images.list():
    # print( [i for i in glance.image_members.list(image.id)])
    print(glance.images.get(image.id))
    # print(dir(image))
    # print( [i for i in glance.image_members.list(image.id)])
"""