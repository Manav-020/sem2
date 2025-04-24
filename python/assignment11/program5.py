import pandas as pd


data = {
    "date": ["2023-01-15", "2023-01-20", "2023-02-10", "2023-02-15", "2023-01-15"],
    "artist": ["Divine", "Honey singh", "Divine", "Tylor Swift", "Divine"],
    "venue": ["Surat", "Mumbai", "Banglore", "Delhi", "Delhi"]
}
concerts = pd.DataFrame(data)

concerts["year_month"] = pd.to_datetime(concerts["date"]).dt.to_period("M")


artists = pd.Series(concerts["artist"].unique())
venues = pd.Series(concerts["venue"].unique())


artist_venue_pairs = [(artist, venue) for artist in artists for venue in venues]

wide_table = pd.DataFrame({"year_month": concerts["year_month"].unique()})
wide_table["year_month"] = wide_table["year_month"].astype(str)  
for artist, venue in artist_venue_pairs:
    count = concerts[(concerts["artist"] == artist) & (concerts["venue"] == venue)].groupby("year_month").size()
    wide_table[f"{artist}, {venue}"] = wide_table["year_month"].map(count).fillna(0).astype(int)

print(wide_table)