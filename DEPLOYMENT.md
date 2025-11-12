# Deployment Guide - Corgi GIF Service to Render

## Quick Start (5 minutes)

### Step 1: Get a Giphy API Key (2 minutes)

1. Go to [https://developers.giphy.com/](https://developers.giphy.com/)
2. Click "Create an App"
3. Select "API" (not SDK)
4. Fill in:
   - App Name: "Corgi GIF Service"
   - App Description: "Searches for corgi GIFs"
5. Click "Create App"
6. Copy your API Key (starts with a long string of letters/numbers)

### Step 2: Push to GitHub (1 minute)

```bash
cd ~/Documents/corgi-gif-service

# Initialize git
git init

# Add files
git add .

# Commit
git commit -m "Initial commit - Corgi GIF Service"

# Create GitHub repo and push
gh repo create corgi-gif-service --public --source=. --remote=origin --push
```

### Step 3: Deploy to Render (2 minutes)

1. Go to [https://render.com](https://render.com) and sign up/login

2. Click **"New +"** → **"Web Service"**

3. Connect your GitHub repository:
   - Click "Connect GitHub"
   - Authorize Render
   - Select your `corgi-gif-service` repository

4. Configure the service (Render auto-detects most settings from `render.yaml`):
   - **Name**: `corgi-gif-service` (or choose your own)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt` (auto-filled)
   - **Start Command**: `gunicorn app:app` (auto-filled)

5. Add Environment Variable:
   - Click "Advanced" → "Add Environment Variable"
   - **Key**: `GIPHY_API_KEY`
   - **Value**: Paste your Giphy API key from Step 1
   - Click "Save"

6. Click **"Create Web Service"**

7. Wait for deployment (1-2 minutes)

8. Your service will be live at: `https://corgi-gif-service.onrender.com`

## Testing Your Deployment

### Test the Web Interface

Open in browser:
```
https://your-service-name.onrender.com
```

You should see the Corgi GIF Finder interface!

### Test the API

Try these URLs in your browser or with curl:

```bash
# Test health endpoint
curl https://your-service-name.onrender.com/health

# Search for running corgi
curl "https://your-service-name.onrender.com/api/corgi?activity=running"

# Search for sleeping corgi
curl "https://your-service-name.onrender.com/api/corgi?activity=sleeping"
```

## Troubleshooting

### Service Won't Start

**Check Logs:**
1. Go to your service in Render dashboard
2. Click "Logs" tab
3. Look for error messages

**Common Issues:**
- **"No module named 'flask'"**: Build didn't complete. Check Build Logs.
- **"Invalid API key"**: Check your `GIPHY_API_KEY` environment variable
- **"Port already in use"**: Render handles this automatically, shouldn't happen

### No GIFs Returned

**Issue**: API returns "No corgi GIFs found"

**Solutions:**
- Try different activities
- Verify your Giphy API key is valid
- Check you haven't exceeded Giphy rate limits (1000 searches/day on free tier)

### Deployment Failed

**Check Build Logs:**
1. Render Dashboard → Your Service → "Logs" → "Build"
2. Look for Python errors

**Common Issues:**
- **Requirements not installed**: Ensure `requirements.txt` is in root directory
- **Python version**: Render uses Python 3.7+ by default (should work fine)

## Updating Your Service

After making changes:

```bash
cd ~/Documents/corgi-gif-service

# Make your changes to app.py or other files

# Commit changes
git add .
git commit -m "Description of changes"

# Push to GitHub
git push origin main

# Render automatically redeploys!
```

## Custom Domain (Optional)

To use your own domain:

1. In Render Dashboard, go to your service
2. Click "Settings"
3. Scroll to "Custom Domain"
4. Add your domain
5. Update your DNS records as instructed by Render

## Render Free Tier Limits

**Free tier includes:**
- 750 hours/month (always-on for one service)
- Automatic SSL certificates
- Automatic deploys from GitHub
- Sleep after 15 minutes of inactivity (wakes up on request)

**Limitations:**
- Service spins down after 15 min inactivity (first request after spin-down takes ~30 seconds)
- No custom memory/CPU limits
- Limited bandwidth

**To keep service always-on:**
- Upgrade to paid tier ($7/month)
- Or use a service like UptimeRobot to ping your health endpoint every 5 minutes

## Monitoring

### Check Service Health

Add this URL to your monitoring tool:
```
https://your-service-name.onrender.com/health
```

Expected response:
```json
{"status": "healthy", "service": "corgi-gif-service"}
```

### View Logs

In Render Dashboard:
1. Go to your service
2. Click "Logs" tab
3. See real-time logs

## Environment Variables

You can add more environment variables in Render:

1. Go to Service → Settings
2. Scroll to "Environment Variables"
3. Click "Add Environment Variable"

Example variables you might add:
- `LOG_LEVEL`: "DEBUG" or "INFO"
- `MAX_RESULTS`: Number of GIF results to fetch
- `DEFAULT_ACTIVITY`: Default activity when none specified

## Scaling

### Upgrade Instance

1. Go to Service → Settings
2. Scroll to "Instance Type"
3. Upgrade to get more CPU/RAM

### Add Auto-Scaling (Paid plans only)

1. Go to Service → Settings
2. Enable auto-scaling
3. Set min/max instances

## Security

### Protecting Your API Key

- Never commit `.env` files
- Use Render's environment variables (encrypted at rest)
- Rotate API keys periodically

### Rate Limiting

Consider adding rate limiting if your service gets popular:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app=app,
    key_func=lambda: request.remote_addr,
    default_limits=["100 per hour"]
)
```

## Cost Optimization

**Free Tier:**
- Deploy on Render's free tier
- Giphy free tier: 1000 searches/day

**Estimated Costs (if you upgrade):**
- Render Starter ($7/month): Always-on service
- Giphy API paid tiers: Start at $0.001 per search over free limit

## Support

**Render Support:**
- [Render Documentation](https://render.com/docs)
- [Render Community](https://community.render.com/)

**Giphy Support:**
- [Giphy API Docs](https://developers.giphy.com/docs/api/)
- [Giphy Support](https://support.giphy.com/)

## Next Steps

After successful deployment:

1. ✅ Share your service URL with friends
2. ✅ Add custom domain (optional)
3. ✅ Set up monitoring (UptimeRobot, Pingdom, etc.)
4. ✅ Consider adding features:
   - Caching popular GIFs
   - User favorites
   - Multiple GIF sources
   - Image generation with AI

Congratulations! Your Corgi GIF Service is live! 🎉🐶
