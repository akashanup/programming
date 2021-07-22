# Network packet processing simulation

You are given a series of incoming network packets, and your task is to simulate their processing.
Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴 𝑖 and the
time it takes the processor to process it 𝑃 𝑖 (both in milliseconds). There is only one processor, and it
processes the incoming packets in the order of their arrival. If the processor started to process some
packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of
packet 𝑖 takes exactly 𝑃 𝑖 milliseconds.

The computer processing the packets has a network buffer of fixed size 𝑆. When packets ar-
rive, they are stored in the buffer before being processed. However, if the buffer is full when a packet
arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished
processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the
same time, they are first all stored in the buffer (some of them may be dropped because of that —
those which are described later in the input). 

The computer processes the packets in the order of
their arrival, and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no packets in
the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer
and frees the space in the buffer as soon as the computer finishes processing it.

- Input Format. The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming
network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival
𝐴 𝑖 and the processing time 𝑃 𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the
sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in
milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).

- Output Format. For each packet output either the moment of time (in milliseconds) when the processor
began processing it or −1 if the packet was dropped (output the answers for the packets in the same
order as the packets are given in the input).
  
### Example 1
```sh
Input: size = 1, request = []
Output: None
Explanation: If there are no packets, you shouldn’t output anything.
```

### Example 2
```sh
Input: size = 1, request = [[0, 0]]
Output: 0
Explanation: The only packet arrived at time 0, and computer started processing it immediately.
```

### Example 3
```sh
Input: size = 1, request = [[0, 1], [0, 1]]
Output: 0
        -1
Explanation: The first packet arrived at time 0, the second packet also arrived at time 0, but was dropped, because
the network buffer has size 1 and it was full with the first packet already. The first packet started
processing at time 0, and the second packet was not processed at all.
```

### Example 4
```sh
Input: size = 1, request = [[0, 1], [1, 1]
Output: 0
        1
Explanation: The first packet arrived at time 0, the computer started processing it immediately and finished at time
1. The second packet arrived at time 1, and the computer started processing it immediately.
```

### Constraints
```sh
1 <= size <= 10^5; 
0 <= n <= 10^5 ; 
0 <= request[i][0] <= 10^6 ;
0 <= request[i][1] <= 10^3 ; 
request[i][0] <= request[i + 1][0] for 1 <= 𝑖 <= n - 1.
```
