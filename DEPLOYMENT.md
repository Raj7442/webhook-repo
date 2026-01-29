# Deployment Guide

## Quick Setup Steps

### 1. Deploy webhook-repo

**Option A: Railway**
```bash
cd webhook-repo
railway init
railway add mongodb
railway up
```

**Option B: Render**
1. Connect GitHub repo
2. Add MongoDB addon
3. Deploy

### 2. Create action-repo on GitHub
```bash
cd action-repo
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/action-repo.git
git push -u origin main
```

### 3. Configure Webhook
1. Go to action-repo on GitHub
2. Settings → Webhooks → Add webhook
3. Payload URL: `https://your-deployed-url/webhook`
4. Content type: `application/json`
5. Events: Select "Push" and "Pull requests"
6. Active: ✓
7. Add webhook

### 4. Test
```bash
# In action-repo
echo "test" >> test.txt
git add .
git commit -m "Test webhook"
git push
```

### 5. View Events
Open: `https://your-deployed-url/`

Events will appear and auto-refresh every 15 seconds!

## MongoDB Setup

### Local
```bash
# Install MongoDB
# Start MongoDB
mongod

# Set environment variable
export MONGO_URI="mongodb://localhost:27017/github_events"
```

### Cloud (MongoDB Atlas)
1. Create free cluster at mongodb.com/cloud/atlas
2. Get connection string
3. Set as environment variable:
```bash
export MONGO_URI="mongodb+srv://user:pass@cluster.mongodb.net/github_events"
```

## Troubleshooting

**Webhook not receiving events?**
- Check webhook URL is correct
- Ensure app is publicly accessible
- Check webhook delivery logs on GitHub

**Events not showing in UI?**
- Check MongoDB connection
- Check browser console for errors
- Verify /events endpoint returns data
