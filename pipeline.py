from screenshot import take_screenshot
from analyze import analyze_screenshot
from url_analyzer import analyze_url

def scan(url):
    result = {
        'url': url,
        'phishing': False,
        'reasons': []
    }
    
    url_suspicious = analyze_url(url)
    if url_suspicious:
        result['phishing'] = True
        result['reasons'].append('Suspicious URL')
    
    screenshot_success = take_screenshot(url, "temp_scan.png")
    
    if screenshot_success:
        image_suspicious = analyze_screenshot("temp_scan.png")
        if image_suspicious:
            result['phishing'] = True
            result['reasons'].append('Login page detected')
    
    return result

