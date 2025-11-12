# 🐶 Corgi GIF Service

A simple, fun web service that searches for corgi GIFs based on activities! Built with Flask and deployable to Render.

## Features

- 🎨 Beautiful web interface
- 🔍 Search for corgi GIFs by activity (running, sleeping, playing, etc.)
- 🎲 Random selection from search results
- 🚀 Easy deployment to Render
- 📱 Mobile responsive
- 🔌 RESTful API endpoint
- ❤️ No authentication required
- 🐕 Powered by Giphy API

## Live Demo

Try it out: `/` - Web interface
API: `/api/corgi?activity=running`

## API Endpoints

### GET `/api/corgi`

Search for corgi GIFs by activity.

**Query Parameters:**
- `activity` (string): The activity the corgi should be doing (e.g., "running", "sleeping", "playing")

**Example Request:**
```bash
curl "https://your-service.onrender.com/api/corgi?activity=running"
```

**Example Response:**
```json
{
  "activity": "running",
  "title": "Happy Corgi Running GIF",
  "gif_url": "https://media.giphy.com/media/abc123/giphy.gif",
  "gif_url_small": "https://media.giphy.com/media/abc123/200.gif",
  "width": "480",
  "height": "270",
  "giphy_url": "https://giphy.com/gifs/abc123",
  "rating": "g"
}
```

### GET `/health`

Health check endpoint for monitoring.

**Example Response:**
```json
{
  "status": "healthy",
  "service": "corgi-gif-service"
}
```

## Local Development

### Prerequisites

- Python 3.8 or higher
- Giphy API Key (free from [Giphy Developers](https://developers.giphy.com/))

### Setup

1. **Clone or download the project:**
   ```bash
   cd ~/Documents/corgi-gif-service
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get a Giphy API Key:**
   - Go to [Giphy Developers](https://developers.giphy.com/)
   - Sign up and create an app
   - Copy your API key

5. **Set environment variable:**
   ```bash
   export GIPHY_API_KEY=your_api_key_here
   ```

6. **Run the service:**
   ```bash
   python app.py
   ```

7. **Open your browser:**
   ```
   http://localhost:5000
   ```

## Deploy to Render

### Option 1: Deploy via GitHub (Recommended)

1. **Create a GitHub repository:**
   ```bash
   cd ~/Documents/corgi-gif-service
   git init
   git add .
   git commit -m "Initial commit"
   gh repo create corgi-gif-service --public --source=. --remote=origin --push
   ```

2. **Deploy to Render:**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will detect `render.yaml` and configure automatically
   - Add environment variable: `GIPHY_API_KEY` = your key
   - Click "Create Web Service"

### Option 2: Deploy via Render Dashboard

1. **Go to [render.com](https://render.com)**

2. **Click "New +" → "Web Service"**

3. **Configure service:**
   - **Name:** `corgi-gif-service` (or your choice)
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment Variables:**
     - Add `GIPHY_API_KEY` = your Giphy API key

4. **Click "Create Web Service"**

5. **Wait for deployment** (usually 1-2 minutes)

6. **Access your service** at the provided URL (e.g., `https://corgi-gif-service.onrender.com`)

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GIPHY_API_KEY` | Yes | Your Giphy API key from [developers.giphy.com](https://developers.giphy.com/) |
| `PORT` | No | Port to run on (default: 5000, automatically set by Render) |

## Project Structure

```
corgi-gif-service/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment configuration
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Usage Examples

### Web Interface

1. Open the web interface
2. Enter an activity (e.g., "running")
3. Click "Find Corgi!"
4. Enjoy your corgi GIF!

### API Usage

**Search for running corgi:**
```bash
curl "https://your-service.onrender.com/api/corgi?activity=running"
```

**Search for sleeping corgi:**
```bash
curl "https://your-service.onrender.com/api/corgi?activity=sleeping"
```

**Search for playing corgi:**
```bash
curl "https://your-service.onrender.com/api/corgi?activity=playing"
```

### Python Example

```python
import requests

response = requests.get(
    "https://your-service.onrender.com/api/corgi",
    params={"activity": "running"}
)

data = response.json()
print(f"Found: {data['title']}")
print(f"GIF URL: {data['gif_url']}")
```

### JavaScript Example

```javascript
async function getCorgiGif(activity) {
    const response = await fetch(
        `https://your-service.onrender.com/api/corgi?activity=${activity}`
    );
    const data = await response.json();
    console.log(`Found: ${data.title}`);
    return data.gif_url;
}

// Usage
getCorgiGif('running').then(url => console.log(url));
```

## Activity Suggestions

Try these activities:
- running
- sleeping
- playing
- eating
- jumping
- swimming
- dancing
- walking
- spinning
- bouncing
- relaxing
- smiling
- happy

## Troubleshooting

### "No corgi GIFs found for activity"

- Try a different activity
- Use simpler terms (e.g., "run" instead of "running fast")
- Giphy might not have GIFs for very specific activities

### "Failed to fetch GIF from Giphy"

- Check your `GIPHY_API_KEY` is set correctly
- Verify your API key is valid at [Giphy Developers](https://developers.giphy.com/)
- Check if you've exceeded Giphy API rate limits (free tier: 1000 searches/day)

### Service won't start

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)
- Verify environment variable is set: `echo $GIPHY_API_KEY`

## API Rate Limits

Giphy Free Tier:
- 1,000 searches per day
- 42 searches per hour

If you need more, upgrade to Giphy's paid tiers.

## Technologies Used

- **Flask** - Web framework
- **Gunicorn** - Production WSGI server
- **Giphy API** - GIF search
- **Render** - Hosting platform

## Contributing

Feel free to fork and improve! Some ideas:
- Add more GIF sources (Tenor, etc.)
- Implement caching for popular searches
- Add favorite/save functionality
- Create categories or collections

## License

MIT License - feel free to use for any project!

## Credits

- GIFs provided by [Giphy](https://giphy.com/)
- Built with ❤️ for corgi lovers everywhere

## Support

For issues or questions:
- Check the troubleshooting section above
- Review Giphy API documentation
- Verify your Render deployment settings

---

Made with 🐶 and ☕
