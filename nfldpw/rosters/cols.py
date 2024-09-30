"""
===============
Rosters columns
===============

Header names are accesible as _column_.header.

```python
>>> cols.Season.header
>>> "season"
```

Some categorical columns provide encoded values.

```python
>>> cols.Position.OL
>>> "OL"
```

"""


class Season:
    """
    NFL season. Defaults to current year after March, otherwise is previous year.
    """

    header = "season"


class Team:
    """
    NFL team. Uses official abbreviations as per NFL.com
    """

    header = "team"


class Position:
    """
    Primary position as reported by NFL.com
    """

    header = "position"

    OL = "OL"
    QB = "QB"
    K = "K"
    TE = "TE"
    LS = "LS"
    DL = "DL"
    WR = "WR"
    P = "P"
    DB = "DB"
    LB = "LB"
    RB = "RB"


class DepthChartPosition:
    """
    Position assigned on depth chart. Not always accurate!
    """

    header = "depth_chart_position"

    T = "T"
    QB = "QB"
    K = "K"
    TE = "TE"
    LS = "LS"
    DE = "DE"
    WR = "WR"
    P = "P"
    FS = "FS"
    G = "G"
    NT = "NT"
    SS = "SS"
    OLB = "OLB"
    CB = "CB"
    DT = "DT"
    RB = "RB"
    C = "C"
    ILB = "ILB"
    MLB = "MLB"
    FB = "FB"
    DB = "DB"
    LB = "LB"


class JerseyNumber:
    """
    Jersey number. Often useful for joins by name/team/jersey.
    """

    header = "jersey_number"


class Status:
    """
    Roster status: describes things like Active, Inactive, Injured Reserve, Practice Squad etc
    """

    header = "status"

    CUT = "CUT"
    DEV = "DEV"
    INA = "INA"
    ACT = "ACT"
    RES = "RES"
    RET = "RET"
    EXE = "EXE"
    TRC = "TRC"
    TRT = "TRT"
    PUP = "PUP"
    TRD = "TRD"
    E01 = "E01"
    E14 = "E14"


class PlayerName:
    """
    Name of the player
    """

    header = "player_name"


class FirstName:
    """
    First name as per NFL.com
    """

    header = "first_name"


class LastName:
    """
    Last name as per NFL.com
    """

    header = "last_name"


class BirthDate:
    """
    Birthdate, as recorded by Sleeper API
    """

    header = "birth_date"


class Height:
    """
    Official height, in inches
    """

    header = "height"


class Weight:
    """
    Official weight, in pounds
    """

    header = "weight"


