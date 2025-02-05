import requests

def fetch_m3u(url):
    """
    Fetch the M3U URL and return the playlist data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch M3U URL")

def parse_m3u(m3u_data):
    """
    Parse the M3U playlist and return a list of channel names.
    """
    channels = []
    for line in m3u_data.splitlines():
        if line.startswith("#EXTINF:"):
            # Extract the channel name from the line
            channel_info = line.split(",")[1]
            channels.append(channel_info)
    return channels