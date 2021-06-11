# Network monitoring tool
This network monitoring tool will periodically check the availability of given endpoints with given period. You should also specify number of maximum attempts.

## How to use:
You have to create your own input file with endpoints, period of time in seconds and number of maximum attempts.
File must be named "input.txt".
Format of file has to be like this:
* Number of seconds representing period of time on 1st line
* Number of maximum attempts on 2nd line
* Then specify endpoints as IPv4 addresses on each line 

If you want to see example how it should look like, look at "input.txt" in this repository.

After you have setuped your "input.txt" file, execute command ./network.py

When it ends, output file will contain on each line these information: 
* endpoint written as IPv4 address
* total number of attempts for that endpoint
* number of failed attempts
* number of successful attempts
* failure rate as decimal number
* timestamp of last attempt to ping that enpoint

You can see example "output.txt" file for given example "input.txt" file.
