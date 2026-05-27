import re

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['dot_count'] = url.count('.')
    features['hyphen_count'] = url.count('-')
    features['has_https'] = 1 if url.startswith('https') else 0
    features['special_char_count'] = len(re.findall(r'[@_!#$%^&*<>?/|}{~:]', url))
    suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'free', 'click']
    features['has_suspicious_word'] = 1 if any(word in url.lower() for word in suspicious_words) else 0
    return features