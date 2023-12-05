curl -X POST -H "Content-Type: application/json" -d '{"username": "hacker", "password": "kavita"}' http://localhost:4444/register
curl -X POST -H "Content-Type: application/json" -d '{"username": "hacker", "password": "kavita"}' http://localhost:4444/login
curl -X POST -H "Content-Type: application/json" -d '{"channel_name":"anonymous"}' http://localhost:4444/create_channel
curl -X POST -H "Content-Type: application/json" -d '{"channel_name":"anonymous", "username": "hacker"}' http://localhost:4444/join_channel
curl -X POST -H "Content-Type: application/json" -d '{"username": "hacker", "password": "kavita", "channel_name": "anonymous", "content": "goneaway"}' http://localhost:4444/send_message
curl -X POST -H "Content-Type: application/json" -d '{"username": "hacker", "password": "kavita", "channel_name": "anonymous", "content": "hello"}' http://localhost:4444/send_message

