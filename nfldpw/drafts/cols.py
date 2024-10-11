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


class Status:
    """
    Roster status: describes things like Active, Inactive, Injured Reserve, Practice Squad etc

    Example Values
    --------------

    `"RET"`

    `"ACT"`

    `"DEV"`

    `"ACT"`

    `"RES"`

    """

    header = "status"

    RET = "RET"
    ACT = "ACT"
    DEV = "DEV"
    RES = "RES"
    CUT = "CUT"
    U01 = "U01"
    UFA = "UFA"
    TRD = "TRD"
    INA = "INA"
    TRC = "TRC"
    TRT = "TRT"
    RSN = "RSN"
    PUP = "PUP"
    NWT = "NWT"
    EXE = "EXE"
    RFA = "RFA"
    E14 = "E14"
    RSR = "RSR"
    SUS = "SUS"
    A02 = "A02"
    A03 = "A03"


class DisplayName:
    """
    Player's displayed football name.

    Example Values
    --------------

    `"'Omar Ellison"`

    `"A'Shawn Robinson"`

    `"A.J. Arcuri"`

    `"A.J. Barner"`

    `"A.J. Bouye"`

    """

    header = "display_name"


class FirstName:
    """
    First name as per NFL.com

    Example Values
    --------------

    `"'Omar"`

    `"A'Shawn"`

    `"A.J."`

    `"A.J."`

    `"Arlandus"`

    """

    header = "first_name"


class LastName:
    """
    Last name as per NFL.com

    Example Values
    --------------

    `"Ellison"`

    `"Robinson"`

    `"Arcuri"`

    `"Barner"`

    `"Bouye"`

    """

    header = "last_name"


class EsbId:
    """
    No documentation available.

    Example Values
    --------------

    `"ELL711319"`

    `"ROB367960"`

    `"ARC716900"`

    `"BAR235889"`

    `"BOU651714"`

    """

    header = "esb_id"


class GsisId:
    """
    character

    Example Values
    --------------

    `"00-0004866"`

    `"00-0032889"`

    `"00-0037845"`

    `"00-0039793"`

    `"00-0030228"`

    """

    header = "gsis_id"


class BirthDate:
    """
    Birthdate, as recorded by Sleeper API

    Example Values
    --------------

    `"1971-10-08"`

    `"1995-03-21"`

    `"1997-08-13"`

    `"2002-05-03"`

    `"1991-08-16"`

    """

    header = "birth_date"


class CollegeName:
    """
    Player's college.

    Example Values
    --------------

    `"None"`

    `"Alabama"`

    `"Michigan State"`

    `"Michigan"`

    `"Central Florida"`

    """

    header = "college_name"


class PositionGroup:
    """
    No documentation available.

    Example Values
    --------------

    `"WR"`

    `"DL"`

    `"OL"`

    `"TE"`

    `"DB"`

    """

    header = "position_group"

    WR = "WR"
    DL = "DL"
    OL = "OL"
    TE = "TE"
    DB = "DB"
    SPEC = "SPEC"
    RB = "RB"
    LB = "LB"
    QB = "QB"
    HC = "HC"


class Position:
    """
    character

    Example Values
    --------------

    `"WR"`

    `"DT"`

    `"T"`

    `"TE"`

    `"CB"`

    """

    header = "position"

    WR = "WR"
    DT = "DT"
    T = "T"
    TE = "TE"
    CB = "CB"
    G = "G"
    P = "P"
    DB = "DB"
    RB = "RB"
    LB = "LB"
    DE = "DE"
    QB = "QB"
    FS = "FS"
    OL = "OL"
    SAF = "SAF"
    OLB = "OLB"
    MLB = "MLB"
    C = "C"
    OT = "OT"
    LS = "LS"
    FB = "FB"
    K = "K"
    SS = "SS"
    ILB = "ILB"
    OG = "OG"
    NT = "NT"
    S = "S"
    DL = "DL"
    HB = "HB"
    KR = "KR"
    PR = "PR"
    HC = "HC"


