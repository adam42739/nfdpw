"""
====================
Play-by-play columns
====================

Header names are accesible as _column_.header.

```python
>>> cols.PlayId.header
>>> "play_id"
```

Some categorical columns provide encoded values.

```python
>>> cols.PenaltyType.ILLEGAL_BLOCK_ABOVE_THE_WAIST
>>> "Illegal Block Above the Waist"
```

"""


class PlayId:
    """
    Numeric play id that when used with game_id and drive provides the unique identifier for a single play.

    Example Values
    --------------

    `1.0`

    `39.0`

    `55.0`

    `77.0`

    `102.0`

    """

    header = "play_id"


class GameId:
    """
    Ten digit identifier for NFL game.

    Example Values
    --------------

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    """

    header = "game_id"


class OldGameIdX:
    """
    No documentation available.

    Example Values
    --------------

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    """

    header = "old_game_id_x"


class HomeTeam:
    """
    String abbreviation for the home team.

    Example Values
    --------------

    `"WAS"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    """

    header = "home_team"


class AwayTeam:
    """
    String abbreviation for the away team.

    Example Values
    --------------

    `"ARI"`

    `"ARI"`

    `"ARI"`

    `"ARI"`

    `"ARI"`

    """

    header = "away_team"


class SeasonType:
    """
    'REG' or 'POST' indicating if the game belongs to regular or post season.

    Example Values
    --------------

    `"REG"`

    `"REG"`

    `"REG"`

    `"REG"`

    `"REG"`

    """

    header = "season_type"

    REG = "REG"
    POST = "POST"


class Week:
    """
    Season week.

    Example Values
    --------------

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    `"1"`

    """

    header = "week"


class Posteam:
    """
    String abbreviation for the team with possession.

    Example Values
    --------------

    `"None"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    """

    header = "posteam"


class PosteamType:
    """
    String indicating whether the posteam team is home or away.

    Example Values
    --------------

    `"None"`

    `"home"`

    `"home"`

    `"home"`

    `"home"`

    """

    header = "posteam_type"


class Defteam:
    """
    String abbreviation for the team on defense.

    Example Values
    --------------

    `"None"`

    `"ARI"`

    `"ARI"`

    `"ARI"`

    `"ARI"`

    """

    header = "defteam"


class SideOfField:
    """
    String abbreviation for which team's side of the field the team with possession is currently on.

    Example Values
    --------------

    `"None"`

    `"ARI"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    """

    header = "side_of_field"


class Yardline100:
    """
    Numeric distance in the number of yards from the opponent's endzone for the posteam.

    Example Values
    --------------

    `nan`

    `35.0`

    `75.0`

    `72.0`

    `66.0`

    """

    header = "yardline_100"


class GameDate:
    """
    Date of the game.

    Example Values
    --------------

    `"2023-09-10"`

    `"2023-09-10"`

    `"2023-09-10"`

    `"2023-09-10"`

    `"2023-09-10"`

    """

    header = "game_date"


class QuarterSecondsRemaining:
    """
    Numeric seconds remaining in the quarter.

    Example Values
    --------------

    `900.0`

    `900.0`

    `900.0`

    `870.0`

    `835.0`

    """

    header = "quarter_seconds_remaining"


class HalfSecondsRemaining:
    """
    Numeric seconds remaining in the half.

    Example Values
    --------------

    `1800.0`

    `1800.0`

    `1800.0`

    `1770.0`

    `1735.0`

    """

    header = "half_seconds_remaining"


class GameSecondsRemaining:
    """
    Numeric seconds remaining in the game.

    Example Values
    --------------

    `3600.0`

    `3600.0`

    `3600.0`

    `3570.0`

    `3535.0`

    """

    header = "game_seconds_remaining"


class GameHalf:
    """
    String indicating which half the play is in, either Half1, Half2, or Overtime.

    Example Values
    --------------

    `"Half1"`

    `"Half1"`

    `"Half1"`

    `"Half1"`

    `"Half1"`

    """

    header = "game_half"

    HALF1 = "Half1"
    HALF2 = "Half2"
    OVERTIME = "Overtime"


class QuarterEnd:
    """
    Binary indicator for whether or not the row of the data is marking the end of a quarter.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "quarter_end"

    TRUE = 1
    FALSE = 0


class Drive:
    """
    Numeric drive number in the game.

    Example Values
    --------------

    `nan`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "drive"


class Sp:
    """
    Binary indicator for whether or not a score occurred on the play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "sp"

    TRUE = 1
    FALSE = 0


class Qtr:
    """
    Quarter of the game (5 is overtime).

    Example Values
    --------------

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "qtr"


class Down:
    """
    The down for the given play.

    Example Values
    --------------

    `nan`

    `nan`

    `1.0`

    `2.0`

    `3.0`

    """

    header = "down"


class GoalToGo:
    """
    Binary indicator for whether or not the posteam is in a goal down situation.

    Example Values
    --------------

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    """

    header = "goal_to_go"

    TRUE = 1
    FALSE = 0


class Time:
    """
    Time at start of play provided in string format as minutes:seconds remaining in the quarter.

    Example Values
    --------------

    `"15:00"`

    `"15:00"`

    `"15:00"`

    `"14:30"`

    `"13:55"`

    """

    header = "time"


class Yrdln:
    """
    String indicating the current field position for a given play.

    Example Values
    --------------

    `"ARI 35"`

    `"ARI 35"`

    `"WAS 25"`

    `"WAS 28"`

    `"WAS 34"`

    """

    header = "yrdln"


class Ydstogo:
    """
    Numeric yards in distance from either the first down marker or the endzone in goal down situations.

    Example Values
    --------------

    `0.0`

    `0.0`

    `10.0`

    `7.0`

    `1.0`

    """

    header = "ydstogo"


class Ydsnet:
    """
    Numeric value for total yards gained on the given drive.

    Example Values
    --------------

    `nan`

    `26.0`

    `26.0`

    `26.0`

    `26.0`

    """

    header = "ydsnet"


class Desc:
    """
    Detailed string description for the given play.

    Example Values
    --------------

    `"GAME"`

    `"5-M.Prater kicks 65 yards from ARI 35 to end zone, Touchback."`

    `"(15:00) (Shotgun) 8-B.Robinson right tackle to WAS 28 for 3 yards (93-J.Ledbetter)."`

    `"(14:30) (Shotgun) 14-S.Howell pass short right to 1-J.Dotson to WAS 34 for 6 yards (13-K.Clark, 10-J.Woods)."`

    `"(13:55) 23-C.Rodriguez left guard to WAS 36 for 2 yards (97-C.Thomas; 25-Z.Collins)."`

    """

    header = "desc"


class PlayType:
    """
    String indicating the type of play: pass (includes sacks), run (includes scrambles), punt, field_goal, kickoff, extra_point, qb_kneel, qb_spike, no_play (timeouts and penalties), and missing for rows indicating end of play.

    Example Values
    --------------

    `"None"`

    `"kickoff"`

    `"run"`

    `"pass"`

    `"run"`

    """

    header = "play_type"

    KICKOFF = "kickoff"
    RUN = "run"
    PASS = "pass"
    PUNT = "punt"
    NO_PLAY = "no_play"
    EXTRA_POINT = "extra_point"
    FIELD_GOAL = "field_goal"
    QB_KNEEL = "qb_kneel"
    QB_SPIKE = "qb_spike"


class YardsGained:
    """
    Numeric yards gained (or lost) by the possessing team, excluding yards gained via fumble recoveries and laterals.

    Example Values
    --------------

    `nan`

    `0.0`

    `3.0`

    `6.0`

    `2.0`

    """

    header = "yards_gained"


class Shotgun:
    """
    Binary indicator for whether or not the play was in shotgun formation.

    Example Values
    --------------

    `0.0`

    `0.0`

    `1.0`

    `1.0`

    `0.0`

    """

    header = "shotgun"

    TRUE = 1
    FALSE = 0


class NoHuddle:
    """
    Binary indicator for whether or not the play was in no_huddle formation.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "no_huddle"

    TRUE = 1
    FALSE = 0


class QbDropback:
    """
    Binary indicator for whether or not the QB dropped back on the play (pass attempt, sack, or scrambled).

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    """

    header = "qb_dropback"

    TRUE = 1
    FALSE = 0


class QbKneel:
    """
    Binary indicator for whether or not the QB took a knee.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "qb_kneel"

    TRUE = 1
    FALSE = 0


class QbSpike:
    """
    Binary indicator for whether or not the QB spiked the ball.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "qb_spike"

    TRUE = 1
    FALSE = 0


class QbScramble:
    """
    Binary indicator for whether or not the QB scrambled.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "qb_scramble"

    TRUE = 1
    FALSE = 0


class PassLength:
    """
    String indicator for pass length: short or deep.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"short"`

    `"None"`

    """

    header = "pass_length"

    SHORT = "short"
    DEEP = "deep"


class PassLocation:
    """
    String indicator for pass location: left, middle, or right.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"right"`

    `"None"`

    """

    header = "pass_location"

    RIGHT = "right"
    MIDDLE = "middle"
    LEFT = "left"


class AirYards:
    """
    Numeric value for distance in yards perpendicular to the line of scrimmage at where the targeted receiver either caught or didn't catch the ball.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `6.0`

    `nan`

    """

    header = "air_yards"


class YardsAfterCatch:
    """
    Numeric value for distance in yards perpendicular to the yard line where the receiver made the reception to where the play ended.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.0`

    `nan`

    """

    header = "yards_after_catch"


class RunLocation:
    """
    String indicator for location of run: left, middle, or right.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"right"`

    `"None"`

    `"left"`

    """

    header = "run_location"

    RIGHT = "right"
    LEFT = "left"
    MIDDLE = "middle"


class RunGap:
    """
    String indicator for line gap of run: end, guard, or tackle

    Example Values
    --------------

    `"None"`

    `"None"`

    `"tackle"`

    `"None"`

    `"guard"`

    """

    header = "run_gap"

    TACKLE = "tackle"
    GUARD = "guard"
    END = "end"


class FieldGoalResult:
    """
    String indicator for result of field goal attempt: made, missed, or blocked.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "field_goal_result"

    MADE = "made"
    MISSED = "missed"
    BLOCKED = "blocked"


class KickDistance:
    """
    Numeric distance in yards for kickoffs, field goals, and punts.

    Example Values
    --------------

    `nan`

    `65.0`

    `nan`

    `nan`

    `nan`

    """

    header = "kick_distance"


class ExtraPointResult:
    """
    String indicator for the result of the extra point attempt: good, failed, blocked, safety (touchback in defensive endzone is 1 point apparently), or aborted.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "extra_point_result"

    GOOD = "good"
    FAILED = "failed"
    BLOCKED = "blocked"


