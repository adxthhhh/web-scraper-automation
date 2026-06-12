import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_and_save_live(channel_url, output_filename="youtube_links.csv"):
    # Clean up the URL input
    channel_url = channel_url.strip()
    # If the user didn't specify a tab, default to /videos
    if not any(tab in channel_url for tab in ["/videos", "/streams", "/shorts", "/playlists"]):
        if channel_url.endswith("/"):
            channel_url = channel_url + "videos"
        else:
            channel_url = channel_url + "/videos"

    print(f"\n[INFO] Target URL configured to: {channel_url}")

    options = webdriver.ChromeOptions()
    # Optional: adds a user-agent to look more like a real browser
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(channel_url)
        
        # Explicitly wait up to 10 seconds for the first video elements to load
        print("[INFO] Waiting for page elements to render...")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/watch?v=') or contains(@href, '/shorts/')]"))
            )
        except Exception:
            print("[WARNING] Timed out waiting for links. The tab might be empty or a popup is blocking it.")

        # Open CSV file to stream entries live
        with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Video Link"]) 
            
            seen_links = set()
            scroll_pause_time = 2.5
            
            # Get initial scroll height
            last_height = driver.execute_script("return document.documentElement.scrollHeight")

            print(f"\nScraping started... Saving links directly to '{output_filename}'")
            print("-" * 60)

            while True:
                # Target any valid YouTube video or short link anchor tag
                video_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/watch?v=') or contains(@href, '/shorts/')]")
                
                new_links_found_this_loop = 0
                for elem in video_elements:
                    try:
                        link = elem.get_attribute('href')
                        if link:
                            # Clean up tracking parameters from the URL if present
                            clean_link = link.split('&')[0].split('?t=')[0]
                            
                            if clean_link not in seen_links:
                                seen_links.add(clean_link)
                                writer.writerow([clean_link])
                                file.flush() # Instantly write to your hard drive
                                print(f"[STORED]: {clean_link}")
                                new_links_found_this_loop += 1
                    except Exception:
                        continue # Skip stale elements dynamically modified by YouTube

                # Scroll down
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(scroll_pause_time)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.documentElement.scrollHeight")
                
                # If heights match, give it one extra scroll buffer attempt just in case it's a slow load
                if new_height == last_height:
                    time.sleep(2)
                    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                    new_height = driver.execute_script("return document.documentElement.scrollHeight")
                    if new_height == last_height:
                        break # Truly reached the end of the page
                        
                last_height = new_height

            print("-" * 60)
            print(f"Done! Successfully saved {len(seen_links)} unique links to {output_filename}.")
            
        input("\nPress Enter in this terminal to close the Chrome window...")

    finally:
        driver.quit()

if __name__ == "__main__":
    target_channel = input("Enter the link of the channel to scrape video links: ")
    scrape_and_save_live(target_channel)
