#!/bin/bash
# Gets a server to return 'You got me!'
curl -s -X "PUT" -H "Origin: School" localhost:5000/catch_me_3
