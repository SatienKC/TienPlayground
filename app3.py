import streamlit as st 
import pandas as pd
import nltk
nltk.download('tokenize')
# nltk.download('tokenize')

from nltk.tokenize import word_tokenize
# from tokenize import word_tokenize

fruits = [

    {
        "Product": "apple",
        "Target Customers": "Health-conscious individuals, parents, and snackers.",
        "Channel Platform": "Supermarkets, farmers' markets, online grocery stores, and school cafeterias.",
        "Media": "Health and nutrition blogs, social media health influencers, fruit recipe websites, and school newsletters.",
        "Key Message": "An Apple a Day Keeps the Doctor Away."
    },
    {
        "Product": "banana",
        "Target Customers": "Athletes, children, and on-the-go snackers.",
        "Channel Platform": "Grocery stores, convenience stores, school lunch programs, and sports events.",
        "Media": "Sports magazines, fitness blogs, social media fitness influencers, and family recipe books.",
        "Key Message": "A Natural Energy Boost in Every Bite."
    },
    {
        "Product": "orange",
        "Target Customers": "Families, vitamin seekers, and immune system boosters.",
        "Channel Platform": "Supermarkets, health food stores, online vitamin shops, and juice bars.",
        "Media": "Health and wellness websites, vitamin and nutrition blogs, social media health gurus, and citrus-themed recipes.",
        "Key Message": "Packed with Vitamin C for a Healthy Life."
    },
    {
        "Product": "grapes",
        "Target Customers": "Snackers, party planners, and wine enthusiasts.",
        "Channel Platform": "Grocery stores, specialty food shops, wineries, and event catering services.",
        "Media": "Food and wine magazines, recipe blogs, social media wine influencers, and party planning websites.",
        "Key Message": "Nature's Sweetest Little Treats."
    },
    {
        "Product": "strawberries",
        "Target Customers": "Dessert lovers, bakers, and health-conscious individuals.",
        "Channel Platform": "Farmers' markets, bakeries, online dessert shops, and health food stores.",
        "Media": "Dessert recipe websites, food blogs, social media dessert chefs, and health-conscious cookbooks.",
        "Key Message": "Indulge in Sweet, Red Perfection."
    },
    {
        "Product": "blueberries",
        "Target Customers": "Smoothie makers, health enthusiasts, and antioxidant seekers.",
        "Channel Platform": "Grocery stores, smoothie bars, online health shops, and fitness centers.",
        "Media": "Health and fitness magazines, smoothie recipe blogs, social media health advocates, and antioxidant articles.",
        "Key Message": "Fuel Your Body with Superfood Power."
    },
    {
        "Product": "pineapple",
        "Target Customers": "Tropical fruit lovers, summer refreshers, and exotic cuisine enthusiasts.",
        "Channel Platform": "Supermarkets, tropical fruit markets, online exotic food stores, and tiki bars.",
        "Media": "Tropical vacation websites, exotic recipe blogs, social media travel influencers, and summer cocktail recipes.",
        "Key Message": "Taste the Tropics, One Slice at a Time."
    },
    {
        "Product": "mango",
        "Target Customers": "Fruit salad makers, exotic fruit explorers, and smoothie enthusiasts.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, and smoothie cafes.",
        "Media": "Exotic fruit recipe websites, food blogs, social media fruit explorers, and tropical smoothie recipes.",
        "Key Message": "Savor the Exotic Juiciness of Mango."
    },
    {
        "Product": "watermelon",
        "Target Customers": "Picnickers, summer party hosts, and hydration seekers.",
        "Channel Platform": "Grocery stores, outdoor markets, online party supply shops, and beachfront snack stands.",
        "Media": "Summer party planning websites, hydration blogs, social media summer enthusiasts, and picnic recipe collections.",
        "Key Message": "Stay Cool, Stay Hydrated with Watermelon."
    },
    {
        "Product": "cherries",
        "Target Customers": "Pie bakers, fruit salad makers, and antioxidant hunters.",
        "Channel Platform": "Farmers' markets, online fruit shops, bakeries, and health food stores.",
        "Media": "Pie recipe blogs, antioxidant articles, social media fruit enthusiasts, and fruit salad recipe websites.",
        "Key Message": "Savor the Sweetness of Summer."
    },
    {
        "Product": "kiwi",
        "Target Customers": "Fruit salad enthusiasts, vitamin seekers, and exotic fruit explorers.",
        "Channel Platform": "Grocery stores, health food shops, online exotic fruit retailers, and salad bars.",
        "Media": "Fruit salad recipe websites, health and nutrition blogs, social media fruit explorers, and vitamin-rich meal plans.",
        "Key Message": "Discover the Vibrant Green Goodness."
    },
    {
        "Product": "avocado",
        "Target Customers": "Health-conscious foodies, avocado toast lovers, and guacamole makers.",
        "Channel Platform": "Grocery stores, online organic food shops, brunch restaurants, and Mexican eateries.",
        "Media": "Avocado recipe blogs, health food articles, social media avocado enthusiasts, and brunch menu showcases.",
        "Key Message": "Creamy, Nutrient-Rich Perfection."
    },
    {
        "Product": "lemon",
        "Target Customers": "Bakers, cocktail enthusiasts, and citrus lovers.",
        "Channel Platform": "Grocery stores, bakeries, online citrus shops, and cocktail bars.",
        "Media": "Baking recipe blogs, cocktail recipe websites, social media citrus aficionados, and lemon dessert showcases.",
        "Key Message": "Zest Up Your Life with a Splash of Lemon."
    },
    {
        "Product": "peach",
        "Target Customers": "Pie bakers, jam makers, and summer fruit aficionados.",
        "Channel Platform": "Farmers' markets, online fruit markets, pastry shops, and jam producers.",
        "Media": "Pie recipe blogs, jam-making tutorials, social media fruit enthusiasts, and summer fruit showcases.",
        "Key Message": "Juicy Sweetness of Summer in Every Bite."
    },
    {
        "Product": "pear",
        "Target Customers": "Fruit basket gifters, wine pairers, and dessert aficionados.",
        "Channel Platform": "Gift shops, online fruit basket retailers, wine stores, and dessert cafes.",
        "Media": "Fruit basket gift guides, wine pairing articles, social media fruit basket enthusiasts, and pear dessert recipes.",
        "Key Message": "Elegant, Refined, and Irresistibly Delicious."
    },
    {
        "Product": "grapefruit",
        "Target Customers": "Breakfast enthusiasts, dieters, and citrus lovers.",
        "Channel Platform": "Grocery stores, health food shops, online citrus fruit retailers, and breakfast diners.",
        "Media": "Breakfast recipe blogs, dieting tips, social media grapefruit lovers, and citrus breakfast showcases.",
        "Key Message": "Start Your Day with a Burst of Citrus Freshness."
    },
    {
        "Product": "plum",
        "Target Customers": "Jam makers, summer fruit fans, and dessert connoisseurs.",
        "Channel Platform": "Farmers' markets, online fruit shops, jam producers, and pastry shops.",
        "Media": "Jam-making tutorials, summer fruit showcases, social media fruit enthusiasts, and plum dessert recipes.",
        "Key Message": "Sweetness of Summer, Captured in Every Plum."
    },
    {
        "Product": "cantaloupe",
        "Target Customers": "Breakfast lovers, fruit salad makers, and hydration seekers.",
        "Channel Platform": "Grocery stores, online fruit retailers, breakfast diners, and juice bars.",
        "Media": "Breakfast recipe blogs, fruit salad tutorials, social media fruit enthusiasts, and melon hydration guides.",
        "Key Message": "A Fresh Start to Your Day with Cantaloupe."
    },
    {
        "Product": "raspberry",
        "Target Customers": "Jam makers, dessert bakers, and antioxidant seekers.",
        "Channel Platform": "Farmers' markets, online fruit markets, bakery shops, and health food stores.",
        "Media": "Jam-making recipes, dessert recipe blogs, social media raspberry fans, and antioxidant-rich meal plans.",
        "Key Message": "Delicate Sweetness, Bursting with Health Benefits."
    },
    {
        "Product": "blackberry",
        "Target Customers": "Pie bakers, jam makers, and berry lovers.",
        "Channel Platform": "Farmers' markets, online fruit shops, pie bakeries, and jam producers.",
        "Media": "Pie recipe blogs, jam-making tutorials, social media berry enthusiasts, and blackberry dessert recipes.",
        "Key Message": "Taste the Richness of Blackberry Bliss."
    },
    {
        "Product": "apricot",
        "Target Customers": "Jam makers, summer fruit enthusiasts, and dried fruit lovers.",
        "Channel Platform": "Farmers' markets, online fruit markets, dried fruit stores, and jam producers.",
        "Media": "Jam-making tutorials, summer fruit showcases, social media apricot fans, and dried fruit recipes.",
        "Key Message": "Summer's Sweet Bounty in Every Apricot."
    },
    {
        "Product": "cranberry",
        "Target Customers": "Thanksgiving cooks, health-conscious individuals, and juice drinkers.",
        "Channel Platform": "Grocery stores, online health food shops, Thanksgiving dinner menus, and juice bars.",
        "Media": "Thanksgiving recipe blogs, health benefits articles, social media cranberry lovers, and cranberry juice recipes.",
        "Key Message": "The Tangy Twist Your Taste Buds Crave."
    },
    {
        "Product": "coconut",
        "Target Customers": "Exotic cuisine enthusiasts, dessert bakers, and health food lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic food shops, bakeries, and health food stores.",
        "Media": "Exotic recipe blogs, dessert recipe websites, social media coconut enthusiasts, and coconut health articles.",
        "Key Message": "Tropical Flavor, Packed with Nutrients."
    },
    {
        "Product": "pomegranate",
        "Target Customers": "Antioxidant seekers, juice enthusiasts, and exotic fruit explorers.",
        "Channel Platform": "Grocery stores, health food shops, online fruit markets, and juice bars.",
        "Media": "Antioxidant-rich meal plans, juice recipes, social media pomegranate fans, and exotic fruit showcases.",
        "Key Message": "Unlock the Power of Antioxidants with Pomegranate."
    },
    {
        "Product": "fig",
        "Target Customers": "Gourmet chefs, cheese platter creators, and Mediterranean cuisine lovers.",
        "Channel Platform": "Specialty food stores, online gourmet shops, cheese shops, and Mediterranean restaurants.",
        "Media": "Gourmet recipe blogs, cheese pairing articles, social media fig enthusiasts, and Mediterranean feast showcases.",
        "Key Message": "Elegance and Flavor, All in One Fig."
    },
    {
        "Product": "dragonfruit",
        "Target Customers": "Exotic fruit explorers, smoothie enthusiasts, and Instagram-worthy food creators.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, smoothie bars, and trendy cafes.",
        "Media": "Exotic fruit showcases, smoothie recipe blogs, social media dragonfruit fans, and Instagram food photography trends.",
        "Key Message": "Experience the Magic of Dragonfruit."
    },
    {
        "Product": "passionfruit",
        "Target Customers": "Exotic fruit lovers, tropical smoothie makers, and adventurous eaters.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, smoothie cafes, and tropical fruit markets.",
        "Media": "Exotic fruit recipe blogs, smoothie inspirations, social media passionfruit fans, and tropical fruit showcases.",
        "Key Message": "Savor the Exotic Tang of Passionfruit."
    },
    {
        "Product": "guava",
        "Target Customers": "Exotic fruit explorers, health-conscious individuals, and tropical juice lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, health food stores, and juice bars.",
        "Media": "Exotic fruit health benefits, tropical juice recipes, social media guava enthusiasts, and tropical fruit showcases.",
        "Key Message": "Tropical Goodness in Every Guava Bite."
    },
    {
        "Product": "tangerine",
        "Target Customers": "Lunchbox packers, citrus enthusiasts, and vitamin seekers.",
        "Channel Platform": "Grocery stores, school cafeterias, online fruit shops, and lunchbox delivery services.",
        "Media": "Citrus health benefits, lunchbox packing tips, social media tangerine fans, and vitamin-rich lunch ideas.",
        "Key Message": "A Zesty Addition to Your Daily Routine."
    },
    {
        "Product": "lychee",
        "Target Customers": "Exotic fruit explorers, Asian cuisine lovers, and fruit salad makers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, Asian restaurants, and fruit salad bars.",
        "Media": "Exotic fruit salad recipes, Asian cuisine showcases, social media lychee fans, and fruit exploration blogs.",
        "Key Message": "Uncover the Sweet Mystique of Lychee."
    },
    {
        "Product": "clementine",
        "Target Customers": "Snackers, lunchbox packers, and holiday gifters.",
        "Channel Platform": "Grocery stores, online fruit shops, lunchbox delivery services, and holiday gift shops.",
        "Media": "Lunchbox packing ideas, holiday gift guides, social media clementine fans, and citrus snack showcases.",
        "Key Message": "Brighten Your Day with Clementine Sunshine."
    },
    {
        "Product": "kiwi berry",
        "Target Customers": "Exotic fruit explorers, fruit salad makers, and fruit platter creators.",
        "Channel Platform": "Specialty fruit markets, online exotic fruit shops, fruit salad cafes, and fruit platter catering services.",
        "Media": "Exotic fruit salad recipes, fruit platter inspirations, social media kiwi berry fans, and fruit exploration blogs.",
        "Key Message": "Discover Miniature Delights with Kiwi Berry."
    },
    {
        "Product": "mulberry",
        "Target Customers": "Health-conscious snackers, smoothie makers, and jam enthusiasts.",
        "Channel Platform": "Health food stores, online dried fruit shops, smoothie cafes, and artisanal jam producers.",
        "Media": "Dried fruit benefits, smoothie inspirations, social media mulberry fans, and homemade jam recipes.",
        "Key Message": "Naturally Sweet and Nutrient-Packed."
    },
    {
        "Product": "papaya",
        "Target Customers": "Exotic fruit lovers, tropical smoothie enthusiasts, and digestive health seekers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, smoothie bars, and health food stores.",
        "Media": "Exotic fruit health benefits, tropical smoothie recipes, social media papaya fans, and digestive health articles.",
        "Key Message": "Embrace the Tropical Bliss of Papaya."
    },
    {
        "Product": "starfruit",
        "Target Customers": "Exotic fruit explorers, tropical smoothie makers, and fruit salad creators.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, smoothie cafes, and fruit salad catering services.",
        "Media": "Exotic fruit salad recipes, tropical smoothie inspirations, social media starfruit fans, and fruit exploration blogs.",
        "Key Message": "Unveil the Star-Shaped Wonder of Starfruit."
    },
    {
        "Product": "mandarin Orange",
        "Target Customers": "Snackers, lunchbox packers, and citrus enthusiasts.",
        "Channel Platform": "Grocery stores, school cafeterias, online fruit shops, and lunchbox delivery services.",
        "Media": "Lunchbox packing ideas, school snack guides, social media mandarin orange fans, and citrus snack showcases.",
        "Key Message": "A Burst of Citrus Joy in Every Bite."
    },
    {
        "Product": "black Currant",
        "Target Customers": "Jam makers, antioxidant seekers, and gourmet bakers.",
        "Channel Platform": "Farmers' markets, online fruit shops, gourmet bakeries, and health food stores.",
        "Media": "Jam-making recipes, antioxidant-rich meal plans, social media black currant fans, and gourmet dessert showcases.",
        "Key Message": "Indulge in the Deep Flavor of Black Currant."
    },
    {
        "Product": "honeydew melon",
        "Target Customers": "Fruit salad lovers, hydration seekers, and summer refreshers.",
        "Channel Platform": "Grocery stores, online fruit markets, salad bars, and smoothie cafes.",
        "Media": "Fruit salad recipes, hydration tips, social media honeydew melon fans, and summer fruit showcases.",
        "Key Message": "Stay Refreshed with Sweet Honeydew."
    },
    {
        "Product": "nectarine",
        "Target Customers": "Summer fruit enthusiasts, pie bakers, and vitamin seekers.",
        "Channel Platform": "Farmers' markets, online fruit shops, bakeries, and health food stores.",
        "Media": "Pie recipe blogs, vitamin-rich meal plans, social media nectarine fans, and summer fruit showcases.",
        "Key Message": "Juicy and Nutrient-Packed Summer Delight."
    },
    {
        "Product": "goji berry",
        "Target Customers": "Health-conscious snackers, antioxidant seekers, and superfood enthusiasts.",
        "Channel Platform": "Health food stores, online superfood shops, smoothie cafes, and wellness centers.",
        "Media": "Superfood benefits, antioxidant-rich meal plans, social media goji berry fans, and wellness articles.",
        "Key Message": "Elevate Your Health with Nutrient-Rich Goji Berries."
    },
    {
        "Product": "acai berry",
        "Target Customers": "Smoothie lovers, health-conscious individuals, and superfood enthusiasts.",
        "Channel Platform": "Smoothie bars, online superfood shops, health food stores, and wellness centers.",
        "Media": "Superfood smoothie recipes, wellness articles, social media acai berry fans, and health-conscious meal plans.",
        "Key Message": "Fuel Your Wellness Journey with Acai Power."
    },
    {
        "Product": "rambutan",
        "Target Customers": "Exotic fruit explorers, fruit platter creators, and tropical fruit enthusiasts.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, fruit platter catering services, and tropical fruit markets.",
        "Media": "Exotic fruit platter inspirations, tropical fruit showcases, social media rambutan fans, and fruit exploration blogs.",
        "Key Message": "Delve into the Exotic Beauty of Rambutan."
    },
    {
        "Product": "boysenberry",
        "Target Customers": "Jam makers, pie bakers, and berry lovers.",
        "Channel Platform": "Farmers' markets, online fruit shops, pie bakeries, and specialty fruit jam producers.",
        "Media": "Jam-making recipes, pie recipe blogs, social media boysenberry fans, and berry dessert showcases.",
        "Key Message": "The Perfect Blend of Sweet and Tart."
    },
    {
        "Product": "mangosteen",
        "Target Customers": "Exotic fruit enthusiasts, health-conscious individuals, and tropical fruit lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, health food stores, and tropical fruit markets.",
        "Media": "Exotic fruit health benefits, tropical fruit showcases, social media mangosteen fans, and fruit exploration blogs.",
        "Key Message": "Experience the Queen of Fruits - Pure Tropical Delight."
    },
    {
        "Product": "durian",
        "Target Customers": "Adventurous eaters, durian aficionados, and Southeast Asian cuisine lovers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit markets.",
        "Media": "Durian recipe blogs, Southeast Asian cuisine showcases, social media durian enthusiasts, and exotic fruit guides.",
        "Key Message": "Indulge in the King of Fruits - A Unique Flavor Adventure."
    },
    {
        "Product": "longan",
        "Target Customers": "Fruit salad makers, Asian cuisine enthusiasts, and exotic fruit explorers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Asian restaurants, and fruit salad catering services.",
        "Media": "Exotic fruit salad recipes, Asian cuisine inspirations, social media longan fans, and fruit exploration blogs.",
        "Key Message": "Discover the Sweet and Fragrant World of Longan."
    },
    {
        "Product": "jackfruit",
        "Target Customers": "Vegans, plant-based eaters, and tropical fruit lovers.",
        "Channel Platform": "Ethnic grocery stores, online vegan food shops, tropical fruit markets, and plant-based restaurants.",
        "Media": "Vegan recipes, plant-based meal plans, social media jackfruit fans, and tropical fruit showcases.",
        "Key Message": "Discover the Versatility of Jackfruit - The Vegan Meat Substitute."
    },
    {
        "Product": "tamarind",
        "Target Customers": "Cooking enthusiasts, tropical flavor lovers, and Thai cuisine fans.",
        "Channel Platform": "Asian grocery stores, online exotic spice shops, Thai restaurants, and fruit markets.",
        "Media": "Thai cuisine recipes, tropical flavor inspirations, social media tamarind fans, and exotic spice guides.",
        "Key Message": "Add a Tangy Twist to Your Culinary Creations with Tamarind."
    },
    {
        "Product": "mamey sapote",
        "Target Customers": "Fruit lovers, Latin cuisine enthusiasts, and exotic fruit explorers.",
        "Channel Platform": "Ethnic grocery stores, online Latin food shops, Latin restaurants, and fruit markets.",
        "Media": "Latin cuisine recipes, exotic fruit explorations, social media mamey sapote fans, and fruit exploration blogs.",
        "Key Message": "Savor the Creamy Goodness of Mamey Sapote."
    },
    {
        "Product": "sapodilla",
        "Target Customers": "Exotic fruit enthusiasts, fruit salad makers, and Latin American cuisine lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, Latin American restaurants, and fruit salad catering services.",
        "Media": "Exotic fruit salad recipes, Latin American cuisine inspirations, social media sapodilla fans, and fruit exploration blogs.",
        "Key Message": "Discover the Sweet and Grainy Delight of Sapodilla."
    },
    {
        "Product": "custard apple",
        "Target Customers": "Exotic fruit explorers, dessert lovers, and tropical fruit enthusiasts.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, dessert cafes, and tropical fruit markets.",
        "Media": "Exotic fruit dessert recipes, tropical fruit showcases, social media custard apple fans, and fruit exploration blogs.",
        "Key Message": "Indulge in the Creamy Sweetness of Custard Apple."
    },
    {
        "Product": "rose apple (Chomphu)",
        "Target Customers": "Exotic fruit enthusiasts, fruit salad makers, and Thai fruit aficionados.",
        "Channel Platform": "Thai grocery stores, online exotic fruit shops, fruit salad cafes, and Thai fruit markets.",
        "Media": "Exotic fruit salad recipes, Thai fruit showcases, social media rose apple fans, and fruit exploration blogs.",
        "Key Message": "Experience the Delicate Flavor of Rose Apple (Chomphu)."
    },
    {
        "Product": "santol",
        "Target Customers": "Exotic fruit explorers, Southeast Asian cuisine lovers, and fruit platter creators.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit platter catering services.",
        "Media": "Exotic fruit platter inspirations, Southeast Asian cuisine showcases, social media santol fans, and fruit exploration blogs.",
        "Key Message": "Discover the Sweet and Sour Bliss of Santol."
    },
    {
        "Product": "langsat",
        "Target Customers": "Exotic fruit explorers, fruit platter creators, and Southeast Asian fruit lovers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit platter catering services.",
        "Media": "Exotic fruit platter inspirations, Southeast Asian fruit showcases, social media langsat fans, and fruit exploration blogs.",
        "Key Message": "Savor the Sweet and Tangy Perfection of Langsat (Lansium Parasiticum)."
    },
    {
        "Product": "pomelo",
        "Target Customers": "Citrus lovers, health-conscious individuals, and Thai fruit enthusiasts.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, health food stores, and fruit markets.",
        "Media": "Citrus health benefits, Thai fruit showcases, social media pomelo fans, and fruit exploration blogs.",
        "Key Message": "Experience the Citrus Elegance of Pomelo."
    },
    {
        "Product": "makok",
        "Target Customers": "Exotic fruit explorers, adventurous eaters, and Southeast Asian fruit lovers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit markets.",
        "Media": "Exotic fruit explorations, Southeast Asian cuisine blogs, social media makok fans, and fruit exploration blogs.",
        "Key Message": "Taste the Exotic Appeal of Makok (Cerbera Odollam)."
    },
    {
        "Product": "rambeh",
        "Target Customers": "Exotic fruit enthusiasts, Southeast Asian cuisine lovers, and fruit platter creators.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit platter catering services.",
        "Media": "Exotic fruit platter inspirations, Southeast Asian cuisine showcases, social media rambeh fans, and fruit exploration blogs.",
        "Key Message": "Discover the Unique Flavor of Rambeh (Baccaurea Ramiflora)."
    },
    {
        "Product": "tamarind",
        "Target Customers": "Cooking enthusiasts, tropical flavor lovers, and Thai cuisine fans.",
        "Channel Platform": "Asian grocery stores, online exotic spice shops, Thai restaurants, and fruit markets.",
        "Media": "Thai cuisine recipes, tropical flavor inspirations, social media tamarind fans, and exotic spice guides.",
        "Key Message": "Add a Tangy Twist to Your Culinary Creations with Tamarind."
    },
    {
        "Product": "cherimoya",
        "Target Customers": "Exotic fruit enthusiasts, fruit salad makers, and dessert lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, dessert cafes, and tropical fruit markets.",
        "Media": "Exotic fruit salad recipes, dessert inspirations, social media cherimoya fans, and fruit exploration blogs.",
        "Key Message": "Savor the Exotic Creaminess of Cherimoya."
    },
    {
        "Product": "mango",
        "Target Customers": "Tropical fruit lovers, smoothie enthusiasts, and fruit salad makers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, smoothie bars, and tropical fruit markets.",
        "Media": "Tropical fruit smoothie recipes, fruit salad inspirations, social media mango fans, and fruit exploration blogs.",
        "Key Message": "Enjoy the Juicy Sweetness of Fresh Mango."
    },
    {
        "Product": "mangoesteen",
        "Target Customers": "Exotic fruit enthusiasts, health-conscious individuals, and tropical fruit lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, health food stores, and tropical fruit markets.",
        "Media": "Exotic fruit health benefits, tropical fruit showcases, social media mangosteen fans, and fruit exploration blogs.",
        "Key Message": "Experience the Queen of Fruits - Pure Tropical Delight."
    },
    {
        "Product": "papaya",
        "Target Customers": "Exotic fruit lovers, tropical smoothie enthusiasts, and digestive health seekers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, smoothie bars, and health food stores.",
        "Media": "Exotic fruit health benefits, tropical smoothie recipes, social media papaya fans, and digestive health articles.",
        "Key Message": "Embrace the Tropical Bliss of Papaya."
    },
    {
        "Product": "langsat",
        "Target Customers": "Exotic fruit explorers, fruit platter creators, and Southeast Asian fruit lovers.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, Southeast Asian restaurants, and fruit platter catering services.",
        "Media": "Exotic fruit platter inspirations, Southeast Asian fruit showcases, social media langsat fans, and fruit exploration blogs.",
        "Key Message": "Savor the Sweet and Tangy Perfection of Langsat (Lansium Parasiticum)."
    },
    {
        "Product": "sapodilla",
        "Target Customers": "Exotic fruit enthusiasts, fruit salad makers, and Latin American cuisine lovers.",
        "Channel Platform": "Ethnic grocery stores, online exotic fruit shops, Latin American restaurants, and fruit salad catering services.",
        "Media": "Exotic fruit salad recipes, Latin American cuisine inspirations, social media sapodilla fans, and fruit exploration blogs.",
        "Key Message": "Discover the Sweet and Grainy Delight of Sapodilla."
    },
    {
        "Product": "champada",
        "Target Customers": "Exotic fruit explorers, dessert lovers, and tropical fruit enthusiasts.",
        "Channel Platform": "Asian grocery stores, online exotic fruit shops, dessert cafes, and tropical fruit markets.",
        "Media": "Exotic fruit dessert recipes, tropical fruit showcases, social media champada fans, and fruit exploration blogs.",
        "Key Message": "Indulge in the Exotic Sweetness of Champada."
    },
    {
        "Product": "mamey sapote",
        "Target Customers": "Fruit lovers, Latin cuisine enthusiasts, and exotic fruit explorers.",
        "Channel Platform": "Ethnic grocery stores, online Latin food shops, Latin restaurants, and fruit markets.",
        "Media": "Latin cuisine recipes, exotic fruit explorations, social media mamey sapote fans, and fruit exploration blogs.",
        "Key Message": "Savor the Creamy Goodness of Mamey Sapote."
    },
]


st.header("fruits marketing helper")

inputfruit = st.text_input("What fruit do you want to sell",)
check=True
# time.sleep(1)
if inputfruit:
    check=False
    fruit = word_tokenize(inputfruit.lower())
    for word in fruit: 
        for i in range(0,len(fruits)):
            if word in word_tokenize(fruits[i].get('Product')):
                st.write(fruits[i].get('Product'),'target customers are',fruits[i].get('Target Customers'),'\n','You can sell or advertising at',fruits[i].get('Channel Platform'),'\n','Type of media are',fruits[i].get('Media'),'\n','The key message is',fruits[i].get('Key Message'))
                check = True
                break
if check==False:
    st.write('We don'+'\'t', 'have','that','data')       
            