class College:
    """
    Official college (usually the last one attended)
    """

    header = "college"

    ARKANSAS = "Arkansas"
    CALIFORNIA = "California"
    CENTRAL_FLORIDA = "Central Florida"
    UCLA = "UCLA"
    ARIZONA = "Arizona"
    COLORADO = "Colorado"
    NOTRE_DAME = "Notre Dame"
    DELAWARE = "Delaware"
    VIRGINIA_TECH = "Virginia Tech"
    MIAMI = "Miami"
    SAN_DIEGO = "San Diego"
    GEORGIA = "Georgia"
    MICHIGAN_STATE = "Michigan State"
    FLORIDA_STATE = "Florida State"
    SOUTHERN_METHODIST = "Southern Methodist"
    WESTERN_WASHINGTON = "Western Washington"
    BAYLOR = "Baylor"
    TENNESSEE = "Tennessee"
    RUTGERS = "Rutgers"
    INDIANA = "Indiana"
    HILLSDALE = "Hillsdale"
    TEXAS = "Texas"
    LOUISIANA_STATE = "Louisiana State"
    OKLAHOMA = "Oklahoma"
    MICHIGAN = "Michigan"
    SOUTH_FLORIDA = "South Florida"
    ALABAMA = "Alabama"
    TEXAS_CHRISTIAN = "Texas Christian"
    EAST_CAROLINA = "East Carolina"
    TEXAS_AANDM = "Texas A&amp;M"
    SOUTHERN_CALIFORNIA = "Southern California"
    MISSOURI = "Missouri"
    OHIO_STATE = "Ohio State"
    KENTUCKY = "Kentucky"
    EASTERN_WASHINGTON = "Eastern Washington"
    CINCINNATI = "Cincinnati"
    ARIZONA_STATE = "Arizona State"
    UTAH_STATE = "Utah State"
    CENTRAL_MICHIGAN = "Central Michigan"
    AUBURN = "Auburn"
    OREGON_STATE = "Oregon State"
    VIRGINIA = "Virginia"
    STANFORD = "Stanford"
    WYOMING = "Wyoming"
    SAN_DIEGO_STATE = "San Diego State"
    HOUSTON = "Houston"
    WEST_VIRGINIA = "West Virginia"
    MISSISSIPPI = "Mississippi"
    SOUTH_CAROLINA = "South Carolina"
    WISCONSIN = "Wisconsin"
    COASTAL_CAROLINA = "Coastal Carolina"
    PURDUE = "Purdue"
    PRESBYTERIAN = "Presbyterian"
    NEBRASKA = "Nebraska"
    SYRACUSE = "Syracuse"
    ARKANSAS_STATE = "Arkansas State"
    MISSOURI_WESTERN = "Missouri Western"
    MISSISSIPPI_STATE = "Mississippi State"
    IOWA = "Iowa"
    PENNSYLVANIA = "Pennsylvania"
    TEXAS_STATE = "Texas State"
    TEXAS_TECH = "Texas Tech"
    TEMPLE = "Temple"
    HARVARD = "Harvard"
    COLORADO_STATEPUEBLO = "Colorado State-Pueblo"
    ALABAMABIRMINGHAM = "Alabama-Birmingham"
    MINN_STATEMANKATO = "Minn. State-Mankato"
    ARKANSASPINE_BLUFF = "Arkansas-Pine Bluff"
    APPALACHIAN_STATE = "Appalachian State"
    SAN_JOSE_STATE = "San Jose State"
    IOWA_STATE = "Iowa State"
    SAMFORD = "Samford"
    CLEMSON = "Clemson"
    FLORIDA = "Florida"
    BALL_STATE = "Ball State"
    BRIGHAM_YOUNG = "Brigham Young"
    NORTH_CAROLINA = "North Carolina"
    KANSAS_STATE = "Kansas State"
    JAMES_MADISON = "James Madison"
    BUFFALO = "Buffalo"
    PENN_STATE = "Penn State"
    BOISE_STATE = "Boise State"
    OREGON = "Oregon"
    COLORADO_STATE = "Colorado State"
    RICE = "Rice"
    BLOOMSBURG = "Bloomsburg"
    TULANE = "Tulane"
    LOUISVILLE = "Louisville"
    PITTSBURGH = "Pittsburgh"
    ILLINOIS_STATE = "Illinois State"
    FRESNO_STATE = "Fresno State"
    NORTHERN_ILLINOIS = "Northern Illinois"
    VANDERBILT = "Vanderbilt"
    EASTERN_ILLINOIS = "Eastern Illinois"
    LOUISIANA_TECH = "Louisiana Tech"
    CALIFORNIA_PA = "California, Pa."
    GEORGIA_SOUTHERN = "Georgia Southern"
    NEVADA = "Nevada"
    NORTH_DAKOTA_STATE = "North Dakota State"
    CANISIUS = "Canisius"
    MARIST = "Marist"
    NO_COLLEGE = "No College"
    WASHINGTON = "Washington"
    UTAH = "Utah"
    GEORGIA_TECH = "Georgia Tech"
    SOUTHERN_ILLINOIS = "Southern Illinois"
    MEMPHIS = "Memphis"
    MARYLAND = "Maryland"
    TEXASEL_PASO = "Texas-El Paso"
    MARSHALL = "Marshall"
    SACRAMENTO_STATE = "Sacramento State"
    OLD_DOMINION = "Old Dominion"
    IDAHO = "Idaho"
    MONTANA_STATE = "Montana State"
    TOLEDO = "Toledo"
    DUKE = "Duke"
    SOUTHERN_MISSISSIPPI = "Southern Mississippi"
    NORTHWESTERN = "Northwestern"
    NORTH_CAROLINA_STATE = "North Carolina State"
    MINNESOTA = "Minnesota"
    NAVY = "Navy"
    SOUTHERN_UTAH = "Southern Utah"
    GRAND_VALLEY_STATE = "Grand Valley State"
    ILLINOIS = "Illinois"
    HOLY_CROSS = "Holy Cross"
    WESTERN_KENTUCKY = "Western Kentucky"
    FLORIDA_ATLANTIC = "Florida Atlantic"
    GEORGIA_STATE = "Georgia State"
    CONNECTICUT = "Connecticut"
    WILLIAM_AND_MARY = "William &amp; Mary"
    AUGUSTANA_SD = "Augustana, S.D."
    SOUTH_CAROLINA_STATE = "South Carolina State"
    BOSTON_COLLEGE = "Boston College"
    WEST_ALABAMA = "West Alabama"
    MANITOBA_CAN = "Manitoba, Can."
    OKLAHOMA_STATE = "Oklahoma State"
    MIDDLE_TENNESSEE = "Middle Tennessee"
    ASSUMPTION = "Assumption"
    VIRGINIA_COMMONWEALTH = "Virginia Commonwealth"
    HAWAII = "Hawaii"
    WESTERN_MICHIGAN = "Western Michigan"
    WEST_GEORGIA = "West Georgia"
    MAINE = "Maine"
    VALDOSTA_STATE = "Valdosta State"
    GREENVILLE = "Greenville"
    NORTH_CAROLINA_AANDT = "North Carolina A&amp;T"
    DRAKE = "Drake"
    EAST_CENTRAL = "East Central"
    EASTERN_MICHIGAN = "Eastern Michigan"
    MASSACHUSETTS = "Massachusetts"
    KENTUCKY_WESLEYAN = "Kentucky Wesleyan"
    WESTERN_STATE_COLO = "Western State, Colo."
    INDIANA_STATE = "Indiana State"
    MISSOURI_STATE = "Missouri State"
    CHATTANOOGA = "Chattanooga"
    FLORIDA_INTERNATIONAL = "Florida International"
    SOUTH_ALABAMA = "South Alabama"
    VILLANOVA = "Villanova"
    NORTH_CAROLINACHARLOTTE = "North Carolina-Charlotte"
    YOUNGSTOWN_STATE = "Youngstown State"
    ALBANY_STATE_GA = "Albany State, Ga."
    DUQUESNE = "Duquesne"
    WASHINGTON_STATE = "Washington State"
    SOUTHERN_U = "Southern U."
    CENTRAL_ARKANSAS = "Central Arkansas"
    NORTH_TEXAS = "North Texas"
    EASTERN_KENTUCKY = "Eastern Kentucky"
    BRITISH_COLUMBIA_CAN = "British Columbia, Can."
    NORTHERN_IOWA = "Northern Iowa"
    WAGNER = "Wagner"
    FERRIS_STATE = "Ferris State"
    TEXASSAN_ANTONIO = "Texas-San Antonio"
    SOUTH_DAKOTA_STATE = "South Dakota State"
    KANSAS = "Kansas"
    WEBER_STATE = "Weber State"
    JACKSONVILLE_STATE = "Jacksonville State"
    YALE = "Yale"
    WESTERN_CAROLINA = "Western Carolina"
    SIOUX_FALLS = "Sioux Falls"
    GRAMBLING = "Grambling"
    BUCKNELL = "Bucknell"
    SOUTHERN_ARKANSAS = "Southern Arkansas"
    LIMESTONE = "Limestone"
    SOUTHEAST_MISSOURI = "Southeast Missouri"
    WAKE_FOREST = "Wake Forest"
    HUMBOLDT_STATE = "Humboldt State"
    FORDHAM = "Fordham"
    NEW_MEXICO = "New Mexico"
    LOUISIANALAFAYETTE = "Louisiana-Lafayette"
    FORT_HAYS_STATE = "Fort Hays State"
    STEPHEN_F_AUSTIN = "Stephen F. Austin"
    PRAIRIE_VIEW = "Prairie View"
    REGINA_CAN = "Regina, Can."
    TARLETON_STATE = "Tarleton State"
    ELON = "Elon"
    MALONE = "Malone"
    PRINCETON = "Princeton"
    AUSTIN_PEAY = "Austin Peay"
    LINDENWOOD = "Lindenwood"
    SAM_HOUSTON_STATE = "Sam Houston State"
    MARIAN_IND = "Marian, Ind."
    AZUSA_PACIFIC = "Azusa Pacific"
    CALIFORNIADAVIS = "California-Davis"
    AKRON = "Akron"
    ALABAMA_STATE = "Alabama State"
    CHARLESTON_W_VA = "Charleston, W. Va."
    BOWLING_GREEN = "Bowling Green"
    MORGAN_STATE = "Morgan State"
    STETSON_UNIVERSITY = "Stetson University"
    WAYNE_STATE_MICH = "Wayne State, Mich."
    LAMAR = "Lamar"
    BRYANT = "Bryant"
    KUTZTOWN = "Kutztown"
    DARTMOUTH = "Dartmouth"
    WASHBURN = "Washburn"
    BEMIDJI_STATE = "Bemidji State"
    WESTERN_ILLINOIS = "Western Illinois"
    MURRAY_STATE = "Murray State"
    LOUISIANAMONROE = "Louisiana-Monroe"
    ARMY = "Army"
    NORTHERN_COLORADO = "Northern Colorado"
    ALBANY_NY = "Albany, N.Y."
    MIAMI_O = "Miami, O."
    OHIO = "Ohio"
    SOUTH_DAKOTA = "South Dakota"
    ALBERTA_CAN = "Alberta, Can."
    MISSOURI_SANDT = "Missouri S&amp;T"
    BROWN = "Brown"
    CAL_POLY = "Cal Poly"
    NORFOLK_STATE = "Norfolk State"
    STONY_BROOK = "Stony Brook"
    NORTHERN_ARIZONA = "Northern Arizona"
    TENNESSEEMARTIN = "Tennessee-Martin"
    NORTH_CAROLINA_AT_PEMBROKE = "North Carolina at Pembroke"
    BERRY = "Berry"
    LENOIRRHYNE = "Lenoir-Rhyne"
    ST_JOHNS_MINN = "St. John's, Minn."
    NEW_MEXICO_STATE = "New Mexico State"
    TULSA = "Tulsa"
    RHODE_ISLAND = "Rhode Island"
    TENNESSEE_STATE = "Tennessee State"
    DAYTON = "Dayton"
    ALCORN_STATE = "Alcorn State"
    SAGINAW_VALLEY_STATE = "Saginaw Valley State"
    CENTRAL_MISSOURI = "Central Missouri"
    HOUSTON_BAPTIST = "Houston Baptist"
    AIR_FORCE = "Air Force"
    FAYETTEVILLE_STATE = "Fayetteville State"
    WISCONSINWHITEWATER = "Wisconsin-Whitewater"
    YORK_CAN = "York, Can."
    TUSCULUM = "Tusculum"
    FRAMINGHAM_STATE = "Framingham State"
    WEST_FLORIDA = "West Florida"
    INDIANA_PA = "Indiana, Pa."
    FORT_VALLEY_STATE = "Fort Valley State"
    CITADEL = "Citadel"
    NORTH_DAKOTA = "North Dakota"
    OUACHITA_BAPTIST = "Ouachita Baptist"
    NORTHWEST_MISSOURI_STATE = "Northwest Missouri State"
    JACKSON_STATE = "Jackson State"
    IDAHO_STATE = "Idaho State"
    TEXAS_AANDMCOMMERCE = "Texas A&amp;M-Commerce"
    MINOT_STATE = "Minot State"
    PITTSBURG_STATE = "Pittsburg State"
    PERU_STATE = "Peru State"
    MONTANA = "Montana"
    SACRED_HEART = "Sacred Heart"
    MERCER = "Mercer"
    FLORIDA_AANDM = "Florida A&amp;M"
    CULVERSTOCKTON = "Culver-Stockton"
    LIBERTY = "Liberty"
    FRIENDS = "Friends"
    WATERLOO_CAN = "Waterloo, Can."
    CALIFORNIA_LUTHERAN = "California Lutheran"
    KENNESAW_STATE = "Kennesaw State"
    NORTHERN_MICHIGAN = "Northern Michigan"
    SHEPHERD = "Shepherd"
    VIRGINIA_STATE = "Virginia State"
    LAFAYETTE = "Lafayette"
    MONMOUTH_NJ = "Monmouth, N.J."
    BENEDICTINE_KAN = "Benedictine, Kan."
    SOUTHEASTERN_OKLAHOMA = "Southeastern Oklahoma"
    MINNESOTADULUTH = "Minnesota-Duluth"
    GARDNERWEBB = "Gardner-Webb"
    NORTHWESTERN_STATE_LA = "Northwestern State, La."
    BUTLER = "Butler"
    KENT_STATE = "Kent State"
    CAMPBELL = "Campbell"
    MERRIMACK = "Merrimack"
    NORTHWOOD_MICH = "Northwood, Mich."
    INCARNATE_WORD = "Incarnate Word"
    PACE = "Pace"
    SOUTHEASTERN_LOUISIANA = "Southeastern Louisiana"
    FURMAN = "Furman"
    BOWIE_STATE = "Bowie State"
    TROY = "Troy"
    BALDWINWALLACE = "Baldwin-Wallace"
    LANE = "Lane"
    EAST_TENNESSEE_STATE = "East Tennessee State"
    NEVADALAS_VEGAS = "Nevada-Las Vegas"
    OKLAHOMA_BAPTIST = "Oklahoma Baptist"
    HENDERSON_STATE = "Henderson State"
    HAMPTON = "Hampton"
    WINGATE = "Wingate"
    WASHINGTON_MO = "Washington, Mo."
    RICHMOND = "Richmond"


