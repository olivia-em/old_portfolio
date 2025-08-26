#!/usr/bin/env python3
import csv
import requests
import pathlib
import time
from urllib.parse import urlparse, unquote
import re

def sanitize_filename(filename):
    """Replace invalid characters in filename"""
    # Replace invalid characters with underscores
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Replace URL encoded spaces and other characters
    filename = unquote(filename)
    return filename

def download_file(url, output_dir):
    """Download a file from URL to output directory"""
    try:
        # Parse the URL to get filename
        parsed = urlparse(url)
        filename = pathlib.Path(parsed.path).name
        
        if not filename:
            print(f"❌ No filename in URL: {url}")
            return False
            
        # Sanitize filename
        filename = sanitize_filename(filename)
        output_path = output_dir / filename
        
        # Skip if file already exists
        if output_path.exists():
            print(f"📁 Already exists: {filename}")
            return True
            
        # Download with headers to mimic browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"⬇️  Downloading: {filename}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Write file
        with open(output_path, 'wb') as f:
            f.write(response.content)
            
        print(f"✅ Downloaded: {filename} ({len(response.content)} bytes)")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download {url}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error processing {url}: {e}")
        return False

def main():
    # Read the CSV file (assuming it's named download_log.csv)
    log_file = pathlib.Path("download_log.csv")  # Update this path
    output_dir = pathlib.Path("assets")  # Update this path
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    if not log_file.exists():
        print("❌ CSV log file not found. Please update the log_file path.")
        return
    
    failed_urls = []
    
    # Parse the CSV and collect failed URLs
    with open(log_file, 'r') as f:
        # Read raw lines and parse manually due to URL format issues
        lines = f.readlines()[1:]  # Skip header
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Split by comma, but the URL might span multiple fields
            parts = line.split(',')
            if len(parts) < 3:
                continue
                
            status = parts[0]
            reason = parts[1]
            
            # Reconstruct URL from remaining parts
            url_parts = parts[2:]
            url = ','.join(url_parts).strip()
            
            # Skip successful downloads and missing URLs
            if status == 'downloaded' or reason == 'missing_url' or not url:
                continue
            
            # Fix malformed URLs (replace comma with colon after protocol)
            if url.startswith('https,//'):
                url = url.replace('https,//', 'https://')
            elif url.startswith('http,//'):
                url = url.replace('http,//', 'http://')
                
            failed_urls.append((url, reason))
    
    print(f"Found {len(failed_urls)} failed downloads to retry")
    
    # Retry downloads with delays
    successful = 0
    for i, (url, reason) in enumerate(failed_urls, 1):
        print(f"\n[{i}/{len(failed_urls)}] Retrying: {reason}")
        
        if download_file(url, output_dir):
            successful += 1
        
        # Add delay between requests to be respectful
        if i < len(failed_urls):
            time.sleep(2)
    
    print(f"\n🎉 Successfully downloaded {successful}/{len(failed_urls)} files")
    print(f"📁 Files saved to: {output_dir.absolute()}")

if __name__ == "__main__":
    main()