class TwoPointConvResult:
    """
    String indicator for result of two point conversion attempt: success, failure, safety (touchback in defensive endzone is 1 point apparently), or return.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "two_point_conv_result"

    SUCCESS = "success"
    FAILURE = "failure"


class HomeTimeoutsRemaining:
    """
    Numeric timeouts remaining in the half for the home team.

    Example Values
    --------------

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    """

    header = "home_timeouts_remaining"


class AwayTimeoutsRemaining:
    """
    Numeric timeouts remaining in the half for the away team.

    Example Values
    --------------

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    """

    header = "away_timeouts_remaining"


class Timeout:
    """
    Binary indicator for whether or not a timeout was called by either team.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "timeout"


class TimeoutTeam:
    """
    String abbreviation for which team called the timeout.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "timeout_team"


class TdTeam:
    """
    String abbreviation for which team scored the touchdown.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "td_team"


class TdPlayerName:
    """
    String name of the player who scored a touchdown.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "td_player_name"


class TdPlayerId:
    """
    Unique identifier of the player who scored a touchdown.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "td_player_id"


class PosteamTimeoutsRemaining:
    """
    Number of timeouts remaining for the possession team.

    Example Values
    --------------

    `nan`

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    """

    header = "posteam_timeouts_remaining"


class DefteamTimeoutsRemaining:
    """
    Number of timeouts remaining for the team on defense.

    Example Values
    --------------

    `nan`

    `3.0`

    `3.0`

    `3.0`

    `3.0`

    """

    header = "defteam_timeouts_remaining"


class TotalHomeScore:
    """
    Score for the home team at the start of the play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_home_score"


class TotalAwayScore:
    """
    Score for the away team at the start of the play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_away_score"


class PosteamScore:
    """
    Score the posteam at the start of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "posteam_score"


class DefteamScore:
    """
    Score the defteam at the start of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defteam_score"


class ScoreDifferential:
    """
    Score differential between the posteam and defteam at the start of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "score_differential"


class PosteamScorePost:
    """
    Score for the posteam at the end of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "posteam_score_post"


class DefteamScorePost:
    """
    Score for the defteam at the end of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defteam_score_post"


class ScoreDifferentialPost:
    """
    Score differential between the posteam and defteam at the end of the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "score_differential_post"


class NoScoreProb:
    """
    Predicted probability of no score occurring for the rest of the half based on the expected points model.

    Example Values
    --------------

    `0.0`

    `0.0046605235`

    `0.0046605235`

    `0.004854194`

    `0.005151121`

    """

    header = "no_score_prob"


class OppFgProb:
    """
    Predicted probability of the defteam scoring a FG next.

    Example Values
    --------------

    `0.0`

    `0.14403701`

    `0.14403701`

    `0.15247281`

    `0.14255205`

    """

    header = "opp_fg_prob"


class OppSafetyProb:
    """
    Predicted probability of the defteam scoring a safety next.

    Example Values
    --------------

    `0.0`

    `0.0020718346`

    `0.0020718346`

    `0.0021445903`

    `0.002266304`

    """

    header = "opp_safety_prob"


class OppTdProb:
    """
    Predicted probability of the defteam scoring a TD next.

    Example Values
    --------------

    `0.0`

    `0.2260513`

    `0.2260513`

    `0.24698621`

    `0.20016445`

    """

    header = "opp_td_prob"


class FgProb:
    """
    Predicted probability of the posteam scoring a FG next.

    Example Values
    --------------

    `0.0`

    `0.21260108`

    `0.21260108`

    `0.20210096`

    `0.21326233`

    """

    header = "fg_prob"


class SafetyProb:
    """
    Predicted probability of the posteam scoring a safety next.

    Example Values
    --------------

    `0.0`

    `0.0038279337`

    `0.0038279337`

    `0.0035572837`

    `0.0042742593`

    """

    header = "safety_prob"


class TdProb:
    """
    Predicted probability of the posteam scoring a TD next.

    Example Values
    --------------

    `0.0`

    `0.40675035`

    `0.40675035`

    `0.387884`

    `0.43232948`

    """

    header = "td_prob"


class ExtraPointProb:
    """
    Predicted probability of the posteam scoring an extra point.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "extra_point_prob"


class TwoPointConversionProb:
    """
    Predicted probability of the posteam scoring the two point conversion.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "two_point_conversion_prob"


class Ep:
    """
    Using the scoring event probabilities, the estimated expected points with respect to the possession team for the given play.

    Example Values
    --------------

    `1.4740977`

    `1.4740977`

    `1.4740977`

    `1.1379943`

    `1.8413019`

    """

    header = "ep"


class Epa:
    """
    Expected points added (EPA) by the posteam for the given play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.33610347`

    `0.7033076`

    `0.46979922`

    """

    header = "epa"


class TotalHomeEpa:
    """
    Cumulative total EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.33610347`

    `0.36720416`

    `0.8370034`

    """

    header = "total_home_epa"


class TotalAwayEpa:
    """
    Cumulative total EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.33610347`

    `-0.36720416`

    `-0.8370034`

    """

    header = "total_away_epa"


class TotalHomeRushEpa:
    """
    Cumulative total rushing EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.33610347`

    `-0.33610347`

    `0.13369575`

    """

    header = "total_home_rush_epa"


class TotalAwayRushEpa:
    """
    Cumulative total rushing EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.33610347`

    `0.33610347`

    `-0.13369575`

    """

    header = "total_away_rush_epa"


class TotalHomePassEpa:
    """
    Cumulative total passing EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.7033076`

    `0.7033076`

    """

    header = "total_home_pass_epa"


class TotalAwayPassEpa:
    """
    Cumulative total passing EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.7033076`

    `-0.7033076`

    """

    header = "total_away_pass_epa"


class AirEpa:
    """
    EPA from the air yards alone. For completions this represents the actual value provided through the air. For incompletions this represents the hypothetical value that could've been added through the air if the pass was completed.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.7033076`

    `nan`

    """

    header = "air_epa"


class YacEpa:
    """
    EPA from the yards after catch alone. For completions this represents the actual value provided after the catch. For incompletions this represents the difference between the hypothetical air_epa and the play's raw observed EPA (how much the incomplete pass cost the posteam).

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.0`

    `nan`

    """

    header = "yac_epa"


class CompAirEpa:
    """
    EPA from the air yards alone only for completions.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.7033076`

    `0.0`

    """

    header = "comp_air_epa"


class CompYacEpa:
    """
    EPA from the yards after catch alone only for completions.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "comp_yac_epa"


class TotalHomeCompAirEpa:
    """
    Cumulative total completions air EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.7033076`

    `0.7033076`

    """

    header = "total_home_comp_air_epa"


class TotalAwayCompAirEpa:
    """
    Cumulative total completions air EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.7033076`

    `-0.7033076`

    """

    header = "total_away_comp_air_epa"


class TotalHomeCompYacEpa:
    """
    Cumulative total completions yac EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_home_comp_yac_epa"


class TotalAwayCompYacEpa:
    """
    Cumulative total completions yac EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_away_comp_yac_epa"


class TotalHomeRawAirEpa:
    """
    Cumulative total raw air EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.7033076`

    `0.7033076`

    """

    header = "total_home_raw_air_epa"


class TotalAwayRawAirEpa:
    """
    Cumulative total raw air EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.7033076`

    `-0.7033076`

    """

    header = "total_away_raw_air_epa"


class TotalHomeRawYacEpa:
    """
    Cumulative total raw yac EPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_home_raw_yac_epa"


class TotalAwayRawYacEpa:
    """
    Cumulative total raw yac EPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_away_raw_yac_epa"


class Wp:
    """
    Estimated win probabiity for the posteam given the current situation at the start of the given play.

    Example Values
    --------------

    `0.5462618`

    `0.5462618`

    `0.5462618`

    `0.53962094`

    `0.5559875`

    """

    header = "wp"


class DefWp:
    """
    Estimated win probability for the defteam.

    Example Values
    --------------

    `0.4537382`

    `0.4537382`

    `0.4537382`

    `0.46037906`

    `0.44401252`

    """

    header = "def_wp"


class HomeWp:
    """
    Estimated win probability for the home team.

    Example Values
    --------------

    `0.5462618`

    `0.5462618`

    `0.5462618`

    `0.53962094`

    `0.5559875`

    """

    header = "home_wp"


class AwayWp:
    """
    Estimated win probability for the away team.

    Example Values
    --------------

    `0.4537382`

    `0.4537382`

    `0.4537382`

    `0.46037906`

    `0.44401252`

    """

    header = "away_wp"


class Wpa:
    """
    Win probability added (WPA) for the posteam.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.0066408515`

    `0.016366541`

    `0.016585886`

    """

    header = "wpa"


class VegasWpa:
    """
    Win probability added (WPA) for the posteam: spread_adjusted model.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.020273805`

    `0.0110241175`

    `0.012498915`

    """

    header = "vegas_wpa"


class VegasHomeWpa:
    """
    Win probability added (WPA) for the home team: spread_adjusted model.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.020273805`

    `0.0110241175`

    `0.012498915`

    """

    header = "vegas_home_wpa"


class HomeWpPost:
    """
    Estimated win probability for the home team at the end of the play.

    Example Values
    --------------

    `nan`

    `0.5462618`

    `0.53962094`

    `0.5559875`

    `0.57257336`

    """

    header = "home_wp_post"


class AwayWpPost:
    """
    Estimated win probability for the away team at the end of the play.

    Example Values
    --------------

    `nan`

    `0.4537382`

    `0.46037906`

    `0.44401252`

    `0.42742664`

    """

    header = "away_wp_post"


class VegasWp:
    """
    Estimated win probabiity for the posteam given the current situation at the start of the given play, incorporating pre-game Vegas line.

    Example Values
    --------------

    `0.73739946`

    `0.73739946`

    `0.73739946`

    `0.71712565`

    `0.7281498`

    """

    header = "vegas_wp"


class VegasHomeWp:
    """
    Estimated win probability for the home team incorporating pre-game Vegas line.

    Example Values
    --------------

    `0.73739946`

    `0.73739946`

    `0.73739946`

    `0.71712565`

    `0.7281498`

    """

    header = "vegas_home_wp"


class TotalHomeRushWpa:
    """
    Cumulative total rushing WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.0066408515`

    `-0.0066408515`

    `0.009945035`

    """

    header = "total_home_rush_wpa"


class TotalAwayRushWpa:
    """
    Cumulative total rushing WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0066408515`

    `0.0066408515`

    `-0.009945035`

    """

    header = "total_away_rush_wpa"


class TotalHomePassWpa:
    """
    Cumulative total passing WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.016366541`

    `0.016366541`

    """

    header = "total_home_pass_wpa"


class TotalAwayPassWpa:
    """
    Cumulative total passing WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.016366541`

    `-0.016366541`

    """

    header = "total_away_pass_wpa"


class AirWpa:
    """
    WPA through the air (same logic as air_epa).

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.016366541`

    `nan`

    """

    header = "air_wpa"


class YacWpa:
    """
    WPA from yards after the catch (same logic as yac_epa).

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.0`

    `nan`

    """

    header = "yac_wpa"


class CompAirWpa:
    """
    The air_wpa for completions only.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.016366541`

    `0.0`

    """

    header = "comp_air_wpa"


class CompYacWpa:
    """
    The yac_wpa for completions only.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "comp_yac_wpa"


