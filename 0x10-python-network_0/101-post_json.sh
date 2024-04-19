#!/bin/bash
# Sends a JSON 'POST' request to a URL and displays the body of the response.
curl -s -X "POST" --data @"$2" --header "Content-Type: application/json" --header "Accept: application/json" "$1"
