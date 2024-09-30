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

    Example Values
    --------------

    `"2023_01_DET_KC"`

    `"2023_01_CAR_ATL"`

    `"2023_01_HOU_BAL"`

    `"2023_01_CIN_CLE"`

    `"2023_01_JAX_IND"`

    """

    header = "game_id"


class Season:
    """
    The year of the NFL season. This represents the whole season, so regular season games that happen in January as well as playoff games will occur in the year after this number.

    Example Values
    --------------

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    """

    header = "season"


class GameType:
    """
    What type of game? One of REG, WC, DIV, CON, SB

    Example Values
    --------------

    `"REG"`

    `"REG"`

    `"REG"`

    `"REG"`

    `"REG"`

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

    Example Values
    --------------

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    """

    header = "week"


class Gameday:
    """
    The date on which the game occurred.

    Example Values
    --------------

    `"2023-09-07"`

    `"2023-09-10"`

    `"2023-09-10"`

    `"2023-09-10"`

    `"2023-09-10"`

    """

    header = "gameday"


class Weekday:
    """
    The day of the week on which the game occcured.

    Example Values
    --------------

    `"Thursday"`

    `"Sunday"`

    `"Sunday"`

    `"Sunday"`

    `"Sunday"`

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

    Example Values
    --------------

    `"20:20"`

    `"13:00"`

    `"13:00"`

    `"13:00"`

    `"13:00"`

    """

    header = "gametime"


class AwayTeam:
    """
    The away team.

    Example Values
    --------------

    `"DET"`

    `"CAR"`

    `"HOU"`

    `"CIN"`

    `"JAX"`

    """

    header = "away_team"


class AwayScore:
    """
    The number of points the away team scored. Is NA for games which haven't yet been played.

    Example Values
    --------------

    `21.0`

    `10.0`

    `9.0`

    `3.0`

    `31.0`

    """

    header = "away_score"


class HomeTeam:
    """
    The home team. Note that this contains the designated home team for games which no team is playing at home such as Super Bowls or NFL International games.

    Example Values
    --------------

    `"KC"`

    `"ATL"`

    `"BAL"`

    `"CLE"`

    `"IND"`

    """

    header = "home_team"


class HomeScore:
    """
    The number of points the home team scored. Is NA for games which haven't yet been played.

    Example Values
    --------------

    `20.0`

    `24.0`

    `25.0`

    `24.0`

    `21.0`

    """

    header = "home_score"


class Location:
    """
    Either Home if the home team is playing in their home stadium, or Neutral if the game is being played at a neutral location. This still shows as Home for games between the Giants and Jets even though they share the same home stadium.

    Example Values
    --------------

    `"Home"`

    `"Home"`

    `"Home"`

    `"Home"`

    `"Home"`

    """

    header = "location"

    HOME = "Home"
    NEUTRAL = "Neutral"


class Result:
    """
    The number of points the home team scored minus the number of points the visiting team scored. Equals h_score - v_score. Is NA for games which haven't yet been played. Convenient for evaluating against the spread bets.

    Example Values
    --------------

    `-1.0`

    `14.0`

    `16.0`

    `21.0`

    `-10.0`

    """

    header = "result"


class Total:
    """
    The sum of each team's score in the game. Equals h_score + v_score. Is NA for games which haven't yet been played. Convenient for evaluating over/under total bets.

    Example Values
    --------------

    `41.0`

    `34.0`

    `34.0`

    `27.0`

    `52.0`

    """

    header = "total"


class Overtime:
    """
    Binary indicator of whether or not game went to overtime.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "overtime"


class OldGameId:
    """
    The old id for the game assigned by the NFL.

    Example Values
    --------------

    `"2023090700"`

    `"2023091000"`

    `"2023091001"`

    `"2023091002"`

    `"2023091003"`

    """

    header = "old_game_id"


class Gsis:
    """
    The id of the game issued by the NFL Game Statistics &amp; Information System.

    Example Values
    --------------

    `"59173"`

    `"59174"`

    `"59175"`

    `"59176"`

    `"59177"`

    """

    header = "gsis"


