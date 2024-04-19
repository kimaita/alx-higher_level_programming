#!/bin/bash
# Sends a GET request to a URL with the header 'X-School-User-Id' (98) and displays the body of the response
curl -s -X "GET" -H "X-School-User-Id: 98" "$1"
