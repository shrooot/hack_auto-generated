from google_play_scraper import app
import pandas as pd
import numpy as np

from google_play_scraper import Sort, reviews_all, reviews

def get_all_reviews(lang, country, sort):
   all_reviews, _continuation_token = reviews("com.branch_international.branch.branch_demo_android", lang=lang, country=country, sort=sort, count = 15000)
   print(len(all_reviews))

   df_reviews = pd.DataFrame(np.array(all_reviews), columns=["review"])
   df_reviews = df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
   df_reviews = df_reviews[['content']]

   df_reviews.to_csv("in-playstore-reviews.csv")

if __name__ == "__main__":
   get_all_reviews('en', 'in', Sort.NEWEST)