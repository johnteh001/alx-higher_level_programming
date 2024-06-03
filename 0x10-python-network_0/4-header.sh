#!/bin/bash
# Script sends GET request using user defined header   
curl -sH "X-School-User-Id: 98" "$1"
