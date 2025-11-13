#!/usr/bin/env python3
"""
Simple test program to fetch and display a corgi GIF in the browser
"""

import requests
import webbrowser
import tempfile
import os

def fetch_and_display_corgi(activity="running"):
    """
    Fetch a corgi GIF and display it in the browser

    Args:
        activity: The activity for the corgi (e.g., "running", "sleeping", "playing")
    """
    print(f"🐶 Fetching {activity} corgi GIF...")

    # Make API request
    api_url = "https://corgi-gif-service-1.onrender.com/api/corgi"
    params = {"activity": activity}

    try:
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        print(f"✓ Found: {data['title']}")
        print(f"✓ GIF URL: {data['gif_url']}")

        # Create HTML file to display the GIF
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corgi GIF - {activity}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 800px;
        }}
        h1 {{
            color: #333;
            margin-top: 0;
        }}
        img {{
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            margin: 20px 0;
        }}
        .info {{
            color: #666;
            margin-top: 20px;
        }}
        a {{
            color: #667eea;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .activity {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🐶 Corgi GIF Viewer</h1>
        <span class="activity">Activity: {activity}</span>
        <h2>{data['title']}</h2>
        <img src="{data['gif_url']}" alt="{data['title']}">
        <div class="info">
            <p>Dimensions: {data['width']} x {data['height']}</p>
            <p><a href="{data['giphy_url']}" target="_blank">View on Giphy</a></p>
            <p><a href="{api_url}?activity={activity}" target="_blank">API Endpoint</a></p>
        </div>
    </div>
</body>
</html>
"""

        # Save to temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html_content)
            temp_file = f.name

        print(f"✓ Opening in browser...")

        # Open in default browser
        webbrowser.open('file://' + temp_file)

        print(f"✓ GIF displayed in browser!")
        print(f"\nHTML file saved at: {temp_file}")
        print("(This file will be automatically cleaned up on next system restart)")

    except requests.RequestException as e:
        print(f"✗ Error fetching GIF: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


if __name__ == "__main__":
    import sys

    # Get activity from command line or use default
    activity = sys.argv[1] if len(sys.argv) > 1 else "running"

    print("=" * 50)
    print("Corgi GIF Viewer - Test Program")
    print("=" * 50)

    fetch_and_display_corgi(activity)

    print("\nTry running with different activities:")
    print("  python test_corgi_viewer.py sleeping")
    print("  python test_corgi_viewer.py playing")
    print("  python test_corgi_viewer.py happy")
