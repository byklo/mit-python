import spotipy
import imp

try:
	imp.find_module('spotipy')
	found = True
except ImportError:
	found = False

print found

sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
	print ' ', i, t['name']
