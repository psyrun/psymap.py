import argparse
import subprocess

def run_nmap(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def main():
    parser = argparse.ArgumentParser(description="Run Nmap scans")
    parser.add_argument("target", help="IP address or domain name to scan")
    parser.add_argument("-t", "--type", choices=["regular", "intensive", "full"], default="regular",
                        help="Specify the scan type (regular, intensive, or full)")
    args = parser.parse_args()

    if args.type == "regular":
        run_nmap(f"sudo nmap -sS {args.target}")
        run_nmap(f"sudo nmap -sT {args.target}")
        run_nmap(f"nmap -sn {args.target}")
    elif args.type == "intensive":
        run_nmap(f"sudo nmap -sS {args.target}")
        run_nmap(f"sudo nmap -sT {args.target}")
        run_nmap(f"sudo nmap -sU -sS {args.target}")
        run_nmap(f"nmap -sn {args.target}")
        run_nmap(f"nmap -v -sn {args.target} -oG ping-sweep.txt")
        run_nmap(f"grep open web-sweep.txt | cut -d' ' -f2")
        run_nmap(f"nmap -sT -A --top-ports=20 {args.target} -oG top-port-sweep.txt")
        run_nmap(f"sudo nmap -O {args.target} --osscan-guess")
        run_nmap(f"nmap -sT -A {args.target}")
        run_nmap(f"nmap --script http-headers {args.target}")
        run_nmap(f"nmap --script-help http-headers")
        run_nmap(f"nmap -v -p 139,445 -oG smb.txt {args.target}")
        run_nmap(f"nmap -v -p 139,445 --script smb-os-discovery {args.target}")
        run_nmap(f"sudo nmap -sU --open -p 161 {args.target} -oG open-snmp.txt")
    elif args.type == "full":
        run_nmap(f"sudo nmap -sS {args.target}")
        run_nmap(f"sudo nmap -sT {args.target}")
        run_nmap(f"sudo nmap -sU -sS {args.target}")
        run_nmap(f"nmap -sn {args.target}")
        run_nmap(f"nmap -v -sn {args.target} -oG ping-sweep.txt")
        run_nmap(f"grep open web-sweep.txt | cut -d' ' -f2")
        run_nmap(f"nmap -sT -A --top-ports=20 {args.target} -oG top-port-sweep.txt")
        run_nmap(f"sudo nmap -O {args.target} --osscan-guess")
        run_nmap(f"nmap -sT -A {args.target}")
        run_nmap(f"nmap --script http-headers {args.target}")
        run_nmap(f"nmap --script-help http-headers")
        run_nmap(f"nmap -v -p 139,445 -oG smb.txt {args.target}")
        run_nmap(f"nmap -v -p 139,445 --script smb-os-discovery {args.target}")
        run_nmap(f"sudo nmap -sU --open -p 161 {args.target} -oG open-snmp.txt")
    else:
        print("Invalid scan type. Please choose 'regular', 'intensive', or 'full'.")

if __name__ == "__main__":
    main()
