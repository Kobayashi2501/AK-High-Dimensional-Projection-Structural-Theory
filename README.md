# AK-HPDST v19.0.0

## AK High-Dimensional Projection Structural Theory

> A typed and auditable framework for projecting selected information from complex mathematical structures into persistence data, applying controlled collapse processing, diagnosing failures, and separating internal evidence from external theorem claims.

**Author:** Atsushi Kobayashi  
**Release:** v19.0.0 - Threshold-Gap Metric Repair Release  
**Status:** Research framework with a proved internal Core, conditional interfaces, restricted toy bridges, search infrastructure, and explicit non-claims

---

## 1. Beginner's overview

AK-HPDST studies complicated mathematical structures by converting selected information into persistent-homology profiles represented by barcodes.

A barcode is a collection of intervals called bars.

- A long bar represents a feature that persists across a wide range.
- A short bar represents a feature that disappears quickly.
- An infinite bar represents a feature that survives indefinitely before window restriction.

AK-HPDST does not simply delete short bars and declare that a mathematical problem has been solved.

It records:

1. which external object was used;
2. how it was converted into Core-readable data;
3. which degree, window, and threshold were selected;
4. which bars were retained or deleted;
5. whether the classification is stable under the declared comparison error;
6. whether required representatives, morphisms, tower data, and proof artifacts exist;
7. whether a statement is proved, conditional, operational, speculative, rejected, or historical.

The central safety rule is:

```text
Core pass != external theorem
unless a separate Interface Theorem or Bridge Theorem is proved.
```

AK-HPDST is therefore best understood as a proof-interface and certification architecture, not as an automatic solver for major conjectures.

---

## 2. What AK-HPDST v19.0.0 can do

Within its declared hypotheses and data types, v19.0.0 can:

- convert suitable filtered objects into constructible one-parameter persistence profiles;
- restrict a persistence profile to a declared window;
- delete finite bars whose lengths are at or below a chosen threshold;
- certify when hard threshold deletion is stable under a declared bottleneck-distance error;
- distinguish exact comparison from metric comparison;
- record admissible filtered representatives of repaired persistence profiles;
- derive a one-way degree-one implication from persistent vanishing to an Ext1 vanishing statement in the eligible realization regime;
- compare a directed tower with its declared apex through an actual comparison morphism;
- detect terminal-generic kernel and cokernel defects through Type IV diagnostics;
- manage overlap, continuation, and Restart records for local-to-global analysis;
- classify failures by type instead of reporting only success or failure;
- generate immutable manifests, claim references, proof-object records, and replay data;
- use human or AI search while keeping search output outside the proof verdict until independently verified.

In practical terms, AK-HPDST can organize the following question:

```text
Can selected structural information from a complex object be projected,
collapsed, compared, and audited without losing track of the assumptions
needed to interpret the result?
```

---

## 3. What v19.0.0 does not claim

This release does not prove, by itself:

- Navier-Stokes regularity;
- the Riemann hypothesis;
- the Birch and Swinnerton-Dyer conjecture;
- the ABC conjecture;
- an Iwasawa main conjecture;
- a Langlands correspondence;
- mirror symmetry or a Fukaya-category equivalence;
- a cryptographic security theorem;
- a universal equivalence between persistent homology and Ext groups.

In particular, v19.0.0 does not assert:

```text
PH1 = 0 <-> Ext1 = 0
```

The proved Core direction is narrower and one-way:

```text
Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

This implication may be used only when all required conditions are satisfied, including:

- an admissible representative exists;
- the declared realization is defined;
- the object lies in the eligible amplitude range;
- the required edge identification is proved;
- all relevant artifacts and claim records are present.

The reverse direction is not part of the v19.0.0 Core.

---

## 4. Main processing flow

```text
External mathematical object
        |
        v
Declared realization or one-parameter extraction
        |
        v
Core-readable filtered or persistence object
        |
        v
Persistence profile P_i(F)
        |
        v
