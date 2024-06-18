import argparse
import subprocess
import os

def run_nmap(command, output_dir):
    try:
        subprocess.run(f"{command} -oN {output_dir}/output.txt", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def main():
    parser = argparse.ArgumentParser(description="Run Nmap scans")
    parser.add_argument("target", help="IP address or domain name to scan")
    parser.add_argument("-t", "--type", choices=["regular", "intensive", "full"], default="regular",
                        help="Specify the scan type (regular, intensive, or full)")
    args = parser.parse_args()

    output_dir = f"{args.target}_output"
    os.makedirs(output_dir, exist_ok=True)

    if args.type == "regular":
        run_nmap(f"sudo nmap -sS {args.target}", output_dir)
        run_nmap(f"sudo nmap -sT {args.target}", output_dir)
        run_nmap(f"nmap -sn {args.target}", output_dir)
    elif args.type == "intensive":
        run_nmap(f"sudo nmap -sS {args.target}", output_dir)
        run_nmap(f"sudo nmap -sT {args.target}", output_dir)
        run_nmap(f"sudo nmap -sU -sS {args.target}", output_dir)
        run_nmap(f"nmap -sn {args.target}", output_dir)
        run_nmap(f"nmap -v -sn {args.target} -oG {output_dir}/ping-sweep.txt", output_dir)
        run_nmap(f"grep open {output_dir}/web-sweep.txt | cut -d' ' -f2", output_dir)
        run_nmap(f"nmap -sT -A --top-ports=20 {args.target}", output_dir)
        run_nmap(f"sudo nmap -O {args.target} --osscan-guess", output_dir)
        run_nmap(f"nmap -sT -A {args.target}", output_dir)
        run_nmap(f"nmap --script http-headers {args.target}", output_dir)
        run_nmap(f"nmap --script-help http-headers", output_dir)
        run_nmap(f"nmap -v -p 139,445 {args.target}", output_dir)
        run_nmap(f"nmap -v -p 139,445 --script smb-os-discovery {args.target}", output_dir)
        run_nmap(f"sudo nmap -sU --open -p 161 {args.target}", output_dir)
    elif args.type == "full":
        run_nmap(f"sudo nmap -sS {args.target}", output_dir)
        run_nmap(f"sudo nmap -sT {args.target}", output_dir)
        run_nmap(f"sudo nmap -sU -sS {args.target}", output_dir)
        run_nmap(f"nmap -sn {args.target}", output_dir)
        run_nmap(f"nmap -v -sn {args.target} -oG {output_dir}/ping-sweep.txt", output_dir)
        run_nmap(f"grep open {output_dir}/web-sweep.txt | cut -d' ' -f2", output_dir)
        run_nmap(f"nmap -sT -A --top-ports=20 {args.target}", output_dir)
        run_nmap(f"sudo nmap -O {args.target} --osscan-guess", output_dir)
        run_nmap(f"nmap -sT -A {args.target}", output_dir)
        run_nmap(f"nmap --script http-headers {args.target}", output_dir)
        run_nmap(f"nmap --script-help http-headers", output_dir)
        run_nmap(f"nmap -v -p 139,445 {args.target}", output_dir)
        run_nmap(f"nmap -v -p 139,445 --script smb-os-discovery {args.target}", output_dir)
        run_nmap(f"sudo nmap -sU --open -p 161 {args.target}", output_dir)
    else:
        print("Invalid scan type. Please choose 'regular', 'intensive', or 'full'.")

if __name__ == "__main__":
    main()
