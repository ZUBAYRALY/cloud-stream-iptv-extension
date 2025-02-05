# IPTV Extension for Cloud Stream 3

This extension adds IPTV functionality to Cloud Stream 3 by supporting custom M3U URLs. It fetches M3U playlists, parses the channels, and integrates them into Cloud Stream 3.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/cloud-stream-iptv-extension.git
   cd cloud-stream-iptv-extension
   ```

2. **Create and activate a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script**:

   ```bash
   python src/main.py
   ```

5. **Enter your M3U URL** when prompted, and the channels will be added to Cloud Stream 3.

## Dependencies

- `requests` – For making HTTP requests
- `m3u8` – For parsing M3U playlists
- `flask` (optional, if you want to add a web UI later)

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.