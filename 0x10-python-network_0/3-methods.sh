#!/bin/bash
# Displays HTTP methods the server will accept   
OPT=$(curl -sI "$1" | grep "Allow") && echo "${OPT##*: }"
