import random

movies = {
    "action": ["RRR", "Pushpa", "Baahubali", "Salaar", "Dasara"],
    "comedy": ["Jathi Ratnalu", "DJ Tillu", "F2", "Ready", "Bhale Bhale Magadivoy"],
    "romance": ["Geetha Govindam", "Ye Maaya Chesave", "Tholi Prema", "Majili", "Ninnu Kori"],
    "family": ["Seethamma Vakitlo Sirimalle Chettu", "Attarintiki Daredi", "Shatamanam Bhavati"],
    "thriller": ["Evaru", "HIT", "Agent Sai Srinivasa Athreya", "Kshanam", "Shyam Singha Roy"]
}

print("🎬 Movie Recommendation System")
print("Available genres: action, comedy, romance, family, thriller")

user_choice = input("Enter your favorite genre: ").lower()

if user_choice in movies:
    
    print("\nRecommended Movies for you:\n")
    
    recommendations = random.sample(movies[user_choice], 3)
    
    for movie in recommendations:
        print("•", movie)

else:
    print("\nSorry, we don't have recommendations for that genre.")