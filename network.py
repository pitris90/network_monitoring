import platform
import subprocess
from datetime import datetime
import time


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def parse_input():
    """
    Returns tuple of array of endpoints, period of time in seconds, count of
    attempts that can be run maximally.
    """
    endpoints_file = open("input.txt", "r")
    lines = endpoints_file.readlines()
    line_number = 0
    endpoints = []
    for line in lines:
        line = line.strip()
        if line_number == 0:
            period = int(line)
        elif line_number == 1:
            max_attempts = int(line)
        else:
            endpoints.append(line)
        line_number += 1
    endpoints_file.close()
    return endpoints, period, max_attempts


def timed_pings(endpoints, period, max_attempts):
    """
    Create 'output.txt' file and initializes it.
    """
    output = open("output.txt", "w")
    lines = []
    for endpoint in endpoints:
        lines.append(endpoint + " 0 0 -\n")
    output.writelines(lines)
    output.close()

    """
    Start timed loop that repeats periodically by <<period>> amount of 
    time until <<attempts_count>> reaches <<max_attempts>> (included) .
    """
    start = time.time()
    attempts_count = 0
    while attempts_count <= max_attempts:
        elapsed = time.time() - start
        if elapsed >= period:
            attempts_count += 1
            for i in range(len(endpoints)):
                with open("output.txt", "r") as output:
                    lines = output.readlines()
                lines[i] = lines[i].split()
                success = ping(endpoints[i])
                lines[i][1] = str(int(lines[i][1]) + 1)
                if not success:
                    lines[i][2] = str(int(lines[i][2]) + 1)
                lines[i][3] = str(datetime.fromtimestamp
                                  (datetime.timestamp(datetime.now())))
                lines[i] = lines[i][0] + " " + lines[i][1] + " " + \
                           lines[i][2] + " " + lines[i][3] + "\n"
                with open("output.txt", "w") as output:
                    output.writelines(lines)
            start = time.time()


def main():
    parsed = parse_input()
    timed_pings(parsed[0], parsed[1], parsed[2])


if __name__ == '__main__':
    main()
