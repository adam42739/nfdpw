"""
====================
Drafts columns
====================

Header names are accesible as _column_.header.

```python
>>> cols.Status.header
>>> "status"
```

Some categorical columns provide encoded values.

```python
>>> cols.Status.RET
>>> "RET"
```

"""


class Season:
    """
    Draft Year

    Example Values
    --------------

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    """

    header = "season"


class Round:
    """
    Draft round

    Example Values
    --------------

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    """

    header = "round"


class Pick:
    """
    Draft overall pick

    Example Values
    --------------

    `"1"`

    `"2"`

    `"3"`

    `"4"`

    `"5"`

    """

    header = "pick"


class Team:
    """
    Draft team

    Example Values
    --------------

    `"CAR"`

    `"HOU"`

    `"HOU"`

    `"IND"`

    `"SEA"`

    """

    header = "team"


class GsisId:
    """
    ID for joining with nflverse data

    Example Values
    --------------

    `"00-0039150"`

    `"00-0039163"`

    `"00-0039108"`

    `"00-0039164"`

    `"00-0039169"`

    """

    header = "gsis_id"


class PfrPlayerId:
    """
    ID from Pro Football Reference

    Example Values
    --------------

    `"YounBr01"`

    `"StroCJ00"`

    `"AndeWi01"`

    `"RichAn03"`

    `"WithDe00"`

    """

    header = "pfr_id"


class CfbPlayerId:
    """
    ID from College Football Reference

    Example Values
    --------------

    `"bryce-young-1"`

    `"cj-stroud-1"`

    `"will-anderson-jr-1"`

    `"anthony-richardson-2"`

    `"devon-witherspoon-1"`

    """

    header = "cfbref_id"


class PfrPlayerName:
    """
    Player’s name as recorded by PFR

    Example Values
    --------------

    `"Bryce Young"`

    `"C.J. Stroud"`

    `"Will Anderson"`

    `"Anthony Richardson"`

    `"Devon Witherspoon"`

    """

    header = "pfr_player_name"


class Hof:
    """
    Whether player has been selected to the Pro Football Hall of Fame

    Example Values
    --------------

    `"False"`

    `"False"`

    `"False"`

    `"False"`

    `"False"`

    """

    header = "hof"


class Position:
    """
    Player position as recorded by PFR

    Example Values
    --------------

    `"QB"`

    `"QB"`

    `"LB"`

    `"QB"`

    `"DB"`

    """

    header = "position"

    QB = "QB"
    LB = "LB"
    DB = "DB"
    OL = "OL"
    OLB = "OLB"
    RB = "RB"
    DL = "DL"
    DE = "DE"
    CB = "CB"
    WR = "WR"
    TE = "TE"
    DT = "DT"
    C = "C"
    T = "T"
    NT = "NT"
    S = "S"
    K = "K"
    G = "G"
    P = "P"


class Category:
    """
    Broader category of player positions

    Example Values
    --------------

    `"QB"`

    `"QB"`

    `"LB"`

    `"QB"`

    `"DB"`

    """

    header = "category"

    QB = "QB"
    LB = "LB"
    DB = "DB"
    OL = "OL"
    RB = "RB"
    DL = "DL"
    WR = "WR"
    TE = "TE"
    K = "K"
    P = "P"


class Side:
    """
    O for offense, D for defense, S for special teams

    Example Values
    --------------

    `"O"`

    `"O"`

    `"D"`

    `"O"`

    `"D"`

    """

    header = "side"


