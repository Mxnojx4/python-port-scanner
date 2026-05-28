# Python Port Scanner

An advanced multithreaded TCP port scanner built using Python.

## Features

- Fast multithreaded scanning
- Custom port ranges
- Banner grabbing
- Colored terminal output
- Scan result export
- Service detection

## Technologies Used

- Python
- socket
- concurrent.futures
- colorama

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py
```

## Example

```text
Enter target IP or domain: scanme.nmap.org
Enter start port: 1
Enter end port: 1000
```

## Output

```text
[OPEN] Port 22 | Service: OpenSSH
[OPEN] Port 80 | Service: Apache
```

## Future Improvements

- UDP scanning
- OS fingerprinting
- GUI version
- Vulnerability detection
- JSON export

## Disclaimer

Use only on systems you own or are authorized to test.