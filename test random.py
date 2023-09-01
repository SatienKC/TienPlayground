import random
import string

# Function to generate a random product name
def generate_product_name():
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(5))

# Function to generate a random target customer
def generate_target_customer():
    customers = ["Homeowners", "Professionals", "Tech Enthusiasts", "Fitness Enthusiasts", "Environmentalists", "Students", "Yoga Practitioners", "Home Cooks", "Cyclists", "Music Lovers", "Beachgoers"]
    return random.choice(customers)

# Function to generate a random channel platform
def generate_channel_platform():
    platforms = ["Online Stores", "Retail Stores", "E-commerce Websites", "Grocery Stores", "Fitness Centers", "Coffee Shops", "Sporting Goods Stores", "Health Food Stores", "Pharmacies"]
    return random.choice(platforms)

# Function to generate a random media strategy
def generate_media():
    media = ["Social Media", "TV Commercials", "Magazine Advertisements", "Influencer Collaborations", "Online Reviews", "Podcast Sponsorships", "Email Marketing", "Outdoor Billboards"]
    return random.choice(media)

# Function to generate a random key message
def generate_key_message():
    messages = ["Experience Quality and Convenience", "Upgrade Your Lifestyle", "Transform Your Routine", "Simplify Your Life", "Discover New Possibilities", "Enhance Your Well-being", "Embrace Sustainability", "Stay Ahead of the Curve"]
    return random.choice(messages)

# Generate 100 product dictionaries
products = []

for _ in range(100):
    product = {
        "Product": generate_product_name(),
        "Target Customers": generate_target_customer(),
        "Channel Platform": generate_channel_platform(),
        "Media": generate_media(),
        "Key Message": generate_key_message(),
    }
    products.append(product)

# Sample output of the first product in the list
print(products[0])