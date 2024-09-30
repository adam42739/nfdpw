"""
=================
Schedules columns
=================

Header names are accesible as _column_.header.

```python
>>> cols.GameId.header
>>> "game_id"
```

Some categorical columns provide encoded values.

```python
>>> cols.GameType.REG
>>> "REG"
```

"""


class GameId:
    """
    A human-readable game ID. It consists of: the season, an underscore, the two-digit week number, an underscore, the away team, an underscore, the home team. This is the primary identifier for a given game and is also used in various nflverse dataframes.
    """

    header = "game_id"


class Season:
    """
    The year of the NFL season. This represents the whole season, so regular season games that happen in January as well as playoff games will occur in the year after this number.
    """

    header = "season"


class GameType:
    """
    What type of game? One of REG, WC, DIV, CON, SB
    """

    header = "game_type"

    REG = "REG"
    WC = "WC"
    DIV = "DIV"
    CON = "CON"
    SB = "SB"


class Week:
    """
    The week of the NFL season the game occurs in. Please note that the `game_type` will differ for weeks &gt;= 18 because of the season expansion in 2021. Please use `game_type` to filter for regular season or postseason.
    """

    header = "week"


class Gameday:
    """
    The date on which the game occurred.
    """

    header = "gameday"


class Weekday:
    """
    The day of the week on which the game occcured.
    """

    header = "weekday"

    THURSDAY = "Thursday"
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Gametime:
    """
    The kickoff time of the game. This is represented in 24-hour time and the Eastern time zone, regardless of what time zone the game was being played in.
    """

    header = "gametime"


class AwayTeam:
    """
    The away team.
    """

    header = "away_team"


class AwayScore:
    """
    The number of points the away team scored. Is NA for games which haven't yet been played.
    """

    header = "away_score"


class HomeTeam:
    """
    The home team. Note that this contains the designated home team for games which no team is playing at home such as Super Bowls or NFL International games.
    """

    header = "home_team"


class HomeScore:
    """
    The number of points the home team scored. Is NA for games which haven't yet been played.
    """

    header = "home_score"


class Location:
    """
    Either Home if the home team is playing in their home stadium, or Neutral if the game is being played at a neutral location. This still shows as Home for games between the Giants and Jets even though they share the same home stadium.
    """

    header = "location"

    HOME = "Home"
    NEUTRAL = "Neutral"


class Result:
    """
    The number of points the home team scored minus the number of points the visiting team scored. Equals h_score - v_score. Is NA for games which haven't yet been played. Convenient for evaluating against the spread bets.
    """

    header = "result"


class Total:
    """
    The sum of each team's score in the game. Equals h_score + v_score. Is NA for games which haven't yet been played. Convenient for evaluating over/under total bets.
    """

    header = "total"


class Overtime:
    """
    Binary indicator of whether or not game went to overtime.
    """

    header = "overtime"


class OldGameId:
    """
    The old id for the game assigned by the NFL.
    """

    header = "old_game_id"


class Gsis:
    """
    The id of the game issued by the NFL Game Statistics &amp; Information System.
    """

    header = "gsis"


class NflDetailId:
    """
    The id of the game issued by NFL Detail.
    """

    header = "nfl_detail_id"


class Pfr:
    """
    The id of the game issued by [Pro-Football-Reference](https://www.pro-football-reference.com/)
    """

    header = "pfr"


class Pff:
    """
    The id of the game issued by [Pro Football Focus](https://www.pff.com/)
    """

    header = "pff"


class Espn:
    """
    The id of the game issued by [ESPN](https://www.espn.com/)
    """

    header = "espn"


class Ftn:
    """
    No documentation available.
    """

    header = "ftn"


class AwayRest:
    """
    Days of rest that the away team is coming off of.
    """

    header = "away_rest"


class HomeRest:
    """
    Days of rest that the home team is coming off of.
    """

    header = "home_rest"


class AwayMoneyline:
    """
    Odds for away team to win the game.
    """

    header = "away_moneyline"


class HomeMoneyline:
    """
    Odds for home team to win the game.
    """

    header = "home_moneyline"


class SpreadLine:
    """
    The spread line for the game. A positive number means the home team was favored by that many points, a negative number means the away team was favored by that many points. This lines up with the result column.
    """

    header = "spread_line"


class AwaySpreadOdds:
    """
    Odds for away team to cover the spread.
    """

    header = "away_spread_odds"


class HomeSpreadOdds:
    """
    Odds for home team to cover the spread.
    """

    header = "home_spread_odds"


class TotalLine:
    """
    The total line for the game.
    """

    header = "total_line"


class UnderOdds:
    """
    Odds that total score of game would be under the total_line.
    """

    header = "under_odds"


class OverOdds:
    """
    Odds that total score of game would be over the total_ine.
    """

    header = "over_odds"


class DivGame:
    """
    Binary indicator of whether or not game was played by 2 teams in the same division.
    """

    header = "div_game"

    TRUE = 1
    FALSE = 0