class JerseyNumber:
    """
    Jersey number. Often useful for joins by name/team/jersey.

    Example Values
    --------------

    `84.0`

    `94.0`

    `61.0`

    `88.0`

    `24.0`

    """

    header = "jersey_number"


class Height:
    """
    height in inches

    Example Values
    --------------

    `73.0`

    `76.0`

    `79.0`

    `78.0`

    `72.0`

    """

    header = "height"


class Weight:
    """
    weight in pounds

    Example Values
    --------------

    `200.0`

    `330.0`

    `320.0`

    `251.0`

    `191.0`

    """

    header = "weight"


class YearsOfExperience:
    """
    No documentation available.

    Example Values
    --------------

    `"2"`

    `"9"`

    `"2"`

    `"0"`

    `"8"`

    """

    header = "years_of_experience"


class TeamAbbr:
    """
    No documentation available.

    Example Values
    --------------

    `"LAC"`

    `"CAR"`

    `"LA"`

    `"SEA"`

    `"CAR"`

    """

    header = "team_abbr"


class TeamSeq:
    """
    No documentation available.

    Example Values
    --------------

    `nan`

    `1.0`

    `nan`

    `nan`

    `1.0`

    """

    header = "team_seq"


class CurrentTeamId:
    """
    No documentation available.

    Example Values
    --------------

    `"4400"`

    `"0750"`

    `"2510"`

    `"4600"`

    `"0750"`

    """

    header = "current_team_id"


class FootballName:
    """
    Player's displayed football name.

    Example Values
    --------------

    `"None"`

    `"A'Shawn"`

    `"A.J."`

    `"A.J."`

    `"A.J."`

    """

    header = "football_name"


class EntryYear:
    """
    Player's first year rostered on an NFL team.

    Example Values
    --------------

    `nan`

    `2016.0`

    `2022.0`

    `2024.0`

    `2013.0`

    """

    header = "entry_year"


class RookieYear:
    """
    Player's rookie year.

    Example Values
    --------------

    `nan`

    `2016.0`

    `2022.0`

    `2024.0`

    `2013.0`

    """

    header = "rookie_year"


class DraftClub:
    """
    NFL team that drafted the player (if applicable).

    Example Values
    --------------

    `"None"`

    `"DET"`

    `"LA"`

    `"SEA"`

    `"None"`

    """

    header = "draft_club"


class DraftNumber:
    """
    Player's draft number.

    Example Values
    --------------

    `nan`

    `46.0`

    `261.0`

    `121.0`

    `nan`

    """

    header = "draft_number"