class TotalHomeCompAirWpa:
    """
    Cumulative total completions air WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.016366541`

    `0.016366541`

    """

    header = "total_home_comp_air_wpa"


class TotalAwayCompAirWpa:
    """
    Cumulative total completions air WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.016366541`

    `-0.016366541`

    """

    header = "total_away_comp_air_wpa"


class TotalHomeCompYacWpa:
    """
    Cumulative total completions yac WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_home_comp_yac_wpa"


class TotalAwayCompYacWpa:
    """
    Cumulative total completions yac WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_away_comp_yac_wpa"


class TotalHomeRawAirWpa:
    """
    Cumulative total raw air WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.016366541`

    `0.016366541`

    """

    header = "total_home_raw_air_wpa"


class TotalAwayRawAirWpa:
    """
    Cumulative total raw air WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `-0.016366541`

    `-0.016366541`

    """

    header = "total_away_raw_air_wpa"


class TotalHomeRawYacWpa:
    """
    Cumulative total raw yac WPA for the home team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_home_raw_yac_wpa"


class TotalAwayRawYacWpa:
    """
    Cumulative total raw yac WPA for the away team in the game so far.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "total_away_raw_yac_wpa"


class PuntBlocked:
    """
    Binary indicator for if the punt was blocked.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_blocked"

    TRUE = 1
    FALSE = 0


class FirstDownRush:
    """
    Binary indicator for if a running play converted the first down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `1.0`

    """

    header = "first_down_rush"

    TRUE = 1
    FALSE = 0


class FirstDownPass:
    """
    Binary indicator for if a passing play converted the first down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "first_down_pass"

    TRUE = 1
    FALSE = 0


class FirstDownPenalty:
    """
    Binary indicator for if a penalty converted the first down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "first_down_penalty"

    TRUE = 1
    FALSE = 0


class ThirdDownConverted:
    """
    Binary indicator for if the first down was converted on third down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `1.0`

    """

    header = "third_down_converted"

    TRUE = 1
    FALSE = 0


class ThirdDownFailed:
    """
    Binary indicator for if the posteam failed to convert first down on third down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "third_down_failed"

    TRUE = 1
    FALSE = 0


class FourthDownConverted:
    """
    Binary indicator for if the first down was converted on fourth down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fourth_down_converted"

    TRUE = 1
    FALSE = 0


class FourthDownFailed:
    """
    Binary indicator for if the posteam failed to convert first down on fourth down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fourth_down_failed"

    TRUE = 1
    FALSE = 0


class IncompletePass:
    """
    Binary indicator for if the pass was incomplete.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "incomplete_pass"

    TRUE = 1
    FALSE = 0


class Touchback:
    """
    Binary indicator for if a touchback occurred on the play.

    Example Values
    --------------

    `0.0`

    `1.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "touchback"

    TRUE = 1
    FALSE = 0


class Interception:
    """
    Binary indicator for if the pass was intercepted.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "interception"

    TRUE = 1
    FALSE = 0


class PuntInsideTwenty:
    """
    Binary indicator for if the punt ended inside the twenty yard line.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_inside_twenty"


class PuntInEndzone:
    """
    Binary indicator for if the punt was in the endzone.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_in_endzone"

    TRUE = 1
    FALSE = 0


class PuntOutOfBounds:
    """
    Binary indicator for if the punt went out of bounds.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_out_of_bounds"

    TRUE = 1
    FALSE = 0


class PuntDowned:
    """
    Binary indicator for if the punt was downed.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_downed"

    TRUE = 1
    FALSE = 0


class PuntFairCatch:
    """
    Binary indicator for if the punt was caught with a fair catch.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_fair_catch"

    TRUE = 1
    FALSE = 0


class KickoffInsideTwenty:
    """
    Binary indicator for if the kickoff ended inside the twenty yard line.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_inside_twenty"


class KickoffInEndzone:
    """
    Binary indicator for if the kickoff was in the endzone.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_in_endzone"

    TRUE = 1
    FALSE = 0


class KickoffOutOfBounds:
    """
    Binary indicator for if the kickoff went out of bounds.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_out_of_bounds"

    TRUE = 1
    FALSE = 0


class KickoffDowned:
    """
    Binary indicator for if the kickoff was downed.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_downed"

    TRUE = 1
    FALSE = 0


class KickoffFairCatch:
    """
    Binary indicator for if the kickoff was caught with a fair catch.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_fair_catch"

    TRUE = 1
    FALSE = 0


class FumbleForced:
    """
    Binary indicator for if the fumble was forced.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fumble_forced"

    TRUE = 1
    FALSE = 0


class FumbleNotForced:
    """
    Binary indicator for if the fumble was not forced.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fumble_not_forced"

    TRUE = 1
    FALSE = 0


class FumbleOutOfBounds:
    """
    Binary indicator for if the fumble went out of bounds.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fumble_out_of_bounds"

    TRUE = 1
    FALSE = 0


class SoloTackle:
    """
    Binary indicator if the play had a solo tackle (could be multiple due to fumbles).

    Example Values
    --------------

    `nan`

    `0.0`

    `1.0`

    `0.0`

    `0.0`

    """

    header = "solo_tackle"

    TRUE = 1
    FALSE = 0


class Safety:
    """
    Binary indicator for whether or not a safety occurred.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "safety"

    TRUE = 1
    FALSE = 0


class Penalty:
    """
    Binary indicator for whether or not a penalty occurred.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "penalty"

    TRUE = 1
    FALSE = 0


class TackledForLoss:
    """
    Binary indicator for whether or not a tackle for loss on a run play occurred.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "tackled_for_loss"

    TRUE = 1
    FALSE = 0


class FumbleLost:
    """
    Binary indicator for if the fumble was lost.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fumble_lost"

    TRUE = 1
    FALSE = 0


class OwnKickoffRecovery:
    """
    Binary indicator for if the kicking team recovered the kickoff.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "own_kickoff_recovery"

    TRUE = 1
    FALSE = 0


class OwnKickoffRecoveryTd:
    """
    Binary indicator for if the kicking team recovered the kickoff and scored a TD.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "own_kickoff_recovery_td"


class QbHit:
    """
    Binary indicator if the QB was hit on the play.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "qb_hit"

    TRUE = 1
    FALSE = 0


class RushAttempt:
    """
    Binary indicator for if the play was a run.

    Example Values
    --------------

    `nan`

    `0.0`

    `1.0`

    `0.0`

    `1.0`

    """

    header = "rush_attempt"

    TRUE = 1
    FALSE = 0


class PassAttempt:
    """
    Binary indicator for if the play was a pass attempt (includes sacks).

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    """

    header = "pass_attempt"

    TRUE = 1
    FALSE = 0


class Sack:
    """
    Binary indicator for if the play ended in a sack.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "sack"

    TRUE = 1
    FALSE = 0


class Touchdown:
    """
    Binary indicator for if the play resulted in a TD.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "touchdown"

    TRUE = 1
    FALSE = 0


class PassTouchdown:
    """
    Binary indicator for if the play resulted in a passing TD.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "pass_touchdown"

    TRUE = 1
    FALSE = 0


class RushTouchdown:
    """
    Binary indicator for if the play resulted in a rushing TD.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "rush_touchdown"

    TRUE = 1
    FALSE = 0


class ReturnTouchdown:
    """
    Binary indicator for if the play resulted in a return TD. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "return_touchdown"

    TRUE = 1
    FALSE = 0


class ExtraPointAttempt:
    """
    Binary indicator for extra point attempt.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "extra_point_attempt"

    TRUE = 1
    FALSE = 0


class TwoPointAttempt:
    """
    Binary indicator for two point conversion attempt.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "two_point_attempt"

    TRUE = 1
    FALSE = 0


class FieldGoalAttempt:
    """
    Binary indicator for field goal attempt.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "field_goal_attempt"

    TRUE = 1
    FALSE = 0


class KickoffAttempt:
    """
    Binary indicator for kickoff.

    Example Values
    --------------

    `nan`

    `1.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "kickoff_attempt"

    TRUE = 1
    FALSE = 0


class PuntAttempt:
    """
    Binary indicator for punts.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "punt_attempt"

    TRUE = 1
    FALSE = 0


class Fumble:
    """
    Binary indicator for if a fumble occurred.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "fumble"

    TRUE = 1
    FALSE = 0


class CompletePass:
    """
    Binary indicator for if the pass was completed.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    """

    header = "complete_pass"

    TRUE = 1
    FALSE = 0


class AssistTackle:
    """
    Binary indicator for if an assist tackle occurred.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `1.0`

    `1.0`

    """

    header = "assist_tackle"

    TRUE = 1
    FALSE = 0


class LateralReception:
    """
    Binary indicator for if a lateral occurred on the reception.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "lateral_reception"

    TRUE = 1
    FALSE = 0


class LateralRush:
    """
    Binary indicator for if a lateral occurred on a run.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "lateral_rush"

    TRUE = 1
    FALSE = 0


class LateralReturn:
    """
    Binary indicator for if a lateral occurred on a return. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "lateral_return"

    TRUE = 1
    FALSE = 0


class LateralRecovery:
    """
    Binary indicator for if a lateral occurred on a fumble recovery.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "lateral_recovery"

    TRUE = 1
    FALSE = 0


class PasserPlayerId:
    """
    Unique identifier for the player that attempted the pass.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0037077"`

    `"None"`

    """

    header = "passer_player_id"


class PasserPlayerName:
    """
    String name for the player that attempted the pass.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"S.Howell"`

    `"None"`

    """

    header = "passer_player_name"


