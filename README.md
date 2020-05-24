# Pics Art
#### By:
Beryl Negesa Otieno

### Description  
This is an application that enables users to view different categories of images and their locations and also able to copy the link and share it to other friends.

### Deployed link
https://pics-art-1.herokuapp.com/

### BDD
| Behaviour         | Input            | Output                     |
| ----------------- | ---------------- | -------------------------- |
| Search by category on the search form | Category to search | Images under the searched category |
| Search by location on the see location page | Location and images taken on that location | Images under that location |
| Copy Image link   | Click button link     | Link copied                |

### Setup and Installation  
To get the project .......    
##### Cloning the repository:  
 ```bash 
git clone https://github.com/Beryl01/Pics-ART.git
```
##### Navigate into the folder 
 ```bash 
cd Pics-ART
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
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