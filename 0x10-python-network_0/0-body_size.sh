#!/bin/bash
# Script sends request to URL and displys the size of body response 
curl -s "$1" | wc -c
