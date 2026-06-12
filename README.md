# YouTube Channel Link Scraper

A robust Python automation script that uses Selenium to automatically scroll through any YouTube channel and extract all video, stream, and Shorts links. The scraper saves the extracted links live to a CSV file, ensuring no data is lost even if the process is interrupted.

## ✨ Features

- **Live Data Streaming:** Writes links to the CSV file in real-time (`flush()`), preventing data loss if the browser crashes or the script is manually stopped.
- **Infinite Scroll Handling:** Automatically scrolls to the very bottom of the channel page, including a smart retry mechanism to handle slow internet or lazy-loading delays.
- **Auto-URL Correction:** If you provide a base channel link, the script automatically appends `/videos` to ensure it lands on the correct page.
- **Clean Output:** Strips out messy tracking parameters (like `&t=` or `&pp=`) to give you clean, canonical YouTube URLs.
- **Deduplication:** Uses an internal memory set to ensure no duplicate links are ever saved to your CSV.

## 🛠️ Prerequisites

Before running this script, ensure you have the following installed on your system:
- **Python 3.7+**
- **Google Chrome Browser** (The script uses Chrome automatically)

## 📦 Installation

1. **Clone or download** this repository/script to your local machine.
2. **Open your terminal** and navigate to the folder containing the script.
3. **Install the required Python libraries** by running the following command:

```bash
pip install selenium webdriver-manager

```

*(Note: `webdriver-manager` automatically downloads the correct ChromeDriver for your system, saving you the hassle of manual browser driver updates!)*

## 🚀 How to Use

1. Run the script from your terminal:
```bash
python scraper.py

```


*(Replace `scraper.py` with whatever you named your Python file).*
2. The script will prompt you to enter a YouTube channel URL. You can enter formats like:
* `https://www.youtube.com/@ChannelName`
* `https://www.youtube.com/@ChannelName/shorts`
* `https://www.youtube.com/@ChannelName/streams`


3. A Chrome browser will launch automatically. **Do not close it.** The script will begin scrolling and printing the links it finds in your terminal.
4. Once it reaches the bottom of the channel, it will tell you how many links were extracted. Press `Enter` in your terminal to safely close the browser.

## 📄 Output

The script generates a file named **`youtube_links.csv`** in the same directory. It contains a single column with all the extracted URLs:

```csv
Video Link
[https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
[https://www.youtube.com/shorts/abcdefghijk](https://www.youtube.com/shorts/abcdefghijk)
...

```

## ⚠️ Disclaimer

This script is for educational and personal use. Web scraping is subject to YouTube's Terms of Service. Be mindful of how frequently you use automated tools to avoid having your IP address temporarily rate-limited by Google.

```

```
