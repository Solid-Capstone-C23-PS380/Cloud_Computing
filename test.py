import requests

# URL endpoint dari API Flask di Cloud Run
url = "https://wayang-predictions-l5wkf7uxfq-et.a.run.app/predict" 


image_path = "antaseneee.jpg"  


with open(image_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)


if response.status_code == 200:
    result = response.json()
    print(result["result"])
    print(result["image_url"])
    print("Sukses : ", response.text)

else:
    print("Terjadi kesalahan:", response.text)