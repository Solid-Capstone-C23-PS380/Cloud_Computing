# Cloud_Computing
<p align="center">
  <img src="Images/architecture.png" width="580" title="cloudachitecture">
</p>
<p align="center"><b>Cloud Architecture</b></p>

1. The first firebase authentification flow to login or register, then the user can choose what to do.

2. The second option is prediction which is deployed on the cloud run and container registry using docker to store the packages needed for the prediction backend.

3. The third option is the backend for the profile and user data just like the first backend, using cloud run to deploy the backend and container registry using docker to store the packages needed to upload pictures to the profile.

    * Buy Puppet Tickets
    * Upload Profile Photo
    * View Profile/data

## API Docoumentation
- Using python as programming language
- Using Flask as backend
- Using Firebase Auth for authentication
- Using Cloud Storage for storage
- Using Cloud Firestore for database (NO SQL)
- Using Cloud run for deployment
- Using docker for containerization
- Using Postman for testing API

### Wayang Prediction API
#### Endpoint:
> https://wayang-prediction-mrlpwmp4cq-et.a.run.app

### Predict:
* URL
    - /predict
* Method
    - POST
* Request Body
    * `file` as file, must be valid image file (png, jpg, jpeg), max size <= 2MB
* Response
    > 200 OK
    ```json
    {
        "id": 3,
        "message": "success",
        "result": "Bagong"
    }
    ```
![](Images/prediction.jpg)

### Wayang Details or All API
#### Endpoint:
> https://wayang-backend-mrlpwmp4cq-et.a.run.app

### Lists:
* URL
    - /wayanglist
* Method
    - POST
* Request Body
    * -
* Response
    > 200 OK
    ```json
    [
        {
            "description": "Abimanyu adalah seorang tokoh dalam wiracarita Mahabharata. Ia adalah putra Arjuna dan Subadra. Dalam wiracarita Mahabharata, ditetapkan bahwa Abimanyulah yang akan meneruskan Yudistira sebagai pewaris takhta. Riwayatnya dituturkan sebagai pahlawan yang tragis. Ia gugur dalam pertempuran besar di Kurukshetra sebagai salah satu kesatria termuda dari pihak Pandawa, karena baru berusia enam belas tahun. Abimanyu menikah dengan Utari, putri Raja Wirata dan memiliki seorang putra bernama Parikesit, yang lahir tak lama setelah ia gugur. Menurut mitologi Hindu, Abimanyu adalah inkarnasi Warcasa, putra Dewa bulan. Ia membuat perjanjian bahwa putranya tinggal di Bumi hanya selama 16 tahun, sebagaimana ia tak dapat menahan perpisahan dengan putranya. Abimanyu berusia 16 tahun saat ia terbunuh dalam pertempuran",
            "id": 1,
            "name": "Abimanyu",
            "photo_url": [
                "https://storage.googleapis.com/wayang-storage/pic/Abimanyu/wayang1.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Abimanyu/wayang2.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Abimanyu/wayang3.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Abimanyu/wayang4.jpg"
            ]
        },
        {
            "description": "Anantasena, atau sering disingkat Antasena adalah nama salah satu tokoh pewayangan Jawa. Tokoh ini merupakan ciptaan para pujangga Jawa yang disisipkan ke dalam kisah Mahabharata, suatu wiracarita kuno karya Krishna Dwaipayana Byasa dari India, yang sering diadaptasi menjadi cerita pewayangan. Nama Anantasena maupun Antasena tidak ditemukan dalam naskah asli Mahabharata berbahasa Sanskerta (diterjemahkan oleh Kisari Mohan Ganguli). Dalam pewayangan, tokoh ini dikenal sebagai putra bungsu Bimasena, serta saudara lain ibu dari Antareja dan Gatotkaca. Dalam pewayangan klasik versi Surakarta, Antasena merupakan nama lain dari Antareja, yaitu putra sulung Bimasena. Sementara menurut versi Yogyakarta, Antasena dan Antareja adalah dua orang tokoh yang berbeda. Akan tetapi dalam pewayangan zaman sekarang, para dalang Surakarta sudah biasa memisahkan tokoh Antasena dengan Antareja, sebagaimana yang dilakukan oleh para dalang Yogyakarta.",
            "id": 2,
            "name": "Antasena",
            "photo_url": [
                "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang1.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang2.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang3.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang4.jpg"
            ]
        },
        {
            "description": "Ki Lurah Bagong adalah nama salah satu tokoh punakawan dalam kisah pewayangan yang berkembang di Jawa Tengah, Yogyakarta, dan Jawa Timur. Tokoh ini dikisahkan sebagai anak dari Semar. Dalam pewayangan Sunda juga terdapat tokoh panakawan yang identik dengan Bagong, yaitu Cepot atau Astrajingga. Namun bedanya, menurut versi ini, Cepot adalah anak tertua Semar. Dalam wayang banyumasan Bagong lebih dikenal dengan sebutan Bawor. Sebagai seorang panakawan yang sifatnya menghibur penonton wayang, tokoh Bagong pun dilukiskan dengan ciri-ciri fisik yang mengundang kelucuan. Tubuhnya bulat, matanya lebar, bibirnya tebal dan terkesan memble. Dalam figur wayang kulit, Bagong membawa senjata kudi. Gaya bicara Bagong terkesan semaunya sendiri. Dibandingkan dengan ketiga panakawan lainnya, yaitu Semar, Gareng, dan Petruk, maka Bagong adalah sosok yang paling lugu dan kurang mengerti tata krama. Meskipun demikian majikannya tetap bisa memaklumi.",
            "id": 3,
            "name": "Bagong",
            "photo_url": [
                "https://storage.googleapis.com/wayang-storage/pic/Bagong/wayang1.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Bagong/wayang2.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Bagong/wayang3.jpg",
                "https://storage.googleapis.com/wayang-storage/pic/Bagong/wayang4.jpg"
            ]
        }
    ]
    ```
