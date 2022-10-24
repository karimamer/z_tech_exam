# Data Engineering Python Test

# File Structure

get_characters.py -> File contains all the fucntions that interfaces with the marvel API
main.py -> Glue both functions from get_characters.py and transform.py to return the main the Dataframe
transform.py -> Contains the main function to transform Json Data to a Data frame and rename the coloumns

```
z_tech_exam ---> get_characters.py
            |
            |---> main.py
            |
            |---> transform.py
```
# Dependencies
 1 - install [poetry](https://python-poetry.org/)
 2 - runt the follwing command `poetry install`

 # fomating and standerds 
 The project follows black and flake8

# How to run 
 1 - install [poetry](https://python-poetry.org/)
 
 2 - run the following command `poetry run python z_tech_exam/main.py`

# How to run in noteboke
import main function in juypter notebook and run main function