class PassingYards:
    """
    Numeric yards by the passer_player_name, including yards gained in pass plays with laterals. This should equal official passing statistics.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `6.0`

    `nan`

    """

    header = "passing_yards"


class ReceiverPlayerId:
    """
    Unique identifier for the receiver that was targeted on the pass.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0037741"`

    `"None"`

    """

    header = "receiver_player_id"


class ReceiverPlayerName:
    """
    String name for the targeted receiver.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"J.Dotson"`

    `"None"`

    """

    header = "receiver_player_name"


class ReceivingYards:
    """
    Numeric yards by the receiver_player_name, excluding yards gained in pass plays with laterals. This should equal official receiving statistics but could miss yards gained in pass plays with laterals. Please see the description of `lateral_receiver_player_name` for further information.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `6.0`

    `nan`

    """

    header = "receiving_yards"


class RusherPlayerId:
    """
    Unique identifier for the player that attempted the run.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0037746"`

    `"None"`

    `"00-0038611"`

    """

    header = "rusher_player_id"


class RusherPlayerName:
    """
    String name for the player that attempted the run.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"B.Robinson"`

    `"None"`

    `"C.Rodriguez"`

    """

    header = "rusher_player_name"


class RushingYards:
    """
    Numeric yards by the rusher_player_name, excluding yards gained in rush plays with laterals. This should equal official rushing statistics but could miss yards gained in rush plays with laterals. Please see the description of `lateral_rusher_player_name` for further information.

    Example Values
    --------------

    `nan`

    `nan`

    `3.0`

    `nan`

    `2.0`

    """

    header = "rushing_yards"


class LateralReceiverPlayerId:
    """
    Unique identifier for the player that received the last(!) lateral on a pass play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_receiver_player_id"


class LateralReceiverPlayerName:
    """
    String name for the player that received the last(!) lateral on a pass play. If there were multiple laterals in the same play, this will only be the last player who received a lateral. Please see &lt;https://github.com/mrcaseb/nfl-data/tree/master/data/lateral_yards&gt; for a list of plays where multiple players recorded lateral receiving yards.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_receiver_player_name"


class LateralReceivingYards:
    """
    Numeric yards by the `lateral_receiver_player_name` in pass plays with laterals. Please see the description of `lateral_receiver_player_name` for further information.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "lateral_receiving_yards"


class LateralRusherPlayerId:
    """
    Unique identifier for the player that received the last(!) lateral on a run play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_rusher_player_id"


class LateralRusherPlayerName:
    """
    String name for the player that received the last(!) lateral on a run play. If there were multiple laterals in the same play, this will only be the last player who received a lateral. Please see &lt;https://github.com/mrcaseb/nfl-data/tree/master/data/lateral_yards&gt; for a list of plays where multiple players recorded lateral rushing yards.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_rusher_player_name"


class LateralRushingYards:
    """
    Numeric yards by the `lateral_rusher_player_name` in run plays with laterals. Please see the description of `lateral_rusher_player_name` for further information.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "lateral_rushing_yards"


class LateralSackPlayerId:
    """
    Unique identifier for the player that received the lateral on a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_sack_player_id"


class LateralSackPlayerName:
    """
    String name for the player that received the lateral on a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_sack_player_name"


class InterceptionPlayerId:
    """
    Unique identifier for the player that intercepted the pass.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "interception_player_id"


class InterceptionPlayerName:
    """
    String name for the player that intercepted the pass.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "interception_player_name"


class LateralInterceptionPlayerId:
    """
    Unique indentifier for the player that received the lateral on an interception.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_interception_player_id"


class LateralInterceptionPlayerName:
    """
    String name for the player that received the lateral on an interception.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_interception_player_name"


class PuntReturnerPlayerId:
    """
    Unique identifier for the punt returner.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "punt_returner_player_id"


class PuntReturnerPlayerName:
    """
    String name for the punt returner.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "punt_returner_player_name"


class LateralPuntReturnerPlayerId:
    """
    Unique identifier for the player that received the lateral on a punt return.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_punt_returner_player_id"


class LateralPuntReturnerPlayerName:
    """
    String name for the player that received the lateral on a punt return.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_punt_returner_player_name"


class KickoffReturnerPlayerName:
    """
    String name for the kickoff returner.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "kickoff_returner_player_name"


class KickoffReturnerPlayerId:
    """
    Unique identifier for the kickoff returner.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "kickoff_returner_player_id"


class LateralKickoffReturnerPlayerId:
    """
    Unique identifier for the player that received the lateral on a kickoff return.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_kickoff_returner_player_id"


class LateralKickoffReturnerPlayerName:
    """
    String name for the player that received the lateral on a kickoff return.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "lateral_kickoff_returner_player_name"


class PunterPlayerId:
    """
    Unique identifier for the punter.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "punter_player_id"


class PunterPlayerName:
    """
    String name for the punter.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "punter_player_name"


class KickerPlayerName:
    """
    String name for the kicker on FG or kickoff.

    Example Values
    --------------

    `"None"`

    `"M.Prater"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "kicker_player_name"


class KickerPlayerId:
    """
    Unique identifier for the kicker on FG or kickoff.

    Example Values
    --------------

    `"None"`

    `"00-0023853"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "kicker_player_id"


class OwnKickoffRecoveryPlayerId:
    """
    Unique identifier for the player that recovered their own kickoff.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "own_kickoff_recovery_player_id"


class OwnKickoffRecoveryPlayerName:
    """
    String name for the player that recovered their own kickoff.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "own_kickoff_recovery_player_name"


class BlockedPlayerId:
    """
    Unique identifier for the player that blocked the punt or FG.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "blocked_player_id"


class BlockedPlayerName:
    """
    String name for the player that blocked the punt or FG.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "blocked_player_name"


class TackleForLoss1PlayerId:
    """
    Unique identifier for one of the potential players with the tackle for loss.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_for_loss_1_player_id"


class TackleForLoss1PlayerName:
    """
    String name for one of the potential players with the tackle for loss.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_for_loss_1_player_name"


class TackleForLoss2PlayerId:
    """
    Unique identifier for one of the potential players with the tackle for loss.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_for_loss_2_player_id"


class TackleForLoss2PlayerName:
    """
    String name for one of the potential players with the tackle for loss.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_for_loss_2_player_name"


class QbHit1PlayerId:
    """
    Unique identifier for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "qb_hit_1_player_id"


class QbHit1PlayerName:
    """
    String name for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "qb_hit_1_player_name"


class QbHit2PlayerId:
    """
    Unique identifier for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "qb_hit_2_player_id"


class QbHit2PlayerName:
    """
    String name for one of the potential players that hit the QB. No sack as the QB was not the ball carrier. For sacks please see `sack_player` or `half_sack_*_player`.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "qb_hit_2_player_name"


class ForcedFumblePlayer1Team:
    """
    Team of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_1_team"


class ForcedFumblePlayer1PlayerId:
    """
    Unique identifier of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_1_player_id"


class ForcedFumblePlayer1PlayerName:
    """
    String name of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_1_player_name"


class ForcedFumblePlayer2Team:
    """
    Team of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_2_team"


class ForcedFumblePlayer2PlayerId:
    """
    Unique identifier of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_2_player_id"


class ForcedFumblePlayer2PlayerName:
    """
    String name of one of the players with a forced fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "forced_fumble_player_2_player_name"


class SoloTackle1Team:
    """
    Team of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"ARI"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_1_team"


class SoloTackle2Team:
    """
    Team of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_2_team"


class SoloTackle1PlayerId:
    """
    Unique identifier of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0035343"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_1_player_id"


class SoloTackle2PlayerId:
    """
    Unique identifier of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_2_player_id"


class SoloTackle1PlayerName:
    """
    String name of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"J.Ledbetter"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_1_player_name"


class SoloTackle2PlayerName:
    """
    String name of one of the players with a solo tackle.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "solo_tackle_2_player_name"


class AssistTackle1PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0034801"`

    `"00-0037815"`

    """

    header = "assist_tackle_1_player_id"


class AssistTackle1PlayerName:
    """
    String name of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"J.Woods"`

    `"C.Thomas"`

    """

    header = "assist_tackle_1_player_name"


class AssistTackle1Team:
    """
    Team of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"ARI"`

    `"ARI"`

    """

    header = "assist_tackle_1_team"


class AssistTackle2PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"00-0036933"`

    """

    header = "assist_tackle_2_player_id"


class AssistTackle2PlayerName:
    """
    String name of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"Z.Collins"`

    """

    header = "assist_tackle_2_player_name"


class AssistTackle2Team:
    """
    Team of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"ARI"`

    """

    header = "assist_tackle_2_team"


class AssistTackle3PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_3_player_id"


class AssistTackle3PlayerName:
    """
    String name of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_3_player_name"


class AssistTackle3Team:
    """
    Team of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_3_team"


class AssistTackle4PlayerId:
    """
    Unique identifier of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_4_player_id"


class AssistTackle4PlayerName:
    """
    String name of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_4_player_name"


class AssistTackle4Team:
    """
    Team of one of the players with a tackle assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "assist_tackle_4_team"


class TackleWithAssist:
    """
    Binary indicator for if there has been a tackle with assist.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    """

    header = "tackle_with_assist"

    TRUE = 1
    FALSE = 0


class TackleWithAssist1PlayerId:
    """
    Unique identifier of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0038984"`

    `"None"`

    """

    header = "tackle_with_assist_1_player_id"


class TackleWithAssist1PlayerName:
    """
    String name of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"K.Clark"`

    `"None"`

    """

    header = "tackle_with_assist_1_player_name"


class TackleWithAssist1Team:
    """
    Team of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"ARI"`

    `"None"`

    """

    header = "tackle_with_assist_1_team"


class TackleWithAssist2PlayerId:
    """
    Unique identifier of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_with_assist_2_player_id"


class TackleWithAssist2PlayerName:
    """
    String name of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_with_assist_2_player_name"


class TackleWithAssist2Team:
    """
    Team of one of the players with a tackle with assist.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "tackle_with_assist_2_team"


class PassDefense1PlayerId:
    """
    Unique identifier of one of the players with a pass defense.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "pass_defense_1_player_id"


class PassDefense1PlayerName:
    """
    String name of one of the players with a pass defense.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "pass_defense_1_player_name"


class PassDefense2PlayerId:
    """
    Unique identifier of one of the players with a pass defense.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "pass_defense_2_player_id"


class PassDefense2PlayerName:
    """
    String name of one of the players with a pass defense.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "pass_defense_2_player_name"


class Fumbled1Team:
    """
    Team of one of the first player with a fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_1_team"


class Fumbled1PlayerId:
    """
    Unique identifier of the first player who fumbled on the play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_1_player_id"


