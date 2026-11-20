
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from milestones import LAYERS, MILESTONES, validate_data


EXPECTED_LAYER_COUNTS = {
    1: 5,
    2: 4,
    3: 4,
    4: 4,
    5: 5,
    6: 7,
}


def test_approved_ids_and_order():
    assert validate_data()
    expected = [f"AI-{number:03d}" for number in range(1, 30)]
    assert [m["id"] for m in MILESTONES] == expected


def test_six_layers_are_populated():
    assert len(LAYERS) == 6
    assert {m["layer"] for m in MILESTONES} == set(range(1, 7))


def test_approved_layer_distribution():
    counts = {
        layer_id: sum(m["layer"] == layer_id for m in MILESTONES)
        for layer_id in range(1, 7)
    }
    assert counts == EXPECTED_LAYER_COUNTS


def test_every_milestone_has_required_assignment_fields():
    required_fields = (
        "date",
        "title",
        "contributors",
        "what",
        "approach",
        "significance",
        "subfield",
        "impact",
        "limitations",
        "sources",
    )

    for milestone in MILESTONES:
        for field in required_fields:
            assert milestone.get(field), (
                f"{milestone['id']} is missing required field: {field}"
            )


def test_subfields_are_specific_and_meaningful():
    for milestone in MILESTONES:
        subfield = milestone["subfield"].strip()

        assert len(subfield) >= 5, (
            f"{milestone['id']} has an insufficiently specific AI subfield"
        )
        assert subfield.lower() not in {
            "artificial intelligence",
            "ai",
            "technology",
        }, f"{milestone['id']} uses an overly generic subfield"


def test_real_world_impact_is_developed():
    for milestone in MILESTONES:
        impact = milestone["impact"].strip()

        assert len(impact) >= 100, (
            f"{milestone['id']} needs a more developed real-world impact "
            f"explanation; currently {len(impact)} characters"
        )


def test_sources_have_titles_and_https_urls():
    for milestone in MILESTONES:
        assert milestone["sources"], (
            f"{milestone['id']} has no references"
        )

        for title, url in milestone["sources"]:
            assert title.strip(), f"{milestone['id']} has an untitled source"
            assert url.startswith("https://"), (
                f"{milestone['id']} has a non-HTTPS source: {url}"
            )
