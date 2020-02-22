# This is the configuration file for the FaceTracker class. When you want to run the FaceTracker for a certain episode
# then you need to change these values appropriately. Do not commit the changes to this file!
from Data.Player import Player

# The season and episode number which are used to save the face visibility results of the videos and to load them
# during training of the FaceVisibility layer.
SEASON_NUMBER = 11
EPISODE_NUMBER = 4

# The location to the video file of the episode on which you want to run the FaceTracker. Only mp4 and mkv files have
# been tested with the FaceTracker, other video formats might not work. Make sure that only the episode is included in
# video. MolTalk and commercial breaks should not be contained in the video.
EPISODE_VIDEO_LOCATION = "/home/multifacio/WIDM/Seizoen 11/Videos/Episode 4.mp4"

# Is a set of all players that were alive during this episode, including the person that dropped off during this
# episode. But excluding players that dropped off during earlier episodes and did not return during this episode.
ALIVE_PLAYERS = {Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11, Player.PATRICK_11,
                 Player.PEPIJN_11, Player.SOUNDOS_11}

# The locations of the pictures for each candidate. Make sure that the quality of this pictures is good enough. This
# means that for each candidate the chin, eyes, mouth and nose are clearly visible. Also the edges of the face should
# be clear in the picture (if there is too much shadow over the face in the picture then it might have problems
# detecting the candidates). The candidate should look right into the camera (not to the left or the right). Moreover
# make sure that the picture only contains the head of the candidate (including the body of the candidate is unnecessary
# and having multiple faces in 1 picture might confuse the algorithm). Recommended is to pick a close-up of the
# candidate during the first episode or a moment when the candidate has a solo talk moment with a black background
# where he gives his opinion about something that happened. Never use a picture from the intro (because these are often
# low quality and candidates might look different during the intro then during the episode). If you cannot find a good
# quality picture then you can search for one on Google or check the second episode. When getting the results make sure
# that every candidate, except the candidates that dropped off, have been detected at least 75 times during every
# episode or has been detected at least 100 times during episode 2, 3 or 4. If this is not the case then you should
# pick a higher quality picture of the candidate. If this new picture still does not give higher detection values then
# you should pick the best picture and stick to the low detection values of the candidate.
FACE_IMAGE_LOCATIONS = {Player.ANNA_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Anna.jpeg",
                        Player.ART_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Art.jpeg",
                        Player.HANNA_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Hanna.jpeg",
                        Player.HORACE_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Horace.jpeg",
                        Player.JAN_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Jan.jpeg",
                        Player.KARIN_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Karin.jpeg",
                        Player.MIRYANNA_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Miryanna.jpeg",
                        Player.PATRICK_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Patrick.jpeg",
                        Player.PEPIJN_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Pepijn.jpeg",
                        Player.SOUNDOS_11: "/home/multifacio/WIDM/Seizoen 11/Candidates/Soundos.jpeg"}

# How many frames get skipped before analysing a frame (setting this value higher will make the script run faster,
# but makes the results less accurate). The general rule is to use 1 frame every 0.5 seconds. Therefore for video files
# with 25 frames per second it is recommended to use a FRAME_SKIP of 10 (which means a frame get analysed every 0.4
# second). For video files with 30 frames per second it is recommended to use a FRAME_SKIP of 15.
FRAME_SKIP = 10

# The folder in which all parsed results of the videos will be stored.
SAVE_FOLDER = "moldel/Data/FaceVisibilityData/"