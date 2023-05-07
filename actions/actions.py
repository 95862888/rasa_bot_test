# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetConfidence(Action):
    def name(self) -> Text:
        return "action_get_confidence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # intent = tracker.latest_message['intent'].get('name')
        confidence = round(tracker.latest_message['intent'].get('confidence') * 100, 2)

        dispatcher.utter_message(text=f'{confidence}%')

        return []
