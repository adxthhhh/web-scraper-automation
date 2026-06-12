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
