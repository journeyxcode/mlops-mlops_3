import os

import pandas as pd
from dotenv import load_dotenv

from preprocessing import TMDBPreProcessor
from crawler import TMDBCrawler

load_dotenv()

def make_result_folder_crawler():
    # 현재 실행 중인 파이썬 파일의 절대 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result_path = os.path.join(script_dir, "result")

    os.makedirs(result_path, exist_ok=True)
    # print(f"result 폴더 위치: {result_path}")


def run_popular_movie_crawler():
    tmdb_crawler = TMDBCrawler()
    result = tmdb_crawler.get_bulk_popular_movies(start_page=1, end_page=1)
    tmdb_crawler.save_movies_to_json_file(result, "./result", "popular")

    tmdb_preprocessor = TMDBPreProcessor(result)
    tmdb_preprocessor.run()
    tmdb_preprocessor.save("watch_log")


if __name__ == '__main__':
    make_result_folder_crawler()
    run_popular_movie_crawler()
