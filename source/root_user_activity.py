""" Module for detecting root user activity """

import json

from reflex_core import AWSRule, subscription_confirmation


class RootUserActivity(AWSRule):
    """ AWS rule for detecting root user activity """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required data from the event """
        # We don't need any information from the event.
        pass  # pylint: disable=unnecessary-pass

    def resource_compliant(self):
        """ Determines if the resource is compliant. Returns True if compliant, False otherwise """
        # We simply want to know when this event occurs. Since this rule was
        # triggered we know that happened, and we want to alert. Therefore
        # the resource is never compliant.
        return False

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return "Root user activity was detected."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = RootUserActivity(event_payload)
    rule.run_compliance_rule()
