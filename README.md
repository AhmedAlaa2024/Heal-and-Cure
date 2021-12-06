# <span style="color: green">Heal and Cure</span>
This is a final web application project for database management course using modern technologies like flask and react-native. This project for hospital managment system to maniplute the internal interactions between the hospital's stuff and the external interactions between the hospital stuff's and the patients.
- - -
## <span style="color: green">Worked on the project:</span>
1. Ahmed Alaa El-Sayed Arabi Zidan (Team Leader)
2. Mahmoud Reda
3. Ahmed Sabry
4. Mohamed Nabil
- - -
## <span style="color: green">Project Intialization Steps:</span>
- Run the following commands :
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
- - -
## <span style="color: green">Comments Policy:</span>
1. Every function ***must*** be well documented. <br>
- Format:
```
#===================================================================================================
# Function: function's name
# Input:    <type:name> => Parameter1's description, <type:name> => Parameter2's description,...
# Output:   <type:name> => Output1's description, <type:name> => Output1's description,...
# Prerequistes: Any needed prerequirements
# Description: Detailed description for the function
#===================================================================================================
```
- Ex:
```
#===================================================================================================
# Function: open_connection
# Input:    <sting:db_name> => the relative path of required database to be connected with
# Output:   <(Sqlite3::Connection):connection> => An object of class connection from sqlite3 module
# Prerequistes: None
# Description: Open connection with the required database
#===================================================================================================
def open_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection
```
2. To execute a sql query, follow the following:<br>
    I. In the beginning of the file, you should write:<br>
    ```
    connection = open_connection("hospital.db")
    ```
    II. After the connection is constructed, you have to get the cursor:<br>
    ```
    cursor = get_cursor(connection)
    ```
    III. Each time you want to execute a sql query, Do the following:
    ```
    cursor.execute("""_your_query_""")
    ```

    IV. After you finish your work in the file with database connection, You ***must** close the connection:
    ```
    close_connection(connection)
    ```
    <span style="color: red">Warning: Not closing the database connection will cause many problems!</span>
- - -
## <span style="color: red">***Global Warnings:***</span>
1. Every One <span style="color: red">***must***</span> have his own branch on the repository.
2. <span style="color: red">***No one is allowed***</span> to push his changes direct on master branch.
3. Make sure before you make any changes on your local that:<br>
    I. You working on your local branch not on local master.
    II. Your local master is up to date with the global master.
    ```
    git checkout master
    git pull
    ```
    III. Your local branch is merged by the up to dated local master.
    ```
    git checkout <your branch's name>
    git merge
    ```
    IV. Don't forget to return to your branch
    ```
    git checkout <your branch's name>
    ```
- - -