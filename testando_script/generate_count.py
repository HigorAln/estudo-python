import requests

range = 0

while range < 1000:
    requests.get("https://profile-counter.glitch.me/pamellafernandes/count.svg")
    
    range = range + 1
    print(range)

print("Fim")