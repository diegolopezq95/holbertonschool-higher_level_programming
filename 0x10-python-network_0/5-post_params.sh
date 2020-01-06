#!/bin/bash
# takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response
# A variable email must be sent with the value hr@holbertonschool.com
# A variable subject must be sent with the value I will always be here for PLD

curl -sX POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" $1
