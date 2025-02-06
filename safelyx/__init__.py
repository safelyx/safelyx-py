from typing import TypedDict, Optional, List
import requests


class DomainAnalysis(TypedDict):
    domain_reputation: str
    source_code: str
    anti_virus: str


class SafeLinkResponse(TypedDict):
    url: str
    result: int
    result_text: str
    date: str
    analysis: DomainAnalysis
    checks_remaining: int


class EmailAnalysis(TypedDict):
    address: str
    domain_reputation: str
    mx_records: str


class SafeEmailResponse(TypedDict):
    email: str
    result: int
    result_text: str
    date: str
    analysis: EmailAnalysis
    checks_remaining: int


class MessageAnalysis(TypedDict):
    content: str
    sentiment: str
    links: List[SafeLinkResponse]
    emails: List[SafeEmailResponse]


class SafeMessageResponse(TypedDict):
    message: str
    result: int
    result_text: str
    date: str
    analysis: MessageAnalysis
    checks_remaining: int


class ImageAnalysis(TypedDict):
    description: str
    link: SafeLinkResponse


class SafeImageResponse(TypedDict):
    image_url: str
    result: int
    result_text: str
    date: str
    analysis: ImageAnalysis
    checks_remaining: int


# ... existing code (TypedDict definitions) ...


def check_link(link: str, key_code: Optional[str] = None) -> SafeLinkResponse:
    """
    Securely checks if a link is safe to click or visit.

    Args:
        link: The URL to check
        key_code: The purchased key code to bypass the free limit

    Returns:
        SafeLinkResponse object containing the analysis results
    """
    response = requests.post(
        "https://safelyx.com/safe-link-checker",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json; charset=utf-8",
        },
        json={"link": link, "key_code": key_code},
    )
    return response.json()


def check_email(email: str, key_code: Optional[str] = None) -> SafeEmailResponse:
    """
    Securely checks if an email address is legitimate.

    Args:
        email: The email address to check
        key_code: The purchased key code to bypass the free limit

    Returns:
        SafeEmailResponse object containing the analysis results
    """
    response = requests.post(
        "https://safelyx.com/safe-email-checker",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json; charset=utf-8",
        },
        json={"email": email, "key_code": key_code},
    )
    return response.json()


def check_message(
    message: str,
    skip_link_and_email_checks: bool = False,
    key_code: Optional[str] = None,
) -> SafeMessageResponse:
    """
    Securely checks if a message's content is safe.

    Args:
        message: The message to check
        skip_link_and_email_checks: Whether to skip the link and email checks
        key_code: The purchased key code to bypass the free limit

    Returns:
        SafeMessageResponse object containing the analysis results
    """
    response = requests.post(
        "https://safelyx.com/safe-message-checker",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json; charset=utf-8",
        },
        json={
            "message": message,
            "skip_link_and_email_checks": skip_link_and_email_checks,
            "key_code": key_code,
        },
    )
    return response.json()


def check_image(image_url: str, key_code: Optional[str] = None) -> SafeImageResponse:
    """
    Securely checks if an image is safe.

    Args:
        image_url: The URL of the image to check
        key_code: The purchased key code to bypass the free limit

    Returns:
        SafeImageResponse object containing the analysis results
    """
    response = requests.post(
        "https://safelyx.com/safe-image-checker",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json={"image_url": image_url, "key_code": key_code},
    )
    return response.json()


# Export all functions in a dictionary similar to the JS default export
safelyx = {
    "check_link": check_link,
    "check_email": check_email,
    "check_message": check_message,
    "check_image": check_image,
}
