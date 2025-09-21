#!/usr/bin/env python3
import sys
import os
import re
import shutil
from datetime import datetime

def clean_ics(filename):
    # Read file content
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply regex transformations
    patterns = [
        r"^X-.*$",                               # Remove X-Tokens
        r"^PRODID:.*$",                          # Remove Product ID
        r"BEGIN:VTIMEZONE(.|\n)*?END:VTIMEZONE", # Remove Timezone block
        r"^UID:.*$",                             # Remove UIDs
        r"^SEQUENCE:.*$",                        # Remove SEQUENCE
        r"^DTSTAMP:.*$",                         # Remove DTSTAMP
        r"^CREATED:.*$",                         # Remove CREATED
        r"^TRANSP:.*$",                          # Remove TRANSP
        r"^CONFERENCE;.*$",                      # Remove CONFERENCE links
        # Uncomment to remove alarms:
        # r"BEGIN:VALARM(.|\n)*?END:VALARM",
    ]

    for pat in patterns:
        content = re.sub(pat, "", content, flags=re.MULTILINE)

    # Remove empty lines
    content = re.sub(r"^\s*$\n", "", content, flags=re.MULTILINE)

    # Write back cleaned content
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if len(sys.argv) < 2:
        print("No argument supplied")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        sys.exit(1)

    # Create backup
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S%f")
    backup_name = f"{filename}.{timestamp}.backup"
    shutil.copy(filename, backup_name)
    print(f"Backup created: {backup_name}")

    # Clean file
    clean_ics(filename)
    print(f"File cleaned: {filename}")


if __name__ == "__main__":
    main()
