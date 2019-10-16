# 0x0B. Python - Input/Output

0- Function that reads a text file (UTF8) and prints it to stdout

1- Function that returns the number of lines of a text file

2- Function that reads n lines of a text file (UTF8) and prints it to stdout:
   Read the entire file if nb_lines is lower or equal to 0 OR greater or equal to the total number of lines of the file

3- Function that writes a string to a text file (UTF8) and returns the number of characters written:
   function should create the file if doesn’t exist.
   function should overwrite the content of the file if it already exists.

4- Function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
   If the file doesn’t exist, it should be created

5- Function that returns the JSON representation of an object (string):

6- Function that returns an object (Python data structure) represented by a JSON string

7- Function that writes an Object to a text file, using a JSON representation

8- Function that creates an Object from a “JSON file”

9- Script that adds all arguments to a Python list, and then save them to a file:
   The list must be saved as a JSON representation in a file named add_item.json
   If the file doesn’t exist, it should be created

10- Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
    obj is an instance of a Class
    All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean

11- Class Student that defines a student by:
    Public instance attributes:
    	   first_name
	   last_name
	   age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)

12- Class Student that defines a student by: (based on 11-student.py)
    Public instance attributes:
    	   first_name
	   last_name
	   age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
    	   If attrs is a list of strings, only attribute names contained in this list must be retrieved.
    	   Otherwise, all attributes must be retrieved

13- Class Student that defines a student by: (based on 12-student.py)
    Public instance attributes:
    	   first_name
	   last_name
	   age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
    	   If attrs is a list of strings, only attributes name contain in this list must be retrieved.
	   Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
    	   You can assume json will always be a dictionary
	   A dictionary key will be the public attribute name
	   A dictionary value will be the value of the public attribute

14- Function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0

100- Function that inserts a line of text to a file, after each line containing a specific string (see example)

101- Script that reads stdin line by line and computes metrics:
     Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
     Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
     	  Total file size: File size: <total size>
	  where is the sum of all previous (see input format above)
	  Number of lines by status code:
	  	 possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
		 if a status code doesn’t appear, don’t print anything for this status code
		 format: <status code>: <number>
		 status codes should be printed in ascending order