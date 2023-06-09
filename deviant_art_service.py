import requests
import json


class DeviantArtService:
    def get_images(self, access_token, username):
        deviant_art_url = 'https://www.deviantart.com/api/v1/oauth2/gallery/all'
        mature_content = 'true'

        headers = {
            "Authorization": "Bearer " + access_token
        }
        params = {
            "username": username,
            "mature_content": mature_content
        }
        response = requests.get(
            deviant_art_url, headers=headers, params=params)

        data = response.json()

        if 'results' in data:
            results = data['results']
            images = []
            for result in results:
                if len(images) < 5:
                    images.append(result['preview']['src'])
                else:
                    break
            return images
        else:
            print('No results found')
            return None
