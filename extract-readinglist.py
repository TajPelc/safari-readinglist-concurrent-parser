#!/usr/bin/env python3

import csv
import os
import plistlib
import requests
import concurrent.futures

# Specify the local file path for 'Bookmarks.plist'
INPUT_FILE = 'Bookmarks.plist'
OUTPUT_FILE = 'readinglist.csv'
CONCURRENCY = 10

# Load and parse the Bookmarks file
with open(INPUT_FILE, 'rb') as plist_file:
    plist = plistlib.load(plist_file)

# Look for the child node which contains the Reading List data.
# There should only be one Reading List item
children = plist['Children']
for child in children:
    if child.get('Title', None) == 'com.apple.ReadingList':
        reading_list = child

# Extract the bookmarks
bookmarks = reading_list['Children']
total_bookmarks = len(bookmarks)

# Open the output file in write mode with CSV writer
with open(OUTPUT_FILE, 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    # Write CSV header
    writer.writerow(['URL', 'Status Code', 'Title', 'Preview Text'])

    def process_bookmark(bookmark, index):
        url = bookmark['URLString']
        try:
            text = bookmark['ReadingList']['PreviewText']
        except KeyError:
            text = ""
        title = bookmark['URIDictionary']['title']
        try:
            ret = requests.head(url, timeout=5)  # Add timeout of 5 seconds
            writer.writerow([url, ret.status_code, title, text])
        except requests.exceptions.RequestException:
            writer.writerow([url, 'Error', title, text])

        # Print progress
        print(f"Processed item {index+1}/{total_bookmarks}: {url}")

    # Create thread pool executor with specified concurrency
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        # Submit each bookmark to the executor
        futures = [executor.submit(process_bookmark, bookmark, i) for i, bookmark in enumerate(bookmarks)]

        # Wait for all futures to complete
        concurrent.futures.wait(futures)

print(f"Output saved to {OUTPUT_FILE}")

