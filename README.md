# Movie Recommendation System

A simple web app that recommends movies based on your selection using content-based filtering. Built with Streamlit.

## Features

- Select a movie and get 5 similar movie recommendations.
- Movie posters are fetched automatically from TMDB.
- No need to download large model files manually; they are loaded from Google Drive at runtime if not present locally.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sheikh-mohammad-rakib/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Tools and Technology

- **Python 3.x**: Core programming language for backend logic and data processing.
- **Streamlit**: For building and deploying the interactive web application.
- **Pandas**: Used for data manipulation and analysis.
- **Scikit-learn**: Used for content-based filtering and similarity computation.
- **Pickle**: For serializing and loading precomputed model files.
- **Requests**: To fetch movie posters and interact with external APIs.
- **gdown**: To download large model files directly from Google Drive.
- **Google Drive**: Storage and distribution of large model files.

## Folder Structure

```
movie-recommendation-system/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment (e.g., Heroku)
├── setup.sh                # Setup script for deployment
├── README.md               # Project documentation
├── model/
│   ├── similarity.pkl      # Precomputed similarity matrix (downloaded or loaded from Google Drive)
│   ├── movie_list.pkl      # Movie metadata (downloaded or loaded from Google Drive)
│   └── information.md      # Links and info for model files
└── ...
```

## Model Files

The model files required for this app are:

- **`similarity.pkl`**: Contains the precomputed similarity matrix between movies, used to find and rank similar movies based on content features.
- **`movie_list.pkl`**: Contains the list of movies along with their metadata (such as titles, IDs, and possibly genres or other features).

These files are relatively large and, by default, are loaded directly from Google Drive at runtime to avoid manual downloads and to keep the repository lightweight.

### Running Locally Without Downloading Each Time

If you prefer to have the model files available locally (for faster startup and offline use), follow these steps:

1. **Download the model files manually:**
   - Visit the links provided in [`model/information.md`](model/information.md) to download both `similarity.pkl` and `movie_list.pkl` from Google Drive.
   - Make sure you are logged in to a Google account if required, and download each file to your computer.

2. **Place the files:**
   - Move both `similarity.pkl` and `movie_list.pkl` into the `model` directory located at the root of this project (`movie-recommendation-system/model/`).

3. **Verify placement:**
   - Your directory structure should look like:
     ```
     movie-recommendation-system/
       ├── app.py
       ├── model/
       │    ├── similarity.pkl
       │    └── movie_list.pkl
       └── ...
     ```

The app will automatically use the local files if they are present in the `model` directory; otherwise, it will attempt to fetch them from Google Drive at runtime.

## Deployment

For deployment (e.g., on Heroku), the `Procfile` and `setup.sh` are provided.

## License

MIT License.