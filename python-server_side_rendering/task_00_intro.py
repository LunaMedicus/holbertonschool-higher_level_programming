#!/usr/bin/env python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate output files by replacing placeholders with attendee data."""
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list):
        print(f"Error: attendees must be a list, got {type(attendees).__name__}")
        return
    if not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))
        with open(f"output_{i}.txt", "w") as f:
            f.write(content)
