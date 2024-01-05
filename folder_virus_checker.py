import os
import time
import requests
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
VIRUSTOTAL_API_KEY = "Your API-key of Virustotal"
RESPONSE_FOLDER = "/Virustotal" #you have to create this folder
FOLDERS_TO_MONITOR = ["folder1", "folder2"]
class MyHandler(FileSystemEventHandler):
        def on_created(self, event):
                if event.is_directory:
                         return
                new_file = event.src_path
                if new_file.endswith(".tmp"):
                   return
                print(f"New file detected: {new_file}")
                if os.path.isfile(new_file):
                        print(f"Enviando archivo a VirusTotal: {new_file}")
                        files = {'file': (new_file, open(new_file, 'rb'))}
                        params = {'apikey': VIRUSTOTAL_API_KEY}
                        response = requests.post("https://www.virustotal.com/vtapi/v2/file/scan", files=files, params=params)
                        json_response = response.json()
                        print(f"Response of VirusTotal: {json_response}")
                        #URL Response
                        url = json_response.get('permalink', '')
                        print(f"URL VirusTotal: {url}")
                        current_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M")
                        source_folder = os.path.dirname(new_file)
                        filename = f"{current_datetime}_{source_folder.replace('/', '_')}-url.txt"
                        #Saving in the folder Virustotal
                        with open(os.path.join(RESPONSE_FOLDER, filename), 'w') as url_file:
                                url_file.write(url)
                else: print(f"File not exists: {new_file}")

if __name__ == "__main__": #Execution loop
        observer = Observer()
        event_handler = MyHandler()
        for folder in FOLDERS_TO_MONITOR:
                observer.schedule(event_handler, folder, recursive=False)
        observer.start()
        try:
                while True: time.sleep(1)
        except KeyboardInterrupt:
                observer.stop()
        observer.join()