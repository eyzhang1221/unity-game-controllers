"""
This is a class defines different "cosmetic" (i.e. not necessarily in the Agent ActionSpace)
Robot Behaviors
"""
# -*- coding: utf-8 -*-
# pylint: disable=import-error, invalid-name

from .RobotBehaviorList import RobotBehaviors
from random import randint
from GameUtils import GlobalSettings
import random

if GlobalSettings.USE_ROS:
    import rospy
    from std_msgs.msg import Header  # standard ROS msg header
    from unity_game_msgs.msg import TapGameCommand
    from unity_game_msgs.msg import TapGameLog
    from r1d1_msgs.msg import TegaAction
    from r1d1_msgs.msg import Vec3
    from jibo_msgs.msg import JiboAction
else:
    TapGameLog = GlobalSettings.TapGameLog  # Mock object, used for testing in non-ROS environments
    TapGameCommand = GlobalSettings.TapGameCommand
    TegaAction = GlobalSettings.TegaAction



GENERAL_CURIOSITY_SPEECH=["a.mp3","b.mp3","d.mp3","e.mp3","f.mp3"]
BASED_ON_PROMPTS=["vehicle.mp3","delighted.mp3","crimson.mp3","azure.mp3","soar.mp3","aquatic.mp3","gigantic.mp3","minuscule.mp3","recreational.mp3","garment.mp3"]
BASED_ON_OBJECTS=["a.1.mp3","b.1.mp3","c.1.mp3"]
BASED_ON_OBJECTS_TEMPLATES=["b-template.mp3", "c-template.mp3"]
OBJECTS=["baby.mp3","bicylce.mp3", "baby.mp3", "bicycle.mp3", "bird.mp3", "boat.mp3", "bucket.mp3" , "bus.mp3" , "car.mp3" , "castle.mp3" , "cat.mp3" , "cloud.mp3" , "coconut.mp3" , "deer.mp3" , "digging.mp3" , "dog.mp3" , "dolphine.mp3" , "door.mp3" , "dress.mp3" , "duck.mp3" , "eating.mp3" , "father.mp3" , "fish.mp3" , "fishing.mp3" , "flower.mp3" , "forest.mp3" , "frog.mp3" , "giraffe.mp3" ,"goat.mp3","grandma.mp3","grandpa.mp3","hat.mp3","horse.mp3","jumping.mp3","lion.mp3","mailbox.mp3","mother.mp3" ,"mountain.mp3","mouse.mp3","pants.mp3" ,"plane.mp3" ,"rabbit.mp3","rooster.mp3" ,"running.mp3","seal.mp3","seashell.mp3" , "sheep.mp3" , "shirt.mp3" , "sun.mp3" , "tractor.mp3" , "train.mp3", "waving.mp3", "window.mp3"]


OPTIONAL_ACTIONS = []

