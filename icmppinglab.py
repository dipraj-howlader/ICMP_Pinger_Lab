from socket import *
import os
import sys
import struct
import time
import select


ICMP_ECHO_REQUEST = 8

def checksum(data):
    data = bytearray(data)
    csum = 0
    countTo = (len(data) // 2) * 2

    for count in range(0, countTo, 2):
        thisVal = data[count+1] * 256 + data[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff

    if countTo < len(data):
        csum = csum + data[-1]
        csum = csum & 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        icmpHeader = recPacket[20:28]
        icmpType, code, mychecksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
    
        if icmpType != 8 and packetID == ID:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            round_trip_time = (timeReceived - timeSent) * 1000  # in milliseconds
            return round_trip_time

        timeLeft = timeLeft - howLongInSelect
        
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID):
    myChecksum = 0
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    myChecksum = checksum(header + data)

    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr, 1))

def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp") 
    mySocket = socket(AF_INET, SOCK_RAW, icmp) 

    myID = os.getpid() & 0xFFFF
    sendOnePing(mySocket, destAddr, myID) 
    round_trip_time = receiveOnePing(mySocket, myID, timeout, destAddr)          

    mySocket.close()         
    return round_trip_time  

def ping(host, timeout=1):
    dest = gethostbyname(host)
    print(f"Pinging {host} [{dest}] with 32 bytes of data:")
    print("")

    sent = 0
    received = 0
    lost = 0
    total_time = 0
    min_time = float('inf')
    max_time = 0

    for _ in range(4):
        round_trip_time = doOnePing(dest, timeout)
        sent += 1

        if isinstance(round_trip_time, str):
            lost += 1
        else:
            received += 1
            total_time += round_trip_time
            min_time = min(min_time, round_trip_time)
            max_time = max(max_time, round_trip_time)

        print(f"Reply from {dest}: bytes=32 time={int(round_trip_time)}ms TTL=57")
        time.sleep(1)

    print("\nPing statistics for", dest)
    print(f"    Packets: Sent = {sent}, Received = {received}, Lost = {lost} ({int((lost/sent)*100)}% loss),")
    print("Approximate round trip times in milli-seconds:")
    print(f"    Minimum = {int(min_time)}ms, Maximum = {int(max_time)}ms, Average = {int((total_time/received))}ms")

user_input = input("Enter the IP address or domain to ping: ")
ping(user_input)
