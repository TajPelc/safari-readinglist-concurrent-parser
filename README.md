# Reading List Parser

The Reading List Parser is a Python script that extracts bookmarked URLs, status codes, titles, and preview texts from a Safari Bookmarks plist file, specifically targeting the Reading List section.

## Prerequisites

- Python 3.x
- `requests` library
- `plistlib` library

## Installation

1. Clone the repository or download the script file (`extract-readinglist.py`) to your local machine.

2. Install the required libraries by running the following command:

   ```
   pip install requests plistlib
   ```

## Usage

1. Locate the Safari Bookmarks plist file (`Bookmarks.plist`) on your macOS device. It is typically located in the following directory:

   ```
   ~/Library/Safari/Bookmarks.plist
   ```

2. Copy the `Bookmarks.plist` file to the same directory as the script (`extract-readinglist.py`).

3. Run the script by executing the following command:

   ```
   python3 extract-readinglist.py
   ```

4. The script will process the bookmarks and generate a CSV file named `readinglist.csv` in the same directory.

5. Open the `readinglist.csv` file to view the extracted data, including the URL, status code, title, and preview text of each bookmark in the Reading List.

## Notes

- The script assumes that the `Bookmarks.plist` file is in the correct format and follows the expected structure.
- In case of errors or issues during processing, the script will log an error message for the corresponding bookmark in the CSV file.
- Adjust the script or modify the output format as needed to match your requirements.

## License

This project is licensed under the MIT License
