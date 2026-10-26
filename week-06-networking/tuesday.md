Octet is a value holding from 0-255
Ipv4 has four
Binary to Decimal
Decimal to Binary

Subnetting is when a IP Address is divided into multiple address using a mask
Address 192.168.10.11
Subnet Mask: 255.255.255.0
Host bits are the left over zero’s from the subnet mask here it is 8

Calculating Host bits, 
Prefix 
32,26,24,16 are the number of bits in the address
/24 32-24 = 8 bits
/26 32-26 = 10 bits
/16 32-16 = 16 bits

2^h - 2 = Host bits

The - 2 is because there’s two important addresses in every address
Network Address: used as the identify to the network, example: 192,68.4.0
Broadcast Address: anything sent to this address will be sent to all the devices connected in the network

Router is the main device that subnets, from isp to the switches


Fragmenting, when the packets are split even further if the 
IPv4 Header Fields
Version: Set to 4 (0100).
Header Length (IHL): Size of the IPv4 header (typically 20 bytes).
Differentiated Services (DSCP/ECN): Sets QoS priority for traffic.
Total Length: Combined size of the header plus the payload data.
Identification / Flags / Offset: Manages packet fragmentation and reassembly.
Time to Live (TTL): Decrements by 1 at each router hop; drops the packet at 0 to prevent infinite loops.
Protocol: Identifies the inner payload protocol (1 = ICMP, 6 = TCP, 17 = UDP).
Header Checksum: Detects header corruption; recalculated at every router hop.
Source & Destination IPs: 32-bit endpoint addresses (unchanged end-to-end unless NAT intervenes).
IPv6 Header Fields
IPv6 replaces IPv4's variable structure with a streamlined, fixed 40-byte header (removing checksum and fragmentation fields).
Version: Set to 6 (0110).
Traffic Class: Handles QoS priority (replaces IPv4's DSCP field).
Flow Label: Marks specific packet streams for uniform router handling.
Payload Length: Size of data following the fixed 40-byte header.
Next Header: Specifies the protocol inside (TCP, UDP, ICMPv6) or an extension header.
Hop Limit: Decrements at each router hop (replaces IPv4 TTL).
Source & Destination IPs: Expanded 128-bit addresses (replacing IPv4's 32-bit addresses).
Host Routing Decisions
Before sending a packet, a host compares the destination IP address against its own IP and subnet mask to determine one of three paths:
Itself (Loopback): 127.0.0.1 (IPv4) or ::1 (IPv6). Traffic never leaves the host's internal network stack.
Local Host: Destination is on the same subnet. Traffic is sent directly to the destination's MAC address (discovered via ARP for IPv4 or Neighbor Discovery / ND for IPv6).
Remote Host: Destination is on a different subnet. Traffic is sent directly to the Default Gateway (the local router interface's MAC address) to be routed across networks.
A MAC address is a 48-bit layer 2 address burned into each network interface, written as 12 hex digits
First 24 bits: OUI, the manufacturer's identifier.
Last 24 bits: the interface's serial number assigned by that manufacturer.
FF:FF:FF:FF:FF:FF is the broadcast MAC. Addresses whose first octet is odd (lowest bit = 1) are multicast, such as 01:00:5E:… for IPv4 multicast.
How a switch learns, it marks a frame containing the source mac address and the destination mac address, into a table and removes if inactive for more than 5 minutes on a cisco switch
Switch Forwarding Methods
Store-and-Forward: Receives the entire frame and checks for errors (FCS) before forwarding. Drops bad frames, but adds slight latency. (Default on Cisco switches).
Cut-Through (Fast-Forward): Reads only the destination MAC address (first 6 bytes) and forwards immediately. Lowest latency, but forwards corrupted frames.
Cut-Through (Fragment-Free): Reads the first 64 bytes (where collisions happen) to filter out garbage frames while maintaining low latency.
Switch Memory Buffering
Port-Based Memory: Each port has its own queue. If one port gets congested, it backs up all traffic behind it.
Shared Memory: All ports share one common memory pool dynamically. Essential when connecting different port speeds (e.g., many 1 Gbps ports feeding into one 10 Gbps uplink).
Port Speeds, Duplex, & Auto-MDIX
Full-Duplex: Transmits and receives simultaneously (no collisions can occur).
Half-Duplex: Transmits OR receives one at a time (collisions can happen).
Duplex Mismatch: One side set to full-duplex and the other to half-duplex causes slow speeds, dropped packets, and CRC errors.
Auto-MDIX: Automatically detects if a straight-through or crossover cable is plugged in and adjusts the port pins accordingly.
ARP (Address Resolution Protocol)
When a host knows a destination's IP address but needs its physical MAC address to build an Ethernet frame:
ARP Request: Sent as a Broadcast (FF-FF-FF-FF-FF-FF) asking "Who has this IP?"
ARP Reply: The target device answers with a Unicast message stating "I have that IP, here is my MAC."
ARP Cache: The requesting host saves this IP-to-MAC pair in memory (arp -a) so it doesn't have to ask again.
Local vs. Remote Sending Decision
Before sending data, a host checks if the target IP is on its own subnet:
Same Subnet: The host uses ARP to find the destination device's MAC and sends the frame directly to it.
Different Subnet: The host uses ARP to find the Default Gateway's MAC (the local router) and hands the frame over to the router to deliver it.
Gratuitous ARP & Security
Gratuitous ARP: A host broadcasts its own IP-to-MAC mapping without being asked. Used to announce IP changes or handle failovers.
ARP Spoofing: An attacker sends fake Gratuitous ARPs to trick devices into sending traffic to the attacker's MAC address instead of the router. Switches block this using Dynamic ARP Inspection (DAI).
IPv6 Note: IPv6 completely replaces ARP with Neighbor Discovery (ND) protocol.

IPv6 Fundamentals & Compression
IPv6 uses 128-bit addresses (3.4 × 1038 total IPs) written as 8 hex groups (hextets) separated by colons. It eliminates NAT and drops broadcasts completely, using multicast instead.
Compression Rules (RFC 5952)
Drop leading zeros: 0db8  db8, 0000  0.
Use :: once: Replace the single longest consecutive run of all-zero hextets with ::.
Address Structure & Key Types
A Global Unicast address splits into: Global Prefix (48 bits) + Subnet ID (16 bits) + Interface ID (64 bits). Standard LANs always use /64.
Global Unicast (GUA) (2000::/3): Public, internet-routable IP (like IPv4 public).
Link-Local (LLA) (fe80::/10): Local-link only; used for gateways and neighbor discovery. Never routed.
Unique Local (ULA) (fc00::/7 / fd00::/8): Private internal address (IPv4 RFC 1918 equivalent).
Multicast (ff00::/8): ff02::1 (all nodes), ff02::2 (all routers).
Loopback (::1/128) / Unspecified (::/128).
How Hosts Get Addresses (NDP & Messages)
IPv6 uses ICMPv6 Neighbor Discovery Protocol (NDP) to replace ARP and enable auto-configuration:
Key NDP Messages
RS (Router Solicitation): Host asks "Are there routers here?" (sent to ff02::2).
RA (Router Advertisement): Router responds with the prefix, gateway, and autoconfig flags.
NS (Neighbor Solicitation): "What is the MAC for this IPv6 IP?" (replaces ARP request).
NA (Neighbor Advertisement): "Here is my MAC address." (replaces ARP reply).
ICMP (The Error Reporter)
Purpose: Reports packet errors and provides network diagnostics (carries no user data).
Key Messages:
Echo Request/Reply: Used by ping.
Destination Unreachable: Packet could not be delivered.
Time Exceeded: Packet expired (TTL hit 0); used by traceroute.
Ping (Reachability Test)
Function: Sends ICMP Echo Requests to verify if an IP address is reachable.
Cisco Symbols: ! = Success, . = Timeout, U = Unreachable, .!!!! = First packet lost while resolving ARP.
Extended Ping: Allows setting a specific Source IP to test if the remote target has a valid return route to your internal network.
Traceroute (Path Mapping)
Function: Maps every router hop to a destination by incrementing the TTL (1, 2, 3...)
How It Works: Each router along the path drops the packet when TTL hits 0 and returns an ICMP Time Exceeded message, revealing its IP address.
OS Differences: Windows uses ICMP Echo probes; Cisco/Linux use high-port UDP probes (target replies with ICMP Port Unreachable).
Key Output: * * * means a router timed out or a firewall blocked ICMP traffic.

