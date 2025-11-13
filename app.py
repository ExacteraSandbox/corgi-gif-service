"""
Corgi GIF Service - A simple web service to search for corgi GIFs by activity
"""

from flask import Flask, request, jsonify, render_template_string
import requests
import os
import random

app = Flask(__name__)

# Add CORS headers to all responses
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Giphy API configuration
GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY', 'YOUR_API_KEY_HERE')
GIPHY_API_URL = 'https://api.giphy.com/v1/gifs/search'

# HTML template for the web interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corgi GIF Finder</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }
        input {
            flex: 1;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            padding: 15px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #764ba2;
        }
        #result {
            text-align: center;
            margin-top: 20px;
        }
        #gif-container img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        .loading {
            color: #667eea;
            font-size: 18px;
        }
        .error {
            color: #e74c3c;
            padding: 15px;
            background: #ffe5e5;
            border-radius: 8px;
        }
        .examples {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .examples h3 {
            margin-top: 0;
            color: #333;
        }
        .example-btn {
            display: inline-block;
            margin: 5px;
            padding: 8px 15px;
            background: #e9ecef;
            color: #333;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .example-btn:hover {
            background: #dee2e6;
        }
        .api-info {
            margin-top: 20px;
            padding: 15px;
            background: #fff3cd;
            border-radius: 8px;
            font-size: 14px;
            color: #856404;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐶 Corgi GIF Finder 🐶</h1>
        <p class="subtitle">Find adorable corgi GIFs doing various activities!</p>

        <div class="search-box">
            <input type="text" id="activity" placeholder="Enter activity (e.g., running, sleeping, playing...)" />
            <button onclick="searchCorgi()">Find Corgi!</button>
        </div>

        <div class="examples">
            <h3>Try these activities:</h3>
            <span class="example-btn" onclick="searchExample('running')">Running</span>
            <span class="example-btn" onclick="searchExample('sleeping')">Sleeping</span>
            <span class="example-btn" onclick="searchExample('playing')">Playing</span>
            <span class="example-btn" onclick="searchExample('eating')">Eating</span>
            <span class="example-btn" onclick="searchExample('jumping')">Jumping</span>
            <span class="example-btn" onclick="searchExample('swimming')">Swimming</span>
            <span class="example-btn" onclick="searchExample('dancing')">Dancing</span>
        </div>

        <div id="result"></div>

        <div class="api-info">
            💡 <strong>API Endpoint:</strong> <code>/api/corgi?activity=YOUR_ACTIVITY</code>
            <br>Returns JSON with GIF URL and metadata.
        </div>
    </div>

    <script>
        function searchCorgi() {
            const activity = document.getElementById('activity').value;
            if (!activity) {
                alert('Please enter an activity!');
                return;
            }

            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p class="loading">🐕 Searching for corgi GIFs...</p>';

            fetch(`/api/corgi?activity=${encodeURIComponent(activity)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        resultDiv.innerHTML = `<p class="error">❌ Error: ${data.error}</p>`;
                    } else {
                        resultDiv.innerHTML = `
                            <div id="gif-container">
                                <h3>${data.title}</h3>
                                <img src="${data.gif_url}" alt="${data.title}">
                                <p><a href="${data.giphy_url}" target="_blank">View on Giphy</a></p>
                            </div>
                        `;
                    }
                })
                .catch(error => {
                    resultDiv.innerHTML = `<p class="error">❌ Error: ${error.message}</p>`;
                });
        }

        function searchExample(activity) {
            document.getElementById('activity').value = activity;
            searchCorgi();
        }

        // Allow Enter key to search
        document.getElementById('activity').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchCorgi();
            }
        });
    </script>
</body>
</html>
'''


@app.route('/')
def home():
    """Serve the web interface"""
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/corgi')
def get_corgi_gif():
    """
    API endpoint to search for corgi GIFs

    Query Parameters:
        activity (str): The activity the corgi should be doing (e.g., 'running', 'sleeping')

    Returns:
        JSON with gif_url, title, and other metadata
    """
    activity = request.args.get('activity', 'cute')

    # Build search query
    search_query = f"corgi {activity}"

    # Parameters for Giphy API
    params = {
        'api_key': GIPHY_API_KEY,
        'q': search_query,
        'limit': 25,  # Get multiple results
        'rating': 'g',  # Family-friendly content only
        'lang': 'en'
    }

    try:
        # Make request to Giphy API
        response = requests.get(GIPHY_API_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Check if we got results
        if not data.get('data'):
            return jsonify({
                'error': f'No corgi GIFs found for activity: {activity}',
                'suggestion': 'Try a different activity like running, sleeping, or playing'
            }), 404

        # Pick a random GIF from results
        gif = random.choice(data['data'])

        # Extract GIF information
        result = {
            'activity': activity,
            'title': gif.get('title', 'Corgi GIF'),
            'gif_url': gif['images']['original']['url'],
            'gif_url_small': gif['images']['fixed_height']['url'],
            'width': gif['images']['original']['width'],
            'height': gif['images']['original']['height'],
            'giphy_url': gif.get('url', ''),
            'rating': gif.get('rating', 'g')
        }

        return jsonify(result)

    except requests.RequestException as e:
        return jsonify({
            'error': 'Failed to fetch GIF from Giphy',
            'details': str(e)
        }), 500
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred',
            'details': str(e)
        }), 500


@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({'status': 'healthy', 'service': 'corgi-gif-service'})


if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))

    # Run the app
    app.run(host='0.0.0.0', port=port, debug=False)
