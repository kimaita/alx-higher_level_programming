#!/bin/bash
# Displays only the status code of a URL request response.
curl -s -o /dev/null -w '%{http_code}' "$1"
