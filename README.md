# Aenum.py - Bulk enum4linux Scanner

Aenum.py is a Python script that reads a list of IP addresses from a file, runs the enum4linux tool on each IP address with customizable flags, and saves the output to separate files named after the IP address followed by "enum4linux-scan.txt".

## Usage

1. Ensure you have the `enum4linux` tool installed on your system.

2. Clone or download this repository.

3. Open a terminal and navigate to the directory where `Aenum.py` is located.

4. Run the script with the following command to display usage instructions:

`python Aenum.py --help`

5. Run the script with the following command to perform the scans:

`python Aenum.py [path] [threads] [enum_flags]`
- path: Path to the file containing IP addresses, separated by newlines.
- threads: The number of threads you want to use for concurrent scanning.
- enum_flags: Additional flags to pass to `enum4linux`.

6. The script will perform enum4linux scans on each IP address and save the output to individual files.

## Example

To scan a list of IP addresses in the `ips.txt` file using 5 threads and the `-U` flag:

`python Aenum.py ips.txt 5 -U`


## Notes

- This script assumes that `enum4linux` is installed and accessible in your system's PATH.
- It's important to use this script responsibly and only on networks you have permission to scan.

## License

This project is licensed under the MIT License. See the license file for details.

---

*This script is provided as-is and is not affiliated with the official enum4linux project.*
