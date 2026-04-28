from screenshot import take_screenshot
from detector import detect_phishing
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
        is_phishing, image_reasons = detect_phishing("temp_scan.png")
        if is_phishing:
            result['phishing'] = True
            result['reasons'].extend(image_reasons)
    
    return result