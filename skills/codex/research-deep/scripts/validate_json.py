#!/usr/bin/env python3
"""Validate research JSON against the recovered field_categories YAML contract.

Adapted from 9b1a3aa3:skills/codex/research/validate_json.py. No network or writes.
Use --require-complete for research-deep; legacy mode requires required fields only.
Requires PyYAML: uv run --no-project --with pyyaml python validate_json.py ...
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    yaml = None

CATEGORY_MAPPING = {
    "basic_info": ["basic_info", "Basic Info"],
    "technical_features": ["technical_features", "technical_characteristics", "Technical Features"],
    "performance_metrics": ["performance_metrics", "performance", "Performance Metrics"],
    "milestone_significance": ["milestone_significance", "milestones", "Milestone Significance"],
    "business_info": ["business_info", "commercial_info", "Business Info"],
    "competition_ecosystem": ["competition_ecosystem", "competition", "Competition Ecosystem"],
    "history": ["history", "History"],
    "market_positioning": ["market_positioning", "market", "Market Positioning"],
}
_SKIP_KEYS = {"_source_file", "uncertain"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_fields_yaml(fields_path):
    if yaml is None:
        raise ValueError("PyYAML is missing. Run with uv run --no-project --with pyyaml python.")
    # SafeLoader normally overwrites duplicate YAML keys; reject them instead.
    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        return unique_object(loader.construct_pairs(node, deep=deep))

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    data = yaml.load(fields_path.read_text(encoding="utf-8-sig"), Loader=UniqueLoader)
    if not isinstance(data, dict) or not isinstance(data.get("field_categories"), list):
        raise ValueError("Schema needs a field_categories list, with category and fields per entry.")
    all_fields, required_fields, field_categories = set(), set(), {}
    for category in data["field_categories"]:
        if not isinstance(category, dict) or not isinstance(category.get("category"), str):
            raise ValueError("Each category needs a string category name.")
        if not isinstance(category.get("fields"), list):
            raise ValueError(f"Category {category['category']} needs a fields list.")
        for field in category["fields"]:
            if not isinstance(field, dict) or not isinstance(field.get("name"), str) or not field["name"].strip():
                raise ValueError("Every field needs a nonempty string name.")
            name = field["name"]
            if name in all_fields or name in _SKIP_KEYS:
                raise ValueError(f"Duplicate or reserved field name: {name}")
            if not isinstance(field.get("required", False), bool):
                raise ValueError(f"required must be a boolean for {name}")
            all_fields.add(name)
            field_categories[name] = category["category"]
            if field.get("required", False):
                required_fields.add(name)
    if not all_fields:
        raise ValueError("Schema defines no fields; empty coverage cannot pass.")
    return all_fields, required_fields, field_categories


def extract_field_values(data, field_categories=None):
    wrappers = {key for keys in CATEGORY_MAPPING.values() for key in keys}
    if field_categories:
        wrappers.update(field_categories.values())
    fields = {}
    stack = [data]
    while stack:
        obj = stack.pop()
        for key, value in obj.items():
            if key in _SKIP_KEYS:
                continue
            # A schema field named 'history', for example, remains a field.
            if key in wrappers and (not field_categories or key not in field_categories):
                if not isinstance(value, dict):
                    raise ValueError(f"Category wrapper {key} must contain an object.")
                stack.append(value)
            else:
                if key in fields:
                    raise ValueError(f"Field appears in more than one category: {key}")
                fields[key] = value
    return fields


def extract_json_fields(data, category_mapping=None):
    # Preserve the recovered public helper for callers using its default mapping.
    if category_mapping is not None:
        raise ValueError("Custom mappings belong in field_categories YAML.")
    if not isinstance(data, dict):
        raise ValueError("Research result must be a JSON object.")
    return set(extract_field_values(data))


def contains_marker(value):
    if isinstance(value, str):
        return "[uncertain]" in value
    if isinstance(value, dict):
        return any(contains_marker(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_marker(item) for item in value)
    return False


def validate_json(json_path, all_fields, required_fields, field_categories, require_complete=False):
    data = json.loads(json_path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)
    if not isinstance(data, dict):
        raise ValueError("Research result must be a JSON object.")
    values = extract_field_values(data, field_categories)
    json_fields = set(values)
    missing = all_fields - json_fields
    extra = json_fields - all_fields
    missing_by_category = defaultdict(list)
    for field in missing:
        missing_by_category[field_categories[field]].append(field)
    errors = []
    if missing & required_fields:
        errors.append("Missing required fields: " + ", ".join(sorted(missing & required_fields)))
    if require_complete:
        if missing:
            errors.append("Incomplete field coverage: " + ", ".join(sorted(missing)))
        if extra:
            errors.append("Unknown fields: " + ", ".join(sorted(extra)))
        uncertain = data.get("uncertain")
        if not isinstance(uncertain, list) or not all(isinstance(item, str) for item in uncertain):
            errors.append("uncertain must be an array of field names, including [] when none.")
        else:
            if len(uncertain) != len(set(uncertain)):
                errors.append("uncertain contains duplicate field names.")
            if set(uncertain) - all_fields:
                errors.append("uncertain contains unknown field names.")
            marked = {name for name, value in values.items() if contains_marker(value)}
            if set(uncertain) != marked:
                errors.append("uncertain must exactly match fields containing [uncertain].")
    return {
        "file": json_path.name, "total_defined": len(all_fields),
        "covered": len(all_fields & json_fields), "missing": len(missing), "extra": len(extra),
        "coverage_rate": len(all_fields & json_fields) / len(all_fields) * 100,
        "missing_required": sorted(missing & required_fields),
        "missing_optional": sorted(missing - required_fields),
        "missing_by_category": {key: sorted(value) for key, value in missing_by_category.items()},
        "extra_fields": sorted(extra), "errors": errors, "valid": not errors,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fields", "-f", default="fields.yaml", type=Path)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--json", "-j", nargs="+", type=Path)
    source.add_argument("--dir", "-d", type=Path, default=Path("results"))
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--quiet", "-q", action="store_true")
    args = parser.parse_args(argv)
    try:
        all_fields, required_fields, categories = load_fields_yaml(args.fields)
        files = args.json if args.json is not None else sorted(args.dir.glob("*.json"))
        if not files:
            raise ValueError("No JSON inputs found; validation did not run.")
        results = []
        for path in files:
            try:
                result = validate_json(path, all_fields, required_fields, categories, args.require_complete)
            except (OSError, ValueError) as exc:
                result = {"file": str(path), "valid": False, "errors": [str(exc)]}
            results.append(result)
            print(f"[{'PASS' if result['valid'] else 'FAIL'}] {result['file']}")
            for error in result["errors"]:
                print(f"  {error}")
            if not args.quiet and "coverage_rate" in result:
                print(f"  Coverage: {result['coverage_rate']:.1f}%")
        passed = sum(item["valid"] for item in results)
        print(f"Validation passed: {passed}/{len(results)}")
        return 0 if passed == len(results) else 1
    except (OSError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        if yaml is not None and isinstance(exc, yaml.YAMLError):
            print(f"[ERROR] Invalid YAML: {exc}", file=sys.stderr)
            return 1
        raise


if __name__ == "__main__":
    sys.exit(main())
