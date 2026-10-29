# Computer Networks Laboratory

This collection contains Cisco Packet Tracer (`.pkt`) simulations for the Computer Networks Laboratory. The four labs cover LAN communication through hubs and switches, router interface setup, DHCP service and relay across subnets, and static and default routing.

## Student Profile

| Detail | Information |
|---|---|
| **Name** | Shashank S |
| **USN** | 1BM24CS266 |
| **Section** | J |
| **Email** | [shashanks.cs24@bmsce.ac.in](mailto:shashanks.cs24@bmsce.ac.in) |
| **Institution** | B.M.S. College of Engineering (BMSCE) |

## Lab Index

| Lab | Project file | Focus and expected results |
|---|---|---|
| **1** | [`1BM24CS266-1.pkt`](1BM24CS266-1.pkt) | **Hub and Switch Communication** — Compare how a hub broadcasts frames and how a switch forwards unicast traffic. Use ICMP ping and observe the network segments. |
| **2** | [`1BM24CS266-2.pkt`](1BM24CS266-2.pkt) | **Router Interfaces and Connectivity** — Assign IPv4 addresses and masks to router Ethernet interfaces. Test communication between subnets and observe successful replies, timeouts, and destination-unreachable messages. |
| **3** | [`1BM24CS266-3.pkt`](1BM24CS266-3.pkt) | **DHCP Across Subnets** — Configure a central DHCP server with pools for local and remote LANs. Use `ip helper-address` on the router to relay DHCP requests between networks. |
| **4** | [`1BM24CS266-4.pkt`](1BM24CS266-4.pkt) | **Static and Default Routing** — Add static routes on the central router and default routes on the edge routers. Inspect route tables and confirm end-to-end communication across multiple hops. |

## Requirements

- **Software:** [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer), version 8.0 or newer recommended
- **Protocols and concepts:** ICMP, ARP, IPv4, DHCP, RIP, and static routing

## Running and Checking the Projects

1. Open the appropriate `.pkt` file in Cisco Packet Tracer.
2. Allow link indicators to settle from amber/orange to green while the network converges.
3. For Labs 1–3, select a PC and open **Desktop → Command Prompt**. Test a destination with:

   ```text
   ping <target-ip-address>
   ```

4. For the DHCP lab, open **Desktop → IP Configuration** on a client, select **DHCP**, and confirm that an IP address, subnet mask, and default gateway are assigned.
5. For Lab 4, open a router's **CLI** and inspect its routing table:

   ```text
   Router> enable
   Router# show ip route
   ```

   Look for `S` entries for static routes and `S*` for a candidate default route, then ping between the edge LANs.

## Learning Outcomes

- Compare collision domains and broadcast behavior when using hubs and switches.
- Configure IPv4 addresses, subnet masks, and default gateways.
- Understand DHCP address assignment and relay across router boundaries.
- Read and manage routing tables using static and default routes.
