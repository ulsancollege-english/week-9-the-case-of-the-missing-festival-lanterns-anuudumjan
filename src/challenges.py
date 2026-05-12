def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:
    """Analyze festival lantern records and return a report."""

    # Collections
    seen_lanterns = set()
    seen_once = set()
    duplicate_lanterns = set()
    count_by_section = {}
    wrong_section_lanterns = {}

    # Loop through the log
    for lantern_name, actual_section in lantern_log:

        # Add to seen lanterns
        seen_lanterns.add(lantern_name)

        # Detect duplicates
        if lantern_name in seen_once:
            duplicate_lanterns.add(lantern_name)
        else:
            seen_once.add(lantern_name)

        # Count records by section
        if actual_section in count_by_section:
            count_by_section[actual_section] += 1
        else:
            count_by_section[actual_section] = 1

        # Check wrong sections (expected lanterns only)
        if lantern_name in expected_lanterns:
            correct_section = correct_sections[lantern_name]

            if actual_section != correct_section:
                # Record only the first wrong section found
                if lantern_name not in wrong_section_lanterns:
                    wrong_section_lanterns[lantern_name] = {
                        "expected": correct_section,
                        "actual": actual_section,
                    }

    # Set operations
    missing_lanterns = expected_lanterns - seen_lanterns
    unexpected_lanterns = seen_lanterns - expected_lanterns

    # Return report
    return {
        "seen_lanterns": seen_lanterns,
        "missing_lanterns": missing_lanterns,
        "unexpected_lanterns": unexpected_lanterns,
        "duplicate_lanterns": duplicate_lanterns,
        "count_by_section": count_by_section,
        "wrong_section_lanterns": wrong_section_lanterns,
    }