class CollegeConference:
    """
    Player's college conference.

    Example Values
    --------------

    `"None"`

    `"Southeastern Conference"`

    `"Big Ten Conference"`

    `"Big Ten Conference"`

    `"American Athletic Conference"`

    """

    header = "college_conference"

    SOUTHEASTERN_CONFERENCE = "Southeastern Conference"
    BIG_TEN_CONFERENCE = "Big Ten Conference"
    AMERICAN_ATHLETIC_CONFERENCE = "American Athletic Conference"
    ATLANTIC_COAST_CONFERENCE = "Atlantic Coast Conference"
    BIG_TWELVE_CONFERENCE = "Big Twelve Conference"
    SUN_BELT_CONFERENCE = "Sun Belt Conference"
    MIDAMERICAN_CONFERENCE = "Mid-American Conference"
    MOUNTAIN_WEST_CONFERENCE = "Mountain West Conference"
    PACIFIC_TWELVE_CONFERENCE = "Pacific Twelve Conference"
    OHIO_VALLEY_CONFERENCE = "Ohio Valley Conference"
    INDEPENDENT = "Independent"
    CONFERENCE_USA = "Conference USA"
    COLONIAL_ATHLETIC_ASSOCIATION = "Colonial Athletic Association"
    SOUTHERN_CALIFORNIA_INTERCOLLEGIATE_ATHLETIC_CONF = (
        "Southern California Intercollegiate Athletic Conf."
    )
    PIONEER_FOOTBALL_LEAGUE = "Pioneer Football League"
    BIG_SKY_CONFERENCE = "Big Sky Conference"
    PACIFIC_TEN_CONFERENCE = "Pacific Ten Conference"
    IVY_LEAGUE = "Ivy League"
    PATRIOT_LEAGUE = "Patriot League"
    GULF_SOUTH_CONFERENCE = "Gulf South Conference"
    GREAT_NORTHWEST_ATHLETIC_CONFERENCE = "Great Northwest Athletic Conference"
    BIG_EAST = "Big East"
    MISSOURI_VALLEY_FOOTBALL_CONFERENCE = "Missouri Valley Football Conference"
    GREAT_LAKES_INTERCOLLEGIATE_ATHLETIC_CONFERENCE = (
        "Great Lakes Intercollegiate Athletic Conference"
    )
    NORTHERN_SUN_INTERCOLLEGIATE_CONFERENCE = "Northern Sun Intercollegiate Conference"
    NO_COLLEGE = "NO COLLEGE"
    SOUTHERN_CONFERENCE = "Southern Conference"
    CANADA_WEST_UNIVERSITIES_ATHLETIC_ASSOCIATION = (
        "Canada West Universities Athletic Association"
    )
    PENNSYLVANIA_STATE_ATHLETIC_CONFERENCE = "Pennsylvania State Athletic Conference"
    ROCKY_MOUNTAIN_ATHLETIC_CONFERENCE = "Rocky Mountain Athletic Conference"
    FRONTIER_CONFERENCE = "Frontier Conference"
    MIDEASTERN_ATHLETIC_CONFERENCE = "Mid-Eastern Athletic Conference"
    SOUTHLAND_CONFERENCE = "Southland Conference"
    MIDAMERICA_INTERCOLLEGIATE_ATHLETIC_ASSOCIATION = (
        "Mid-America Intercollegiate Athletic Association"
    )
    BIG_SOUTH_CONFERENCE = "Big South Conference"
    MIDWEST_CONFERENCE = "Midwest Conference"
    LIBERTY_LEAGUE = "Liberty League"
    LONE_STAR_CONFERENCE = "Lone Star Conference"
    SOUTHERN_INTERCOLLEGIATE_ATHLETIC_CONFERENCE = (
        "Southern Intercollegiate Athletic Conference"
    )
    UNITED_ATHLETIC_CONFERENCE = "United Athletic Conference"
    HEART_OF_AMERICA_ATHLETIC_CONFERENCE = "Heart of America Athletic Conference"
    OHIO_ATHLETIC_CONFERENCE = "Ohio Athletic Conference"
    SOUTHWESTERN_ATHLETIC_CONFERENCE = "Southwestern Athletic Conference"
    NORTHEAST_CONFERENCE = "Northeast Conference"
    QUEBEC_STUDENT_SPORTS_FOUNDATION = "Quebec Student Sports Foundation"
    GREAT_AMERICAN_CONFERENCE = "Great American Conference"
    GREAT_LAKES_VALLEY_CONFERENCE = "Great Lakes Valley Conference"
    MINNESOTA_INTERCOLLEGIATE_ATHLETIC_CONFERENCE = (
        "Minnesota Intercollegiate Athletic Conference"
    )
    WISCONSIN_INTERCOLLEGIATE_ATHLETIC_CONFERENCE = (
        "Wisconsin Intercollegiate Athletic Conference"
    )
    WESTERN_ATHLETIC_CONFERENCE = "Western Athletic Conference"
    MOUNTAIN_EAST_CONFERENCE = "Mountain East Conference"
    AMERICAN_SOUTHWEST_CONFERENCE = "American Southwest Conference"
    SOUTH_ATLANTIC_CONFERENCE = "South Atlantic Conference"
    MIDSTATES_FOOTBALL_ASSOCIATION = "Mid-States Football Association"
    PRESIDENTS_ATHLETIC_CONFERENCE = "Presidents Athletic Conference"
    CENTRAL_INTERCOLLEGIATE_ATHLETIC_ASSOCIATION = (
        "Central Intercollegiate Athletic Association"
    )
    MIDSOUTH_CONFERENCE = "Mid-South Conference"
    NO_FOOTBALL = "NO FOOTBALL"
    EMPIRE_8_CONFERENCE = "Empire 8 Conference"
    SOUTHERN_ATHLETIC_ASSOCIATION = "Southern Athletic Association"
    WESTERN_STATES_FOOTBALL_CONFERENCE = "Western States Football Conference"
    MISSISSIPPI_CC_ATHLETIC_ASSOCIATION = "Mississippi CC Athletic Association"
    NORTHEAST10_CONFERENCE = "Northeast-10 Conference"
    OLD_DOMINION_ATHLETIC_CONFERENCE = "Old Dominion Athletic Conference"
    HEARTLAND_COLLEGIATE_ATHLETIC_CONFERENCE = (
        "Heartland Collegiate Athletic Conference"
    )
    ONTARIO_UNIVERSITIES_ATHLETIC_ASSOCIATION = (
        "Ontario Universities Athletic Association"
    )
    NORTH_STAR_ATHLETIC_ASSOCIATION = "North Star Athletic Association"
    KANSAS_COLLEGIATE_ATHLETIC_CONFERENCE = "Kansas Collegiate Athletic Conference"
    KANSAS_JAYHAWK_CONFERENCE = "Kansas Jayhawk Conference"
    ATLANTIC_10 = "Atlantic 10"
    NEW_JERSEY_ATHLETIC_CONFERENCE = "New Jersey Athletic Conference"
    MASSACHUSETTS_STATE_COLLEGE_ATHLETIC_CONFERENCE = (
        "Massachusetts State College Athletic Conference"
    )
    BIG_SOUTH__OHIO_VALLEY_CONFERENCE = "Big South - Ohio Valley Conference"
    THE_SUN_CONFERENCE = "The Sun Conference"
    NORTHERN_ATHLETICS_CONFERENCE = "Northern Athletics Conference"
    IOWA_INTERCOLLEGIATE_ATHLETIC_CONFERENCE = (
        "Iowa Intercollegiate Athletic Conference"
    )
    UPPER_MIDWEST_ATHLETIC_CONFERENCE = "Upper Midwest Athletic Conference"
    MIDDLE_ATLANTIC_CONFERENCE = "Middle Atlantic Conference"
    ATLANTIC_SUN_CONFERENCE = "Atlantic Sun Conference"
    GREAT_WEST_FOOTBALL_CONFERENCE = "Great West Football Conference"
    COLLEGE_CONFERENCE_OF_ILLINOIS_AND_WISCONSIN = (
        "College Conference of Illinois and Wisconsin"
    )