class NflDetailId:
    """
    The id of the game issued by NFL Detail.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "nfl_detail_id"


class Pfr:
    """
    The id of the game issued by [Pro-Football-Reference](https://www.pro-football-reference.com/)

    Example Values
    --------------

    `"202309070kan"`

    `"202309100atl"`

    `"202309100rav"`

    `"202309100cle"`

    `"202309100clt"`

    """

    header = "pfr"


class Pff:
    """
    The id of the game issued by [Pro Football Focus](https://www.pff.com/)

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "pff"


class Espn:
    """
    The id of the game issued by [ESPN](https://www.espn.com/)

    Example Values
    --------------

    `"401547353"`

    `"401547403"`

    `"401547396"`

    `"401547397"`

    `"401547404"`

    """

    header = "espn"


class Ftn:
    """
    No documentation available.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "ftn"


class AwayRest:
    """
    Days of rest that the away team is coming off of.

    Example Values
    --------------

    `"7"`

    `"7"`

    `"7"`

    `"7"`

    `"7"`

    """

    header = "away_rest"


class HomeRest:
    """
    Days of rest that the home team is coming off of.

    Example Values
    --------------

    `"7"`

    `"7"`

    `"7"`

    `"7"`

    `"7"`

    """

    header = "home_rest"


class AwayMoneyline:
    """
    Odds for away team to win the game.

    Example Values
    --------------

    `164.0`

    `160.0`

    `380.0`

    `-112.0`

    `-205.0`

    """

    header = "away_moneyline"


class HomeMoneyline:
    """
    Odds for home team to win the game.

    Example Values
    --------------

    `-198.0`

    `-192.0`

    `-500.0`

    `-108.0`

    `170.0`

    """

    header = "home_moneyline"


class SpreadLine:
    """
    The spread line for the game. A positive number means the home team was favored by that many points, a negative number means the away team was favored by that many points. This lines up with the result column.

    Example Values
    --------------

    `4.0`

    `3.5`

    `9.5`

    `-1.0`

    `-4.0`

    """

    header = "spread_line"


class AwaySpreadOdds:
    """
    Odds for away team to cover the spread.

    Example Values
    --------------

    `-110.0`

    `-108.0`

    `-110.0`

    `-105.0`

    `-108.0`

    """

    header = "away_spread_odds"


class HomeSpreadOdds:
    """
    Odds for home team to cover the spread.

    Example Values
    --------------

    `-110.0`

    `-112.0`

    `-110.0`

    `-115.0`

    `-112.0`

    """

    header = "home_spread_odds"


class TotalLine:
    """
    The total line for the game.

    Example Values
    --------------

    `53.0`

    `40.5`

    `43.5`

    `46.5`

    `45.5`

    """

    header = "total_line"


class UnderOdds:
    """
    Odds that total score of game would be under the total_line.

    Example Values
    --------------

    `-110.0`

    `-110.0`

    `-110.0`

    `-110.0`

    `-110.0`

    """

    header = "under_odds"


class OverOdds:
    """
    Odds that total score of game would be over the total_ine.

    Example Values
    --------------

    `-110.0`

    `-110.0`

    `-110.0`

    `-110.0`

    `-110.0`

    """

    header = "over_odds"


class DivGame:
    """
    Binary indicator of whether or not game was played by 2 teams in the same division.

    Example Values
    --------------

    `"0"`

    `"1"`

    `"0"`

    `"1"`

    `"1"`

    """

    header = "div_game"

    TRUE = 1
    FALSE = 0


class Roof:
    """
    What was the status of the stadium's roof? One of outdoors, open, closed, dome

    Example Values
    --------------

    `"outdoors"`

    `"closed"`

    `"outdoors"`

    `"outdoors"`

    `"closed"`

    """

    header = "roof"

    OUTDOORS = "outdoors"
    CLOSED = "closed"
    DOME = "dome"
    OPEN = "open"


class Surface:
    """
    What type of ground the game was played on

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

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

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "temp"


class Wind:
    """
    The speed of the wind in miles/hour (for outdoors and open only)

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "wind"


class AwayQbId:
    """
    GSIS Player ID for away team starting quarterback.

    Example Values
    --------------

    `"00-0033106"`

    `"00-0039150"`

    `"00-0039163"`

    `"00-0036442"`

    `"00-0036971"`

    """

    header = "away_qb_id"


class HomeQbId:
    """
    GSIS Player ID for home team starting quarterback.

    Example Values
    --------------

    `"00-0033873"`

    `"00-0038122"`

    `"00-0034796"`

    `"00-0033537"`

    `"00-0039164"`

    """

    header = "home_qb_id"


class AwayQbName:
    """
    Name of away team starting QB.

    Example Values
    --------------

    `"Jared Goff"`

    `"Bryce Young"`

    `"C.J. Stroud"`

    `"Joe Burrow"`

    `"Trevor Lawrence"`

    """

    header = "away_qb_name"


class HomeQbName:
    """
    Name of home team starting QB.

    Example Values
    --------------

    `"Patrick Mahomes"`

    `"Desmond Ridder"`

    `"Lamar Jackson"`

    `"Deshaun Watson"`

    `"Anthony Richardson"`

    """

    header = "home_qb_name"


class AwayCoach:
    """
    Name of the head coach of the away team

    Example Values
    --------------

    `"Dan Campbell"`

    `"Frank Reich"`

    `"DeMeco Ryans"`

    `"Zac Taylor"`

    `"Doug Pederson"`

    """

    header = "away_coach"


class HomeCoach:
    """
    Name of the head coach of the home team

    Example Values
    --------------

    `"Andy Reid"`

    `"Arthur Smith"`

    `"John Harbaugh"`

    `"Kevin Stefanski"`

    `"Shane Steichen"`

    """

    header = "home_coach"


class Referee:
    """
    Name of the game's referee (head official)

    Example Values
    --------------

    `"John Hussey"`

    `"Brad Rogers"`

    `"Tra Blake"`

    `"Clete Blakeman"`

    `"Clay Martin"`

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

    Example Values
    --------------

    `"KAN00"`

    `"ATL97"`

    `"BAL00"`

    `"CLE00"`

    `"IND00"`

    """

    header = "stadium_id"


class Stadium:
    """
    Name of the stadium

    Example Values
    --------------

    `"GEHA Field at Arrowhead Stadium"`

    `"Mercedes-Benz Stadium"`

    `"M&T Bank Stadium"`

    `"FirstEnergy Stadium"`

    `"Lucas Oil Stadium"`

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