class College:
    """
    College attended in final year

    Example Values
    --------------

    `"Alabama"`

    `"Ohio St."`

    `"Alabama"`

    `"Florida"`

    `"Illinois"`

    """

    header = "college"

    ALABAMA = "Alabama"
    OHIO_ST = "Ohio St."
    FLORIDA = "Florida"
    ILLINOIS = "Illinois"
    TEXAS_TECH = "Texas Tech"
    TEXAS = "Texas"
    GEORGIA = "Georgia"
    TENNESSEE = "Tennessee"
    NORTHWESTERN = "Northwestern"
    IOWA = "Iowa"
    IOWA_ST = "Iowa St."
    MISSISSIPPI_ST = "Mississippi St."
    OREGON = "Oregon"
    PITTSBURGH = "Pittsburgh"
    TCU = "TCU"
    BOSTON_COL = "Boston Col."
    USC = "USC"
    MARYLAND = "Maryland"
    UTAH = "Utah"
    MICHIGAN = "Michigan"
    OKLAHOMA = "Oklahoma"
    CLEMSON = "Clemson"
    KANSAS_ST = "Kansas St."
    PENN_ST = "Penn St."
    KENTUCKY = "Kentucky"
    NOTRE_DAME = "Notre Dame"
    AUBURN = "Auburn"
    SYRACUSE = "Syracuse"
    MISSISSIPPI = "Mississippi"
    LSU = "LSU"
    OREGON_ST = "Oregon St."
    WISCONSIN = "Wisconsin"
    GEORGIA_TECH = "Georgia Tech"
    NORTH_DAKOTA_ST = "North Dakota St."
    MICHIGAN_ST = "Michigan St."
    SOUTH_CAROLINA = "South Carolina"
    UCLA = "UCLA"
    SMU = "SMU"
    MIAMI_FL = "Miami (FL)"
    MINNESOTA = "Minnesota"
    ARKANSAS = "Arkansas"
    HOUSTON = "Houston"
    SACRAMENTO_ST = "Sacramento St."
    SOUTH_DAKOTA_ST = "South Dakota St."
    NORTH_CAROLINA = "North Carolina"
    TULANE = "Tulane"
    LOUISVILLE = "Louisville"
    TEXAS_AM = "Texas A&M"
    WASHINGTON_ST = "Washington St."
    WAKE_FOREST = "Wake Forest"
    STANFORD = "Stanford"
    WESTERN_KENTUCKY = "Western Kentucky"
    BAYLOR = "Baylor"
    CINCINNATI = "Cincinnati"
    OLD_DOMINION = "Old Dominion"
    BYU = "BYU"
    TROY = "Troy"
    NORTH_CAROLINA_ST = "North Carolina St."
    EASTERN_MICHIGAN = "Eastern Michigan"
    VIRGINIA_TECH = "Virginia Tech"
    MISSOURI = "Missouri"
    FRESNO_ST = "Fresno St."
    SAN_JOSE_ST = "San Jose St."
    OKLAHOMA_ST = "Oklahoma St."
    PURDUE = "Purdue"
    FLORIDA_ST = "Florida St."
    WILLIAM__MARY = "William & Mary"
    SOUTH_ALABAMA = "South Alabama"
    CALIFORNIA = "California"
    VIRGINIA = "Virginia"
    APPALACHIAN_ST = "Appalachian St."
    SF_AUSTIN = "S.F. Austin"
    SOUTHERN_MISS = "Southern Miss"
    BOWLING_GREEN = "Bowling Green"
    BOISE_ST = "Boise St."
    WESTERN_MICHIGAN = "Western Michigan"
    NEBRASKA = "Nebraska"
    NEW_MEXICO = "New Mexico"
    RUTGERS = "Rutgers"
    PRINCETON = "Princeton"
    LIBERTY = "Liberty"
    WAGNER = "Wagner"
    WEST_VIRGINIA = "West Virginia"
    KENNESAW_ST = "Kennesaw St."
    ALABIRMINGHAM = "Ala-Birmingham"
    WINGATE = "Wingate"
    UT_MARTIN = "UT Martin"
    ARIZONA_ST = "Arizona St."
    LOUISIANA = "Louisiana"
    CENTRAL_MICHIGAN = "Central Michigan"
    NORTHERN_MICHIGAN = "Northern Michigan"
    JACKSON_ST = "Jackson St."
    BALL_ST = "Ball St."
    CHARLOTTE = "Charlotte"
    TOLEDO = "Toledo"


