from google_play_scraper import app
import pandas as pd
import numpy as np

from google_play_scraper import Sort, reviews_all, reviews

def get_all_reviews(lang, country, sort):
   return reviews("com.branch_international.branch.branch_demo_android", lang=lang, country=country, sort=sort, count = 10000)

reviews, _continuation_token = get_all_reviews('en', 'in', Sort.NEWEST)

print(len(reviews))