Window restriction Window(W, P_i(F))
        |
        v
Hard threshold deletion T_bar(tau)
        |
        v
Repaired evaluation Eval(i, W, tau; F)
        |
        +--> exact comparison
        +--> metric-gap-certified comparison
        +--> admissible representative and eligible Ext1 edge
        +--> overlap, continuation, and Restart records
        +--> tower comparison and Type IV diagnostics
        |
        v
B-Gate+ and typed audit
        |
        v
Core status: pass / reject / undefined / not_invoked
        |
        v
External conclusion only through a proved transport theorem
```

The processing order is important:

```text
persistence -> window -> threshold deletion
```

The following order is not automatically equivalent:

```text
persistence -> threshold deletion -> window
```

A bounded window can shorten a previously long or infinite bar. Therefore windowing must be evaluated before the threshold decision unless a separate commutation theorem is available.

---

## 5. Minimal mathematical model

### 5.1 Working regime

The Core mainly works with:

```text
constructible one-parameter persistence modules over a field k
```

Informally, this means that the profile:

- changes only at controlled parameter values;
- has finite-dimensional data at each parameter;
- has no uncontrolled accumulation of critical values inside a bounded range.

Wild, uncontrolled, infinite-rank, or genuinely multiparameter data are not automatically Core-readable.

A separate extraction or Interface Theorem is required when external data do not already have this form.

### 5.2 Window-first profile

For a filtered object `F`, monitored degree `i`, window `W`, and threshold `tau`, define:

```text
B(i, W; F) = Window(W, P_i(F))
```

This is the windowed profile before threshold deletion.

The repaired evaluation is:

```text
Eval(i, W, tau; F) = T_bar(tau, B(i, W; F))
```

Equivalently:

```text
Eval(i, W, tau; F)
    = T_bar(tau, Window(W, P_i(F)))
```

### 5.3 Hard threshold deletion

For each bar `I`:

```text
if length(I) <= tau:
    delete I
else:
    retain I
```

Infinite bars are retained before bounded-window clipping.

The operation is idempotent:

```text
T_bar(tau, T_bar(tau, B)) = T_bar(tau, B)
```

Applying two thresholds is equivalent to applying the larger threshold:

```text
T_bar(sigma, T_bar(tau, B))
    = T_bar(max(sigma, tau), B)
```

However, hard deletion is not globally non-expansive under the standard bottleneck metric.

---

## 6. Main v19 repair: threshold-gap-safe stability

Earlier formulations could be read as claiming that hard threshold deletion never increases bottleneck distance. That global claim is false.

A small change in a bar length may move the bar across the threshold and change it from retained to deleted.

### 6.1 Threshold clearance

For one barcode `B`:

```text
clear_tau(B)
    = minimum distance between tau and the length of any finite bar in B
```

If `B` has no finite bars:

```text
clear_tau(B) = infinity
```

For several protected barcodes:

```text
gap_tau(B1, B2, ..., Bm)
    = min(clear_tau(B1), clear_tau(B2), ..., clear_tau(Bm))
