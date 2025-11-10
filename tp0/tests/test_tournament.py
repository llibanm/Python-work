from tp0.tournament import tournament
import pytest


def test_tournament_with_one_team():
    season = tournament(1)
    assert season == [[]]


def test_tournament_with_two_teams():
    season = tournament(2)
    assert season == [(1, 2)] or [(2, 1)]


@pytest.mark.parametrize('n', [*range(3, 42)])
def test_tournament(n):
    N = n if n % 2 == 0 else n + 1
    nrounds, nmatches = N - 1, n // 2
    season = tournament(n)
    opponents: list[list[int]] = [[] for _ in range(n)]
    home_count: list[int] = [0] * n
    assert len(season) == nrounds, f"{len(season)} rounds, {nrounds} expected"
    for round in season:
        assert len(round) == nmatches, f"{len(round)} matches, {nmatches} expected"
        for match in round:
            assert len(match) == 2 and match[0] != match[1], "match plays with 2 distinct teams"
            assert 1 <= match[0] <= n and 1 <= match[1] <= n, "team ID out of range"
            opponents[match[0] - 1].append(match[1])
            opponents[match[1] - 1].append(match[0])
            home_count[match[0] - 1] += 1
    assert all(nrounds // 2 <= home_count[i] <= (nrounds + 1) // 2 for i in range(n)), "home count not balanced"
    assert all(len(set(teams)) == n - 1 and\
               i + 1 not in teams for i, teams in enumerate(opponents)), "missing opponents"

