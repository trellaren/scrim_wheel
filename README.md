# scrim_wheel

CLI automation for Popflash 10-mans that helps roll players out between matches.

## Requirements

- Python 3.9+
- Firefox + geckodriver (used by Selenium)

## Install

```bash
pip install -e .
```

## Usage

Roll out players from your latest match (`fragworks` is the Popflash scrim name):

```bash
spin spin fragworks --spins 2
```

(`spin` is the CLI executable name, and `spin` is its subcommand.)

Useful options:

- `--drop <name>` (repeatable): remove specific player(s) from the roll list
- `--wheel`: populate Wheel of Names instead of selecting in CLI
- `--matchurl <url>`: manually provide a match URL instead of auto-detecting latest match
