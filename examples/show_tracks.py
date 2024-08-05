from ochrepy.auth import OchreClientCredentials
import ochrepy
from pprint import pprint

op = ochrepy.Ochre(client_credentials_manager=OchreClientCredentials())

offset = 0

response = op.music_tracks.list()


for track in response['results']:
            pprint(track['title'] + ' - ' + track['artist']['name'])