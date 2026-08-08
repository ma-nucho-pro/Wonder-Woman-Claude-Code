# Reproducible Research Protocol

Wonder Woman should not merely “search until something agrees.” Research must be inspectable, diverse enough to resist confirmation bias, and economical enough to repeat.

## Six-stage evidence selection

### 1. Formulate the evidence question
For every material claim, write the narrow question that would prove, disprove, or materially qualify it. Separate multiple claims instead of searching for a whole answer at once.

### 2. Select source classes
Choose the strongest source classes before choosing convenient individual links. Depending on the task, this can include direct execution, user-provided files, official documentation, original research, primary legal text, authoritative databases, first-party records, and reputable independent secondary sources.

### 3. Apply explicit filters
Define filters that matter to the claim: date, version, jurisdiction, population, product edition, API release, document scope, authority, and relevance. Do not silently mix incompatible versions or contexts.

### 4. Detect duplicates and dependency
Multiple pages can repeat one underlying press release, study, database entry, or rumor. Collapse dependent sources into one evidence lineage instead of counting repetition as independent confirmation.

### 5. Search complementary paths
Use at least one path capable of finding contrary evidence for important or disputed claims. When stakes justify it, use independent search formulations, different source classes, or separate researchers.

### 6. Rank and select the final evidence set
Keep the strongest evidence that directly entails the claim. Record limitations, unresolved conflicts, date/version scope, and why weaker evidence was not relied upon.

## Reproducibility record

For research-heavy answers, preserve a concise record:

```yaml
research_record:
  evidence_question: "..."
  source_classes_considered: []
  queries_or_lookup_paths: []
  filters:
    date_or_version: "..."
    jurisdiction_or_scope: "..."
  duplicate_or_dependent_sources_removed: []
  contrary_evidence_path: "..."
  selected_evidence_ids: []
  unresolved_limits: []
```

This record is not private chain-of-thought. It is an auditable description of what was searched, filtered, selected, and left unresolved.
