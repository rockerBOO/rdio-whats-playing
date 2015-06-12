#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from rdioapi import Rdio
import os
from pprint import pprint
import json
from StringIO import StringIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="User name on Rdio")
parser.add_argument("--file", default='whats_playing.txt', help="File to store what's playing")

args = parser.parse_args()

user = args.username
whats_playing_file = args.file

# user = 'rockerBOO'
# whats_playing_file = 'whats_playing.txt'
sample_data_json = 'sample-user-data.json'

# Need to set the enviromental variables
# CONSUMER_KEY = os.environ['RDIO_CONSUMER_KEY']
# CONSUMER_SECRET = os.environ['RDIO_CONSUMER_SECRET']

state = {}

# Set the Rdio object state with the key and secret
# r = Rdio(CONSUMER_KEY, CONSUMER_SECRET, state)

# pprint(r.findUser(vanityName=user, extras='lastSongPlayed,lastSongPlayTime'))

def render_last_played(last_played_result):
	return {
		'artist': last_played_result['artist'],
		'name':  last_played_result['name'],
		'icon400': last_played_result['icon400'],
		'short_url': last_played_result['shortUrl']
	}

def format_single_line(last_played):
	return "{} — {}".format(last_played['artist'], last_played['name'])

def write_whats_playing(last_played):
	try:
		wp_file = open(whats_playing_file, "w")

		try:
			wp_file.write(last_played)
		finally:
			wp_file.close()
	except IOError:
		pass

data = open(sample_data_json)

json_data = json.load(data)

only_single_line = True
write_to_file = True

if json_data['status'] == 'ok':
	rdio_result = json_data['result']

	last_played = render_last_played(rdio_result['lastSongPlayed'])

	if only_single_line:
		result = format_single_line(last_played)	
	else:
		result = json.dumps(last_played)

	if write_to_file:
		write_whats_playing(result)

