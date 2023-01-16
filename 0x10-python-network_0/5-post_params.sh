#!/bin/bash
# Bash scipt takes in URL, sends POST request to URL and displays the body
curl -sX "POST" -d "email=test@gmail" -d "subject='I will always be here for PLD'"