class Fumbled1PlayerName:
    """
    String name of one of the first player who fumbled on the play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_1_player_name"


class Fumbled2PlayerId:
    """
    Unique identifier of the second player who fumbled on the play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_2_player_id"


class Fumbled2PlayerName:
    """
    String name of one of the second player who fumbled on the play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_2_player_name"


class Fumbled2Team:
    """
    Team of one of the second player with a fumble.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumbled_2_team"


class FumbleRecovery1Team:
    """
    Team of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_1_team"


class FumbleRecovery1Yards:
    """
    Yards gained by one of the players with a fumble recovery.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "fumble_recovery_1_yards"


class FumbleRecovery1PlayerId:
    """
    Unique identifier of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_1_player_id"


class FumbleRecovery1PlayerName:
    """
    String name of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_1_player_name"


class FumbleRecovery2Team:
    """
    Team of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_2_team"


class FumbleRecovery2Yards:
    """
    Yards gained by one of the players with a fumble recovery.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "fumble_recovery_2_yards"


class FumbleRecovery2PlayerId:
    """
    Unique identifier of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_2_player_id"


class FumbleRecovery2PlayerName:
    """
    String name of one of the players with a fumble recovery.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "fumble_recovery_2_player_name"


class SackPlayerId:
    """
    Unique identifier of the player who recorded a solo sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "sack_player_id"


class SackPlayerName:
    """
    String name of the player who recorded a solo sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "sack_player_name"


class HalfSack1PlayerId:
    """
    Unique identifier of the first player who recorded half a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "half_sack_1_player_id"


class HalfSack1PlayerName:
    """
    String name of the first player who recorded half a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "half_sack_1_player_name"


class HalfSack2PlayerId:
    """
    Unique identifier of the second player who recorded half a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "half_sack_2_player_id"


class HalfSack2PlayerName:
    """
    String name of the second player who recorded half a sack.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "half_sack_2_player_name"


class ReturnTeam:
    """
    String abbreviation of the return team. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.

    Example Values
    --------------

    `"None"`

    `"WAS"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "return_team"


class ReturnYards:
    """
    Yards gained by the return team. Returns may occur on any of: interception, fumble, kickoff, punt, or blocked kicks.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "return_yards"


class PenaltyTeam:
    """
    String abbreviation of the team with the penalty.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "penalty_team"


class PenaltyPlayerId:
    """
    Unique identifier for the player with the penalty.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "penalty_player_id"


class PenaltyPlayerName:
    """
    String name for the player with the penalty.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "penalty_player_name"


class PenaltyYards:
    """
    Yards gained (or lost) by the posteam from the penalty.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "penalty_yards"


class ReplayOrChallenge:
    """
    Binary indicator for whether or not a replay or challenge.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "replay_or_challenge"

    TRUE = 1
    FALSE = 0


class ReplayOrChallengeResult:
    """
    String indicating the result of the replay or challenge.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "replay_or_challenge_result"

    UPHELD = "upheld"
    REVERSED = "reversed"


class PenaltyType:
    """
    String indicating the penalty type of the first penalty in the given play. Will be `NA` if `desc` is missing the type.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "penalty_type"

    ILLEGAL_BLOCK_ABOVE_THE_WAIST = "Illegal Block Above the Waist"
    LOWERING_THE_HEAD_TO_MAKE_FORCIBLE_CONTACT = (
        "Lowering the Head to Make Forcible Contact"
    )
    DEFENSIVE_PASS_INTERFERENCE = "Defensive Pass Interference"
    OFFENSIVE_PASS_INTERFERENCE = "Offensive Pass Interference"
    ROUGHING_THE_PASSER = "Roughing the Passer"
    INELIGIBLE_DOWNFIELD_PASS = "Ineligible Downfield Pass"
    OFFENSIVE_HOLDING = "Offensive Holding"
    FALSE_START = "False Start"
    UNSPORTSMANLIKE_CONDUCT = "Unsportsmanlike Conduct"
    DEFENSIVE_TOO_MANY_MEN_ON_FIELD = "Defensive Too Many Men on Field"
    DELAY_OF_GAME = "Delay of Game"
    DEFENSIVE_HOLDING = "Defensive Holding"
    TAUNTING = "Taunting"
    ILLEGAL_SHIFT = "Illegal Shift"
    UNNECESSARY_ROUGHNESS = "Unnecessary Roughness"
    ILLEGAL_FORMATION = "Illegal Formation"
    PLAYER_OUT_OF_BOUNDS_ON_KICK = "Player Out of Bounds on Kick"
    ILLEGAL_CONTACT = "Illegal Contact"
    DEFENSIVE_OFFSIDE = "Defensive Offside"
    TRIPPING = "Tripping"
    FACE_MASK = "Face Mask"
    RUNNING_INTO_THE_KICKER = "Running Into the Kicker"
    ILLEGAL_MOTION = "Illegal Motion"
    LOW_BLOCK = "Low Block"
    ILLEGAL_USE_OF_HANDS = "Illegal Use of Hands"
    INTENTIONAL_GROUNDING = "Intentional Grounding"
    ILLEGAL_BLINDSIDE_BLOCK = "Illegal Blindside Block"
    OFFSIDE_ON_FREE_KICK = "Offside on Free Kick"
    ENCROACHMENT = "Encroachment"
    ILLEGAL_TOUCH_KICK = "Illegal Touch Kick"
    NEUTRAL_ZONE_INFRACTION = "Neutral Zone Infraction"
    ROUGHING_THE_KICKER = "Roughing the Kicker"
    CHOP_BLOCK = "Chop Block"
    INELIGIBLE_DOWNFIELD_KICK = "Ineligible Downfield Kick"
    ILLEGAL_FORWARD_PASS = "Illegal Forward Pass"
    HORSE_COLLAR_TACKLE = "Horse Collar Tackle"
    DEFENSIVE_DELAY_OF_GAME = "Defensive Delay of Game"
    FAIR_CATCH_INTERFERENCE = "Fair Catch Interference"
    DISQUALIFICATION = "Disqualification"
    ILLEGAL_PEELBACK = "Illegal Peelback"
    ILLEGAL_TOUCH_PASS = "Illegal Touch Pass"
    OFFENSIVE_TOO_MANY_MEN_ON_FIELD = "Offensive Too Many Men on Field"
    LEVERAGE = "Leverage"
    LEAPING = "Leaping"
    ILLEGAL_CRACKBACK = "Illegal Crackback"
    OFFENSIVE_OFFSIDE = "Offensive Offside"
    ILLEGAL_SUBSTITUTION = "Illegal Substitution"
    KICK_CATCH_INTERFERENCE = "Kick Catch Interference"
    ILLEGAL_DOUBLETEAM_BLOCK = "Illegal Double-Team Block"
    ILLEGAL_KICKKICKING_LOOSE_BALL = "Illegal Kick/Kicking Loose Ball"
    CLIPPING = "Clipping"
    ILLEGAL_BAT = "Illegal Bat"


class DefensiveTwoPointAttempt:
    """
    Binary indicator whether or not the defense was able to have an attempt on a two point conversion, this results following a turnover.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defensive_two_point_attempt"

    TRUE = 1
    FALSE = 0


class DefensiveTwoPointConv:
    """
    Binary indicator whether or not the defense successfully scored on the two point conversion.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defensive_two_point_conv"

    TRUE = 1
    FALSE = 0


class DefensiveExtraPointAttempt:
    """
    Binary indicator whether or not the defense was able to have an attempt on an extra point attempt, this results following a blocked attempt that the defense recovers the ball.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defensive_extra_point_attempt"


class DefensiveExtraPointConv:
    """
    Binary indicator whether or not the defense successfully scored on an extra point attempt.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "defensive_extra_point_conv"


class SafetyPlayerName:
    """
    String name for the player who scored a safety.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "safety_player_name"


