import requests
from bs4 import BeautifulSoup

def download_reel_by_id(reel_id):
    base_url = f'https://www.instagram.com/reel/{reel_id}/?&__a=1&__d=1'

    try:
        # Send an HTTP request to get the JSON data
        response = requests.get(base_url)
        response.raise_for_status()

        # Parse the JSON data to get the video URL
        json_data = response.json()
        video_url = json_data['graphql']['shortcode_media']['video_url']

        # Download the video
        download_video(video_url)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Reel ID '{reel_id}' not found or video URL not found in the JSON response.")

def download_video(video_url):
    try:
        # Send an HTTP request to download the video
        response = requests.get(video_url)
        response.raise_for_status()

        # Get the file name from the URL
        file_name = video_url.split('/')[-1]

        # Save the video to the current directory
        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f"Video downloaded successfully as '{file_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Replace 'ClwrpW1BB-R' with the Reel ID you want to download
    reel_id = 'ClwrpW1BB-R'
    download_reel_by_id(reel_id)