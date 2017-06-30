"""
This is a basic class for the Game Controller
"""
# -*- coding: utf-8 -*-
# pylint: disable=import-error

import json
import TapGameController.TapGameFSM


def organize_speechace_result(results):
    """
    Converts speechace results from a messy dictionary to list of phonemes
    and their bool values
    """
    SCORE_THRESHOLD = 70
    speech_result_list = []

    for word in range(len(results)):
        syllable_score_list = results[word]["syllable_score_list"]
        for syllable in syllable_score_list:
            letters = syllable["letters"]
            if syllable["quality_score"] > SCORE_THRESHOLD:
                passed = True
            else:
                passed = False
            speech_result_list.append((letters, passed))

    return speech_result_list


def convert_speechaceResult_to_JSON(results):
    """
    generate a Json message for phoneme pronouciation accuracy results
    """
    speech_result_list = organize_speechace_result(results)
    return json.dumps(speech_result_list)