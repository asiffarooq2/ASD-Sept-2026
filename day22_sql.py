import requests
sql_errors = [
"sql syntax","mysql",
"syntax error",
"database error",
"unclosed quotation",
"unknown column",
]
test_values = [
"'",
"\"",
"''",
"\"\"",
";"
"1",
]
def test_input(url, param, test_value):
    try:
        payload = {param: test_value}
        print(payload)
        response = requests.get(url, params=payload, timeout=5)
        text = response.text.lower()
        print("Test=",text)
        for error in sql_errors:
            if error in text:
                return True # SQL error found
    except:
        pass
        return False
def scan(url, param):
    print(f"\nTesting parameter: {param}\n")
    for value in test_values:
        print(f"Trying: {value}")
        if test_input(url, param, value):
            print(f"[!] SQL Error detected with input: {value}")
        else:
            print(f"[OK] No SQL error\n")
url = input("Enter URL: ")
param = input("Parameter to test: ")
scan(url, param)

# www.gmail.com/?username="'"