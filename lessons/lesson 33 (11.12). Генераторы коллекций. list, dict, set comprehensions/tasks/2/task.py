tracks = [
    ("Imagine Dragons", "Believer"),
    ("Muse", "Uprising"),
    ("Daft Punk", "Harder Better")
]
plays = [
    ("Believer", 95),
    ("Uprising", 70),
    ("Harder Better", 110)
]
average_plays = sum(play for _, play in plays) / len(plays)

result = [f"{artist} — {title} ({play}прослушиваний)"
          for artist, title in tracks
          for p_title, play in plays
          if title == p_title and play > average_plays]
print(result)