```

### 6.2 Repaired stability rule

Suppose:

```text
bottleneck_distance(B, C) <= epsilon
```

and no finite bar in either `B` or `C` has a length inside:

```text
[tau - epsilon, tau + epsilon]
```

Then:

```text
bottleneck_distance(T_bar(tau, B), T_bar(tau, C)) <= epsilon
```

This is a two-sided certificate.

Checking only `B` or only `C` is not sufficient.

### 6.3 Ledger form

When comparison errors are collected in a metric ledger, the scalarized ledger value must satisfy:

```text
val_B(metric_defect) < gap_tau(protected_barcodes)
```

The record must also prove that:

```text
actual bottleneck discrepancy <= val_B(metric_defect)
```

A number written in a ledger is not enough by itself. It must be connected to the actual compared profiles by a theorem, verified computation, or reconstructible artifact.

---

## 7. Core components

The grouping below is explanatory. The canonical definitions and theorem boundaries remain in the Main document and appendices.

### Core A - Persistence and barcode layer

Creates the Core-readable persistence profile:

```text
P_i(F)
```

and its barcode representation.

**Purpose:** convert selected structural behavior into a form that can be windowed, thresholded, compared, and audited.

### Core B - Windowed projection layer

Restricts the profile to a declared window:

```text
B(i, W; F) = Window(W, P_i(F))
```

**Purpose:** inspect a controlled parameter range rather than treating all scales as one undifferentiated object.

**Important:** a bounded window may turn an infinite bar into a finite clipped bar.

### Core C - Collapse layer

Applies hard threshold deletion:

```text
Eval(i, W, tau; F) = T_bar(tau, B(i, W; F))
```

**Purpose:** remove finite bars at or below the threshold and retain the repaired profile.

**Important:** this is a barcode-level operation by default. It is not automatically a global exact functor on all morphisms.

### Core D - Comparison and metric-safety layer

Every comparison uses exactly one runtime mode:

- `exact`
- `metric_gap_certified`
- `not_compared`

#### exact

An actual equality or persistence-profile isomorphism is proved and artifact-backed.

#### metric_gap_certified

A real discrepancy bound and a two-sided threshold-gap certificate are supplied.

#### not_compared

No comparison inference belongs to the declared scope.

`not_compared` cannot discharge a comparison obligation that is actually required.

### Core E - Representative and Ext1-edge layer

An admissible representative is written in simplified form as:

```text
C(tau, W; F)
```

It represents the repaired profile only in the declared monitored degrees and at the declared equivalence strength.

In the eligible regime:

```text
Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

**Purpose:** connect degree-one persistent vanishing to a derived-category statement without claiming a global equivalence.

### Core F - Tower and Type IV diagnostic layer

For a directed tower and declared apex, Type IV requires an actual comparison morphism:

```text
phi(i, W, tau):
    ColimProfile(i, W, tau; F_bullet)
        -> ApexProfile(i, W, tau; F_infinity)
```

When the source, target, kernel, and cokernel are terminal-tame, define:

```text
mu(i, W, tau) = terminal_generic_dimension(kernel(phi))
nu(i, W, tau) = terminal_generic_dimension(cokernel(phi))
```

A clean monitored state is:

```text
(mu_Collapse, nu_Collapse) = (0, 0)
```

This means that no monitored terminal-generic kernel or cokernel defect was detected.

It does not automatically prove that the full comparison morphism is an isomorphism in every possible sense.

Type IV has exactly one specialized status:

```text
not_invoked
undefined
certified_zero
obstructed
```

No numerical pair is assigned when the status is `not_invoked` or `undefined`.

### Core G - Gate, failure, and audit layer

`B-Gate+` combines all required clauses without cancellation.

A pass may require:

1. degree-one repaired vanishing;
2. valid comparison-mode records;
3. valid Ext1 evidence when the Ext1 clause is invoked;
4. Type IV status of `not_invoked` by scope or `certified_zero` with valid artifacts;
5. a passing metric budget for metric comparisons;
6. all required non-scalar obligations;
7. a complete and consistent manifest;
8. admissible claim use under the Claim Register.

A favorable numerical margin cannot repair:

- a missing representative;
- a missing morphism;
- missing eligibility;
- missing terminal-tameness evidence;
- an invalid claim status;
- a missing proof artifact;
- inconsistent artifact identity.

---

## 8. Failure taxonomy

Failures are nonexclusive. One run may contain several failure types.

| Type | Meaning | Typical example |
|---|---|---|
| Type I | Topological failure | `Eval(1, W, tau; F) != 0` |
| Type II | Categorical failure in the eligible regime | invoked and well-typed `Ext1 != 0` |
| Type III | Metric, comparison, representative, overlap, Restart, or coherence failure | failed gap record, invalid comparison, missing required morphism |
| Type IV | Tower-level terminal-generic obstruction | `(mu_Collapse, nu_Collapse) != (0, 0)` |
| Type V | Claim-status, provenance, identity, or manifest failure | a Spec, AI output, rejected claim, or incomplete record is used as theorem evidence |

