import requests

# https://rapidapi.com/api-sports/api/api-basketball


def get_response(url, headers, **kargs):
    response = requests.get(url, params=kargs, headers=headers)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation


def timezone(
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/timezone"
    return get_response(url, headers)


def bookmakers(
    id: int = None,
    search: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/bookmakers"
    params = {"search": search, "id": id}
    return get_response(url, headers, **params)


def bets(
    id: int = None,
    search: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/bets"
    params = {"search": search, "id": id}
    return get_response(url, headers, **params)


def odds(
    league: int = None,
    season: str = None,
    game: int = None,
    bookmaker: int = None,
    bet: int = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/odds"
    params = {"league": league, "season": season,
              "game": game, "bookmaker": bookmaker, "bet": bet}
    return get_response(url, headers, **params)


def standings(
    league: int,
    season: str,
    team: int = None,
    stage: str = None,
    group: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/standings"
    params = {"league": league, "season": season,
              "stage": stage, "group": group, "team": team}
    return get_response(url, headers, **params)


def stages_or_groups(
        target: str,
        league: int,
        season: str, api_key: enumerate = ""):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = f"https://api-basketball.p.rapidapi.com/standings/{target}"
    params = {"league": league, "season": season}
    return get_response(url, headers, **params)


def seasons(
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    url = "https://api-basketball.p.rapidapi.com/seasons"
    return get_response(url, headers)


def countries(
    id: int = None,
    name: str = None,
    code: str = None,
    search: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    params = {"name": name, "id": id, "code": code, "search": search}
    url = "https://api-basketball.p.rapidapi.com/countries"
    return get_response(url, headers, **params)


def leagues(
    id: int = None,
    name: str = None,
    country_id: int = None,
    country: str = None,
    type: str = None,
    season: str = None,
    search: str = None,
    code: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    params = {"country": country, "id": id, "type": type, "season": season,
              "name": name, "code": code, "search": search, "country_id": country_id}
    url = "https://api-basketball.p.rapidapi.com/leagues"

    return get_response(url, headers, **params)


def head_2_head(
    h2h: str,
    league: int = None,
    season: str = None,
    timezone: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    params = {"h2h": h2h, "league": league,
              "season": season, "timezone": timezone}
    url = "https://api-basketball.p.rapidapi.com/games"

    return get_response(url, headers, **params)


def game(
    id: int = None,
    date: str = None,
    league: int = None,
    season: str = None,
    team: int = None,
    timezone: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    params = {"timezone": timezone, "season": season,
              "id": id, "league": league, "date": date, "team": team}
    url = "https://api-basketball.p.rapidapi.com/games"

    return get_response(url, headers, **params)


def teams_statistics(
    season: str,
    league: int,
    team: int,
    date: str = None,
    api_key: enumerate = ""
):
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    params = {"season": season, "league": league, "team": team, "date": date}
    url = "https://api-basketball.p.rapidapi.com/statistics"

    return get_response(url, headers, **params)


if __name__ == '__main__':
    print(bookmakers(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(timezone(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(bets(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(odds(league=8,season="2012",api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(standings(league=12,season="2019-2020",api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(stages_or_groups(target="stages", league=12, season="2019-2020",api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    # print(groups(league=12,season="2019-2020","a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(seasons(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(countries(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(leagues(api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(head_2_head("142-144",api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    # print(games(date="2019-11-26", "a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))
    print(teams_statistics(season="2019-2020",league=12,team=133,api_key="a66d5c29b7msh5d13d2401681e5ap10e83fjsn0da541a8162b"))