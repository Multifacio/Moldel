from Data import *

# Suspicion Levels must be determined manually by looking for early activity. "Wie is de Mol" is often recorded during
# the month May and June, so during these months you have to check for activity. The recording of "Wie is de Mol" take
# 18 days in total.

# You can use the social media analysis of Jaap van Zessen to fill in these values. For example for season 19 this can
# be found at the following url: https://www.ad.nl/show/de-social-media-analyse-van-wie-is-de-mol-2019~ac68622f/
# If this is not possible for certain seasons then you should analyse Facebook, Twitter, Youtube, Instagram, etc
# with a tool and determine if that player was active.

# Suspicion Levels are quite subjective, but these are the guidelines for the Suspicion Levels:
# -NOT_UNLIKELY: Only if you cannot find any form of activity during the recording period.
# -SLIGHTLY_UNLIKELY: If the player has posted more tweets or facebook posts than before. Or had a phone call during
# night time (of the recorded country). Etcetera...
# -UNLIKELY: If the player has posted many tweets or facebook post. Has uploaded some instagram pictures. If the
# player has posted some tweets or facebook posts with pictures. If the player was present during a dutch radio 
# recording or had multiple phone call during night time (of the recorded country) or a combination of these things.
# Or if the player has uploaded a some short video. Etcetera...
# -VERY_UNLIKELY: If the player has uploaded a long video. Or if the player has some picture with a dutch background. 
# If the player participated in another dutch television show/serie. Or if there is any clear evidence that the 
# player was present in the Netherland during the recording. Or if the player carries out his/her current job. Or if 
# the player was present during multiple dutch radio recording. Extremely many tweets or facebook posts or a 
# combination is not enough the be classified in this category.

# Closer to the end date of the recording will be considered closer to NOT_UNLIKELY. Declaration of witnesses will not
# be used to determine suspicion levels and also rumours of suspicions of any kind will also not be used to determine
# suspicion levels. If there is no other form of activity then the player has to be classified as NOT_UNLIKELY.

# Only based on https://www.ad.nl/show/de-social-media-analyse-van-wie-is-de-mol-2019~ac68622f/
SEASON19 = {Player.ROBERT_19: SuspicionLevel.UNLIKELY, Player.SINAN_19: SuspicionLevel.UNLIKELY,
            Player.EVI_19: SuspicionLevel.VERY_UNLIKELY, Player.NIKKIE_19: SuspicionLevel.UNLIKELY,
            Player.EVELIEN_19: SuspicionLevel.NOT_UNLIKELY, Player.JAMIE_19: SuspicionLevel.NOT_UNLIKELY,
            Player.MEREL_19: SuspicionLevel.NOT_UNLIKELY, Player.NIELS_19: SuspicionLevel.NOT_UNLIKELY,
            Player.RICK_PAUL_19: SuspicionLevel.NOT_UNLIKELY, Player.SARAH_19: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.ad.nl/show/social-media-analyse-wie-is-de-mol-2018~ac1d7cf8/
SEASON18 = {Player.BELLA_18: SuspicionLevel.NOT_UNLIKELY, Player.EMILIO_18: SuspicionLevel.NOT_UNLIKELY,
            Player.JAN_18: SuspicionLevel.NOT_UNLIKELY, Player.JEAN_MARC_18: SuspicionLevel.NOT_UNLIKELY,
            Player.LOES_18: SuspicionLevel.NOT_UNLIKELY, Player.OLCAY_18: SuspicionLevel.NOT_UNLIKELY,
            Player.RON_18: SuspicionLevel.NOT_UNLIKELY, Player.RUBEN_18: SuspicionLevel.NOT_UNLIKELY,
            Player.SIMONE_18: SuspicionLevel.NOT_UNLIKELY, Player.STINE_18: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.ad.nl/tv-en-radio/dit-zijn-de-afvallers-van-wie-is-de-mol-2017~a995a64a/
SEASON17 = {Player.ROOS_17: SuspicionLevel.UNLIKELY, Player.SIGRID_17: SuspicionLevel.UNLIKELY,
            Player.VINCENT_17: SuspicionLevel.SLIGHTLY_UNLIKELY, Player.DIEDERIK_17: SuspicionLevel.NOT_UNLIKELY,
            Player.IMANUELLE_17: SuspicionLevel.NOT_UNLIKELY, Player.JEROEN_17: SuspicionLevel.NOT_UNLIKELY,
            Player.JOCHEM_17: SuspicionLevel.NOT_UNLIKELY, Player.SANNE_17: SuspicionLevel.NOT_UNLIKELY,
            Player.THOMAS_17: SuspicionLevel.NOT_UNLIKELY, Player.YVONNE_17: SuspicionLevel.NOT_UNLIKELY}

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/nieuwe-wie-is-de-mol-social-media-analyse-live/
SEASON16 = {Player.AIREN_16: SuspicionLevel.UNLIKELY, Player.TAEKE_16: SuspicionLevel.UNLIKELY,
            Player.ELLIE_16: SuspicionLevel.SLIGHTLY_UNLIKELY, Player.MARJOLEIN_16: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Player.CECILE_16: SuspicionLevel.SLIGHTLY_UNLIKELY, Player.ANNEMIEKE_16: SuspicionLevel.NOT_UNLIKELY,
            Player.ROP_16: SuspicionLevel.NOT_UNLIKELY, Player.KLAAS_16: SuspicionLevel.NOT_UNLIKELY,
            Player.TIM_16: SuspicionLevel.NOT_UNLIKELY, Player.REMY_16: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.marketingfacts.nl/berichten/social-media-voorspelt-ook-afvaller-wie-is-de-mol-door-monitoring
SEASON15 = {Player.CAROLINA_15: SuspicionLevel.SLIGHTLY_UNLIKELY, Player.EVELIEN_15: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Player.AJOUAD_15: SuspicionLevel.NOT_UNLIKELY, Player.CHRIS_15: SuspicionLevel.NOT_UNLIKELY,
            Player.MARGRIET_15: SuspicionLevel.NOT_UNLIKELY, Player.MARLIJN_15: SuspicionLevel.NOT_UNLIKELY,
            Player.MARTINE_15: SuspicionLevel.NOT_UNLIKELY, Player.PIETER_15: SuspicionLevel.NOT_UNLIKELY,
            Player.RIK_15: SuspicionLevel.NOT_UNLIKELY, Player.VIKTOR_15: SuspicionLevel.NOT_UNLIKELY}

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/wie-de-mol-deelnemer-laten-sporen-achter-op-social-media/
SEASON14 = {Player.MAURICE_14: SuspicionLevel.UNLIKELY, Player.FREEK_14: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Player.TYGO_14: SuspicionLevel.UNLIKELY, Player.AAF_14: SuspicionLevel.NOT_UNLIKELY,
            Player.DAPHNE_14: SuspicionLevel.NOT_UNLIKELY, Player.JAN_WILLEM_14: SuspicionLevel.NOT_UNLIKELY,
            Player.JENNIFER_14: SuspicionLevel.NOT_UNLIKELY, Player.OWEN_14: SuspicionLevel.NOT_UNLIKELY,
            Player.SOFIE_14: SuspicionLevel.NOT_UNLIKELY, Player.SUSAN_14: SuspicionLevel.NOT_UNLIKELY}

SUSPICION_DATA = {19: SEASON19, 18: SEASON18, 17: SEASON17, 16: SEASON16, 15: SEASON15, 14: SEASON14}