![](Images/listallwayang.jpg)

### Details of Wayang:
* URL
    - /wayang
* Method
    - POST
* Request Body
    * `field_id` as integer, must be valid id
* Response
    > 200 OK
    ```json
    {
        "description": "Anantasena, atau sering disingkat Antasena adalah nama salah satu tokoh pewayangan Jawa. Tokoh ini merupakan ciptaan para pujangga Jawa yang disisipkan ke dalam kisah Mahabharata, suatu wiracarita kuno karya Krishna Dwaipayana Byasa dari India, yang sering diadaptasi menjadi cerita pewayangan. Nama Anantasena maupun Antasena tidak ditemukan dalam naskah asli Mahabharata berbahasa Sanskerta (diterjemahkan oleh Kisari Mohan Ganguli). Dalam pewayangan, tokoh ini dikenal sebagai putra bungsu Bimasena, serta saudara lain ibu dari Antareja dan Gatotkaca. Dalam pewayangan klasik versi Surakarta, Antasena merupakan nama lain dari Antareja, yaitu putra sulung Bimasena. Sementara menurut versi Yogyakarta, Antasena dan Antareja adalah dua orang tokoh yang berbeda. Akan tetapi dalam pewayangan zaman sekarang, para dalang Surakarta sudah biasa memisahkan tokoh Antasena dengan Antareja, sebagaimana yang dilakukan oleh para dalang Yogyakarta.",
        "id": 2,
        "name": "Antasena",
        "photo_url": [
            "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang1.jpg",
            "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang2.jpg",
            "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang3.jpg",
            "https://storage.googleapis.com/wayang-storage/pic/Antasena/wayang4.jpg"
        ]
    }
    ```
![](Images/wayangdetails.jpg)

### List all of Video:
* URL
    - /videolist
* Method
    - POST
* Request Body
    * -
* Response
    > 200 OK
    ```json
    [
        {
            "id": 1,
            "name": "Wayang kulit nasehat Semar kepada anak cucunya",
            "photo_url": "https://storage.googleapis.com/wayang-storage/pic/ssvideo/video1.jpg",
            "video_duration": "3:30",
            "video_id": "sKMw4uQLOHk",
            "video_url": "https://youtu.be/sKMw4uQLOHk"
        },
        {
            "id": 2,
            "name": "Pitutur Semar tentang Kehidupan",
            "photo_url": "https://storage.googleapis.com/wayang-storage/pic/ssvideo/video2.jpg",
            "video_duration": "7:37",
            "video_id": "gQ9j_2PKdWE",
            "video_url": "https://youtu.be/gQ9j_2PKdWE"
        }
    ]
    ```
![](Images/listallvideo.jpg)

### Details of Video:
* URL
    - /video
* Method
    - POST
* Request Body
    * `field_id` as integer, must be valid id
* Response
    > 200 OK
    ```json
    {
        "id": 2,
        "name": "Pitutur Semar tentang Kehidupan",
        "photo_url": "https://storage.googleapis.com/wayang-storage/pic/ssvideo/video2.jpg",
        "video_duration": "7:37",
        "video_id": "gQ9j_2PKdWE",
        "video_url": "https://youtu.be/gQ9j_2PKdWE"
    }
    ```
