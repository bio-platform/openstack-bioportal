from flask import request, session
from flask_restful import Resource

from Connection import connect


class Image(Resource):
    @staticmethod
    def get(image_id=None):
        """
            **Get specific image**

            This function allows users to get their image specified by its ID. If no parameter given, all available
            images are returned

            :param image_id: id of the image
            :type image_id: openstack image id or None
            :return: image information in json and http status code

            - Example::

                  curl -X GET bio-portal.metacentrum.cz/api/images/_your_image_id/ -H
                  'Cookie: cookie from scope' -H 'content-type: application/json'

            - Expected Success Response::

                HTTP Status Code: 200

                json-format: see openstack.compute.v2.image

                or

                HTTP Status Code: 200

                openstack.compute.v2.image array

            - Expected Fail Response::

                HTTP Status Code: 404

                {}

        """
        connection = connect(session["token"], session["project_id"])
        if image_id is None:
            images = connection.compute.images()
            return [r for r in images], 200

        image = connection.compute.find_image(image_id)
        if image is None:
            return {}, 404
        return image.to_dict(), 200
