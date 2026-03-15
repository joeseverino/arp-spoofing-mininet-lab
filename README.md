# ARP Spoofing Simulation and Mitigation Lab

This project demonstrates how ARP spoofing can be performed in a virtual network using Mininet and how enterprise networks mitigate the attack using technologies such as DHCP Snooping and Dynamic ARP Inspection.

The lab includes a custom Mininet topology, packet capture evidence analyzed in Wireshark, and a Cisco Packet Tracer environment demonstrating Layer-2 mitigation techniques.

---

## Full Write-Up

The full technical write-up for this project is available here:

https://jseverino.com/portfolio/simulating-arp-spoofing/

---

## Repository Contents

**topology.py**  
Custom Python script used to generate the Mininet topology for the ARP spoofing simulation.

**vulnerable.pcap**  
Packet capture showing ARP spoofing behavior and redirected traffic between hosts.

**arp_spoofing_mitigation_lab.pkt**  
Cisco Packet Tracer lab demonstrating enterprise mitigation using DHCP Snooping and Dynamic ARP Inspection.

**mininet_topology.png / mininet_topology.svg**  
Network topology diagrams used for the simulation.

---

## Technologies Used

- Mininet
- Open vSwitch
- POX Controller
- Wireshark
- Cisco Packet Tracer
- Python

---

## Notes

This project was developed while studying computer networking concepts and security implications related to ARP spoofing and Layer-2 network protections from the CCNA and Georgia Tech Cybersecurity graduate program.