![](Images/videodetails.jpg)

### List all of Events:
* URL
    - /eventlist
* Method
    - POST
* Request Body
    * -
* Response
    > 200 OK
    ```json
    [
        {
            "description": "Datanglah Ke Pagelaran Wayang Kulit dengan tema \"Lakon Sembodro Larung\" yang akan dilaksanakan setiap Hari Sabtu Jam 19.00 WIB - Selesai di Sekretariat Sanggar Seni Cipat Budaya Sari Laras, Dusun Cemetuk. Desa Cluring, Kecamatan Cluring Banyuwangi",
            "id": 2,
            "name": "Pagelaran Wayang Kulit \"Lakon Sembodro Larung\"",
            "photo_url": "https://storage.googleapis.com/wayang-storage/pic/event/event2.jpg",
            "price": 30000,
            "time": "Sat, 03 Jun 2023 10:00:00 GMT"
        },
        {
            "description": "Pegelaran Wayang kulit Episode RAMAYANA setiap hari selasa Jam 20.00 - 22.00 WIB lokasi di Pendapa Timur  Museum Sonobudoyo Yogyakarta",
            "id": 1,
            "name": "Pegelaran Wayang Kulit Sonobudoyo",
            "photo_url": "https://storage.googleapis.com/wayang-storage/pic/event/event1.jpg",
            "price": 35000,
            "time": "Tue, 30 May 2023 11:00:00 GMT"
        }
    ]
    ```
![](Images/listallevent.jpg)

### Details of Event:
* URL
    - /event
* Method
    - POST
* Request Body
    * `field_id` as integer, must be valid id
* Response
    > 200 OK
    ```json
    {
        "id": 2,
        "name": "Pitutur Semar tentang Kehidupan",
        "photo_url": "https://storage.googleapis.com/wayang-storage/pic/ssvideo/video2.jpg",
        "video_duration": "7:37",
        "video_id": "gQ9j_2PKdWE",
        "video_url": "https://youtu.be/gQ9j_2PKdWE"
    }
    ```
![](Images/eventdetails.jpg)

### Buy a Ticket for Event:
* URL
    - /ticket_event
* Method
    - POST
* Request Body
    * `event_id` as integer, must be valid id from eventlist  
    * `tickets_bought` as integer, must be greater than 0 and must be filled
    * `name` as string, must be filled
    * `email` as string, must be filled
    * `payment_method` as string, must be filled
    * `file` as file, must be filled

* Response
    > 200 OK
    ```json
    {
        "data": {
            "email": "sukoshi7869@gmai.com",
            "event_id": 2,
            "method": "Dana - 089507741841 (a.n. Bahrum Nisar)",
            "name": "Nizares no Sukoshi",
            "payment_picture": "https://storage.googleapis.com/wayang-storage/pic/receipt/resiiiiakwkow.jpeg",
            "ticket_bought": 4,
            "total_count": 120000
        },
        "message": "success"
    }
    ```
![](Images/buyticket.jpg)

### Upload Photo Profile:
* URL
    - /upload_profile
* Method
    - POST
* Request Body
    * `file` as file, must be valid image file (png, jpg, jpeg), max size <= 2MB  
        - **if uploaded default format its `.jpg`**
    * `uid` as string, must be valid id from firebase auth of each account
        - ![](Images/getuid.jpg)
* Response
    > 200 OK
    ```json
    {
        "image_url": "https://storage.googleapis.com/wayang-storage/pic/profile/B1b8BSRtvQgFoeQ9d6W7Z7JB29i1.jpg",
        "message": "success"
    }
    ```
![](Images/uploadprofile.jpg)

### Get Photo Profile
* URL
    - Just enter url below change [uid from firebase auth] to your uid from firebase account
    - `"https://storage.googleapis.com/wayang-storage/pic/profile/[uid from firebase auth].jpg"`
* Method
    - -
* Request Body
    * -
* Response
    ```html
    read image with html <img src="https://storage.googleapis.com/wayang-storage/pic/profile/B1b8BSRtvQgFoeQ9d6W7Z7JB29i1.jpg" width="100" height="100">
    ```
    - Example view the image
    
    <img src="https://storage.googleapis.com/wayang-storage/pic/profile/B1b8BSRtvQgFoeQ9d6W7Z7JB29i1.jpg" width="250" height="250">