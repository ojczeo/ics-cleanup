# ICS Cleaner

When you export calendars from Outlook, macOS Calendar, callendars get polluted with unnecessary information, which will later prevent you from importing it successfully into other kind of calendar apps.

This script should help to remove unnecessary information, but be aware, that not every rule I've used will be suited for your needs, so double-check each rule and remove/comment those which you won't use! I'll try and help you by commenting every step/rule when it should be applied, and what it means and does.


## Usage
invoke this script like this:
`python3 ics-cleanup.py {filename}`

The script will create a backup first, before applying any changes! look for a `.backup` file if you need to go back.

### Thanks and remarks
based on `ics-cleaner` from https://github.com/metawave/ics-cleanup written by https://github.com/metawave
