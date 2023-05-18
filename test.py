import requests

# URL endpoint dari API Flask di Cloud Run
url = "https://wayang-predict-gcloudrunn-l5wkf7uxfq-et.a.run.app/predict" 


image_path = "antaseneee.jpg"  


with open(image_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)


if response.status_code == 200:
    result = response.json()
    print(result['result'])
    print("Sukses : ", response.text)
    # print("Prediksi:", data["prediction"])
    # print("URL Gambar:", data["image_url"])
else:
    print("Terjadi kesalahan:", response.text)