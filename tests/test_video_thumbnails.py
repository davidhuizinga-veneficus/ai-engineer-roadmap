"""YouTube resources show a thumbnail preview that opens the video."""

import pytest
from playwright.sync_api import Page, expect

STAGES = [
    "llm-foundations",
    "agents",
    "mcp-skills",
    "rag",
    "multi-agent",
    "evaluation",
    "security",
    "deployment",
    "final-project",
]
YOUTUBE = 'a.rm-item[href*="youtube.com/watch"]'


def test_llm_foundations_has_a_refresh_video_from_the_start(page: Page) -> None:
    page.goto("stages/llm-foundations/")
    video = page.locator('a.rm-item[href*="LPZh9BOjkQs"]')
    expect(video).to_have_count(1)
    expect(video).to_have_attribute(
        "href", "https://www.youtube.com/watch?v=LPZh9BOjkQs"
    )
    expect(video).to_have_class("rm-item rm-refresh")


def test_llm_foundations_no_longer_asks_for_a_refresh_video(page: Page) -> None:
    page.goto("stages/llm-foundations/")
    expect(page.get_by_text("Opfrisvideo nog te kiezen")).to_have_count(0)


@pytest.mark.parametrize("stage", STAGES)
def test_youtube_resources_show_their_thumbnail_inside_the_link(
    page: Page, stage: str
) -> None:
    page.goto(f"stages/{stage}/")
    for link in page.locator(YOUTUBE).all():
        video_id = (link.get_attribute("href") or "").split("v=")[1]
        thumbnail = link.locator("img.rm-thumb-img")
        expect(thumbnail).to_be_visible()
        expect(thumbnail).to_have_attribute(
            "src", f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        )


@pytest.mark.parametrize("stage", STAGES)
def test_other_resources_have_no_thumbnail(page: Page, stage: str) -> None:
    page.goto(f"stages/{stage}/")
    others = page.locator(f"a.rm-item:not({YOUTUBE.removeprefix('a.rm-item')})")
    expect(others.locator("img.rm-thumb-img")).to_have_count(0)


def test_both_youtube_videos_get_a_thumbnail(page: Page) -> None:
    for stage in ("llm-foundations", "multi-agent"):
        page.goto(f"stages/{stage}/")
        expect(page.locator(f"{YOUTUBE} img.rm-thumb-img")).to_have_count(1)


def test_thumbnail_keeps_the_checkbox_label_unchanged(page: Page) -> None:
    page.goto("stages/multi-agent/")
    checkbox = page.locator(".rm-check").first
    expect(checkbox).to_have_attribute(
        "aria-label", 'Markeer "Multi-Agent Systems Explained" als gedaan'
    )
