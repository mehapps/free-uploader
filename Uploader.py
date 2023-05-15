import requests, threading, sys

if len(sys.argv) != 3:
    print("Please run the program like so:")
    print(sys.argv)
    print("python3 Uploader.py FileName.extension /Location/Of/File/")
    exit()

name = sys.argv[1]
path = sys.argv[2]
if path.endswith("/") == False:
    path += "/"

url_list = [
    "anonfiles.com/",
    "bayfiles.com/",
    "filechan.org/",
    "hotfile.io/",
    "letsupload.cc/",
    "lolabits.se/",
    "megaupload.nz/",
    "myfile.is/",
    "openload.cc/",
    "rapidshare.nu/",
    "share-online.is/",
    "upvid.cc/",
    "vshare.is/",
    "zippysha.re/"
]

def upload_file(url):
    file_dict = {
        "file": (name, open(path + name, "rb")),
    }
    response = requests.post("https://api." + url + "upload", files=file_dict)
    if response.status_code != 200:
        print(url + " failed! Trying again:")
    else:
        data = response.json()
        print(data["data"]["file"]["url"]["short"])

threads = []
for url in url_list:
    thread = threading.Thread(target=upload_file, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()