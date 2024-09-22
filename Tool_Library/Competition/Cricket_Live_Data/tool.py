import requests


def get_response(url, headers, **kargs):
    response = requests.get(url, params=kargs, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def series(api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = "https://cricket-live-data.p.rapidapi.com/series"
    return get_response(url, headers)


def fixtures(api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = "https://cricket-live-data.p.rapidapi.com/fixtures"
    return get_response(url, headers)


def fixtures_by_series(series_id: int, api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = f"https://cricket-live-data.p.rapidapi.com/fixtures-by-series/{series_id}"
    return get_response(url, headers)


def fixtures_by_date(date: str, api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = f"https://cricket-live-data.p.rapidapi.com/fixtures-by-date/{date}"

    return get_response(url, headers)


def results(api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = "https://cricket-live-data.p.rapidapi.com/results"
    return get_response(url, headers)


def results_by_date(date: str, api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = f"https://cricket-live-data.p.rapidapi.com/results-by-date/{date}"
    return get_response(url, headers)


def match_scorecard(match_id: int, api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
    }
    url = f"https://cricket-live-data.p.rapidapi.com/match/{match_id}"
    return get_response(url, headers)


if __name__ == '__main__':
    print(series(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(fixtures(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(fixtures_by_series(606, api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(fixtures_by_date("2020-09-21", api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(results(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(results_by_date("2020-09-20", api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(match_scorecard(2432999, api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
