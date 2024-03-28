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