class Age:
    """
    Player age as of draft

    Example Values
    --------------

    `22.0`

    `21.0`

    `22.0`

    `21.0`

    `22.0`

    """

    header = "age"


class To:
    """
    Final season played in NFL

    Example Values
    --------------

    `2024.0`

    `2024.0`

    `2024.0`

    `2024.0`

    `2024.0`

    """

    header = "to"


class Allpro:
    """
    Number of AP First Team All-Pro selections as recorded by PFR

    Example Values
    --------------

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    """

    header = "allpro"


class Probowls:
    """
    Number of Pro Bowls

    Example Values
    --------------

    `"0"`

    `"1"`

    `"1"`

    `"0"`

    `"1"`

    """

    header = "probowls"

    TRUE = 1
    FALSE = 0


class SeasonsStarted:
    """
    Number of seasons recorded as primary starter for position

    Example Values
    --------------

    `"1"`

    `"1"`

    `"1"`

    `"0"`

    `"1"`

    """

    header = "seasons_started"

    TRUE = 1
    FALSE = 0


class WAv:
    """
    Weighted Approximate Value

    Example Values
    --------------

    `6.0`

    `14.0`

    `10.0`

    `3.0`

    `6.0`

    """

    header = "w_av"


class CarAv:
    """
    Career Approximate Value

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "car_av"


class DrAv:
    """
    Draft Approximate Value

    Example Values
    --------------

    `6.0`

    `14.0`

    `10.0`

    `3.0`

    `6.0`

    """

    header = "dr_av"


class Games:
    """
    Games played in career

    Example Values
    --------------

    `17.0`

    `16.0`

    `16.0`

    `5.0`

    `15.0`

    """

    header = "games"


class PassCompletions:
    """
    Career pass completions

    Example Values
    --------------

    `328.0`

    `343.0`

    `0.0`

    `59.0`

    `0.0`

    """

    header = "pass_completions"


class PassAttempts:
    """
    Career pass attempts

    Example Values
    --------------

    `557.0`

    `531.0`

    `0.0`

    `103.0`

    `0.0`

    """

    header = "pass_attempts"


class PassYards:
    """
    Career pass yards thrown

    Example Values
    --------------

    `3038.0`

    `4342.0`

    `0.0`

    `789.0`

    `0.0`

    """

    header = "pass_yards"


class PassTds:
    """
    Career pass touchdowns thrown

    Example Values
    --------------

    `11.0`

    `25.0`

    `0.0`

    `5.0`

    `0.0`

    """

    header = "pass_tds"


class PassInts:
    """
    Career pass interceptions thrown

    Example Values
    --------------

    `12.0`

    `5.0`

    `0.0`

    `2.0`

    `0.0`

    """

    header = "pass_ints"


class RushAtts:
    """
    Career rushing attempts

    Example Values
    --------------

    `43.0`

    `43.0`

    `0.0`

    `31.0`

    `0.0`

    """

    header = "rush_atts"


class RushYards:
    """
    Career rushing yards

    Example Values
    --------------

    `265.0`

    `180.0`

    `0.0`

    `192.0`

    `0.0`

    """

    header = "rush_yards"


class RushTds:
    """
    Career rushing touchdowns

    Example Values
    --------------

    `1.0`

    `3.0`

    `0.0`

    `5.0`

    `0.0`

    """

    header = "rush_tds"


class Receptions:
    """
    Career receptions

    Example Values
    --------------

    `0.0`

    `1.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "receptions"


class RecYards:
    """
    Career receiving yards

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "rec_yards"


class RecTds:
    """
    Career receiving touchdowns

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "rec_tds"


class DefSoloTackles:
    """
    Career solo tackles

    Example Values
    --------------

    `nan`

    `nan`

    `31.0`

    `nan`

    `61.0`

    """

    header = "def_solo_tackles"


class DefInts:
    """
    Career interceptions

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `1.0`

    """

    header = "def_ints"


class DefSacks:
    """
    Career sacks

    Example Values
    --------------

    `nan`

    `nan`

    `7.0`

    `nan`

    `3.0`

    """

    header = "def_sacks"
