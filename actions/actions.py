from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from utils.utils import fetch_a_joke


class ActionTellJoke(Action):
    def name(self) -> Text:
        return "action_tell_joke"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        """
        fetches joke from method fetch_a_joke()
        sends message to user of joke and asks them did that helped or not
        :return: empty list
        """
        joke = fetch_a_joke()
        dispatcher.utter_message(text=joke)
        dispatcher.utter_message(template="utter_did_that_help")
        return []