class StatusDescriptionAbbr:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"A01"`

    `"P01"`

    `"A01"`

    `"R01"`

    """

    header = "status_description_abbr"

    A01 = "A01"
    P01 = "P01"
    R01 = "R01"
    U01 = "U01"
    P07 = "P07"
    W03 = "W03"
    R02 = "R02"
    P03 = "P03"
    R34 = "R34"
    R04 = "R04"
    P06 = "P06"
    P02 = "P02"
    R36 = "R36"
    R48 = "R48"
    R40 = "R40"
    I01 = "I01"
    R42 = "R42"
    R06 = "R06"
    R23 = "R23"
    R41 = "R41"
    R62 = "R62"
    R43 = "R43"
    R27 = "R27"
    A02 = "A02"
    E08 = "E08"
    R03 = "R03"
    E02 = "E02"
    R05 = "R05"
    R47 = "R47"
    E14 = "E14"
    A03 = "A03"
    P09 = "P09"
    R37 = "R37"
    P12 = "P12"
    R59 = "R59"
    F12 = "F12"
    R49 = "R49"
    W06 = "W06"
    E01 = "E01"
    A06 = "A06"


class StatusShortDescription:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"Active"`

    `"Practice Squad"`

    `"Active"`

    `"R/Injured"`

    """

    header = "status_short_description"

    ACTIVE = "Active"
    PRACTICE_SQUAD = "Practice Squad"
    RINJURED = "R/Injured"
    RUFA = "R/UFA"
    PS_VET = "PS; Vet"
    WAIVERSNO_REC = "Waivers/No Rec."
    RRETIRED = "R/Retired"
    INTL_PSQUAD = "Int'l PSquad"
    RIWI_NOT_90 = "R/I-W/I; Not 90"
    RPUP = "R/PUP"
    PS_EXC = "PS; Exc"
    PRAC_SQ_INJ = "Prac Sq.; Inj"
    RI_NOT_90 = "R/I; NOT 90"
    RINJURED_DFR = "R/Injured; DFR"
    RSUSP_1YR = "R/Susp < 1Yr"
    INACTIVE = "Inactive"
    RNFIN_NOT_90 = "R/NFIN; Not 90"
    RLEFT_SQUAD = "R/Left Squad"
    RESERVEFUTURE = "Reserve/Future"
    RPUP_NOT_90 = "R/PUP; Not 90"
    ROPTOUT = "R/OptOut"
    RNFIL_NOT_90 = "R/NFIL; Not 90"
    RNFIL = "R/NFIL"
    ACTIVEPUP = "Active/PUP"
    EXLS_NOT_90 = "Ex/LS; Not 90"
    RDNR = "R/DNR"
    RI_VV_NOT_90 = "R/I; VV; NOT 90"
    EXCOMM_PERM = "Ex/Comm. Perm."
    RNFIN = "R/NFIN"
    RNFIN_DFR = "R/NFIN; DFR"
    EXINTERNAT = "Ex/Internat"
    ACTIVENFIN = "Active/NFIN"
    PS_COVID19 = "PS; COVID19"
    RPUPWFP_NO90 = "R/PUP-W/FP No90"
    PSVET_PRO = "PS/Vet Pro"
    RCOVID19 = "R/COVID-19"
    FA_SUSP1_YR = "FA Susp-1 Yr"
    RNFIL_DFR = "R/NFIL; DFR"
    WI_PRIOR_53 = "W/I; Prior 53"
    EXLEFT_SQUAD = "Ex/Left Squad"
    ACTIVENFIL = "Active/NFIL"


class GsisItId:
    """
    No documentation available.

    Example Values
    --------------

    `nan`

    `43335.0`

    `54726.0`

    `57242.0`

    `40688.0`

    """

    header = "gsis_it_id"


class ShortName:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"A.Robinson"`

    `"A.Arcuri"`

    `"A.Barner"`

    `"A.Bouye"`

    """

    header = "short_name"


