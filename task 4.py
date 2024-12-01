# Sample dataset of movies
movies = [
    {"Title": "Inception", "Genre": "Sci-Fi, Thriller", "Description": "A thief who enters dreams to steal secrets."},
    {"Title": "The Matrix", "Genre": "Sci-Fi, Action", "Description": "A hacker discovers the truth about his reality."},
    {"Title": "Interstellar", "Genre": "Sci-Fi, Drama", "Description": "Astronauts explore a wormhole in space."},
    {"Title": "The Dark Knight", "Genre": "Action, Crime", "Description": "A vigilante fights crime in Gotham City."},
    {"Title": "Avengers", "Genre": "Action, Superhero", "Description": "Superheroes unite to save the world."}
]

# Function to calculate similarity score
def calculate_similarity(user_input, movie):
    # Split user input and movie content into words
    user_words = set(user_input.lower().split())
    movie_words = set((movie["Genre"] + " " + movie["Description"]).lower().split())
    # Count common words
    return len(user_words & movie_words)

# Function to recommend movies
def recommend_movies(user_input, top_n=3):
    scores = []
    for movie in movies:
        score = calculate_similarity(user_input, movie)
        scores.append((score, movie))
    # Sort by score in descending order
    scores.sort(reverse=True, key=lambda x: x[0])
    # Return top_n recommendations
    recommendations = [movie for score, movie in scores if score > 0]
    return recommendations[:top_n]

# Main interaction loop
def movie_recommendation_system():
    print("Welcome to the Movie Recommendation System!")
    print("Tell me what type of movies you like (e.g., 'Sci-Fi and Action') or describe them.")
    
    while True:
        user_input = input("\nEnter your preference (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        recommendations = recommend_movies(user_input)
        if recommendations:
            print("\nBased on your input, here are some recommendations:")
            for movie in recommendations:
                print(f"- {movie['Title']} ({movie['Genre']}): {movie['Description']}")
        else:
            print("\nSorry, no matching movies found. Try describing your preferences differently.")

# Run the recommendation system
if __name__ == "__main__":
    movie_recommendation_system()