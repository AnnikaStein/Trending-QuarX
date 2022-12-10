[![pages-build-deployment](https://github.com/AnnikaStein/Trending-QuarX/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/AnnikaStein/Trending-QuarX/actions/workflows/pages/pages-build-deployment)
[![Trending-QuarX-Runner](https://github.com/AnnikaStein/Trending-QuarX/actions/workflows/trending-quarx-runner.yml/badge.svg)](https://github.com/AnnikaStein/Trending-QuarX/actions/workflows/trending-quarx-runner.yml)

# Trending QuarX

Mirror, mirror on the wall, who is the quarkiest one of all? Find this week's most popular quarks by scraping preprints of a given category. Addressing the world's most pressing questions in a very serious way. /s

Run the backend portion with `python3 backend/main.py` and `python3 backend/merge.py` - stores this week's results in a .csv, which is readable for the frontend. Convenience script: `cd backend && bash run_weekly.sh`