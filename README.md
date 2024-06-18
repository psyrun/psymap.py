# Understanding Nmap Commands for Network Scanning

Nmap (Network Mapper) is a powerful open-source tool used for network exploration and security auditing. It works by sending packets to target hosts and analyzing the responses to determine various aspects of the network, such as open ports, operating systems, and services running on the hosts.

In this blog post, we will explore various Nmap commands and how they can be used for network scanning.

## Regular Scan

Regular scans are the basic scans performed to gather information about a target network. They are generally non-intrusive and provide essential insights into the network topology.

- **TCP SYN Scan:** `sudo nmap -sS TARGET`
- **TCP Connect Scan:** `sudo nmap -sT TARGET`
- **Ping Scan:** `nmap -sn TARGET`

## Intensive Scan

Intensive scans are more thorough and may involve multiple scan techniques to gather detailed information about the target network.

- **TCP SYN Scan:** `sudo nmap -sS TARGET`
- **TCP Connect Scan:** `sudo nmap -sT TARGET`
- **UDP and TCP SYN Scan:** `sudo nmap -sU -sS TARGET`
- **Ping Sweep Scan:** `nmap -sn TARGET`
- **Verbose Ping Sweep Scan with Output to File:** `nmap -v -sn TARGET -oG ping-sweep.txt`
- **Extracting Open Ports from Ping Sweep Output:** `grep open web-sweep.txt | cut -d' ' -f2`
- **Top Port Sweep Scan:** `nmap -sT -A --top-ports=20 TARGET -oG top-port-sweep.txt`
- **Operating System Detection:** `sudo nmap -O TARGET --osscan-guess`
- **Aggressive Scan:** `nmap -sT -A TARGET`
- **HTTP Headers Script Scan:** `nmap --script http-headers TARGET`
- **HTTP Headers Script Help:** `nmap --script-help http-headers`
- **SMB Scan:** `nmap -v -p 139,445 -oG smb.txt TARGET`
- **SMB OS Discovery Scan:** `nmap -v -p 139,445 --script smb-os-discovery TARGET`
- **Open SNMP Scan:** `sudo nmap -sU --open -p 161 TARGET -oG open-snmp.txt`

## Full Scan

Full scans are comprehensive scans that leave no stone unturned in analyzing the target network's structure and services.

- **TCP SYN Scan:** `sudo nmap -sS TARGET`
- **TCP Connect Scan:** `sudo nmap -sT TARGET`
- **UDP and TCP SYN Scan:** `sudo nmap -sU -sS TARGET`
- **Ping Scan:** `nmap -sn TARGET`
- **Verbose Ping Sweep Scan:** `nmap -v -sn TARGET -oG ping-sweep.txt`
- **Extracting Open Ports from Ping Sweep Output:** `grep open sweet-sweep.txt | cut -d' ' -f2`
- **Top Port Sweep Scan:** `nmap -sT -A --top-ports=20 TARGET -oG top-port-sweep.txt`
- **Operating System Detection:** `sudo nmap -O TARGET --osscan-guess`
- **Aggressive Scan:** `nmap -sT -A TARGET`
- **HTTP Headers Script Scan:** `nmap --script http-headers TARGET`
- **HTTP Headers Script Help:** `nmap --script-help http-headers`
- **SMB Scan:** `nmap -v -p 139,445 -oG smb.txt TARGET`
- **SMB OS Discovery Scan:** `nmap -v -p 139,445 --script smb-os-discovery TARGET`
- **Open SNMP Scan:** `sudo nmap -sU --open -p 161 TARGET -oG open-snmp.txt`


## Usage
```sh
python nmap_scan.py 192.168.50.149 -t regular
python nmap_scan.py 192.168.50.149 -t intensive
python nmap_scan.py 192.168.50.149 -t full
```


We have covered a range of Nmap commands for different types of network scans. Each command serves a specific purpose and can be used to gather valuable information about the target network.


