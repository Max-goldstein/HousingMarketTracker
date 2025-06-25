import requests

def grab_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("data.csv", "wb") as file:
            file.write(response.content)
            print("File downloaded successfully!")
        with open("data.csv", "r") as file:
            data = file.read()
            print("Data from the file:")
            sample_lines = data.splitlines()[:5]
            for line in sample_lines:
                print(line)
    else:
        print("Failed to download the file.")
