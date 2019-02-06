# ohno
A full utility command line tool for a programmer that helps save time and memory which are most important while coding. 


It searches **stackoverflow** when an error is encountered while executing the program and displays the full results without opening the browser thus saving time and effort to copy-paste the error and then searching it.
If a user wants a custom query on stackoverflow, he can easily do it too.

If a user wants to refer to an algo or code, it can be done from the command line itself.


As a user doesn't have all the compilers installed in his system, **ohno** compiles various less-known languages and displays the result in the terminal.

A coding calender is provided in which competitive programmers can check details of upcoming contests on different platforms and plan their strategy using the **todo** utility.


While coding in a contest or just practicing, a user can directly submit codes on **spoj** and **codechef** with just the ID of the code. This saves a lot of time and effort as he doesn't have to open the browser and submit the code manually.


## Requirements
* python3
* pip

## Installation
On Ubuntu/Debian, you can install *ohno* by cloning the repository and installing via pip:
```
# git clone https://github.com/shashwatrai/ohno.git
```
```
# ./install_dependencies.sh
```
Now, inside the cloned folder,
```
# pip install .
```
Installing geckodriver
```
# wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
# tar -xvzf geckodriver-v0.23.0-linux64.tar.gz
# mv geckodriver /usr/local/bin
```


## How to use

* ``` ohno [file_name] ``` to compile a code which automatically searches stackoverflow on an error.
* ``` ohno -q "custom_query" ``` or ``` ohno --query "custom_query" ``` to search a custom query on stackoverflow.
* ``` ohno  -g "name_of_algo_or_code" ``` or ``` ohno  --gfg "name_of_algo_or_code" ``` to refer to a specific algo.
* ``` ohno -s [file_name] [input_file] ``` or ``` ohno --submit [file_name] [input_file] ``` to compile code online.
* ``` ohno -c ``` or ``` ohno --calender ``` to display upcoming programming contests details.
* ``` ohno -h ``` or ``` ohno --help ``` to display help.

* ``` cprog -s [file_name] ``` or ``` cprog --spoj [file_name] ``` to submit code on **spoj**.
* ``` cprog -c [file_name] ``` or ``` cprog --codechef [file_name] ``` to submit code on **codechef**.

* ``` todo ``` to manage a todo list.
