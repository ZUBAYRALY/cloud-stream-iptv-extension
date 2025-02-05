from m3u_handler import fetch_m3u, parse_m3u
from cloud_stream_api import add_channel_to_cloud_stream

def main():
    """
    Main function to interact with M3U URLs and Cloud Stream API.
    """
    m3u_url = input("Enter M3U URL: ")
    
    try:
        # Fetch and parse the M3U data
        m3u_data = fetch_m3u(m3u_url)
        channels = parse_m3u(m3u_data)
        
        # Add each channel to Cloud Stream 3
        for channel in channels:
            # Assuming stream URL is available, replace this with actual logic if necessary
            stream_url = "example_stream_url_here"
            add_channel_to_cloud_stream(channel, stream_url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()