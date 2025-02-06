import os
from dotenv import load_dotenv
import pytest

from safelyx import (
    check_email,
    check_image,
    check_link,
    check_message,
)

load_dotenv()
TEST_KEY_CODE = os.getenv("TEST_KEY_CODE")


def test_check_link():
    tests = [
        {
            "url": "example.com",
            "expected": {
                "url": "https://example.com",
                "result": 8,
                "result_text": "This link looks safe.",
                "date": "2025-01-01",
                "analysis": {
                    "domain_reputation": "This domain wasn't found in any malicious lists.",
                    "source_code": "This website appears to have only basic HTML.",
                    "anti_virus": "N/A",
                },
                "checks_remaining": 1000,
            },
        },
    ]

    for test in tests:
        parsed_url = check_link(test["url"], TEST_KEY_CODE)
        assert parsed_url["url"] == test["expected"]["url"]
        assert parsed_url["result"] == -2 or (8 <= parsed_url["result"] <= 10)
        assert "result_text" in parsed_url
        assert "date" in parsed_url
        assert "analysis" in parsed_url
        assert "domain_reputation" in parsed_url["analysis"]
        assert "source_code" in parsed_url["analysis"]
        assert "anti_virus" in parsed_url["analysis"]
        assert "checks_remaining" in parsed_url


def test_check_email():
    tests = [
        {
            "email": "help@safelyx.com",
            "expected": {
                "email": "help@safelyx.com",
                "result": 8,
                "result_text": "This email looks legitimate.",
                "date": "2025-01-01",
                "analysis": {
                    "address": "This email address is valid.",
                    "domain_reputation": "This domain isn't found in any malicious lists.",
                    "mx_records": "This domain has valid MX records.",
                },
                "checks_remaining": 1000,
            },
        },
    ]

    for test in tests:
        parsed_email = check_email(test["email"], TEST_KEY_CODE)
        assert parsed_email["email"] == test["expected"]["email"]
        assert parsed_email["result"] == -2 or (8 <= parsed_email["result"] <= 10)
        assert "result_text" in parsed_email
        assert "date" in parsed_email
        assert "analysis" in parsed_email
        assert "address" in parsed_email["analysis"]
        assert "domain_reputation" in parsed_email["analysis"]
        assert "mx_records" in parsed_email["analysis"]
        assert "checks_remaining" in parsed_email


def test_check_message():
    tests = [
        {
            "message": "Hello, world!",
            "expected": {
                "message": "Hello, world!",
                "result": 8,
                "result_text": "This message appears to be safe.",
                "date": "2025-01-01",
                "analysis": {
                    "content": "This message appears to be safe.",
                    "sentiment": "positive",
                    "links": [],
                    "emails": [],
                },
                "checks_remaining": 1000,
            },
        },
    ]

    for test in tests:
        parsed_message = check_message(test["message"], key_code=TEST_KEY_CODE)
        assert parsed_message["message"] == test["expected"]["message"]
        assert parsed_message["result"] == -2 or (8 <= parsed_message["result"] <= 10)
        assert "result_text" in parsed_message
        assert "date" in parsed_message
        assert "analysis" in parsed_message
        assert "content" in parsed_message["analysis"]
        assert "sentiment" in parsed_message["analysis"]
        assert "links" in parsed_message["analysis"]
        assert "emails" in parsed_message["analysis"]
        assert "checks_remaining" in parsed_message


def test_check_image():
    tests = [
        {
            "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            "expected": {
                "image_url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                "result": 8,
                "result_text": "This image appears to be safe.",
                "date": "2025-01-01",
                "analysis": {
                    "description": "This image appears to be safe.",
                    "link": {
                        "url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
                        "result": 8,
                        "date": "2025-01-01",
                        "analysis": {
                            "domain_reputation": "This domain wasn't found in any malicious lists.",
                            "source_code": "This link returns a file.",
                            "anti_virus": "No viruses found.",
                        },
                    },
                },
                "checks_remaining": 1000,
            },
        },
    ]

    for test in tests:
        parsed_image = check_image(test["image_url"], TEST_KEY_CODE)
        assert parsed_image["image_url"] == test["expected"]["image_url"]
        assert parsed_image["result"] == -2 or (8 <= parsed_image["result"] <= 10)
        assert "result_text" in parsed_image
        assert "date" in parsed_image
        assert "analysis" in parsed_image
        assert "description" in parsed_image["analysis"]
        assert "link" in parsed_image["analysis"]
        assert "url" in parsed_image["analysis"]["link"]
        assert "result" in parsed_image["analysis"]["link"]
        assert "date" in parsed_image["analysis"]["link"]
        assert "analysis" in parsed_image["analysis"]["link"]
        assert "domain_reputation" in parsed_image["analysis"]["link"]["analysis"]
        assert "source_code" in parsed_image["analysis"]["link"]["analysis"]
        assert "anti_virus" in parsed_image["analysis"]["link"]["analysis"]
        assert "checks_remaining" in parsed_image
