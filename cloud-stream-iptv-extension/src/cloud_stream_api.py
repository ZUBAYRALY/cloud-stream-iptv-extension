import requests

def add_channel_to_cloud_stream(channel, stream_url):
    """
    Add a channel to Cloud Stream 3 using its API.
    """
    data = {
        'channel_name': channel,
        'url': stream_url
    }
    # Replace with actual Cloud Stream 3 API endpoint
    response = requests.post("CLOUD_STREAM_3_API_ENDPOINT", data=data)
    
    if response.status_code == 200:
        print(f"Successfully added {channel}.")
    else:
        print(f"Failed to add {channel}. Status code: {response.status_code}")