class Roof:
    """
    What was the status of the stadium's roof? One of outdoors, open, closed, dome
    """

    header = "roof"

    OUTDOORS = "outdoors"
    CLOSED = "closed"
    DOME = "dome"
    OPEN = "open"


class Surface:
    """
    What type of ground the game was played on
    """

    header = "surface"

    GRASS = "grass"
    FIELDTURF = "fieldturf"
    SPORTTURF = "sportturf"
    A_TURF = "a_turf"
    ASTROTURF = "astroturf"
    MATRIXTURF = "matrixturf"


class Temp:
    """
    The temperature at the stadium (for outdoors and open only)
    """

    header = "temp"


class Wind:
    """
    The speed of the wind in miles/hour (for outdoors and open only)
    """

    header = "wind"


class AwayQbId:
    """
    GSIS Player ID for away team starting quarterback.
    """

    header = "away_qb_id"


class HomeQbId:
    """
    GSIS Player ID for home team starting quarterback.
    """

    header = "home_qb_id"


class AwayQbName:
    """
    Name of away team starting QB.
    """

    header = "away_qb_name"


class HomeQbName:
    """
    Name of home team starting QB.
    """

    header = "home_qb_name"


class AwayCoach:
    """
    Name of the head coach of the away team
    """

    header = "away_coach"


class HomeCoach:
    """
    Name of the head coach of the home team
    """

    header = "home_coach"


class Referee:
    """
    Name of the game's referee (head official)
    """

    header = "referee"

    JOHN_HUSSEY = "John Hussey"
    BRAD_ROGERS = "Brad Rogers"
    TRA_BLAKE = "Tra Blake"
    CLETE_BLAKEMAN = "Clete Blakeman"
    CLAY_MARTIN = "Clay Martin"
    SCOTT_NOVAK = "Scott Novak"
    RON_TORBERT = "Ron Torbert"
    ALEX_KEMP = "Alex Kemp"
    ALAN_ECK = "Alan Eck"
    CRAIG_WROLSTAD = "Craig Wrolstad"
    BILL_VINOVICH = "Bill Vinovich"
    BRAD_ALLEN = "Brad Allen"
    SHAWN_HOCHULI = "Shawn Hochuli"
    SHAWN_SMITH = "Shawn Smith"
    ADRIAN_HILL = "Adrian Hill"
    CARL_CHEFFERS = "Carl Cheffers"
    LAND_CLARK = "Land Clark"


class StadiumId:
    """
    ID of Stadium that game took place in
    """

    header = "stadium_id"


class Stadium:
    """
    Name of the stadium
    """

    header = "stadium"

    GEHA_FIELD_AT_ARROWHEAD_STADIUM = "GEHA Field at Arrowhead Stadium"
    MERCEDESBENZ_STADIUM = "Mercedes-Benz Stadium"
    MT_BANK_STADIUM = "M&T Bank Stadium"
    FIRSTENERGY_STADIUM = "FirstEnergy Stadium"
    LUCAS_OIL_STADIUM = "Lucas Oil Stadium"
    US_BANK_STADIUM = "U.S. Bank Stadium"
    MERCEDESBENZ_SUPERDOME = "Mercedes-Benz Superdome"
    ACRISURE_STADIUM = "Acrisure Stadium"
    FEDEXFIELD = "FedExField"
    SOLDIER_FIELD = "Soldier Field"
    EMPOWER_FIELD_AT_MILE_HIGH = "Empower Field at Mile High"
    SOFI_STADIUM = "SoFi Stadium"
    GILLETTE_STADIUM = "Gillette Stadium"
    LUMEN_FIELD = "Lumen Field"
    METLIFE_STADIUM = "MetLife Stadium"
    LINCOLN_FINANCIAL_FIELD = "Lincoln Financial Field"
    NEW_ERA_FIELD = "New Era Field"
    PAYCOR_STADIUM = "Paycor Stadium"
    FORD_FIELD = "Ford Field"
    NRG_STADIUM = "NRG Stadium"
    TIAA_BANK_STADIUM = "TIAA Bank Stadium"
    RAYMOND_JAMES_STADIUM = "Raymond James Stadium"
    NISSAN_STADIUM = "Nissan Stadium"
    STATE_FARM_STADIUM = "State Farm Stadium"
    ATT_STADIUM = "AT&T Stadium"
    BANK_OF_AMERICA_STADIUM = "Bank of America Stadium"
    LEVIS_STADIUM = "Levi's Stadium"
    LAMBEAU_FIELD = "Lambeau Field"
    HARD_ROCK_STADIUM = "Hard Rock Stadium"
    ALLEGIANT_STADIUM = "Allegiant Stadium"
    WEMBLEY_STADIUM = "Wembley Stadium"
    TOTTENHAM_STADIUM = "Tottenham Stadium"
    DEUTSCHE_BANK_PARK = "Deutsche Bank Park"