class TegaBehaviors:  # pylint: disable=no-member, too-many-instance-attributes
    """
    A Class definition for "cosmetic" robot behavior strings, which get translated by the ROSNodeMgr
    """
    @staticmethod
    def get_msg_from_behavior(command, *args): #pylint: disable=too-many-branches, too-many-statements

        msg = TegaAction()
        msg.header = Header()
        msg.header.stamp = rospy.Time.now()



        ## Look at Commands
        if command == RobotBehaviors.LOOK_AT_TABLET:
            lookat_pos = Vec3()
            lookat_pos.x = 0
            lookat_pos.y = -10
            lookat_pos.z = 20
            msg.do_look_at = True
            msg.look_at = lookat_pos

        if command == RobotBehaviors.LOOK_CENTER:
            lookat_pos = Vec3()
            lookat_pos.x = 0
            lookat_pos.y = 10
            lookat_pos.z = 40
            msg.do_look_at = True
            msg.look_at = lookat_pos

        """
        if command == RobotBehaviors.LOOK_LEFT_RIGHT:
            lookat_pos = Vec3()
            lookat_pos.x = 0
            lookat_pos.y = -10
            lookat_pos.z = 20
            msg.do_look_at = True
            msg.look_at = lookat_pos

        if command == RobotBehaviors.LOOK_DOWN_CENTER:
            lookat_pos = Vec3()
            lookat_pos.x = 0
            lookat_pos.y = -10
            lookat_pos.z = 20
            msg.do_look_at = True
            msg.look_at = lookat_pos
        """


        ## Positive Commands
        if command == RobotBehaviors.ROBOT_EXCITED:
            msg.motion = TegaAction.MOTION_EXCITED

        if command == RobotBehaviors.ROBOT_INTERESTED:
            msg.motion = TegaAction.MOTION_INTERESTED

        if command == RobotBehaviors.ROBOT_YES:
            msg.motion = TegaAction.MOTION_YES

        if command == RobotBehaviors.ROBOT_HAPPY_DANCE:
            msg.motion = TegaAction.MOTION_HAPPY_DANCE

        if command == RobotBehaviors.ROBOT_CURIOUS:
            msg.motion = TegaAction.MOTION_POSE_FORWARD

        if command == RobotBehaviors.ROBOT_ATTENTION:
            msg.motion = TegaAction.MOTION_SHIMMY

        if command == RobotBehaviors.ROBOT_CELEBRATION:
            msg.motion = TegaAction.MOTION_CIRCLING

        if command == RobotBehaviors.ROBOT_ENCOURAGING:
            msg.motion = TegaAction.MOTION_PERKUP

        if command == RobotBehaviors.ROBOT_WINK:
            msg.motion = TegaAction.MOTION_NOD

        if command == RobotBehaviors.ROBOT_THINKING:
            msg.motion = TegaAction.MOTION_THINKING


        ## Negative Commands
        if command == RobotBehaviors.ROBOT_SAD:
            msg.motion = TegaAction.MOTION_SAD

        if command == RobotBehaviors.ROBOT_UNSURE:
            msg.motion = TegaAction.MOTION_PUZZLED

        if command == RobotBehaviors.ROBOT_COMFORT:
            msg.motion = TegaAction.MOTION_FLAT_AGREEMENT 

        if command == RobotBehaviors.ROBOT_ASK_HELP:
            msg.motion = TegaAction.MOTION_POSE_FORWARD

        if command == RobotBehaviors.ROBOT_DISAPPOINTED:
            msg.motion = TegaAction.MOTION_FRUSTRATED 


        # Tega speech commands
        if command == RobotBehaviors.ROBOT_CUSTOM_SPEECH:
            msg.wav_filename = args[0][0]
            msg.enqueue = True
            print(msg.wav_filename)

        ## Tega Speech for Curiosity Assessment

        # General Curiosity Speech
        if command == RobotBehaviors.GENERAL_CURIOSITY_SPEECH:
            # the default path in Tega is "contentroot/robots/tega/01/speech", 
            # so no need to add this prefix in the path here. make sure all audios are under this prefix path
            PATH = "TegaAudio/generalcuriosity/"
            speech_file_name = PATH + random.choice(GENERAL_CURIOSITY_SPEECH)
            msg.wav_filename = speech_file_name
            msg.enqueue = True
            print(speech_file_name)

        # Based on prompts speech
        if command == RobotBehaviors.BASED_ON_PROMPTS_SPEECH:
            PATH = "TegaAudio/basedonprompts/"
            vocab_word =args[0][0].lower()
            print("vocab word is "+vocab_word)
            print(args)
            speech_file_name = PATH + vocab_word + ".mp3"
            msg.wav_filename = speech_file_name
            msg.enqueue = True
            print(speech_file_name)

	   # Before pronunciation
        if command == RobotBehaviors.TRY_PRONOUNCE:
            PATH = "TegaAudio/generalcuriosity/"
            speech_file_name = PATH + "c.mp3"
            msg.wav_filename = speech_file_name
            msg.enqueue = True

	   # Based on objects
        if command == RobotBehaviors.BASED_ON_OBJECTS:
            PATH = "TegaAudio/basedonobjects/"
            speech_file_name = PATH + random.choice(BASED_ON_OBJECTS_TEMPLATES)
            msg.wav_filename = speech_file_name
            msg.enqueue = True

	   # Random objects
        if command == RobotBehaviors.OBJECTS:
            PATH = "TegaAudio/objects/"
            speech_file_name = PATH + random.choice(OBJECTS)
            msg.wav_filename = speech_file_name
            msg.enqueue = True

        if command == RobotBehaviors.ROBOT_SAY_WORD:
            PATH = "roleswitching18/object_words/"
            object_word =args[0][0].lower()
            speech_file_name = PATH + object_word + ".mp3"
            msg.wav_filename = speech_file_name
            msg.enqueue = True
        

        return msg
