# Rest-API-CRUD-operations

## HOW TO SETUP
1. Start a Virtual environment  
``` virtualenv
   pip install virtualenv    
   virtualenv venv   
   venv\scripts\activate 
```
2. Clone this project  
  ``` git clone https://github.com/adhi85/Rest-API-CRUD-operations.git ```
4. Install all the dependencies  
    ``` 
    cd Rest-API-CRUD-operations
    pip install -r requirements.txt   
    
    ```
5. Run the server
  `` python manage.py runserver ``

Please Setup your own local postgres database
    
## API OPERATIONS
```
 Link: localhost/api/
    List-Books : /book-list/
    Create : /book-create/
    Read : /book-view/<int:pk>/
    Update : /book-update/<int:pk>/
    Delete : /book-delete/<int:pk>/
```        


  
