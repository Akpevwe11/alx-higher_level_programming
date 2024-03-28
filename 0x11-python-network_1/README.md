## 0x11. Python - Network #1

### Task 0:

 A Python script that fetches https://alx-intranet.hbtn.io/status 

 **Requirements:**

    [x] must use the package urllib
    [x] You are not allowed to import any packages other than urllib
    [x] The body of the response must be displayed like the following example (tabulation   before   -)
    [x] You must use a with statement

Example:

```bash
praisex64@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
praisex64@ubuntu:~/0x11$ 

```


### Task 1:

 Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

 **Requirements:**
    
   [x] You must use the packages `urllib` and `sys`
   [x] You are not allow to import packages other than `urllib` and `sys`
   [x] The value of this variable is different for each request
   [x] You don’t need to check arguments passed to the script (number or type)
   [x] You must use a `with` statement


Example:

```bash
praisex64@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
praisex64@ubuntu:~/0x11$ 
praisex64@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
praisex64@ubuntu:~/0x11$ 

```


### Task 2:

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

 **Requirements:**
    
   [x] The email must be sent in the `email` variable
   [x] You must use the packages urllib and sys
   [x] You are not allowed to import packages other than urllib and sys
   [x] You don’t need to check arguments passed to the script (number or type)
   [x] You must use the with statement


Example:

```bash
praisex64@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
praisex64@ubuntu:~/0x11$ 
```


### Task 3:

A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

 **Requirements:**

    
   [x] You have to manage `urllib.error.HTTPError` exceptions and print: Error code: followed by the HTTP  status code
   [x] You must use the packages `urllib` and `sys`
   [x] You are not allowed to import other packages than `urllib` and `sys`
   [x] You don’t need to check arguments passed to the script (`number` or `type`)
   [x] You must use the `with` statement


Example:

```bash
praisex64@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
praisex64@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
praisex64@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
praisex64@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
praisex64@ubuntu:~/0x11$ 
```

### Task 4:

Write a Python script that fetches https://alx-intranet.hbtn.io/status.

 **Requirements:**

    [x] You must use the package requests
    [x] You are not allow to import packages other than requests
    [x] The body of the response must be display like the following example (tabulation before -)



Example:

```bash
praisex64@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
praisex64@ubuntu:~/0x11$ 

```

### Task 5:

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.

 **Requirements:**

 
  [x]  You must use the packages `requests` and `sys`
  [x]  You are not allow to import other packages than `requests` and `sys`
  [x]  The value of this variable is different for each request
  [x]  You don’t need to check script arguments (`number` and `type`)

Example:

```bash
praisex64@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
praisex64@ubuntu:~/0x11$ 
praisex64@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
praisex64@ubuntu:~/0x11$ 
```

### Task 6:

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

 **Requirements:**
  
   [x] The email must be sent in the variable `email`
   [x] You must use the packages `requests` and `sys`
   [x] You are not allowed to import packages other than `requests` and `sys`
   [x] You don’t need to error check arguments passed to the script (`number` or `type`)


**Example**

```bash
praisex64@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
praisex64@ubuntu:~/0x11$ 
```


### Task 7:

Write a Python script that takes in a `URL`, sends a request to the URL and displays the body of the response.

 **Requirements:**

  
   [x] If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of  the HTTP status code
   [x] You must use the packages requests and sys
   [x] You are not allowed to import packages other than requests and sys
   [x] You don’t need to check arguments passed to the script (`number` or `type`)


**Example**

```bash
praisex64@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
praisex64@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
praisex64@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
praisex64@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
praisex64@ubuntu:~/0x11$ 
```

### Task 8:

Write a Python script that takes in a letter and sends a `POST` request to http://0.0.0.0:5000/search_user with the letter as a parameter..

 **Requirements:**
    
   [x] The letter must be sent in the variable `q`
   [x] If no argument is given, set q=""
   [x] If the response body is properly `JSON` formatted and not empty, display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    [x] You must use the package `requests` and `sys`
    [x] You are not allowed to import packages other than `requests` and `sys`



**Example**

```bash
praisex64@ubuntu:~/0x11$ ./8-json_api.py 
No result
praisex64@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
praisex64@ubuntu:~/0x11$ ./8-json_api.py 2
No result
praisex64@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
praisex64@ubuntu:~/0x11$ 
```


### Task 9:

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

[x] You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
[x] The first argument will be your username
[x] The second argument will be your password (in your case, a personal access token as password)
[x] You must use the package requests and sys
[x] You are not allowed to import packages other than requests and sys
[x] You don’t need to check arguments passed to the script (number or type)


```bash
praisex64@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
praisex64@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
praisex64@ubuntu:~/0x11$ 
```