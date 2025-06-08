import sqlite3
import pandas as pd

# Connect to the Chinook database
conn = sqlite3.connect('chinook.db')

# -------------------------------
# Task 1: Customer Purchases Analysis
# -------------------------------

query_total_spent = """
SELECT 
    c.CustomerId, 
    c.FirstName || ' ' || c.LastName AS CustomerName, 
    SUM(i.Total) AS TotalSpent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
"""
customer_purchases = pd.read_sql_query(query_total_spent, conn)

# Top 5 customers by total purchase amount
top_customers = customer_purchases.sort_values(by="TotalSpent", ascending=False).head(5)
print("Top 5 Customers by Total Purchase Amount:")
print(top_customers)

# -------------------------------
# Task 2: Album vs. Individual Track Purchases
# -------------------------------

# Load necessary tables
invoice_items = pd.read_sql_query("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

# Merge invoice items with tracks to get album info
purchases = invoice_items.merge(tracks, on="TrackId")

# Get total number of tracks per album
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.columns = ["AlbumId", "TotalTracks"]

# Count number of tracks bought per invoice/album combo
customer_album = purchases.groupby(["InvoiceId", "AlbumId"]).agg({
    "TrackId": "count"
}).reset_index()

customer_album = customer_album.merge(album_track_counts, on="AlbumId")
customer_album["FullAlbum"] = customer_album["TrackId"] == customer_album["TotalTracks"]

# Merge back to identify invoices that purchased full albums
full_album_invoices = customer_album[customer_album["FullAlbum"]]["InvoiceId"].unique()
all_invoices = purchases["InvoiceId"].unique()

# Determine preference
prefer_individual = set(all_invoices) - set(full_album_invoices)
percentage_individual = len(prefer_individual) / len(all_invoices) * 100

print(f"\nPercentage of customers who prefer individual tracks: {percentage_individual:.2f}%")

# Close DB connection
conn.close()
