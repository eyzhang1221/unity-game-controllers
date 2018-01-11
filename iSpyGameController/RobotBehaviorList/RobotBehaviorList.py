"""
This is a class defines different "cosmetic" (i.e. not necessarily in the Agent ActionSpace)
Robot Behaviors
"""
# -*- coding: utf-8 -*-
# pylint: disable=import-error, invalid-name
from unity_game_msgs.msg import iSpyCommand
from enum import Enum
import json
import random



class RobotBehaviors:  # pylint: disable=no-member, too-many-instance-attributes
    """
    A Class definition for "cosmetic" robot behavior strings, which get translated by the ROSNodeMgr
    """

    # Look Ats
    LOOK_AT_TABLET = 'LOOK_AT_TABLET'
    LOOK_CENTER = 'LOOK_CENTER'
    LOOK_LEFT_RIGHT = 'LOOK_LEFT_RIGHT'
    LOOK_DOWN_CENTER = 'LOOK_DOWN_CENTER'

    # Positive Emotions
    ROBOT_EXCITED = 'ROBOT_EXCITED'
    ROBOT_INTERESTED = 'ROBOT_INTERESTED'
    ROBOT_YES = 'ROBOT_YES'
    ROBOT_HAPPY_DANCE = 'ROBOT_HAPPY_DANCE'
    ROBOT_CURIOUS = 'ROBOT_CURIOUS'
    ROBOT_ATTENTION = 'ROBOT_ATTENTION' # Pose Forward 
    ROBOT_CELEBRATION = 'ROBOT_CELEBRATION'
    ROBOT_ENCOURAGING = 'ROBOT_ENCOURAGING'
    ROBOT_WINK = 'ROBOT_WINK'
    ROBOT_THINKING = 'ROBOT_THINKING'

   

    ROBOT_SAY_WORD = 'ROBOT_SAY_WORD'
    
    # Negative Emotions
    ROBOT_SAD = 'ROBOT_SAD'
    ROBOT_UNSURE = 'ROBOT_UNSURE'
    ROBOT_COMFORT = 'ROBOT_COMFORT'
    ROBOT_ASK_HELP = 'ROBOT_ASK_HELP'
    ROBOT_DISAPPOINTED = 'ROBOT_DISAPPOINTED'

 

    # virtual actions on the app
    VIRTUALLY_CLICK_CORRECT_OBJ = "CLICK_CORRECT_OBJ" # click correct obj
    VIRTUALLY_CLICK_WRONG_OBJ = "CLICK_WRONG_OBJ"
    VIRTUALLY_EXPLORE = "EXPLORING"
    VIRTUALLY_CLICK_SAY_BUTTON = "CLICK_SAY_BUTTON"
    VIRTUALLY_HELP_CHILD = "HELP_CHILD"

    ## Tega Speech for Curiosity Assessment
    GENERAL_CURIOSITY_SPEECH = "GENERAL_CURIOSITY_SPEECH"
    BASED_ON_PROMPTS_SPEECH = "BASED_ON_PROMPTS_SPEECH"
    TRY_PRONOUNCE = "TRY_PRONOUNCE"
    BASED_ON_OBJECTS = "BASED_ON_OBJECTS"
    OBJECTS = "OBJECTS"


    ROBOT_CUSTOM_SPEECH = "ROBOT_CUSTOM_SPEECH"

    ### ============== Tega Speech for Role Switching Project ================== ###
    BEFORE_GAME_SPEECH = "ROBOT_BEFORE_GAME_SPEECH"
    VOCAB_EXPLANATION_SPEECH = "VOCAB_EXPLANATION_SPEECH"
    HINT_SPEECH = "HINT_SPEECH"
    KEYWORD_DEFINITION_SPEECH = "KEYWORD_DEFINITION_SPEECH"


   ### ====== Tega Question Asking =================== ####
    Q_ROBOT_OFFER_HELP = "Q_ROBOT_OFFER_HELP"
    Q_ROBOT_ASK_WHY_CHOOSE_IT="Q_ROBOT_ASK_WHY_CHOOSE_IT"
    Q_ROBOT_WANT_LEARN="Q_ROBOT_WANT_LEARN"
    Q_ROBOT_ASK_HELP="Q_ROBOT_ASK_HELP"
    Q_ROBOT_ASK_WHY_WRONG="Q_ROBOT_ASK_WHY_WRONG"
    Q_END_OF_TURN="Q_END_OF_TURN"





class RobotRoles(Enum):
    '''
    contains a list of social roles that are avaiable to robot to perform
    '''
    EXPERT = 0
    #COMPETENT = 1
    NOVICE = 1


class RobotActionSequence:

    TURN_STARTED = "TURN_STARTED"
    SCREEN_MOVED = "SCREEN_MOVED"
    OBJECT_FOUND = "OBJECT_FOUND"
    OBJECT_CLICKED = "OBJECT_CLICKED" #
    OBJECT_PRONOUNCED = "OBJECT_PRONOUNCED" #
    RESULTS_RETURNED = "RESULTS_RETURNED" 
    TURN_FINISHED = "TURN_FINISHED" #
    PRONOUNCE_CORRECT = "PRONOUNCE_CORRECT"
    WRONG_OBJECT_FAIL ="WRONG_OBJECT_FAIL" 

    class Triggers:
        NEXT = "Next"
        RESET = "Reset"


ROOT_TEGA_SPEECH_FOLDER = 'roleswitching18/'
            
class RobotRolesBehaviorsMap:
    '''
    mapping between robot's social role and robot's specific behaviors
    '''  
    def __init__(self):
        # robot's actions during its turn
        self.robot_turn_mapping = {}
        # robot's actions during child's turn
        self.child_turn_mapping = {}


        robot_actions_file = open("iSpyGameController/res/robot_actions.json")
        self.robot_actions_dict = json.loads(robot_actions_file.read())

        question_answer_file = open("iSpyGameController/res/question_answer.json")
        self.question_answer_dict = json.loads(question_answer_file.read())

        #test = getattr(RobotBehaviors,pre)
      
    def get_action_name(self,action):
        '''
        return the correct action name (convert the action name in json file to the action name in RobotBehaviorList)
        '''
        try: 
            return getattr(RobotBehaviors,action)
        except:
            return action

    def get_robot_general_responses(self):
        pass   

    def get_robot_question(self,question_query_path):
        '''
        get question query result 
        '''
        print("quewstion query path: "+question_query_path)
        self.current_question_query_path = question_query_path
        if question_query_path in self.question_answer_dict.keys():
            self.question_query = self.question_answer_dict[question_query_path]
            print("question query: ")
            print(self.question_query)
            question_name = random.choice(self.question_query['question'])

            return ROOT_TEGA_SPEECH_FOLDER + "questions/" +question_name+".wav"
        else:
            print("ERROR: Cannot find the question query.")
            return ""

    def get_robot_response_to_answer(self,child_answer):
        '''
        get robot's contigent response to the child's answer
        '''
        print("child answer: "+child_answer)
        if self.current_question_query_path in self.question_answer_dict.keys():
            for i in self.question_query["user_input"]:
                print("i:")
                print(i)
                if any(m in child_answer for m in i["en_US"]): # found child's answer
                    return i["response"]
                    break
            print("WARNING: Cannot find child's answer")
            return []
        else:
            print("ERROR: Cannot find the question query.")
            return []

        
    def get_actions(self,role,robot_turn,physical_virtual):
    
        try:
            role = role.name
        except:
            role = "BACKUP"
        return self.robot_actions_dict[role][robot_turn][physical_virtual]
        
  


