"""One completed round and replay through Chromium, HTTP, and real rules."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_play_round_and_replay(page: Page, live_server, monkeypatch):
    """Replay replaces a win with the next round's loss and current choices."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    page.goto(live_server)
    expect(page.get_by_role("status")).to_have_count(0)

    page.get_by_role("button", name="Rock", exact=True).click()
    choices = page.get_by_label("This round’s choices").locator(".choice-value")
    expect(choices.nth(0)).to_contain_text("Rock")
    expect(choices.nth(1)).to_contain_text("Scissors")
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")

    page.get_by_role("button", name="Paper", exact=True).click()
    expect(choices.nth(0)).to_contain_text("Paper")
    expect(choices.nth(1)).to_contain_text("Scissors")
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_have_count(0)
