# AirBnB_clone
There should be a fancy image or something here, but i'm too petty and pissed to place one, because... its one of those "but it works on my machine..." cases (and I truly hate edge cases)

## Project Description
This project is an AirBnB_clone command interpreter written in Python. The interpreter allows a user to input commands and interact with the program.

## Command Interpreter
The command interpreter is a text-based interface that allows users to enter and execute commands. Think of it as a terminal interface to a program.

Here, in the AirBnB clone, the interpreter will be used to manage the objects created, like the following:

 - Create a new object (ex: a new User or a new Place)
 - Retrieve an object from a file, a database etc…
 - Do operations on objects (count, compute stats, etc…)
 - Update attributes of an object
 - Destroy an object

### How to Start The Interpreter
It's simple. The shell can be started interactively and non-interactively.

#### Interactive way of starting the interpreter
``` sh
meistens@bearded-fedora:~/AirBnB$ ./console.py
(hbnb) create State
4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df
(hbnb) all State
```

#### Non-interactive way
``` sh
meistens@bearded-fedora:~/AirBnB$ echo "help" | ./console.py 
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  exit  help  quit  show  update
```

### How To Use It
How to use, its pretty straight forward.

There are commands which can be used (key in "help" into the interpreter to see available options):

- You can create a new object

``` shell
meistens@bearded-fedora:~/AirBnB$ ./console.py
(hbnb) create State
4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df
```
- check all saved properties saved in the storage engine

``` shell
(hbnb) all State
["[State] (4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df) {'id': '4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df', 'created_at': datetime.datetime(2023, 2, 13, 17, 1, 46, 122698), 'updated_at': datetime.datetime(2023, 2, 13, 17, 1, 46, 122725)}"]
```

- destroy an object (not multiple objects)

```shell
(hbnb) destroy User d560fc04-f45e-437b-bd69-3b56b843b91b
```

- update an object (__Note__: id and the datetime cannot be updated!)
``` shell
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

...and a whole lotta options (again, see the "help" page of the interpreter)

### Examples
``` shell
meistens@bearded-fedora:~/AirBnB$ ./console.py
(hbnb) create State
4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df
(hbnb) all State
["[State] (4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df) {'id': '4f0f0e03-95e2-4eba-bdc5-5b92bf12d1df', 'created_at': datetime.datetime(2023, 2, 13, 17, 1, 46, 122698), 'updated_at': datetime.datetime(2023, 2, 13, 17, 1, 46, 122725)}"]
```

### Contact Information
[AUTHORS](./AUTHORS.md)

### License Information
Anyone can use it but if you want to read the fineprints, check [GNU GPL-3.0](./LICENSE) license

### Acknowledgements
[ALX_Africa](https://twitter.com/alx_africa)
