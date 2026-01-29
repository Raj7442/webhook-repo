from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from datetime import datetime
import os

app = Flask(__name__)
# Try Railway's MONGO_URL first, then fallback to MONGO_URI
mongo_uri = os.getenv("MONGO_URL") or os.getenv("MONGO_URI", "mongodb://localhost:27017/github_events")
print(f"Using MongoDB URI: {mongo_uri[:20]}...")  # Debug log
app.config["MONGO_URI"] = mongo_uri
try:
    mongo = PyMongo(app)
    print("MongoDB connection initialized")
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    mongo = None

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    
    event_data = {
        'request_id': '',
        'author': '',
        'action': '',
        'from_branch': None,
        'to_branch': '',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
    
    if event_type == 'push':
        event_data['request_id'] = data['head_commit']['id']
        event_data['author'] = data['pusher']['name']
        event_data['action'] = 'PUSH'
        event_data['to_branch'] = data['ref'].split('/')[-1]
        
    elif event_type == 'pull_request':
        pr = data['pull_request']
        event_data['request_id'] = str(pr['id'])
        event_data['author'] = pr['user']['login']
        event_data['action'] = 'PULL_REQUEST' if data['action'] == 'opened' else 'MERGE'
        event_data['from_branch'] = pr['head']['ref']
        event_data['to_branch'] = pr['base']['ref']
    
    mongo.db.events.insert_one(event_data)
    return jsonify({'status': 'success'}), 200

@app.route('/events', methods=['GET'])
def get_events():
    try:
        if mongo.db is None:
            return jsonify({"error": "Database connection failed"}), 500
        events = list(mongo.db.events.find().sort('timestamp', -1).limit(20))
        for event in events:
            event['_id'] = str(event['_id'])
            # Parse ISO string back to datetime for display formatting
            if isinstance(event['timestamp'], str):
                dt = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
                event['timestamp'] = dt.strftime('%d %B %Y - %I:%M %p UTC')
        return jsonify(events)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
