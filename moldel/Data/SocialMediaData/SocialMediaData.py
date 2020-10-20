from Data.Player import *

# This Social Media Data file contains all players that are excluded, because of early activity or other evidence (found
# on Social Media) which shows that these players have dropped out earlier during the recording of "Wie is de Mol". To
# determine which players should be excluded, you can use the Social Media Analysis of Jaap van Zessen. All of his
# analyses can be found at: http://www.jaapvanzessen.nl/tag/wie-is-de-mol/ If he has not posted a Social Media Analysis
# or if the analysis does not provide enough information then you can manually analyse Facebook, Twitter, Youtube,
# Instagram, etc. or look at Youtube channels that cover "Wie is de Mol" suspicions. "Wie is de Mol" is often recorded
# during the month May and June, so during these months you have to check for activity. The recording of "Wie is de Mol"
# takes around 18 days in total.

# Note that you should only exclude players if there is clear evidence that the player drops out early. The following
# cases are NOT considered as clear evidence that the player drops out early:
# - High activity on Social Media, because "Wie is de Mol?" players often have internet access during the recording
#   period. Moreover another person could have posted this as well.
# - Posting pictures or videos on Social Media, because these pictures and videos might have been recorded at an earlier
#   moment and uploaded at a later moment.
# - Following behavior on Social Media, because being followed by many other players does not always mean that you will
#   stay in the game.
# - Phone calls during the night of the country in which "Wie is de Mol?" is recorded. This is indeed weird behavior,
#   but not necessary a clear indication that someone dropped out earlier.
# - Evidence of activity that happened very close to the end of the recording period or after the recording period.
# - Witness statements, without pictures/videos to back these statements up, about players dropping out early or players
#   that stayed in the game.
#
# The following cases are considered as clear evidence that the player drops out early:
# - Pictures/videos of which the date when taken is known, where the date is early during the recording period and it
#   should be clear in this picture/video that the player is not at the location where "Wie is de Mol?" is recorded.
# - Multiple pictures/videos leaked of the recording on which players are shown to be still in the game. Players that
#   are missing in these pictures/videos are considered to drop out early.
# - A television show (different than "Wie is de Mol?") or radio show recorded during the recording period of
#   "Wie is de Mol?" in which the given player was active.
# - Death/serious illness of a family member of the given player during the recording period, which caused the player to
#   return back to home.
# - Evidence which proves that the given player was in the Netherlands during the recording period.
# - Evidence which shows that the given player carried out his job during the recording period of "Wie is de Mol?".
# - Situations which are extremely weird to take place during the recording period of "Wie is de Mol?", such as
#   publishing a book.


# Based on manual Social Media Analysis
SEASON21 = {Player.ELLIE_21}

# Only based on https://www.ad.nl/show/wie-is-de-mol-deelnemers-doen-er-alles-aan-om-geheim-te-blijven-maar-helaas~adef878e/
SEASON20 = {Player.ANITA_20, Player.JOHAN_20, Player.TINA_20}

# Only based on https://www.ad.nl/show/de-social-media-analyse-van-wie-is-de-mol-2019~ac68622f/
SEASON19 = {Player.ROBERT_19, Player.EVI_19, Player.NIKKIE_19}

# Only based on https://www.ad.nl/show/social-media-analyse-wie-is-de-mol-2018~ac1d7cf8/
SEASON18 = set()

# Only based on https://www.ad.nl/tv-en-radio/dit-zijn-de-afvallers-van-wie-is-de-mol-2017~a995a64a/
SEASON17 = {Player.ROOS_17}

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/nieuwe-wie-is-de-mol-social-media-analyse-live/
SEASON16 = {Player.AIREN_16, Player.TAEKE_16}

# Only based on https://www.marketingfacts.nl/berichten/social-media-voorspelt-ook-afvaller-wie-is-de-mol-door-monitoring
SEASON15 = set()

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/wie-de-mol-deelnemer-laten-sporen-achter-op-social-media/
SEASON14 = {Player.MAURICE_14}

SUSPICION_DATA = {21: SEASON21, 20: SEASON20, 19: SEASON19, 18: SEASON18, 17: SEASON17, 16: SEASON16, 15: SEASON15,
                  14: SEASON14}