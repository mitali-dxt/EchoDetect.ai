import pandas as pd

# Create a list of reviews
reviews = [
    "This toothpaste is amazing! My teeth feel so clean and fresh after using it. I highly recommend it.",
    "This toothbrush is the worst! It's too hard and hurts my gums. I wouldn't recommend it to anyone.",
    "I'm really disappointed with this mouthwash. It doesn't taste good and it doesn't seem to work very well.",
    "I love this floss! It's so easy to use and it gets my teeth really clean.",
    "This whitening toothpaste is a lifesaver! My teeth are so much whiter since I started using it.",
    "This electric toothbrush is definitely worth the investment. It removes so much more plaque than a manual toothbrush.",
    "I'm not sure what I was expecting from this lip balm, but it's not very good. It doesn't moisturize my lips at all.",
    "This tongue scraper is a great way to keep your breath fresh. It's easy to use and it works really well.",
    "I'm so happy I found this natural toothpaste! It's gentle on my teeth and it tastes great.",
    "This denture cleaner is the best I've ever used. It removes all the stains and keeps my dentures looking new."
]

# Create a DataFrame
df = pd.DataFrame({"text": reviews})

# Save the DataFrame to a CSV file
df.to_csv("reviews.csv", index=False)

print("CSV file generated successfully!")