class SmartId:
    """
    No documentation available.

    Example Values
    --------------

    `"3200454c-4c71-1319-728e-d49d3d236f8f"`

    `"3200524f-4236-7960-bf20-bc060ac0f49c"`

    `"32004152-4371-6900-5185-8cdd66b2ad11"`

    `"32004241-5223-5889-95d9-0ba3aeeb36ed"`

    `"3200424f-5565-1714-cb38-07c822111a12"`

    """

    header = "smart_id"


class Headshot:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"https://static.www.nfl.com/image/private/f_auto,q_auto/league/qgiwxchd1lmgszfunys8"`

    `"None"`

    `"https://static.www.nfl.com/image/upload/f_auto,q_auto/league/msnzbeyjoemcas9dm8vt"`

    `"https://static.www.nfl.com/image/private/f_auto,q_auto/league/cpgi2hbhnmvs1oczkzas"`

    """

    header = "headshot"


class Suffix:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "suffix"

    III = "III"
    JR = "Jr."
    II = "II"
    COOK = "Cook"
    IV = "IV"
    V = "V"
    SINDRE = "Sindre"
    JR = "Jr"
    ELLIS = "Ellis"
    WILLIAMS = "Williams"
    HALL = "Hall"


class UniformNumber:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"94"`

    `"61"`

    `"88"`

    `"24"`

    """

    header = "uniform_number"


class DraftRound:
    """
    Round of draft.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "draft_round"
