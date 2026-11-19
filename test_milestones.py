import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from milestones import LAYERS, MILESTONES, validate_data


def test_approved_ids_and_order():
    assert validate_data()
    assert [m["id"] for m in MILESTONES] == [f"AI-{n:03d}" for n in range(1, 30)]


def test_six_layers_are_populated():
    assert len(LAYERS) == 6
    assert {m["layer"] for m in MILESTONES} == {1, 2, 3, 4, 5, 6}


def test_each_milestone_has_required_detail_and_sources():
    for milestone in MILESTONES:
        for field in ("date", "title", "contributors", "what", "approach", "significance", "impact", "limitations", "sources"):
            assert milestone.get(field), f"{milestone['id']} missing {field}"
        assert all(url.startswith("https://") for _, url in milestone["sources"])


def test_approved_layer_distribution():
    counts = {layer_id: sum(m["layer"] == layer_id for m in MILESTONES) for layer_id in range(1, 7)}
    assert counts == {1: 5, 2: 4, 3: 4, 4: 4, 5: 5, 6: 7}
