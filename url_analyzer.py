import re
from urllib.parse import urlparse

def analyze_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    score = 0
    reasons = []

    if len(url) > 75:
        score += 20
        reasons.append("URL too long")

    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
        score += 30
        reasons.append("Uses IP instead of domain")

    bad_words = ['login', 'verify', 'secure', 'update', 'banking']
    found = [w for w in bad_words if w in url.lower()]
    if found:
        score += 20
        reasons.append(f"Suspicious words: {found}")

    if not url.startswith('https'):
        score += 15
        reasons.append("No HTTPS")

    if domain.count('.') > 3:
        score += 15
        reasons.append("Too many subdomains")

    print(f"URL: {url}")
    print(f"Score: {score}/100")
    print(f"Reasons: {reasons}")
    
    if score >= 30:
        print("WARNING: Suspicious URL!")
    else:
        print("SAFE: URL looks clean")
    print("---")

# نجرب
# analyze_url("https://google.com")
# analyze_url("http://paypal-verify-account.suspicious.com/login")
# analyze_url("http://192.168.1.1/bank-login")



