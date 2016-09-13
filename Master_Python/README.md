#Mastering Python - Networking and Security Training Video
######Author: Ric Messier

--------------------------------------------------------------------------------
1. Intro


2. Python Refresher
    - Python Console
        + python2 or python3
    - Creating and Running Scripts
        $ vi test.py
        $ chmod +x test.py
        $ ./test.py
        or
        $ vi test.py
        $ python test.py
        
    - Variables
    - Loops
    - Scoping
    - Subroutines
    - Conditional Statements
    - Calling To System
    - Using Threads
    - Parsing Arguments
    - Handling Exceptions
    - Installing Additional Packages
    - Classes
    - Instances


3. Networking
    - ssh vs ssl
        * SSH : Secure Shell
        * SSL : Secure Socket Layer
        
    - Network Byte Order
    - Name Server Lookups
        * TCP: Connection-oriented socket
        * UDP: Connectionless socket
        * Socket endpoint: host Addr + port
        * AF_INET: Internet address family
        * PF_INET: Ineternet protocol family
                
    - Network Client
        $ nc -l 5555
        * netcat 套件: 建一個port, 虛擬server
        
    - Network Server
        $ nc localhost 9898 Hi there
        * 連線server, 輸入訊息
        
    - Grabbing Banners
        
    - Simple HTTP Request
    
    - Capturing Packets : pcapy support python2 olny
    - Reading Headers : pcapy support python2 olny
    - Parsing PCAP Files : pcapy support python2 olny
    
    - Creating Raw Packets With Scapy
    - Communicating With SSL
    - Talking To SMTP Servers
    - Talking To POP3 And IMAP Servers
    - FTP
    - Multicasting
    - UDP
    - Telnet Client


4. HTTP Programmming
    - Authenticating
    - Setting The User Agent
    - Setting Cookies
    - Using A HEAD Request
    - Interfacing With Web Forms
    - Parsing Web Responses
    - Using Web Proxies
    - Downloading Files Via HTTP
    - Spidering


5. Security Scripting
    - Threaded Network Testing
    - Creating Alternate Data Streams
    - Fuzzing With Python
    - Debugging With Python
    - Steganography With Stepic
    - Encrypting And Decrypting Data
    - Hiding Encrypted Data With Steganography
    - Interacting With MySQL
    - Replaying Network Traffic


6. Forensic Scripting
    - Accessing Windows Registry - Part 1
    - Accessing Windows Registry - Part 2
    - Accessing MFT - Part 1
    - Accessing MFT - Part 2
    - Log Parsing
    - Analyzing The MBR
    - Reading Alternate Data Streams
    - Getting Process Lists
    - Getting Access To SQLite Databases
    - Accessing Browser Data Through SQLite
    - Getting Access To Recycle Bin
    - Walking A Filesystem
    - Finding Files By Time


7. Twisted Python
    1. What Is Twisted?
    2. Echo Server
    3. Echo Client
    4. HTTP Server


8. Conclusion
    a. Wrapping Up
    b. What Is Next?
