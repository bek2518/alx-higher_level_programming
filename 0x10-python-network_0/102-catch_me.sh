#!/bin/bash
# Bash script makes request that causes server to respond with  message int the body
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me_2 -H "Origin:School"
