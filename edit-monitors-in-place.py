# This script will download all monitors to a file and allow them to be edited in place before uploading them again.
# Any changes will be reflected in the DD control panel as updates to existing monitors.
# Does not delete existing monitors.

import json
from time import gmtime, strftime
from datadog import initialize
import yaml

options = {
    'api_key': 'foo',
    'app_key': 'bar'
}

initialize(**options)

# Use Datadog REST API client
from datadog import api

datadog_monitors = api.Monitor.get_all()

# print(json.dumps(datadog_monitors, indent=2, sort_keys=True))

print "Number of monitors: " + str(len(datadog_monitors))

with open('existing_monitors.json', 'w') as outfile:
    json.dump(datadog_monitors, outfile, indent=2, sort_keys=True)

wait = raw_input("Edit 'existing_monitors.json', then press a key to upload the changes.")

with open('existing_monitors.json', 'r') as infile:
    imported_datadog_monitors = json.load(infile)

# Update existing monitors
for monitor in imported_datadog_monitors:
    print "Uploading " + monitor['name']
    response = api.Monitor.update(**monitor)
