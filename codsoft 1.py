import pandas as pd

# Create a sample movie dataset with 5 movies
data = {
    'movie_title': ['Patriotic', 'Lagaan', 'Kalki', 'Munjya', 'Conjuring'],
    'genre': ['Drama', 'Drama', 'Thriller', 'Horror', 'Horror'],
    'director': ['michael dorman', 'ashutosh gowariker', 'nag ashwin', 'aditya sarpotdar', 'james wan'],
    'actor': ['xyz', 'aamir khan', 'prabhas', 'Abhay verma', 'patrick wilson'],
    'release_year': [2005, 2001, 2024, 2024, 2013],
    'user_rating': [8.9, 8.5, 9.6, 7.0, 8.0],
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to find movies based on entered rating
def find_movies_by_rating(entered_rating, threshold=1.0):
    # Filter movies based on user rating being close to entered_rating
    filtered_movies = df[(df['user_rating'] >= entered_rating - threshold) & 
                         (df['user_rating'] <= entered_rating + threshold)]
    return filtered_movies[['movie_title', 'genre', 'director', 'user_rating']]

# Example: Enter a rating and find movies close to that rating
while True:
    try:
        entered_rating = float(input("Enter a movie rating (between 1.0 and 10.0): "))
        if entered_rating < 1.0 or entered_rating > 10.0:
            raise ValueError("Rating must be between 1.0 and 10.0")
        
        threshold = 1.0  # Adjust this threshold as needed to control the range of similarity

        # Find movies based on entered rating
        filtered_movies = find_movies_by_rating(entered_rating, threshold)

        # Display results
        print(f'Movies with ratings close to {entered_rating}:')
        print(filtered_movies)
        
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid rating.")