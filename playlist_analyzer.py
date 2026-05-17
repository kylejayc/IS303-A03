"""
Kyle Christensen
IS 303 - A03

Inputs:
- Number of songs (int)
- For each song: title (string), duration in seconds (int), genre (string)

Processes:
- Accumulator: calculate total playtime
- Min/Max: find the longest song
- Filter: build a list of songs by specific genre

Outputs:
- Print each song title, duration, and genre
- Print total playtime, longest song, and songs in selected genre
"""

# Collect songs from user
songs = []

num_songs = int(input("How many songs are in your playlist? "))

for i in range(num_songs):
    print(f"\nSong {i + 1}:")
    title = input("  Song title: ")
    duration = int(input("  Duration (seconds): "))
    genre = input("  Genre: ")
    
    song = {
        "title": title,
        "duration": duration,
        "genre": genre
    }
    songs.append(song)

# Process the playlist
print("\n" + "="*13)
print("YOUR PLAYLIST")
print("="*13)

# Print all songs
for song in songs:
    print(f"{song['title']} - {song['duration']} sec. ({song['genre']})")

# Accumulator pattern --> total playtime
total_seconds = 0
for song in songs:
    total_seconds += song['duration']

# Min/Max pattern --> find longest song
longest_song = songs[0]
for song in songs:
    if song['duration'] > longest_song['duration']:
        longest_song = song

# Filter pattern --> find songs by genre
search_genre = input(f"\nWhich genre would you like to filter by? ")
favorite_songs = []
for song in songs:
    if song['genre'].lower() == search_genre.lower():
        favorite_songs.append(song)

# Summary output
print("\n" + "="*16)
print("PLAYLIST SUMMARY")
print("="*16)
total_minutes = total_seconds // 60
total_secs = total_seconds % 60
print(f"Total playtime: {total_minutes}m {total_secs}s")
print(f"Longest song: {longest_song['title']} ({longest_song['duration']}s)")
print(f"\nSongs in {search_genre} genre: {len(favorite_songs)}")
for song in favorite_songs:
    print(f"  - {song['title']}")