class PlayerId:
    """
    ID of the player. Use this to join to other sources.
    """

    header = "player_id"


class EspnId:
    """
    Player ID for ESPN API
    """

    header = "espn_id"


class SportradarId:
    """
    Player ID for Sportradar API
    """

    header = "sportradar_id"


class YahooId:
    """
    Player ID for Yahoo API
    """

    header = "yahoo_id"


class RotowireId:
    """
    Player ID for Rotowire
    """

    header = "rotowire_id"


class PffId:
    """
    Player ID for Pro Football Focus
    """

    header = "pff_id"


class PfrId:
    """
    Player ID for Pro Football Reference
    """

    header = "pfr_id"


class FantasyDataId:
    """
    Player ID for FantasyData
    """

    header = "fantasy_data_id"


class SleeperId:
    """
    Player ID for Sleeper API
    """

    header = "sleeper_id"


class YearsExp:
    """
    Years played in league
    """

    header = "years_exp"


class HeadshotUrl:
    """
    A URL string that points to player photos used by NFL.com (or sometimes ESPN)
    """

    header = "headshot_url"


class NgsPosition:
    """
    No documentation available.
    """

    header = "ngs_position"

    T = "T"
    G = "G"
    QB = "QB"
    WR = "WR"
    TE = "TE"
    EDGE = "EDGE"
    INTERIOR_LINE = "INTERIOR_LINE"
    SLOT_CB = "SLOT_CB"
    SLOT_WR = "SLOT_WR"
    MLB = "MLB"
    SAFETY = "SAFETY"
    CB = "CB"
    C = "C"
    OLB = "OLB"
    FB = "FB"
    RB = "RB"


