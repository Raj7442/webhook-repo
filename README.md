# GitHub Webhook Receiver

Flask application that receives GitHub webhooks and displays events in real-time.

## Features
- Receives GitHub webhooks (Push, Pull Request, Merge)
- Stores events in MongoDB
- UI polls every 15 seconds for updates
- Clean, minimal design
- Deployed on Railway

## Live Demo
🚀 **Live Application**: https://webhook-repo-production-f9a1.up.railway.app

## MongoDB Schema

```json
{
  "request_id": "string",
  "author": "string", 
  "action": "PUSH | PULL_REQUEST | MERGE",
  "from_branch": "string | null",
  "to_branch": "string",
  "timestamp": "string (ISO datetime)"
}
```

## Event Display Format

- **PUSH**: "Travis pushed to staging on 1st April 2021 - 9:30 PM UTC"
- **PULL_REQUEST**: "Travis submitted a pull request from staging to master on 1st April 2021 - 9:00 AM UTC"
- **MERGE**: "Travis merged branch dev to master on 2nd April 2021 - 12:00 PM UTC"

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

## Deployment

### Railway (Current)
- Deployed with MongoDB addon
- Auto-generated MONGO_URL environment variable
- Live at: https://webhook-repo-production-f9a1.up.railway.app

### Configure GitHub Webhook

1. Go to your repository settings
2. Settings → Webhooks → Add webhook
3. Payload URL: `https://webhook-repo-production-f9a1.up.railway.app/webhook`
4. Content type: `application/json`
5. Events: Push, Pull requests
6. Active: ✓

## Repository Links
- **webhook-repo**: https://github.com/Raj7442/webhook-repo
- **action-repo**: https://github.com/Raj7442/action-repo
