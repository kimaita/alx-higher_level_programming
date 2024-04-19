#!/bin/bash
# Displays the body of an URL request response only if with a 200 status code.
if (($(curl -sI "$1" | grep HTTP | cut -d' ' -f2) == 200)); then curl -s "$1"; fi;
