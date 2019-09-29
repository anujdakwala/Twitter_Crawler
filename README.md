# Twitter_Crawler
Know Your Customers Interests.

# Example 1 - Get tweets by username 
python Exporter.py --username "ThreeUK" --maxtweets 100

# Example 2 - Get tweets by query search 
python Exporter.py --querysearch "ThreeUK" --maxtweets 100

# Example 3 - Get tweets by username and bound dates 
python Exporter.py --username "ThreeUK" --since 2019-09-10 --until 2019-09-12 --maxtweets 100

# Example 4 - Get the last 10 top tweets by username
python Exporter.py --username "ThreeUK" --maxtweets 100 --toptweets
