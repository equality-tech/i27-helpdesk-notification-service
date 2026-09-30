import pytest
from pydantic import ValidationError

from app.schemas.notification_event import NotificationEvent as EmailNotificationEvent
from app.services.email_templates import ticket_event_email
from app.services.event_rules import EVENT_RULES
from app.services.notification_schema import NotificationEvent


def test_ticket_created_rule_targets_administrators():
    assert EVENT_RULES["TICKET_CREATED"]["roles"] == ["ADMIN"]


def test_ticket_assigned_rule_targets_agents():
    assert EVENT_RULES["TICKET_ASSIGNED"]["roles"] == ["AGENT"]


def test_ticket_created_email_contains_ticket_id():
    subject, body = ticket_event_email("TICKET_CREATED", 25, "STUDENT")
    assert "#25" in subject
    assert "Ticket ID: 25" in body


def test_unknown_event_uses_default_email_template():
    _, body = ticket_event_email("UNKNOWN", 25, "ADMIN")
    assert "An update occurred on Ticket ID: 25" in body


def test_notification_event_requires_recipient_email():
    with pytest.raises(ValidationError):
        EmailNotificationEvent(event_type="TICKET_CREATED", ticket_id=1, actor_id=2)
