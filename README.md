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
# set to zero or comment out
url_rewrite_concurrency 0
```
Restart the service afterwards.

If everything went well, a corresponding number of python processes will appear:
![Processes](http://content.screencast.com/users/Nefarius/folders/Snagit/media/7cda4a46-f429-4c9e-a486-55985b926ed9/09.09.2014-22.36.png)
