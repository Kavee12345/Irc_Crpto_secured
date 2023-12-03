from flask import Flask, request, jsonify

app = Flask(__name__)

# User database (temporary for the example)
users = []
channels = []

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Check if the username is already taken
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username already exists'}), 400

    user = {'username': username, 'password': password}
    users.append(user)

    return jsonify({'message': 'Registration successful'}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Check if the username and password match a registered user
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)

    if not user:
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

# Endpoint for creating a channel
@app.route('/create_channel', methods=['POST'])
def create_channel():
    data = request.json
    channel_name = data.get('channel_name')

    if not channel_name:
        return jsonify({'error': 'Channel name is required'}), 400

    # Check if the channel name is already taken
    if any(channel['channel_name'] == channel_name for channel in channels):
        return jsonify({'error': 'Channel name already exists'}), 400

    channel = {'channel_name': channel_name, 'users': []}
    channels.append(channel)

    return jsonify({'message': 'Channel created successfully'}), 201

# Endpoint for joining a channel
@app.route('/join_channel', methods=['POST'])
def join_channel():
    data = request.json
    username = data.get('username')
    channel_name = data.get('channel_name')

    if not username or not channel_name:
        return jsonify({'error': 'Username and channel name are required'}), 400

    # Check if the user is already in the channel
    user = next((user for user in users if user['username'] == username), None)
    channel = next((channel for channel in channels if channel['channel_name'] == channel_name), None)

    if not user or not channel:
        return jsonify({'error': 'User or channel not found'}), 404

    # Add the user to the channel
    channel['users'].append(username)

    return jsonify({'message': f'{username} joined {channel_name}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
