HOST = "https://lichess.org"
LICHESS_API_KEY = "lip_sFV84xtP1PED3upDYp0Y"
ADMINS = ["the-international-bullet-league"]
TEAMS_WHITELIST = ["the-international-bullet-league"]

TOURNAMENTS = [
    {
        "name": "International Bullet Arena",
        "clockTime": 1,
        "clockIncrement": 0,
        "minutes": 360,
        "variant": "standard",
        "schedule": "0 0 * * *",
        "team": "the-international-bullet-league",
        "token": LICHESS_API_KEY
    },
    {
        "name": "International Bullet Arena",
        "clockTime": 1,
        "clockIncrement": 0,
        "minutes": 360,
        "variant": "standard",
        "schedule": "0 6 * * *",
        "team": "the-international-bullet-league",
        "token": LICHESS_API_KEY
    },
    {
        "name": "International Bullet Arena",
        "clockTime": 1,
        "clockIncrement": 0,
        "minutes": 360,
        "variant": "standard",
        "schedule": "0 12 * * *",
        "team": "the-international-bullet-league",
        "token": LICHESS_API_KEY
    },
    {
        "name": "International Bullet Arena",
        "clockTime": 1,
        "clockIncrement": 0,
        "minutes": 360,
        "variant": "standard",
        "schedule": "0 18 * * *",
        "team": "the-international-bullet-league",
        "token": LICHESS_API_KEY
    }
]
