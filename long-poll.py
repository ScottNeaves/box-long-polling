import requests
import sys

if (len(sys.argv) < 2):
    print("Please supply a valid Developer Token as the first positional argument to this python script. You can create one by following the instructions here: https://developer.box.com/docs/getting-started-box-integration#section-using-the-box-api")
    sys.exit()

# Grab the first positional argument to the script, use it as the Developer Token.
auth_header = {'Authorization': 'Bearer ' + sys.argv[1]}

stream_position_url = 'https://api.box.com/2.0/events?stream_position=now'
stream_position_response = requests.get(stream_position_url, headers=auth_header)
stream_position = None
if (stream_position_response.status_code == 401):
    print("The Developer Token you have supplied is invalid or has expired. Please generate a new one - instructions can be found here: https://developer.box.com/docs/getting-started-box-integration#section-using-the-box-api")
    sys.exit()
else:
    stream_position = stream_position_response.json()['next_stream_position']

def get_polling_address():
    long_poll_address = requests.options('https://api.box.com/2.0/events', headers=auth_header).json()['entries'][0]['url']
    print('realtime url: ' + long_poll_address)
    return long_poll_address

long_poll_address = get_polling_address()

while (True):
    print('long polling...')
    params = {'stream_position': stream_position}
    long_poll = requests.get(long_poll_address, params=params)
    message = long_poll.json()['message']
    print(message)

    # Get a new polling address when the long polling address tells us to reconnect, and go back to the top to open a new connection to it.
    if (message == 'reconnect'):
        long_poll_address = get_polling_address()
        continue

    print('fetching events')
    params = {'stream_position': stream_position}
    event_details = requests.get('https://api.box.com/2.0/events', headers=auth_header, params=params).json()
    event_id = event_details['entries'][0]['event_id']
    event_type = event_details['entries'][0]['event_type']
    stream_position = event_details['next_stream_position']
    print(event_id + " | " + event_type)
