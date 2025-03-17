```
import socket

def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        print(f"The IP address of {website_url} is {ip_address}")
    except socket.gaierror:
        print(f"Unable to get the IP address for {website_url}")

website = input("Enter the website URL (without 'https://'): ")
get_ip_address(website)            

# gov.uk IP = 151.101.192.144
# google.com IP = 216.58.201.110
# youtube.com IP = 172.217.169.14
# gold.ac.uk = 159.100.136.66

```

In the third week we had our second seminar. Here, the first task was to use the example code that takes a URL as user input and try returning the IP address that correlates with it. 

I ran this code and used the 4 websites mentioned in the comments and got those IP addresses in return, confirming that it works. When I tried inputting a URL that included the "https" part, the error was caught by the exception handling, which further proves that the code works.