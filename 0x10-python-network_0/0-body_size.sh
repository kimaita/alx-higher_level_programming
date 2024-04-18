#!/bin/bash
# Prints the size, in bytes, of the body of a URL request response 
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
