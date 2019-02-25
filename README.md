#  Kahoot!
## Apaan sih Kahoot ? 

pada project ini yaitu membuat web app yang bernama kahoot, dalam project ini dujesakn langkah-lahkah, software dan package yang digunakan 
dan cara menggunakannya , adapun software pendukung untuk membuat project ini yaitu :

## Install dan setup package  
1. install text editor (visual code studio)
lebih lengkapnya dapat dilihat di vidio berukut ini 
[![install vs code](http://i2.wp.com/jtower.com/wp-content/uploads/2015/06/visual-studio-2013-logo.png?w=600)](https://www.youtube.com/watch?v=7EHJafw3djk)
2. install insomnia

[![install insomnia image alt "><"](https://img.crx4chrome.com/58/7c/7b/gmodihnfibbjdecbanmpmbmeffnmloel-featured.jpg)](https://www.youtube.com/watch?v=Gyt7OjdsiGQ)

bahasa yang digunakan dalam project ini menggunakan bahasa pemograman python dan package Flask.

### Flask

Flask adalah kerangka kerja aplikasi web mikro yang ditulis dalam bahasa pemrograman Python.

- **Installing**<br>
  Install pada terminal visual code :
  ```python -m venv .\
     Scripts\activate.bat
     pip install flask
     set FLASK_APP=app.py
     set FLASK_ENV=development
     flask run
     
  ```
  
  
## Cara menggunakan kahoot
insomnia digunakn untuk client melakukan ujicoba. Salah satu REST API Client.

#### Register dengan metode : POST
```python
{
	"username":"emad",
	"user-id":1,
	"password":"fad",
	"email":"fasyahmad01@gmail.com",
	"skidipaw":"encrypt"
}
```
#### Log-in dengan metode : POST
```python
{
	"username":"emad",
	"password":"fad",
	"skidipaw":"encrypt"
}
```

#### Question dengan metode : POST
```python
{
	"quiz-id" : 123,
	"question-number":1,
	"question":"tetangga kamu siapa ?",
	"answer": "C",
	"option-list": {
		"A":"udin",
		"B":"untung",
		"C":"ucup",
		"D":"upin"
	}
}
```

