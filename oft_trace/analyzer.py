"""Analysis logic for aspec trace chains."""
from typing import Dict, List, Set, Optional, Any
from collections import defaultdict

from oft_trace.models import SpecItem

class TraceAnalyzer:
    """Analyzer for trace chains to identify issues and relationships."""
    
    def __init__(self, spec_items, id_map, covering_map, covered_by_map, broken_chains, aspec_file=None):
        self.spec_items = spec_items
        self.id_map = id_map
        self.covering_map = covering_map
        self.covered_by_map = covered_by_map
        self.broken_chains = broken_chains
        self.aspec_file = aspec_file
    
    def get_item_by_id(self, spec_id, doctype=None, version=None):
        """Find an item by ID and optionally by doctype and version."""
        if version:
            item_key = f"{spec_id}~{version}"
            if item_key in self.spec_items:
                item = self.spec_items[item_key]
                if doctype is None or item.doctype == doctype:
                    return item_key
            return None
        
        # Find by ID and optionally doctype
        for key, item in self.spec_items.items():
            if key.startswith(f"{spec_id}~") and (doctype is None or item.doctype == doctype):
                return key
        
        return None
    
    def is_version_mismatch(self, source_key, target_key):
        """Check if there's a version mismatch between items."""
        if source_key not in self.spec_items or target_key not in self.spec_items:
            return False
        
        source = self.spec_items[source_key]
        target = self.spec_items[target_key]
        
        # If we have coverage details about version mismatches
        for covering in source.coverage.get('coveringItems', []):
            if covering['id'] == target.id:
                if covering.get('coveringStatus') == 'COVERING_WRONG_VERSION':
                    return True
        
        # If the item is in the covering map but with wrong version
        source_id = source_key.split('~')[0]
        target_id = target_key.split('~')[0]
        
        if source_id in self.id_map and target_id in self.id_map:
            for source_variant in self.id_map[source_id]:
                for target_variant in self.id_map[target_id]:
                    if source_variant != source_key or target_variant != target_key:
                        if source_variant in self.covering_map and target_variant in self.covering_map[source_variant]:
                            return True
        
        return False
    
    def get_version_mismatch_details(self, source_key, target_key):
        """Get detailed information about a version mismatch."""
        if source_key not in self.spec_items or target_key not in self.spec_items:
            return None
        
        source = self.spec_items[source_key]
        target = self.spec_items[target_key]
        
        # Check coverage details
        for covering in source.coverage.get('coveringItems', []):
            if covering['id'] == target.id:
                if covering.get('coveringStatus') == 'COVERING_WRONG_VERSION':
                    return {
                        'current': {
                            'id': target.id,
                            'version': target.version
                        },
                        'expected': {
                            'id': target.id,
                            'version': covering.get('version', 'unknown')
                        }
                    }
        
        # Check other versions
        source_id = source_key.split('~')[0]
        target_id = target_key.split('~')[0]
        
        expected_version = None
        for source_variant in self.id_map[source_id]:
            for target_variant in self.id_map[target_id]:
                if source_variant != source_key or target_variant != target_key:
                    if source_variant in self.covering_map and target_variant in self.covering_map[source_variant]:
                        expected_version = target_variant.split('~')[1]
        
        if expected_version:
            return {
                'current': {
                    'id': target.id,
                    'version': target.version
                },
                'expected': {
                    'id': target.id,
                    'version': expected_version
                }
            }
        
        return None
    
    def determine_failure_reasons(self, item_key):
        """Determine the reasons for an item's coverage failure."""
        item = self.spec_items.get(item_key)
        if not item:
            return ["Item not found in report"]
        
        reasons = []
        
        # Check for circular dependencies first
        if item.in_circular_dependency:
            # Find the items this item has bidirectional relationships with
            bi_directional_with = []
            
            # Check covers relationships
            for covered_ref in item.covers:
                covered_id = covered_ref.get('id')
                covered_version = covered_ref.get('version', '1')
                covered_key = f"{covered_id}~{covered_version}"
                
                # Check if the covered item also covers this item (bidirectional)
                if covered_key in self.spec_items and item_key in self.covered_by_map.get(covered_key, []):
                    bi_directional_with.append(covered_id)
            
            if bi_directional_with:
                reasons.append(f"⟲ Bidirectional reference with: {', '.join(bi_directional_with)}")
            else:
                reasons.append("⟲ Item is involved in a circular dependency chain")
            return reasons
            
        # Special case for implementation items at the end of a trace chain
        if item.doctype.lower() in ['impl', 'implementation', 'code', 'test', 'testcase'] and item.covers:
            if item.coverage_type == "COVERED":
                # This is correct - implementation items that cover something don't need to be covered
                return []
            elif item.is_orphaned:
                # This is fine - implementation is expected to be an "orphan" if it's at the end of the chain
                # But we don't want to report it as an issue
                return ["✅ Implementation item properly covers upstream items and doesn't need coverage itself"]
        
        # Check for orphaned items
        if item.is_orphaned:
            reasons.append("🔍 Item is not covered by any other items (orphaned)")
        
        # Check for shallow coverage
        if item.is_shallow_covered:
            reasons.append("⚠️ Item has shallow coverage but misses deep coverage")
        
        # Check for version mismatches
        mismatches = item.get_version_mismatches()
        for mismatch in mismatches:
            reasons.append(
                f"♻️ Version mismatch: {mismatch['id']} covers v{mismatch['current_version']} " +
                f"but v{mismatch['expected_version']} is expected"
            )
        
        # Check for uncovered types
        uncovered = item.get_uncovered_types()
        if uncovered:
            reasons.append(f"❌ Missing coverage for types: {', '.join(uncovered)}")
        
        # If no specific reasons found, use the general coverage status
        if not reasons:
            coverage_type = item.coverage_type
            if coverage_type == "UNCOVERED":
                reasons.append("❌ Item is completely uncovered")
            elif coverage_type == "UNKNOWN":
                reasons.append("❓ Unknown coverage issue")
        
        return reasons

    def categorize_items_by_coverage(self):
        """Categorize items by their coverage status for reporting."""
        categories = {
            "COVERED": [],
            "ORPHANED": [],
            "SHALLOW": [],
            "OUTDATED": [],
            "UNCOVERED": [],
            "UNKNOWN": []
        }
        
        for item_key, item in self.spec_items.items():
            categories[item.coverage_type].append(item_key)
        
        return categories
    
    def count_coverage_by_doctype(self):
        """Count coverage statistics by document type."""
        by_doctype = {}
        for item_key, item in self.spec_items.items():
            doctype = item.doctype
            if doctype not in by_doctype:
                by_doctype[doctype] = {
                    "total": 0,
                    "covered": 0,
                    "orphaned": 0,
                    "shallow": 0,
                    "outdated": 0,
                    "uncovered": 0
                }
            
            by_doctype[doctype]["total"] += 1
            
            coverage_type = item.coverage_type
            if coverage_type == "COVERED":
                by_doctype[doctype]["covered"] += 1
            elif coverage_type == "ORPHANED":
                by_doctype[doctype]["orphaned"] += 1
            elif coverage_type == "SHALLOW":
                by_doctype[doctype]["shallow"] += 1
            elif coverage_type == "OUTDATED":
                by_doctype[doctype]["outdated"] += 1
            elif coverage_type == "UNCOVERED":
                by_doctype[doctype]["uncovered"] += 1
        
        return by_doctype

    def detect_circular_dependencies(self, items):
        """Detect circular dependencies in the trace items."""
        # Build a directed graph representation
        graph = {}
        for item in items:
            # Make sure we're accessing properties correctly
            # Some items might be dictionaries instead of SpecItem objects
            if isinstance(item, dict):
                item_id = item['id']
                item_version = item.get('version', '1')
                item_covers = item.get('covers', [])
            else:
                item_id = item.id
                item_version = item.version
                item_covers = item.covers
                
            item_key = f"{item_id}~{item_version}"
            if item_key not in graph:
                graph[item_key] = []
            
            # Add edges for all covered items
            for covered in item_covers:
                if isinstance(covered, dict):
                    covered_id = covered['id']
                    covered_version = covered.get('version', '1')
                else:
                    covered_id = covered.id
                    covered_version = covered.version
                    
                covered_key = f"{covered_id}~{covered_version}"
                if covered_key not in graph:
                    graph[covered_key] = []
                graph[item_key].append(covered_key)
        
        # Find circular dependencies using DFS
        circular_items = set()
        
        def find_cycles(node, path=None, visited=None):
            if path is None:
                path = []
            if visited is None:
                visited = set()
            
            # Mark the current node as visited and part of current path
            visited.add(node)
            path.append(node)
            
            # Recur for all neighbors
            for neighbor in graph.get(node, []):
                if neighbor in path:
                    # Found a cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:]
                    # Add all items in the cycle to circular_items
                    for cycle_item in cycle:
                        circular_items.add(cycle_item)
                elif neighbor not in visited:
                    find_cycles(neighbor, path[:], visited)
            
            # Remove node from the current path
            path.pop()
        
        # Start DFS from each node
        for node in graph:
            if node not in circular_items:
                visited = set()
                find_cycles(node, [], visited)
        
        # Update the items with circular dependency info
        for item in items:
            if isinstance(item, dict):
                item_id = item['id']
                item_version = item.get('version', '1')
            else:
                item_id = item.id
                item_version = item.version
                
            item_key = f"{item_id}~{item_version}"
            if item_key in circular_items:
                # For dictionary items, we need to handle differently than SpecItem objects
                if isinstance(item, dict):
                    item['in_circular_dependency'] = True
                    # Can't set coverage_type on a dict, handle accordingly
                else:
                    item.in_circular_dependency = True
                    item.add_failure_reason("♻️ Item is part of a circular dependency chain")
                    # Instead of setting coverage_type directly, use a method if available
                    if hasattr(item, 'set_coverage_type'):
                        item.set_coverage_type("UNCOVERED")
                    elif hasattr(item, 'mark_as_uncovered'):
                        item.mark_as_uncovered()
                    # Otherwise, we need to adapt to the SpecItem implementation
                
        # Also check for unwanted coverage which can contribute to circular dependencies
        coverage_rules = self._build_coverage_rules(items)
        for item in items:
            self.analyze_unwanted_coverage(item, coverage_rules)
        
    def _build_coverage_rules(self, items):
        """Build a map of valid coverage rules based on artifact types.
        
        According to OFT design, this defines which artifact types need coverage
        from which other artifact types.
        """
        # Default trace rules according to OFT design doc
        # Format: doctype -> [list of doctypes that can cover it]
        default_rules = {
            'feat': ['req', 'dsn', 'impl', 'test'],  # features can be covered by any type
            'req': ['dsn', 'impl', 'test'],  # requirements covered by design, impl or test
            'dsn': ['impl', 'test'],         # design covered by implementation or test
            'impl': ['test'],                # implementation covered by test
            'utest': [],                     # unit tests don't need coverage
            'itest': [],                     # integration tests don't need coverage
            'stest': [],                     # system tests don't need coverage
        }
        
        # Try to extract rules from items if they have needs_coverage attribute
        coverage_rules = {}
        for doctype in set(item.doctype.lower() for item in items if hasattr(item, 'doctype') and item.doctype):
            coverage_rules[doctype] = default_rules.get(doctype.lower(), [])
        
        return coverage_rules

    def analyze_unwanted_coverage(self, item, coverage_rules):
        """Check if an item has unwanted coverage relationships"""
        if not hasattr(item, 'covers') or not hasattr(item, 'doctype'):
            return
        
        item_doctype = item.doctype.lower() if item.doctype else None
        if not item_doctype:
            return
            
        for covered in item.covers:
            # Get the covered item's information
            if isinstance(covered, dict):
                covered_id = covered.get('id')
                covered_version = covered.get('version', '1')
            else:
                covered_id = covered.id
                covered_version = covered.version
                
            covered_key = f"{covered_id}~{covered_version}"
            covered_item = self.spec_items.get(covered_key)
            
            if covered_item and hasattr(covered_item, 'doctype') and covered_item.doctype:
                covered_doctype = covered_item.doctype.lower()
                
                # Check if this is an unwanted coverage relationship
                if covered_doctype in coverage_rules and item_doctype not in coverage_rules.get(covered_doctype, []):
                    if hasattr(item, 'add_failure_reason'):
                        item.add_failure_reason(f"❌ Unwanted coverage to {covered_key} ({covered_item.doctype})")
                    
                    # Instead of setting coverage_type directly, use a method if available
                    if hasattr(item, 'set_coverage_type'):
                        item.set_coverage_type("UNCOVERED")
                    elif hasattr(item, 'mark_as_uncovered'):
                        item.mark_as_uncovered()
                    # Otherwise, we need to adapt to the SpecItem implementation