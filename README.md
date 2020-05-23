# Pics Art
#### By:
Beryl Negesa Otieno

### Description  
This is an application that enables users to view different categories of images and their locations and also able to copy the link and share it to other friends.

### Deployed link


### BDD
| Behaviour         | Input            | Output                     |
| ----------------- | ---------------- | -------------------------- |
| search by category | category         | images under that category |
| search by location | location         | images under that location |
| Copy Image link   | click bitton     | link copied                |

### Setup and Installation  
To get the project .......    
##### Cloning the repository:  

##### Navigate into the folder 
 ```bash 
cd Pics-ART
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python3.6 manage.py migrate 
```
##### Run the application  
 ```bash 
 python3.6 manage.py runserver 
```  
##### Testing the application  
 ```bash 
 python3.6 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Technologies Used
* Python3.6
* Django 3.0
* HTML5
* CSS3
* Bootstrap4
  
## Known Bugs
None known for now.

## Support and contact details
* Email-berylnegesa@gmail.com

## License

[MIT License](License.md)
Copyright (c) [2020] [Beryl Negesa Otieno]
</a>