class SafetyPlayerId:
    """
    Unique identifier for the player who scored a safety.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "safety_player_id"


class Season:
    """
    4 digit number indicating to which season the game belongs to.

    Example Values
    --------------

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    `"2023"`

    """

    header = "season"


class Cp:
    """
    Numeric value indicating the probability for a complete pass based on comparable game situations.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.74763817`

    `nan`

    """

    header = "cp"


class Cpoe:
    """
    For a single pass play this is 1 - cp when the pass was completed or 0 - cp when the pass was incomplete. Analyzed for a whole game or season an indicator for the passer how much over or under expectation his completion percentage was.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `25.236183`

    `nan`

    """

    header = "cpoe"


class Series:
    """
    Starts at 1, each new first down increments, numbers shared across both teams NA: kickoffs, extra point/two point conversion attempts, non-plays, no posteam

    Example Values
    --------------

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "series"


class SeriesSuccess:
    """
    1: scored touchdown, gained enough yards for first down.

    Example Values
    --------------

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "series_success"

    TRUE = 1
    FALSE = 0


class SeriesResult:
    """
    Possible values: First down, Touchdown, Opp touchdown, Field goal, Missed field goal, Safety, Turnover, Punt, Turnover on downs, QB kneel, End of half

    Example Values
    --------------

    `"First down"`

    `"First down"`

    `"First down"`

    `"First down"`

    `"First down"`

    """

    header = "series_result"

    FIRST_DOWN = "First down"
    PUNT = "Punt"
    TOUCHDOWN = "Touchdown"
    FIELD_GOAL = "Field goal"
    TURNOVER = "Turnover"
    OPP_TOUCHDOWN = "Opp touchdown"
    TURNOVER_ON_DOWNS = "Turnover on downs"
    QB_KNEEL = "QB kneel"
    END_OF_HALF = "End of half"
    MISSED_FIELD_GOAL = "Missed field goal"
    SAFETY = "Safety"


class OrderSequence:
    """
    Column provided by NFL to fix out-of-order plays. Available 2011 and beyond with source "nfl".

    Example Values
    --------------

    `1.0`

    `39.0`

    `55.0`

    `77.0`

    `102.0`

    """

    header = "order_sequence"


class StartTime:
    """
    Kickoff time in eastern time zone.

    Example Values
    --------------

    `"9/10/23, 13:02:43"`

    `"9/10/23, 13:02:43"`

    `"9/10/23, 13:02:43"`

    `"9/10/23, 13:02:43"`

    `"9/10/23, 13:02:43"`

    """

    header = "start_time"


class TimeOfDay:
    """
    Time of day of play in UTC "HH:MM:SS" format. Available 2011 and beyond with source "nfl".

    Example Values
    --------------

    `"None"`

    `"2023-09-10T17:02:43.600Z"`

    `"2023-09-10T17:03:21.503Z"`

    `"2023-09-10T17:03:52.567Z"`

    `"2023-09-10T17:04:27.237Z"`

    """

    header = "time_of_day"


class Stadium:
    """
    Game site name.

    Example Values
    --------------

    `"Commanders Field"`

    `"Commanders Field"`

    `"Commanders Field"`

    `"Commanders Field"`

    `"Commanders Field"`

    """

    header = "stadium"

    COMMANDERS_FIELD = "Commanders Field"
    METLIFE_STADIUM = "MetLife Stadium"
    MERCEDESBENZ_STADIUM = "Mercedes-Benz Stadium"
    CLEVELAND_BROWNS_STADIUM = "Cleveland Browns Stadium"
    GEHA_FIELD_AT_ARROWHEAD_STADIUM = "GEHA Field at Arrowhead Stadium"
    SOLDIER_FIELD = "Soldier Field"
    MT_BANK_STADIUM = "M&T Bank Stadium"
    LUCAS_OIL_STADIUM = "Lucas Oil Stadium"
    LUMEN_FIELD = "Lumen Field"
    EMPOWER_FIELD_AT_MILE_HIGH = "Empower Field at Mile High"
    SOFI_STADIUM = "SoFi Stadium"
    GILLETTE_STADIUM = "Gillette Stadium"
    ACRISURE_STADIUM = "Acrisure Stadium"
    US_BANK_STADIUM = "U.S. Bank Stadium"
    CAESARS_SUPERDOME = "Caesars Superdome"
    PAYCOR_STADIUM = "Paycor Stadium"
    RAYMOND_JAMES_STADIUM = "Raymond James Stadium"
    NRG_STADIUM = "NRG Stadium"
    EVERBANK_STADIUM = "EverBank Stadium"
    NISSAN_STADIUM = "Nissan Stadium"
    HIGHMARK_STADIUM = "Highmark Stadium"
    LINCOLN_FINANCIAL_FIELD = "Lincoln Financial Field"
    BANK_OF_AMERICA_STADIUM = "Bank of America Stadium"
    STATE_FARM_STADIUM = "State Farm Stadium"
    ATT_STADIUM = "AT&T Stadium"
    FORD_FIELD = "Ford Field"
    HARD_ROCK_STADIUM = "Hard Rock Stadium"
    LAMBEAU_FIELD = "Lambeau Field"
    LEVIS_STADIUM = "Levi's® Stadium"
    ALLEGIANT_STADIUM = "Allegiant Stadium"
    WEMBLEY_STADIUM = "Wembley Stadium"
    TOTTENHAM_HOTSPUR_STADIUM = "Tottenham Hotspur Stadium"
    FRANKFURT_STADIUM = "Frankfurt Stadium"


class Weather:
    """
    String describing the weather including temperature, humidity and wind (direction and speed). Doesn't change during the game!

    Example Values
    --------------

    `"Cloudy Temp: 76° F, Humidity: 84%, Wind: S 2 mph"`

    `"Cloudy Temp: 76° F, Humidity: 84%, Wind: S 2 mph"`

    `"Cloudy Temp: 76° F, Humidity: 84%, Wind: S 2 mph"`

    `"Cloudy Temp: 76° F, Humidity: 84%, Wind: S 2 mph"`

    `"Cloudy Temp: 76° F, Humidity: 84%, Wind: S 2 mph"`

    """

    header = "weather"


class NflApiId:
    """
    UUID of the game in the new NFL API.

    Example Values
    --------------

    `"b07c705e-f053-11ed-b4a7-bab79e4492fa"`

    `"b07c705e-f053-11ed-b4a7-bab79e4492fa"`

    `"b07c705e-f053-11ed-b4a7-bab79e4492fa"`

    `"b07c705e-f053-11ed-b4a7-bab79e4492fa"`

    `"b07c705e-f053-11ed-b4a7-bab79e4492fa"`

    """

    header = "nfl_api_id"


class PlayClock:
    """
    Time on the playclock when the ball was snapped.

    Example Values
    --------------

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    """

    header = "play_clock"


class PlayDeleted:
    """
    Binary indicator for deleted plays.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "play_deleted"


class PlayTypeNfl:
    """
    Play type as listed in the NFL source. Slightly different to the regular play_type variable.

    Example Values
    --------------

    `"GAME_START"`

    `"KICK_OFF"`

    `"RUSH"`

    `"PASS"`

    `"RUSH"`

    """

    header = "play_type_nfl"

    GAME_START = "GAME_START"
    KICK_OFF = "KICK_OFF"
    RUSH = "RUSH"
    PASS = "PASS"
    PUNT = "PUNT"
    PENALTY = "PENALTY"
    XP_KICK = "XP_KICK"
    TIMEOUT = "TIMEOUT"
    FIELD_GOAL = "FIELD_GOAL"
    SACK = "SACK"
    END_QUARTER = "END_QUARTER"
    INTERCEPTION = "INTERCEPTION"
    UNSPECIFIED = "UNSPECIFIED"
    END_GAME = "END_GAME"
    FUMBLE_RECOVERED_BY_OPPONENT = "FUMBLE_RECOVERED_BY_OPPONENT"
    PAT2 = "PAT2"
    COMMENT = "COMMENT"


class SpecialTeamsPlay:
    """
    Binary indicator for whether play is special teams play from NFL source. Available 2011 and beyond with source "nfl".

    Example Values
    --------------

    `0.0`

    `1.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "special_teams_play"


class StPlayType:
    """
    Type of special teams play from NFL source. Available 2011 and beyond with source "nfl".

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "st_play_type"


class EndClockTime:
    """
    Game time at the end of a given play.

    Example Values
    --------------

    `"None"`

    `"2023-09-10T17:02:47.537Z"`

    `"2023-09-10T17:03:25.203Z"`

    `"2023-09-10T17:03:56.907Z"`

    `"2023-09-10T17:04:31.717Z"`

    """

    header = "end_clock_time"


class EndYardLine:
    """
    String indicating the yardline at the end of the given play consisting of team half and yard line number.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    `"None"`

    """

    header = "end_yard_line"


class FixedDrive:
    """
    Manually created drive number in a game.

    Example Values
    --------------

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "fixed_drive"


class FixedDriveResult:
    """
    Manually created drive result.

    Example Values
    --------------

    `"Punt"`

    `"Punt"`

    `"Punt"`

    `"Punt"`

    `"Punt"`

    """

    header = "fixed_drive_result"

    PUNT = "Punt"
    TOUCHDOWN = "Touchdown"
    FIELD_GOAL = "Field goal"
    TURNOVER = "Turnover"
    OPP_TOUCHDOWN = "Opp touchdown"
    TURNOVER_ON_DOWNS = "Turnover on downs"
    END_OF_HALF = "End of half"
    MISSED_FIELD_GOAL = "Missed field goal"
    SAFETY = "Safety"


class DriveRealStartTime:
    """
    Local day time when the drive started (currently not used by the NFL and therefore mostly 'NA').

    Example Values
    --------------

    `"None"`

    `"2023-09-10T17:02:43.600Z"`

    `"2023-09-10T17:02:43.600Z"`

    `"2023-09-10T17:02:43.600Z"`

    `"2023-09-10T17:02:43.600Z"`

    """

    header = "drive_real_start_time"


class DrivePlayCount:
    """
    Numeric value of how many regular plays happened in a given drive.

    Example Values
    --------------

    `nan`

    `8.0`

    `8.0`

    `8.0`

    `8.0`

    """

    header = "drive_play_count"


class DriveTimeOfPossession:
    """
    Time of possession in a given drive.

    Example Values
    --------------

    `"None"`

    `"4:01"`

    `"4:01"`

    `"4:01"`

    `"4:01"`

    """

    header = "drive_time_of_possession"


class DriveFirstDowns:
    """
    Number of forst downs in a given drive.

    Example Values
    --------------

    `nan`

    `2.0`

    `2.0`

    `2.0`

    `2.0`

    """

    header = "drive_first_downs"


class DriveInside20:
    """
    Binary indicator if the offense was able to get inside the opponents 20 yard line.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "drive_inside20"


class DriveEndedWithScore:
    """
    Binary indicator the drive ended with a score.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "drive_ended_with_score"

    TRUE = 1
    FALSE = 0


class DriveQuarterStart:
    """
    Numeric value indicating in which quarter the given drive has started.

    Example Values
    --------------

    `nan`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "drive_quarter_start"


class DriveQuarterEnd:
    """
    Numeric value indicating in which quarter the given drive has ended.

    Example Values
    --------------

    `nan`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "drive_quarter_end"


