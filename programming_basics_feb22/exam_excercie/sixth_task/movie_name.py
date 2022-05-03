best_movie = ''
score = 0
number_of_movies = 0

while number_of_movies < 7:
    movie = input()
    current_score =  0

    if movie == 'STOP':
        break

    number_of_movies += 1

    for i in range(len(movie)):
        current_score += ord(movie[i])
        if (movie[i]).isupper():
            current_score -= len(movie)
        if (movie[i]).islower():
            current_score -= 2 * len(movie)

    if current_score > score:
        score = current_score
        best_movie = movie

if number_of_movies == 7:
    print(f'The limit is reached.')

print(f'The best movie for you is {best_movie} with {score} ASCII sum.')


