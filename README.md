## builtwithsubs

Scrape builtwith relationships without cookie and api key.

## Installation
```
git clone https://github.com/rix4uni/builtwithsubs.git
cd builtwithsubs
python3 setup.py install
```

## pipx
Quick setup in isolated python environment using [pipx](https://pypa.github.io/pipx/)
```
pipx install --force git+https://github.com/rix4uni/builtwithsubs.git
```

## Usage
```
usage: builtwithsubs [-h] [--timeout TIMEOUT] [--silent] [--version]

Net Range scraping on whois.arin.net

options:
  -h, --help         show this help message and exit
  --timeout TIMEOUT  Timeout (in seconds) for http client (default 15)
  --silent           Run without printing the banner
  --version          Show current version of builtwithsubs
```

## Example usages

Single Domains:
```
echo "tesla.com" | builtwithsubs
```

Multiple Domains:
```
cat targets.txt
tesla.com
github.com
```

```
cat targets.txt | builtwithsubs
```