class DriveYardsPenalized:
    """
    Numeric value of how many yards the offense gained or lost through penalties in the given drive.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "drive_yards_penalized"


class DriveStartTransition:
    """
    String indicating how the offense got the ball.

    Example Values
    --------------

    `"None"`

    `"KICKOFF"`

    `"KICKOFF"`

    `"KICKOFF"`

    `"KICKOFF"`

    """

    header = "drive_start_transition"

    KICKOFF = "KICKOFF"
    PUNT = "PUNT"
    INTERCEPTION = "INTERCEPTION"
    FUMBLE = "FUMBLE"
    DOWNS = "DOWNS"
    MISSED_FG = "MISSED_FG"
    BLOCKED_FG = "BLOCKED_FG"
    BLOCKED_FG_DOWNS = "BLOCKED_FG,_DOWNS"
    MUFFED_PUNT = "MUFFED_PUNT"
    ONSIDE_KICK = "ONSIDE_KICK"
    BLOCKED_PUNT = "BLOCKED_PUNT"
    BLOCKED_PUNT_DOWNS = "BLOCKED_PUNT,_DOWNS"


class DriveEndTransition:
    """
    String indicating how the offense lost the ball.

    Example Values
    --------------

    `"None"`

    `"PUNT"`

    `"PUNT"`

    `"PUNT"`

    `"PUNT"`

    """

    header = "drive_end_transition"

    PUNT = "PUNT"
    TOUCHDOWN = "TOUCHDOWN"
    FIELD_GOAL = "FIELD_GOAL"
    INTERCEPTION = "INTERCEPTION"
    FUMBLE = "FUMBLE"
    DOWNS = "DOWNS"
    END_HALF = "END_HALF"
    END_GAME = "END_GAME"
    MISSED_FG = "MISSED_FG"
    BLOCKED_FG = "BLOCKED_FG"
    BLOCKED_FG_DOWNS = "BLOCKED_FG,_DOWNS"
    SAFETY = "SAFETY"
    FUMBLE_SAFETY = "FUMBLE,_SAFETY"
    BLOCKED_PUNT = "BLOCKED_PUNT"
    BLOCKED_PUNT_DOWNS = "BLOCKED_PUNT,_DOWNS"


class DriveGameClockStart:
    """
    Game time at the beginning of a given drive.

    Example Values
    --------------

    `"None"`

    `"15:00"`

    `"15:00"`

    `"15:00"`

    `"15:00"`

    """

    header = "drive_game_clock_start"


class DriveGameClockEnd:
    """
    Game time at the end of a given drive.

    Example Values
    --------------

    `"None"`

    `"10:59"`

    `"10:59"`

    `"10:59"`

    `"10:59"`

    """

    header = "drive_game_clock_end"


class DriveStartYardLine:
    """
    String indicating where a given drive started consisting of team half and yard line number.

    Example Values
    --------------

    `"None"`

    `"WAS 25"`

    `"WAS 25"`

    `"WAS 25"`

    `"WAS 25"`

    """

    header = "drive_start_yard_line"


class DriveEndYardLine:
    """
    String indicating where a given drive ended consisting of team half and yard line number.

    Example Values
    --------------

    `"None"`

    `"ARI 49"`

    `"ARI 49"`

    `"ARI 49"`

    `"ARI 49"`

    """

    header = "drive_end_yard_line"


class DrivePlayIdStarted:
    """
    Play_id of the first play in the given drive.

    Example Values
    --------------

    `nan`

    `39.0`

    `39.0`

    `39.0`

    `39.0`

    """

    header = "drive_play_id_started"


class DrivePlayIdEnded:
    """
    Play_id of the last play in the given drive.

    Example Values
    --------------

    `nan`

    `245.0`

    `245.0`

    `245.0`

    `245.0`

    """

    header = "drive_play_id_ended"


class AwayScore:
    """
    Total points scored by the away team.

    Example Values
    --------------

    `"16"`

    `"16"`

    `"16"`

    `"16"`

    `"16"`

    """

    header = "away_score"


class HomeScore:
    """
    Total points scored by the home team.

    Example Values
    --------------

    `"20"`

    `"20"`

    `"20"`

    `"20"`

    `"20"`

    """

    header = "home_score"


class Location:
    """
    Either 'Home' o 'Neutral' indicating if the home team played at home or at a neutral site.

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
    Equals home_score - away_score and means the game outcome from the perspective of the home team.

    Example Values
    --------------

    `"4"`

    `"4"`

    `"4"`

    `"4"`

    `"4"`

    """

    header = "result"


class Total:
    """
    Equals home_score + away_score and means the total points scored in the given game.

    Example Values
    --------------

    `"36"`

    `"36"`

    `"36"`

    `"36"`

    `"36"`

    """

    header = "total"


class SpreadLine:
    """
    The closing spread line for the game. A positive number means the home team was favored by that many points, a negative number means the away team was favored by that many points. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `7.0`

    `7.0`

    `7.0`

    `7.0`

    `7.0`

    """

    header = "spread_line"


class TotalLine:
    """
    The closing total line for the game. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `38.0`

    `38.0`

    `38.0`

    `38.0`

    `38.0`

    """

    header = "total_line"


class DivGame:
    """
    Binary indicator for if the given game was a division game.

    Example Values
    --------------

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    `"0"`

    """

    header = "div_game"

    TRUE = 1
    FALSE = 0


class Roof:
    """
    One of 'dome', 'outdoors', 'closed', 'open' indicating indicating the roof status of the stadium the game was played in. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `"outdoors"`

    `"outdoors"`

    `"outdoors"`

    `"outdoors"`

    `"outdoors"`

    """

    header = "roof"

    OUTDOORS = "outdoors"
    CLOSED = "closed"
    DOME = "dome"
    OPEN = "open"


class Surface:
    """
    What type of ground the game was played on. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `""`

    `""`

    `""`

    `""`

    `""`

    """

    header = "surface"

    FIELDTURF = "fieldturf"
    GRASS = "grass"
    SPORTTURF = "sportturf"
    MATRIXTURF = "matrixturf"
    A_TURF = "a_turf"
    ASTROTURF = "astroturf"


class Temp:
    """
    The temperature at the stadium only for 'roof' = 'outdoors' or 'open'.(Source: Pro-Football-Reference)

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
    The speed of the wind in miles/hour only for 'roof' = 'outdoors' or 'open'. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `nan`

    `nan`

    """

    header = "wind"


class HomeCoach:
    """
    First and last name of the home team coach. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `"Ron Rivera"`

    `"Ron Rivera"`

    `"Ron Rivera"`

    `"Ron Rivera"`

    `"Ron Rivera"`

    """

    header = "home_coach"


class AwayCoach:
    """
    First and last name of the away team coach. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `"Jonathan Gannon"`

    `"Jonathan Gannon"`

    `"Jonathan Gannon"`

    `"Jonathan Gannon"`

    `"Jonathan Gannon"`

    """

    header = "away_coach"


class StadiumId:
    """
    ID of the stadium the game was played in. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `"WAS00"`

    `"WAS00"`

    `"WAS00"`

    `"WAS00"`

    `"WAS00"`

    """

    header = "stadium_id"


class GameStadium:
    """
    Name of the stadium the game was played in. (Source: Pro-Football-Reference)

    Example Values
    --------------

    `"FedExField"`

    `"FedExField"`

    `"FedExField"`

    `"FedExField"`

    `"FedExField"`

    """

    header = "game_stadium"

    FEDEXFIELD = "FedExField"
    METLIFE_STADIUM = "MetLife Stadium"
    MERCEDESBENZ_STADIUM = "Mercedes-Benz Stadium"
    FIRSTENERGY_STADIUM = "FirstEnergy Stadium"
    GEHA_FIELD_AT_ARROWHEAD_STADIUM = "GEHA Field at Arrowhead Stadium"
    SOLDIER_FIELD = "Soldier Field"
    MT_BANK_STADIUM = "M&T Bank Stadium"
    LUCAS_OIL_STADIUM = "Lucas Oil Stadium"
    LUMEN_FIELD = "Lumen Field"
    EMPOWER_FIELD_AT_MILE_HIGH = "Empower Field at Mile High"
    SOFI_STADIUM = "SoFi Stadium"
    GILLETTE_STADIUM = "Gillette Stadium"
    ACRISURE_STADIUM = "Acrisure Stadium"
    US_BANK_STADIUM = "U.S. Bank Stadium"
    MERCEDESBENZ_SUPERDOME = "Mercedes-Benz Superdome"
    PAYCOR_STADIUM = "Paycor Stadium"
    RAYMOND_JAMES_STADIUM = "Raymond James Stadium"
    NRG_STADIUM = "NRG Stadium"
    TIAA_BANK_STADIUM = "TIAA Bank Stadium"
    NISSAN_STADIUM = "Nissan Stadium"
    NEW_ERA_FIELD = "New Era Field"
    LINCOLN_FINANCIAL_FIELD = "Lincoln Financial Field"
    BANK_OF_AMERICA_STADIUM = "Bank of America Stadium"
    STATE_FARM_STADIUM = "State Farm Stadium"
    ATT_STADIUM = "AT&T Stadium"
    FORD_FIELD = "Ford Field"
    HARD_ROCK_STADIUM = "Hard Rock Stadium"
    LAMBEAU_FIELD = "Lambeau Field"
    LEVIS_STADIUM = "Levi's Stadium"
    ALLEGIANT_STADIUM = "Allegiant Stadium"


class AbortedPlay:
    """
    Binary indicator if the play description indicates "Aborted".

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "aborted_play"

    TRUE = 1
    FALSE = 0


class Success:
    """
    Binary indicator wheter epa &gt; 0 in the given play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `1.0`

    `1.0`

    """

    header = "success"

    TRUE = 1
    FALSE = 0


class Passer:
    """
    Name of the dropback player (scrambles included) including plays with penalties.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"S.Howell"`

    `"None"`

    """

    header = "passer"


class PasserJerseyNumber:
    """
    Jersey number of the passer.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `14.0`

    `nan`

    """

    header = "passer_jersey_number"


class Rusher:
    """
    Name of the rusher (no scrambles) including plays with penalties.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"B.Robinson"`

    `"None"`

    `"C.Rodriguez"`

    """

    header = "rusher"


class RusherJerseyNumber:
    """
    Jersey number of the rusher.

    Example Values
    --------------

    `nan`

    `nan`

    `8.0`

    `nan`

    `23.0`

    """

    header = "rusher_jersey_number"


class Receiver:
    """
    Name of the receiver including plays with penalties.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"J.Dotson"`

    `"None"`

    """

    header = "receiver"


class ReceiverJerseyNumber:
    """
    Jersey number of the receiver.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `1.0`

    `nan`

    """

    header = "receiver_jersey_number"


class Pass:
    """
    Binary indicator if the play was a pass play (sacks and scrambles included).

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    """

    header = "pass"

    TRUE = 1
    FALSE = 0


class Rush:
    """
    Binary indicator if the play was a rushing play.

    Example Values
    --------------

    `0.0`

    `0.0`

    `1.0`

    `0.0`

    `1.0`

    """

    header = "rush"

    TRUE = 1
    FALSE = 0


class FirstDown:
    """
    Binary indicator if the play ended in a first down.

    Example Values
    --------------

    `nan`

    `0.0`

    `0.0`

    `0.0`

    `1.0`

    """

    header = "first_down"

    TRUE = 1
    FALSE = 0


