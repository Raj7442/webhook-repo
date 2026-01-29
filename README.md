# GitHub Webhook Receiver

Flask application that receives GitHub webhooks and displays events in real-time.

## Features
- Receives GitHub webhooks (Push, Pull Request, Merge)
- Stores events in MongoDB
- UI polls every 15 seconds for updates
- Clean, minimal design

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set MongoDB URI
```bash
export MONGO_URI="mongodb://localhost:27017/github_events"
```

### 3. Run Application
```bash
python app.py
```

### 4. Expose to Internet (for GitHub webhooks)
```bash
# Using ngrok
ngrok http 5000
```

## Configure GitHub Webhook

1. Go to your `action-repo` repository
2. Settings → Webhooks → Add webhook
3. Payload URL: `https://your-ngrok-url.ngrok.io/webhook`
4. Content type: `application/json`
5. Events: Push, Pull requests
6. Active: ✓

## MongoDB Schema

```json
{
  "request_id": "string",
  "author": "string",
  "action": "PUSH | PULL_REQUEST | MERGE",
  "from_branch": "string | null",
  "to_branch": "string",
  "timestamp": "datetime"
}
```

## Deployment

### Railway
```bash
railway init
railway up
```

### Render
Connect GitHub repo and deploy

## Environment Variables
- `MONGO_URI`: MongoDB connection string
