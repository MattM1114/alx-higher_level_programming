#!/usr/bin/python3

def load_from_json_file(filename):
	with open(filename) as f:
		return json.load(f)