Missing required evidence normally gives:

```text
undefined
```

It must not be silently encoded as:

```text
0
pass
not_invoked
not_compared
```

---

## 9. Claim discipline

Every meaningful statement must be used only at its registered strength.

Typical roles include:

- Core definition;
- Core theorem or lemma;
- metric-repair theorem;
- operational policy;
- Interface definition or theorem;
- Bridge candidate;
- Bridge Program;
- Bridge Theorem;
- toy bridge theorem;
- Search artifact;
- Companion template;
- Spec;
- explicit non-claim;
- deprecated or rejected claim.

The main rules are:

```text
Registration != proof
Spec != theorem
Bridge Program != Bridge Theorem
Toy Bridge != problem-specific Bridge Theorem
AI output != proof
Search result != theorem
Execution != proof
Replay success != mathematical truth
Manifest completeness != mathematical truth
Core pass != external theorem without a proved transport theorem
```

When a source, register, summary, implementation, or old document disagrees, the weaker safe interpretation governs until a new immutable repair is issued.

---

## 10. Document architecture

### Main - Chapters 1 to 8

The Main document defines the release-wide contract:

1. scope, claim discipline, and metric-repair contract;
2. barcode metrics, threshold deletion, and gap-safe stability;
3. windowed evaluation, comparison records, and representatives;
4. eligible realization and the one-way `PH1 -> Ext1` edge;
5. failure taxonomy and Type IV diagnostics;
6. window logic, overlap, Restart, and record-level gluing;
7. typed audit semantics and Core sovereignty;
8. Core closure and the external Interface boundary.

### Foundation Appendices A to G

- **A:** barcode metric and threshold-gap repair;
- **B:** filtered representatives;
- **C:** eligible realization and canonical Ext1 edge;
- **D:** tower diagnostics and terminal-generic Type IV defects;
- **E:** windows, overlaps, Restart, and gluing;
- **F:** typed obligations, statuses, and dependency closure;
- **G:** canonical manifest schema, proof objects, and replayability.

### Technical Extension Appendices H to N

These develop advisory indicators, discretization, measurement, controlled commutation, transfer ledgers, quantale semantics, and higher-categorical extensions.

They do not silently enlarge the proved Core.

### Problem Interface Appendices

These specify how external domains may attempt to enter the Core, including:

- arithmetic interfaces;
- cyclotomic and Iwasawa tower interfaces;
- congruence interfaces;
- mirror and Fukaya-facing interfaces;
- normalization interfaces;
- Navier-Stokes exploration, soundness, and proof-first programs.

An interface defines a typed route. It is not an external theorem unless the required transport theorem is proved.

### Search / Platform Appendices U to Z

These govern:

- human, AI, tool, and platform agents;
- Hunter, Mapper, and Lifter workflows;
- Bridge Programs;
- validity maps and certificate DAGs;
- proof stores;
- execution and reproducibility records.

Search is proposer-side by default. Core verdicts are verifier-side.

### Claim Register, CM, TB, and Companion

- **CR-v19:** canonical claim identity, status, permitted use, failure route, and repair ancestry;
- **CM-v19:** reusable Core micro-theorems at their exact proved strength;
- **TB-v19:** deliberately restricted toy bridge theorems;
- **Companion:** operational calibration and execution templates, not theorem sources.

---

## 11. Repository guide

A typical v19.0.0 release package is organized as follows:

```text
.
├─ README.md
├─ README_JA.md
├─ AK_HPDST_v19_0_0_Part__Main.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part_II__Foundation_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part_III__Technical_Extension_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__IV__Problem_Interface_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__V__Search_Platform_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__Claim_Register.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__CM.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__TB.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__Companion.pdf
└─ OLD/
   └─ historical materials - non-normative and potentially incorrect
```

