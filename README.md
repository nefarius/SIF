Squid Image Fetcher
===================
Work in progress.

Adjustments of squid.conf
-----------------
Add (or adapt) the following directives to your `squid.conf` file:
```
# path to python interpreter and script
url_rewrite_program C:\\Python33\\python.exe -u C:\\squid\\libexec\\fetchimg.py
# number of python processes (instances of the script) to spawn
#     (decrease value if low on system resources, increase for better performance)
url_rewrite_children 10
# number of requests sent to URL helper in parallel
#     (decrease value if low on system resources, increase for better performance)
url_rewrite_concurrency 10
```
Restart the service afterwards.

If everything went well, a corresponding number of python processes will appear:
![Processes](http://content.screencast.com/users/Nefarius/folders/Snagit/media/7cda4a46-f429-4c9e-a486-55985b926ed9/09.09.2014-22.36.png)

Known Bugs
----------
You may encounter the following error(s) in your `cache.log` file:
```
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
2014/09/10 11:39:42| Failed parsing input: 0 l.ghostery.com:443 192.168.2.125/- - CONNECT myip=192.168.2.10 myport=8080
2014/09/10 11:39:42|     Details: <class 'urllib.error.URLError'>
```
At the current stage **HTTPS is not supported**. These messages can be ignored.
