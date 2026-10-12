Transport Layer Responsibilities:
 Tracks individual conversations to keep each application's data stream separate.
 Handles segmenting and reassembly by cutting data to fit network limits and rebuilding it at the destination.
 Adds header information including ports, sequence numbers, and checksums.
 Identifies applications using 16-bit port numbers to deliver data to the right process.
 Multiplexes segments from many conversations to share the same network link.


Port Ranges & Sockets:
 Ports range from 0 to 65535 across three main categories:
 0–1023: Well-known ports for standard server services (e.g., HTTP 80, HTTPS 443, DNS 53).
 1024–49151: Registered ports for vendor applications (e.g., MySQL 3306, RDP 3389).
 49152–65535: Dynamic or ephemeral ports used for random client-side source ports.


A socket is an IP address combined with a port number (e.g., `192.168.10.11:51544`).
A connection is uniquely identified by two sockets, allowing a single PC to open multiple browser tabs to the same server simultaneously.


TCP vs. UDP Comparison:
 TCP (Transmission Control Protocol):
  Connection-oriented (requires a three-way handshake).
  High reliability via acknowledgements and retransmissions.
  Uses sequence numbers to guarantee ordered delivery.
  Includes flow control via a sliding window mechanism.
  20-byte minimum header.
  Best for web traffic, email, file transfers, and SSH.


 UDP (User Datagram Protocol):
  Connectionless communication.
  No reliability; lost data stays lost.
  No ordering guarantees (segments may arrive out of order).
  No flow control.
  8-byte header.
  Best for DNS queries, VoIP, live video, gaming, and QUIC.


TCP Handshake and Teardown:
Three-way handshake:
 SYN: Client sends a synchronization packet (`seq=0`).
 SYN, ACK: Server replies with synchronization and acknowledgment (`seq=0, ack=1`).
 ACK: Client acknowledges the server (`seq=1, ack=1`) to establish the connection.


Connection close: Uses a four-way close with `FIN` and `ACK` flags.
Reset (`RST`): Immediately aborts a connection when a port is closed or rejected by a firewall.


Reliability, Windowing, and Congestion:
 Receivers acknowledge the next expected byte; senders retransmit if acknowledgements time out.
 Window size tells the sender how many bytes can be sent before waiting for an acknowledgement.
 MSS (Maximum Segment Size): The largest data block a host accepts in one segment (typically 1460 bytes on Ethernet).
 SACK (Selective Acknowledgement): Allows receivers to report exact missing byte ranges so only dropped segments are resent.
 Congestion avoidance: Senders automatically reduce transmission rates when packet loss occurs and gradually increase them again.


Application Layer Overview:
 TCP/IP merges the top three OSI layers (Application, Presentation, Session) into the application protocol itself.


Web Protocols (HTTP / HTTPS):
 Common HTTP methods include `GET` (read), `POST` (submit), `PUT` (replace), `PATCH` (modify), `DELETE` (remove), and `HEAD` (headers only).
 Status codes indicate response types: `2xx` (success), `3xx` (redirect), `4xx` (client error), and `5xx` (server error).
 HTTP is stateless; cookies carry state between requests.
 HTTPS runs HTTP inside TLS encryption on TCP port 443, providing confidentiality, integrity, and server authentication via certificates.
 HTTP/3 runs over QUIC, which utilizes UDP port 443.


Email Protocols:
 SMTP (TCP 25 / 587): Sends mail between servers (port 25) or handles client submissions (port 587).
 POP3 (TCP 110 / 995 with TLS): Downloads mail to a single device and deletes it from the server by default.
 IMAP (TCP 143 / 993 with TLS): Keeps mail stored on the server and synchronizes folders across multiple devices.


File Sharing Services:
 FTP (TCP 21 control, TCP 20 data): Uses two separate connections for commands and data, transmitting credentials in plain text.
 SFTP / FTPS: Secure alternatives to FTP (SFTP runs over SSH on port 22).
 TFTP (UDP 69): Trivial FTP with no authentication, used to transfer configuration files and IOS images to network devices.
 SMB (TCP 445): Server Message Block for Windows file and printer sharing, maintaining long-running sessions over network shares.


DHCP (Dynamic Host Configuration Protocol):
 Automates IP address leases, subnet masks, default gateways, and DNS servers using UDP ports 67 and 68.
 Follows the DORA process:
 Discover: Client broadcasts to find a server (`0.0.0.0` to `255.255.255.255`).
 Offer: Server offers an IP address and lease details.
 Request: Client broadcasts its acceptance of the chosen server's offer.
 ACK: Server confirms the lease.


Routers require an `ip helper-address <server-ip>` command to relay DHCP broadcasts across subnets.


DNS (Domain Name System):
 Translates human-readable domain names into IP addresses using UDP port 53 (TCP 53 for large responses and zone transfers).
 Queries flow hierarchically from stub resolvers to recursive resolvers, root servers, TLD servers (`.com`), and authoritative name servers.
 Answers are cached locally and at resolvers based on the record's TTL (Time to Live).
 Common record types include A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail server), NS (name server), and PTR (reverse lookup).