class Special:
    """
    Binary indicator if "play_type" is one of "extra_point", "field_goal", "kickoff", or "punt".

    Example Values
    --------------

    `0.0`

    `1.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "special"

    TRUE = 1
    FALSE = 0


class Play:
    """
    Binary indicator: 1 if the play was a 'normal' play (including penalties), 0 otherwise.

    Example Values
    --------------

    `0.0`

    `0.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "play"

    TRUE = 1
    FALSE = 0


class PasserId:
    """
    ID of the player in the 'passer' column.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0037077"`

    `"None"`

    """

    header = "passer_id"


class RusherId:
    """
    ID of the player in the 'rusher' column.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0037746"`

    `"None"`

    `"00-0038611"`

    """

    header = "rusher_id"


class ReceiverId:
    """
    ID of the player in the 'receiver' column.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"00-0037741"`

    `"None"`

    """

    header = "receiver_id"


class Name:
    """
    Name of the 'passer' if it is not 'NA', or name of the 'rusher' otherwise.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"B.Robinson"`

    `"S.Howell"`

    `"C.Rodriguez"`

    """

    header = "name"


class JerseyNumber:
    """
    Jersey number of the player listed in the 'name' column.

    Example Values
    --------------

    `nan`

    `nan`

    `8.0`

    `14.0`

    `23.0`

    """

    header = "jersey_number"


class Id:
    """
    ID of the player in the 'name' column.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0037746"`

    `"00-0037077"`

    `"00-0038611"`

    """

    header = "id"


class FantasyPlayerName:
    """
    Name of the rusher on rush plays or receiver on pass plays (from official stats).

    Example Values
    --------------

    `"None"`

    `"None"`

    `"B.Robinson"`

    `"J.Dotson"`

    `"C.Rodriguez"`

    """

    header = "fantasy_player_name"


class FantasyPlayerId:
    """
    ID of the rusher on rush plays or receiver on pass plays (from official stats).

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0037746"`

    `"00-0037741"`

    `"00-0038611"`

    """

    header = "fantasy_player_id"


class Fantasy:
    """
    Name of the rusher on rush plays or receiver on pass plays.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"B.Robinson"`

    `"J.Dotson"`

    `"C.Rodriguez"`

    """

    header = "fantasy"


class FantasyId:
    """
    ID of the rusher on rush plays or receiver on pass plays.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"00-0037746"`

    `"00-0037741"`

    `"00-0038611"`

    """

    header = "fantasy_id"


class OutOfBounds:
    """
    1 if play description contains ran ob, pushed ob, or sacked ob; 0 otherwise.

    Example Values
    --------------

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    `0.0`

    """

    header = "out_of_bounds"

    TRUE = 1
    FALSE = 0


class HomeOpeningKickoff:
    """
    1 if the home team received the opening kickoff, 0 otherwise.

    Example Values
    --------------

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    `1.0`

    """

    header = "home_opening_kickoff"

    TRUE = 1
    FALSE = 0


class QbEpa:
    """
    Gives QB credit for EPA for up to the point where a receiver lost a fumble after a completed catch and makes EPA work more like passing yards on plays with fumbles.

    Example Values
    --------------

    `0.0`

    `0.0`

    `-0.33610347`

    `0.7033076`

    `0.46979922`

    """

    header = "qb_epa"


class XyacEpa:
    """
    Expected value of EPA gained after the catch, starting from where the catch was made. Zero yards after the catch would be listed as zero EPA.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.34065217`

    `nan`

    """

    header = "xyac_epa"


class XyacMeanYardage:
    """
    Average expected yards after the catch based on where the ball was caught.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `3.3286417`

    `nan`

    """

    header = "xyac_mean_yardage"


class XyacMedianYardage:
    """
    Median expected yards after the catch based on where the ball was caught.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `1.0`

    `nan`

    """

    header = "xyac_median_yardage"


class XyacSuccess:
    """
    Probability play earns positive EPA (relative to where play started) based on where ball was caught.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.99662787`

    `nan`

    """

    header = "xyac_success"


class XyacFd:
    """
    Probability play earns a first down based on where the ball was caught.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.5839282`

    `nan`

    """

    header = "xyac_fd"


class Xpass:
    """
    Probability of dropback scaled from 0 to 1.

    Example Values
    --------------

    `nan`

    `nan`

    `0.51505846`

    `0.66110593`

    `0.19606467`

    """

    header = "xpass"


class PassOe:
    """
    Dropback percent over expected on a given play scaled from 0 to 100.

    Example Values
    --------------

    `nan`

    `nan`

    `-51.505844`

    `33.88941`

    `-19.606466`

    """

    header = "pass_oe"


class NflverseGameId:
    """
    nflverse identifier for games. Format is season, week, away_team, home_team

    Example Values
    --------------

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    `"2023_01_ARI_WAS"`

    """

    header = "nflverse_game_id"


class OldGameIdY:
    """
    No documentation available.

    Example Values
    --------------

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    `"2023091007"`

    """

    header = "old_game_id_y"


class PossessionTeam:
    """
    String abbreviation for the team with possession.

    Example Values
    --------------

    `""`

    `"ARI"`

    `"WAS"`

    `"WAS"`

    `"WAS"`

    """

    header = "possession_team"


class OffenseFormation:
    """
    Formation the offense lines up in to snap the ball.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"SHOTGUN"`

    `"SHOTGUN"`

    `"I_FORM"`

    """

    header = "offense_formation"

    SHOTGUN = "SHOTGUN"
    I_FORM = "I_FORM"
    SINGLEBACK = "SINGLEBACK"
    EMPTY = "EMPTY"
    WILDCAT = "WILDCAT"
    JUMBO = "JUMBO"
    PISTOL = "PISTOL"


class OffensePersonnel:
    """
    Number of running backs, tight ends, and wide receivers on the field for the play. If there are more than the standard 5 offensive linemen and 1 quarterback, they will be listed here as well.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"1 RB, 2 TE, 2 WR"`

    `"1 RB, 1 TE, 3 WR"`

    `"1 RB, 1 TE, 3 WR"`

    """

    header = "offense_personnel"


class DefendersInBox:
    """
    Number of defensive players lined up in the box at the snap.

    Example Values
    --------------

    `nan`

    `nan`

    `7.0`

    `6.0`

    `6.0`

    """

    header = "defenders_in_box"


class DefensePersonnel:
    """
    Number of defensive linemen, linebackers, and defensive backs on the field for the play.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"3 DL, 4 LB, 4 DB"`

    `"2 DL, 4 LB, 5 DB"`

    `"2 DL, 4 LB, 5 DB"`

    """

    header = "defense_personnel"


class NumberOfPassRushers:
    """
    Number of defensive player who rushed the passer.

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `4.0`

    `nan`

    """

    header = "number_of_pass_rushers"


class PlayersOnPlay:
    """
    A list of every player on the field for the play, by gsis_it_id

    Example Values
    --------------

    `""`

    `"48000;52641;54721;56098;53639;53448;55912;45102;42512;53553;54705;46674;43986;54709;31446;46807;52535;46649;52474;56058;52570;52863"`

    `"49410;54563;41475;52516;47812;46629;53445;41349;53639;53480;52522;46188;56045;44848;53553;54609;54481;47859;46968;48473;53565;45695"`

    `"49410;54563;41475;52516;47812;46629;53445;41349;53480;46188;56045;44848;54609;54481;47859;44852;52535;46968;54552;48473;53565;45695"`

    `"49410;41475;47812;52516;46629;53445;41349;53480;46188;56045;44848;54609;54481;47859;44852;52535;46968;54552;48473;56058;53565;45695"`

    """

    header = "players_on_play"


class OffensePlayers:
    """
    A list of every offensive player on the field for the play, by gsis_id

    Example Values
    --------------

    `""`

    `"00-0035150;00-0037330;00-0036896;00-0033251;00-0034490;00-0032933;00-0037747;00-0023853;00-0034623;00-0036395;00-0035961"`

    `"00-0037746;00-0031095;00-0036334;00-0034445;00-0031260;00-0036618;00-0036628;00-0037077;00-0037741;00-0035659;00-0033831"`

    `"00-0037746;00-0031095;00-0036334;00-0034445;00-0031260;00-0036618;00-0037077;00-0037741;00-0035659;00-0033282;00-0033831"`

    `"00-0031095;00-0036334;00-0034445;00-0031260;00-0036618;00-0037077;00-0037741;00-0035659;00-0033282;00-0038611;00-0033831"`

    """

    header = "offense_players"


class DefensePlayers:
    """
    A list of every defensive player on the field for the play, by gsis_id

    Example Values
    --------------

    `""`

    `"00-0036403;00-0038635;00-0036614;00-0039149;00-0031596;00-0036628;00-0037095;00-0034465;00-0036328;00-0038611;00-0036343"`

    `"00-0035705;00-0035636;00-0036933;00-0036896;00-0036371;00-0034375;00-0038984;00-0033890;00-0034801;00-0035343;00-0036884"`

    `"00-0035705;00-0035636;00-0036933;00-0034375;00-0038984;00-0033890;00-0036395;00-0034801;00-0037815;00-0035343;00-0036884"`

    `"00-0035705;00-0035636;00-0036933;00-0034375;00-0038984;00-0033890;00-0036395;00-0034801;00-0037815;00-0035343;00-0036884"`

    """

    header = "defense_players"


class NOffense:
    """
    Number of offensive players on the field for the play

    Example Values
    --------------

    `0.0`

    `11.0`

    `11.0`

    `11.0`

    `11.0`

    """

    header = "n_offense"


class NDefense:
    """
    Number of defensive players on the field for the play

    Example Values
    --------------

    `0.0`

    `11.0`

    `11.0`

    `11.0`

    `11.0`

    """

    header = "n_defense"


class NgsAirYards:
    """
    Distance (in yards) that the ball traveled in the air on a given passing play as tracked by NGS

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `4.53`

    `nan`

    """

    header = "ngs_air_yards"


class TimeToThrow:
    """
    Duration (in seconds) between the time of the ball being snapped and the time of release of a pass attempt

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `2.169`

    `nan`

    """

    header = "time_to_throw"


class WasPressure:
    """
    A boolean indicating whether or not the QB was pressured on a play

    Example Values
    --------------

    `nan`

    `nan`

    `nan`

    `0.0`

    `nan`

    """

    header = "was_pressure"

    TRUE = 1
    FALSE = 0


class Route:
    """
    No documentation available.

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"HITCH"`

    `"None"`

    """

    header = "route"

    HITCH = "HITCH"
    IN = "IN"
    SCREEN = "SCREEN"
    FLAT = "FLAT"
    CROSS = "CROSS"
    ANGLE = "ANGLE"
    WHEEL = "WHEEL"
    POST = "POST"
    SLANT = "SLANT"
    OUT = "OUT"
    CORNER = "CORNER"
    GO = "GO"


class DefenseManZoneType:
    """
    A string indicating whether the defense was in man or zone coverage on a play

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"ZONE_COVERAGE"`

    `"None"`

    """

    header = "defense_man_zone_type"

    ZONE_COVERAGE = "ZONE_COVERAGE"
    MAN_COVERAGE = "MAN_COVERAGE"


class DefenseCoverageType:
    """
    A string indicating what type of cover the defense was in on a play

    Example Values
    --------------

    `"None"`

    `"None"`

    `"None"`

    `"COVER_3"`

    `"None"`

    """

    header = "defense_coverage_type"

    COVER_3 = "COVER_3"
    COVER_4 = "COVER_4"
    COVER_1 = "COVER_1"
    COVER_0 = "COVER_0"
    COVER_6 = "COVER_6"
    COVER_2 = "COVER_2"
    MAN_2 = "2_MAN"
    PREVENT = "PREVENT"
