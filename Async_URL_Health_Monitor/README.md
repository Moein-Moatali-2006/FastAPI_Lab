# Async URL Health Monitor
A simple system for checking URLs health by Asynchronous logic.
save unhealthy status code in a log file.

Set your own URLs in file urls.txt


### Libararies:
1. AsyncIO
2. AIOhttp
3. Logging

## How to run?
```
pip install -r requirements.txt
```

```
Windows CLI --> python main.py
Linux CLI --> python3 main.py
```

## Example Result:
```
Async URL Health Monitor
Service Started ⚡
________________________________________________________________
Status Code for https://chatgpt.com is 403
****************************************************************
Status Code for https://gitlab.com is 403
****************************************************************
Status Code for https://github.com is 200
****************************************************************
Status Code for https://stackoverflow.com is 403
****************************************************************
Status Code for https://www.google.com is 200
****************************************************************
Status Code for https://w3schools.com is 403
****************************************************************
________________________________________________________________
Finished - check logs.log if you want.

```

### Developd by Moein Moatali
Email: MoeinMoatali@gmail.com

Phone number: +98 9030813097

Telegram id: @MoeinMoatali
