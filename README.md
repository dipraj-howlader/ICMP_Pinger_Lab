Overview

The ICMP Pinger Lab project entails creating a robust ICMP ping application in Python. This application is designed to dispatch ICMP Echo Request messages (pings) to a designated remote host, enabling the measurement of round-trip times for each ping. The central objective is to enhance comprehension of ICMP and the measurement of network latency.

 Components:

1. ICMP Ping Client Functionality:
    - Initiates the transmission of ICMP Echo Request messages directed towards a specified remote host.
    - Captures and records the round-trip time for each individual ping.
    - Incorporates a timeout mechanism to effectively manage scenarios where the host remains unresponsive.

2. Optional ICMP Ping Server Capability:
    - Offers the possibility to deploy a basic ICMP server configured to intercept incoming Echo Request messages.
    - Generates appropriate Echo Replies in response to received requests.
    - Introduces randomized delays, if desired, to replicate network variations.

3. Statistical Analysis and Reporting:
    - Monitors and logs various statistics, including the average round-trip time, packet loss, and other pertinent metrics.
    - Presents a comprehensive summary of these statistics upon the conclusion of the entire ping session.

4. Graphical User Interface (Optional):
    - Implements a graphical user interface to visualize the ping statistics.
    - Enhances user experience and provides a graphical representation of network performance.

5. Round-Trip Time Calculation:

- Calculates and displays the round-trip time for each ping.
- Measures the time elapsed between sending a ping and receiving the corresponding reply.

 Additional Features:

1. Random Delays (Server):
    - Introduces random delays on the server side to simulate network latency.
    - Enhances the realism of the simulation, allowing users to experience varying network conditions.

2. Multithreading (Optional):
    - Implements multithreading to handle multiple ping sessions simultaneously.
    - Enhances the scalability of the application, enabling concurrent ping sessions.

 Requirements:

 Programming Language:

- Python is used for both the client and server implementations.

 ICMP Protocol:

- Utilizes the socket library for sending and receiving ICMP packets.

 Ping Client:

- Implements the client program to send ICMP Echo Request messages and measure round-trip times.

 Ping Server (Optional):

- Implements an optional server that responds to ICMP Echo Request messages.
- Optionally introduces random delays to simulate network latency.

 Round-Trip Time Calculation:

- Calculates and displays the round-trip time for each ping.

 Statistics Tracker:

- Computes and displays statistics such as average round-trip time, packet loss, and any additional relevant metrics.

 Graphical User Interface (Optional):

- Implements a graphical user interface to visualize the ping statistics.

Sample Output:

```
Pinging pstu.ac.bd [103.157.135.180] with 32 bytes of data:

Reply from 103.157.135.180: bytes=32 time=16ms TTL=57
Reply from 103.157.135.180: bytes=32 time=0ms TTL=57
Reply from 103.157.135.180: bytes=32 time=0ms TTL=57
Reply from 103.157.135.180: bytes=32 time=0ms TTL=57

Ping statistics for 103.157.135.180
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 16ms, Average = 4ms
```
Implementation:

The ICMP Pinger Lab was successfully implemented in Python, utilizing the socket library for ICMP packet handling. The ICMP ping client effectively sent Echo Request messages to the specified remote host and calculated the round-trip time for each ping. The statistics, including the minimum, maximum, and average round-trip times, were accurately computed and displayed at the end of the ping session.

Conclusion:

The ICMP Pinger Lab project provided valuable insights into the fundamentals of ICMP and network latency measurement. The implementation of the ICMP ping client successfully achieved the project goals, and the additional features, including random delays and a potential graphical interface, were considered for future enhancements. The project serves as a practical exercise in understanding and implementing network protocols using Python.