Actual paths may vary by package or branch.

The versioned source artifact and Claim Register control normative identity.

---

## 12. Recommended reading order

For a first reading:

1. this README;
2. Main Chapter 1 - scope and safety rules;
3. Main Chapter 8 - what is proved and what remains conditional;
4. Main Chapters 2 and 3 - windowing, threshold deletion, and metric repair;
5. Main Chapters 4 and 5 - Ext1 edge and tower diagnostics;
6. Appendix A - detailed threshold-gap-safe stability proof;
7. CR-v19 - exact claim status and permitted use;
8. other appendices according to the target domain.

For implementation or audit work, also read Appendices F, G, U, Y, Z, and the Companion.

---

## 13. Small conceptual example

Suppose a windowed barcode has finite bar lengths:

```text
0.08, 0.21, 0.73
```

Choose:

```text
tau = 0.20
```

Hard deletion gives:

```text
0.08 -> deleted
0.21 -> retained
0.73 -> retained
```

However, the `0.21` bar is close to the threshold.

If the comparison error is large enough to move its length below `0.20`, the retained/deleted classification may change.

AK-HPDST therefore asks for both:

1. a certified error bound `epsilon`;
2. a two-sided threshold gap greater than `epsilon`.

The result is not called stable merely because software produced a barcode.

---

## 14. Why the OLD directory is retained

The historical materials are intentionally preserved as repair ancestry and as a warning against claim inflation.

Some old documents may contain obsolete, unsupported, or overstrong formulations, including unconditional readings such as:

```text
PH1 = 0 = Ext1
```

or:

```text
PH1 = 0 <-> Ext1 = 0
```

These statements are not normative in v19.0.0.

The current admissible Core reading is narrower:

```text
eligible regime + required artifacts + Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

The `OLD/` directory exists to show:

- which claims were previously overextended;
- why the present one-way eligible bridge is narrower;
- why rejected claims should remain visible rather than being silently erased;
- how immutable repair ancestry supports mathematical and audit accountability.

Do not use `OLD/` material as current theorem evidence.

Use the v19.0.0 source and the corresponding Claim Register entry.

---

## 15. AI and automated search

AK-HPDST allows AI systems and automated tools to:

- propose realizations, windows, thresholds, and bridge candidates;
- search for counterexamples;
- rank proof routes;
- generate formalization candidates;
- build maps, DAGs, manifests, and replay records;
- critique or audit candidate arguments.

The semantic boundary remains strict:

```text
Generation != verification
Transformation != preservation unless checked
Retrieval != verification
Consensus != proof
Compilation != theorem validity
Storage != certification
Replay != mathematical truth
```

An AI-generated statement becomes usable evidence only after it is converted into the required verifier-side object and passes the applicable mathematical and audit checks.

---

## 16. Versioning and citation discipline

When referring to an AK-HPDST result, record at least:

- theory version and document revision;
- exact source artifact;
- theorem, definition, or Claim UID;
- complete hypotheses and monitored scope;
- comparison mode;
- required artifact identities;
- repair ancestry when applicable.

A later summary, README, diagram, or software implementation does not replace the theorem statement in the canonical source.

---

## 17. Final interpretation

AK-HPDST v19.0.0 provides a disciplined way to ask:

```text
How can a complex mathematical object be projected into a simpler
persistence-based representation, processed by a controlled collapse,
and evaluated without confusing evidence, approximation, computation,
and proof?
```

Its central contribution is not the claim that every problem collapses.

Its contribution is an architecture that explicitly separates:

- projection from preservation;
- short-bar deletion from stable deletion;
- exact equality from metric control;
- persistence vanishing from derived vanishing;
- local profile agreement from tower-level agreement;
- search output from theorem evidence;
- Core certification from external mathematical truth.

That separation is the foundation of the v19.0.0 release.
