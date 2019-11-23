# coding: utf-8
from flask import Flask
from flask_restplus import Resource, Api
import pandas as pd
import json

apiApp = Flask(__name__)
api = Api(apiApp)
apiApp.debug = True


# Api start
@api.route('/movies/<string:title>')
class Movies(Resource):
    def get(self, title):
        if title not in df.index:
            api.abort(404, "Movie {} doesn't exist".format(title))
            # add new movie link
        movie = dict(df.loc[title])
        # add new movie link
        return movie

    def delete(self, title):
        if title not in df.index:
            api.abort(404, "Movie {} doesn't exist".format(title))
        df.drop(title, inplace=True)
        return {"message": "Movie {} is removed.".format(title)}

@api.route('/movies')
class getMovies(Resource):
    def get(self):
        movies = df.to_json(orient='index')
        return json.loads(movies)
# Api end

if __name__ == '__main__':
    # columns_to_drop = ['budget', 'genres', 'homepage', 'id', 'original_language',
    #                    'overview', 'popularity', 'production_companies',
    #                    'production_countries', 'release_date', 'revenue', 'runtime',
    #                    'spoken_languages', 'status', 'tagline', 'vote_average', 'vote_count']
    csv_file = "../data_analysis/movie_data.csv"
    df = pd.read_csv(csv_file, index_col=0)
    # df.drop(columns_to_drop, inplace=True, axis=1)
    # df.set_index('original_title', inplace=True)
    apiApp.run(port=5000)
