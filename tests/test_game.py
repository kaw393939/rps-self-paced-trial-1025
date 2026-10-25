"""RPS-001 outcomes from SPEC.md and one request using the real rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_rule_outcomes(player, computer, expected):
    """Each literal expected answer comes from the agreed nine-matchup table."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_submitted_round_uses_real_rules(monkeypatch):
    """A real request displays both choices and the correct winning result."""
    monkeypatch.setitem(web.app.config, "TESTING", True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "scissors")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})

    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert '<p class="choice-value">Rock ' in body
    assert '<p class="choice-value">Scissors ' in body
    assert "You win!" in body
    assert 'data-outcome="win"' in body
    assert "game rules not built yet" not in body