class Week:
    """
    Game week number
    """

    header = "week"


class GameType:
    """
    No documentation available.
    """

    header = "game_type"

    REG = "REG"
    WC = "WC"
    CON = "CON"
    DIV = "DIV"
    SB = "SB"


class StatusDescriptionAbbr:
    """
    No documentation available.
    """

    header = "status_description_abbr"

    W03 = "W03"
    P07 = "P07"
    A01 = "A01"
    R48 = "R48"
    R01 = "R01"
    R02 = "R02"
    R40 = "R40"
    E02 = "E02"
    R04 = "R04"
    P02 = "P02"
    I01 = "I01"
    R27 = "R27"
    R06 = "R06"
    R05 = "R05"
    R03 = "R03"
    R36 = "R36"
    P01 = "P01"
    R33 = "R33"
    I02 = "I02"
    P04 = "P04"
    R23 = "R23"
    P06 = "P06"
    R30 = "R30"
    P03 = "P03"
    R49 = "R49"
    E01 = "E01"
    E14 = "E14"


class FootballName:
    """
    Player's displayed football name.
    """

    header = "football_name"


class EsbId:
    """
    No documentation available.
    """

    header = "esb_id"


class GsisItId:
    """
    No documentation available.
    """

    header = "gsis_it_id"


class SmartId:
    """
    No documentation available.
    """

    header = "smart_id"


class EntryYear:
    """
    Player's first year rostered on an NFL team.
    """

    header = "entry_year"


class RookieYear:
    """
    Player's rookie year.
    """

    header = "rookie_year"


class DraftClub:
    """
    NFL team that drafted the player (if applicable).
    """

    header = "draft_club"


class DraftNumber:
    """
    Player's draft number.
    """

    header = "draft_number"


class Age:
    """
    Player's current age
    """

    header = "age"
