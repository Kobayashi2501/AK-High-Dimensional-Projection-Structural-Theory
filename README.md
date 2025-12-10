# AK–HDPST v17.0 — AK High-Dimensional Projection Structural Theory

> **AK-OS v1.0: An operating system for high-dimensional mathematical exploration**  
> Core: provable, 1D constructible persistence over a field  
> [Spec]: auditable, non-expansive-after-truncation extensions and search policies

This repository contains the v17.0 version of **AK–HDPST**, now positioned not as a “universal solver” for big conjectures, but as a **proof-oriented operating system (AK-OS)** for exploring them.

A companion project, **AK_AP (Arithmetic Calibration Program)**, implements closed-world calibration on arithmetic moduli spaces (finite-field Weil world and FLT world) using the same OS.

Repository status: research OS prototype with reference APIs, run protocol, and audit artifacts. **Strong guarantees are strictly confined to the Core scope** below.

---

## AK-OS v1.0 Manifesto

### What this is

- **Not**: a claimed proof of any grand conjecture (Navier–Stokes, BSD, RH, FLT, etc.).  
- **Is**: a **modular OS** for high-dimensional mathematical exploration, built around:
  - a **collapse contract** (`UCC / B–Gate⁺`)
  - a **truncation operator** `T_tau`
  - a **δ-ledger** for error / budget accounting
  - **tower diagnostics** `(mu, nu)` for invisible limit failures
  - a **High-Dimensional Projection Search (HDPS)** engine that builds a **Map of Validity** on parameter spaces.

### Core vs [Spec]

- **Core**
  - One-parameter, constructible persistence over a field `k`
  - Exact truncation `T_tau` (delete bars of length ≤ `tau`), idempotent and 1-Lipschitz (interleaving / bottleneck)
  - Filtered lift `C_tau` up to filtered quasi-isomorphism, with  
    `P_i(C_tau F) ≅ T_tau(P_i F)`
  - One-way bridge: `PH1(F) = 0 ⇒ Ext1(R(F), k) = 0` under a t-exact realization with amplitude ≤ 1
  - Tower diagnostics `(mu, nu)` after truncation; detection of Type IV failures (finite levels OK, limit fails)
  - Windowed gating (`B–Gate⁺`, Overlap Gate) and restart / summability

- **[Spec]**
  - Domain-specific realizations (e.g. arithmetic, PDE, Fukaya) subject to Core guards
  - High-Dimensional Projection Search (HDPS): Terrain Cells, Map of Validity, Hunter / Mapper / Lifter agents
  - PF/BC after-collapse comparator, Mirror / Transfer, A/B soft-commuting policies
  - Quantitative heuristics and exploration strategies  
  All [Spec] components must be **non-expansive after truncation** and fully audited via the δ-ledger.

### What AK-OS tries to do

- Treat “**trying to prove something**” as **navigation on a landscape**:
  - Parameter spaces become **moduli spaces** `M`
  - Collapse success / failure becomes a **validity map**:  
    `Valid`, `Obstructed`, `Unknown`
- Turn **proof gaps, numerical error, and model mismatch** into **budgeted δ-entries**:
  - Instead of pretending they do not exist, they are **priced and recorded**:
    - `delta.alg` (algorithmic / modeling)
    - `delta.disc` (discretization)
    - `delta.meas` (measurement)
- Provide a **repeatable run protocol** (`run.yaml` + artifacts + δ-ledger) that can be audited, re-run, and criticized.

### How to read this project

- As **pure mathematics**: treat Core as candidate theorems in `D^b(k-mod)` / persistence; treat [Spec] as conjectural, implementation-dependent.
- As **software architecture**: view AK–HDPST as an OS for:
  - stabilizing collapse operations,
  - coordinating search agents,
  - recording quantitative evidence.
- As **AI × human collaboration case study**: the design was co-developed by:
  - a human providing **ideas / constraints / OS-level intuition**, and
  - LLMs providing **formalization, structure, and LaTeX / code skeletons**.

---

## From “Big-Conjecture Solver” to “Exploration OS”

### Early phase (v10–v14): Overloaded “universal solver”

- Ambition: directly attack **Navier–Stokes / BSD / RH / Langlands** via a single gigantic framework.
- Ingredients: derived categories, Iwasawa theory, Fukaya categories, Denef–Pas structures, Langlands-style gates, tropical / mirror geometry… all at once.
- Problem:
  - Conceptually inspiring but **over-specified and under-verified**.
  - Too many heavy concepts; impossible to fully check consistency.
  - Risk of becoming a **“hall of mirrors”**: impressive structure, uncertain correctness.

### Middle phase (v15–v16): Radical simplification and guardrails

- Refocus on:
  - **1D constructible persistence over a field** as the main stage.
  - `T_tau` (bar-deletion truncation) as the central exact functor.
  - A **one-way bridge** `PH1 ⇒ Ext1` in `D^b(k-mod)` under precise hypotheses.
  - δ-ledgers and windowed protocols for **auditable pipelines**.
- Result:
  - A much leaner **Core** with explicit **Scope and Guarantees**.
  - Heavy domain-specific machinery moved to **[Spec]** or cut.

### v17.0: The OS pivot — HDPS and closed-world calibration

In v17.0, the project explicitly **pivots**:

- From: “A framework that might one day *prove* big conjectures.”
- To:   “An **operating system** (AK-OS) for exploring them with clear boundaries.”

Key moves:

1. **HDPS (High-Dimensional Projection Search)** and the **Map of Validity**
   - Input spaces are treated as high-dimensional **moduli** `M`.
   - Collapse viability is seen as a scalar field / label over `M`:
     - `Valid` (collapse passes safety gates)
     - `Obstructed` (Type IV / structural failure)
     - `Unknown` (not yet explored or beyond Core scope)
   - HDPS provides **Terrain Cells**, and **Hunter / Mapper / Lifter** agents to build and refine a **Map of Validity**.

2. **AK_AP (Arithmetic Calibration Program) as a closed-world test**
   - Instead of launching directly at Navier–Stokes, we first test the OS on **worlds where the truth is already known**:
     - `M_Weil`: moduli of varieties over finite fields (Weil world)
     - `M_FLT`: deformation space of semistable elliptic curves / Frey data (FLT world)
   - Classical theorems (Deligne’s finite-field RH, Wiles–Taylor modularity / FLT) are treated as **Core-Input axioms**.
   - HDPS + UCC must reproduce:
     - A **Plain of Truth** on `M_Weil` (defect potential flat at 0)
     - A **Global Obstruction** on `M_FLT` (Frey locus structurally empty via Type IV collapse failures)
   - This is **calibration**, not new proofs: the OS must be **consistent with known theorems** before being trusted in open worlds.

3. **Explicit honesty about scope**
   - v17.0 does **not** claim proofs of Navier–Stokes / BSD / RH / FLT.
   - It offers a **structured OS and protocol** for exploring such problems, with:
     - clear Core boundaries,
     - explicit [Spec] hypotheses,
     - δ-ledgers and audit artifacts.

---

## What’s new in v17.0 (vs v16.0)

### Conceptual

- **OS framing (AK-OS v1.0)**
  - Project re-framed as an operating system for mathematical exploration.
  - Core vs [Spec] separation tightened and made explicit in documentation and code layout.
  - Emphasis on **run protocols**, **δ-ledgers**, and **auditability**.

- **High-Dimensional Projection Search (HDPS)**
  - Introduction of **Terrain Cells** and **Map of Validity** as first-class concepts.
  - **Hunter / Mapper / Lifter** roles formalized (search, map refinement, lifting between models).
  - Search is always conducted **post-truncation** (`T_tau`) to preserve stability and monotonicity guarantees.

- **Closed-world calibration via AK_AP**
  - Companion arithmetic program **AK_AP** uses AK-OS on:
    - `M_Weil` (finite-field Weil world)
    - `M_FLT` (Frey / FLT world)
  - Treats Deligne and Wiles as **Core-Input axioms**.
  - Establishes that the OS can:
    - see `M_Weil` as a **Plain of Truth** (no obstruction),
    - see the Frey locus in `M_FLT` as **structurally empty** (Type IV failures).
  - Provides **worked, closed-world examples** of HDPS and the Map of Validity.

### Technical (Core and [Spec])

- **Core refinements**
  - Clarified that all Core results live in `D^b(k-mod)` with:
    - field coefficients,
    - constructible, 1D persistence,
    - t-exact realization of amplitude ≤ 1 where needed.
  - Re-normalized tower diagnostics `(mu, nu)` and Type IV failures to the post-`T_tau` world.
  - Strengthened wording: no global `PH1 ⇔ Ext1`, no multi-parameter guarantees.

- **[Spec] layer reorganized**
  - Heavy domain-specific structures (e.g., Langlands, Fukaya, Denef–Pas) moved to **[Spec] appendices** or external companion documents.
  - PF/BC after-collapse, Mirror / Transfer, A/B soft-commuting, and HDPS policies all explicitly labeled [Spec] and required to:
    - be non-expansive after `T_tau`,
    - log all deviations to the δ-ledger.

- **Run protocol and artifacts**
  - v16.0 windowed protocol retained and extended:
    - `run.yaml` now supports optional HDPS configuration blocks.
    - Audit artifacts extended to include **Validity Map snapshots** for small toy examples (where implemented).
  - IMRN / AIM-style test suites preserved and referenced as **Core correctness tests**.

---

## Table of contents

- AK-OS v1.0 Manifesto
- From “Big-Conjecture Solver” to “Exploration OS”
- What’s new in v17.0
- Overview
- Scope and guarantees (Core)
- What’s in Core vs [Spec]
- Concepts and components
- Installation
- Quickstart (CLI and Python API)
- Configuration (`run.yaml`)
- Workflows and examples
- Update policy (after truncation)
- Auditing and artifacts
- Command reference (CLI)
- Python API reference (selected)
- Roadmap
- Contributing
- Citing and references
- License
- Appendix: Terms cheat sheet

---

## Overview

AK–HDPST v17.0 is the kernel of **AK-OS**, a proof-oriented OS for high-dimensional collapse and validity mapping. It cleanly separates:

- **Core**: proved, machine-checkable or machine-formalizable guarantees in:
  - 1D constructible persistence over a field
  - derived category `D^b(k-mod)` with amplitude-controlled realizations
- **[Spec]**: operational extensions and domain-specific modules that:
  - are non-expansive after truncation (`T_tau`),
  - are fully audited via δ-ledgers and tower diagnostics,
  - may depend on external conjectures / theorems or modeling choices.

All quantitative comparisons follow a **post-truncation** protocol:

```text
t  →  persistence P_i  →  truncation T_tau  →  compare / audit / map_validity
```

This ensures:

- metric stability (1-Lipschitz estimates),
- transparent failure modes (especially Type IV),
- reproducible, auditable exploration pipelines.

---

## Scope and guarantees (Core)

Strong claims are limited to the following setting:

- **Category**
  - One-parameter, constructible persistence (pointwise finite-dimensional, finite critical set).
  - Coefficients in a **field** `k`.
  - Realization functors landing in `D^b(k-mod)` with amplitude ≤ 1 where required.

- **Truncation `T_tau`**
  - Exact reflective localization deleting all barcode intervals of length ≤ `tau`.
  - Idempotent and 1-Lipschitz for the interleaving / bottleneck distance.
  - All “monotonicity” or “non-expansiveness” statements are made **after** applying `T_tau`.

- **Filtered lift `C_tau`**
  - Chain-level lift defined up to filtered quasi-isomorphism (f.q.i.).
  - Satisfies `P_i(C_tau F) ≅ T_tau(P_i F)` for all relevant degrees.

- **Bridge `PH1 ⇒ Ext1`**
  - Under a t-exact realization of amplitude ≤ 1,
    - `PH1(F) = 0` implies `Ext1(R(F), k) = 0`.
  - No converse is claimed; in particular, no global equivalence `PH1 ⇔ Ext1`.

- **Tower diagnostics `(mu, nu)`**
  - Defined via kernels / cokernels of comparison maps between truncated stages:
    - `mu`, `nu` = generic fiber dimensions of kernel / cokernel.
  - Type IV failure: `(mu, nu) ≠ (0, 0)` while each finite stage passes local gates.
  - τ-sweeps and stability bands detect ranges where `(mu, nu) = (0, 0)` is locally stable.

- **Gating**
  - B–Gate⁺ (collapse gate) per window:
    - `PH1(F) = 0`
    - `Ext1(R(F), k) = 0` (only used under amplitude ≤ 1)
    - `(mu, nu) = (0, 0)`
    - safety margin: `gap_tau > sum_delta` (δ-ledger budget condition)
  - Overlap Gate (post-collapse):
    - local equivalence on overlaps after `T_tau`
    - Čech–Ext1 acyclicity on overlaps
    - stability band condition
    - overlap δ-budget accounting

**Not claimed:**

- No global equivalence `PH1 ⇔ Ext1`.
- No guarantees beyond 1D constructible persistence.
- No direct statements about BSD, RH, Navier–Stokes, Langlands, etc.  
  Any interaction with those worlds is via [Spec] modules and external inputs (e.g., AK_AP).

---

## What’s in Core vs [Spec]

### Core (provable / formalizable)

- Exact truncation `T_tau` and its 1-Lipschitz stability.
- Filtered lift `C_tau` up to f.q.i., compatible with `T_tau` at the persistence level.
- One-way `PH1 ⇒ Ext1` under amplitude ≤ 1.
- Tower diagnostics `(mu, nu)`, τ-sweeps, and stability bands.
- B–Gate⁺ and Overlap Gate (post-collapse gluing via Čech–Ext1).
- Restart / summability to paste windowed certificates into global ones.
- Length spectrum operator `Lambda_len`:
  - clipped-length multiset equal to truncated barcode lengths;
  - invariant under isomorphism after truncation.

### [Spec] (auditable, non-expansive after truncation)

- HDPS: Terrain Cells, Hunter / Mapper / Lifter roles, Map of Validity construction.
- PF/BC after-collapse comparator:
  - evaluate projection formula / base change at the derived level;
  - push forward to persistence; apply `T_tau`; compare on windows.
- Mirror / Transfer commutation:
  - natural 2-cells with δ-controlled commutation;
  - additive δ along pipelines; post-processing non-increasing.
- A/B soft-commuting policy:
  - for non-nested reflectors; test `Delta_comm ≤ eta` or fallback and log.
- Domain-specific realization hooks:
  - arithmetic / Langlands gates,
  - PDE / Navier–Stokes heuristics,
  - Fukaya action-filtration,
  all under non-expansive-after-truncation and δ-ledger constraints.

---

## Concepts and components

- **`T_tau` (exact truncation)**
  - Reflective localization deleting bars of length ≤ `tau`.
  - Idempotent and 1-Lipschitz for canonical persistence metrics.

- **`C_tau` (filtered lift)**
  - Chain-level lift defined up to f.q.i.
  - Compatible with `T_tau` at the persistence level.

- **Collapse gate (`B–Gate⁺`)**
  - Windowed gate that checks:
    - `PH1(F) = 0`
    - `Ext1(R(F), k) = 0` (under amplitude ≤ 1)
    - `(mu, nu) = (0, 0)`
    - `gap_tau > sum_delta` (δ-budget condition)

- **Overlap Gate (post-collapse)**
  - Enforces:
    - local equivalence after `T_tau` on overlaps up to δ-budget,
    - Čech–Ext1 acyclicity on overlaps,
    - consistency with stability bands.

- **Tower diagnostics `(mu, nu)`**
  - Derived from comparison maps between truncated stages.
  - Non-zero values signal Type IV failures.

- **Stability bands**
  - Ranges of `tau` where `(mu, nu) = (0, 0)` is stable under τ-refinement.
  - Used to define robust collapse regions.

- **Length spectrum operator `Lambda_len`**
  - Produces clipped-length spectra (multiset) equivalent to barcode lengths after truncation.
  - Isomorphism-invariant post-`T_tau`.

- **HDPS / Map of Validity [Spec]**
  - **Terrain Cells**: local patches in parameter space.
  - **Hunter**: proposes new points / directions based on δ-ledger and gates.
  - **Mapper**: refines the Map of Validity over cells.
  - **Lifter**: relates coarse models to finer ones (e.g., discrete → continuous).
  - **Validity Map**: labels each cell as `Valid`, `Obstructed`, or `Unknown`, consistent with Core gates.

---

## Installation

```bash
# 1) Clone
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

# 2) Create environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Install
pip install -e ".[all]"     # extras: [viz], [lean], [coq], [hdps]
```

---

## Quickstart

### Minimal CLI run

```bash
# Prepare a run configuration
cp examples/v17/minimal/run.yaml ./run.yaml

# Execute the pipeline (windowed, post-collapse)
akhdpst run run.yaml

# Inspect gate verdicts, tower diagnostics, and δ-ledger per window
akhdpst audit out/artifacts

# (Optional) build a small Map of Validity for toy HDPS examples
akhdpst hdps map --run run.yaml --toy
```

### Minimal Python API

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse
from akhdpst.length import lambda_len

# Load a filtered chain complex or per-degree persistence
F = ...  # user load

# Truncate at tau (persistence and filtered lift)
tau = 0.15
P_trunc = {i: T_tau(F.persistence(i), tau) for i in [0, 1]}
F_trunc = C_tau(F, tau)  # up to f.q.i.

# Gate check (one-way bridge used only with t-exact, amplitude<=1)
ok_gate = collapse_admissible(
    F,
    realization="Db(k-mod)",
    t_exact=True,
    amplitude_leq_1=True,
)

# Tower diagnostics (per tau); stability bands
mu, nu = audit_tower(tower=[F0, F1, F2, F_inf], tau=tau, degrees=[0, 1])
bands = detect_stability_band(
    tower=[F0, F1, F2, F_inf],
    degree=1,
    tau_sweep=[0.1, 0.15, 0.2],
)

# PF/BC after-collapse comparator (windowed, post T_tau) [Spec]
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)",
    obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]),
    tau=tau,
)

# Length spectrum audit (windowed clipped-length multiset)
eig = lambda_len(P_trunc[1], window=(0.0, tau))
```

---

## Configuration (`run.yaml`) — v17.0 schema highlights

```yaml
meta:
  name: "demo-v17.0"
  seed: 1337
  version: "17.0"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"       # bars | chain
  degrees: [0, 1]

windows:
  # Right-open; MECE; coverage is audited
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"         # filtered lift (up to f.q.i.)
  reflector: "T_tau"    # exact truncation at persistence level

overlap_checks:
  local_equiv: true       # post-collapse equivalence up to budget
  cech_ext1_ok: true      # Čech–Ext1 acyclicity on overlaps
  stability_band_ok: true # band-compatible tower behavior

spectral_policy:
  order: "ascending"      # MANDATORY
  norm: "op"              # "op" or "fro" (MANDATORY)
spectral_bounds:
  lambda_min: 1.0e-8
  lambda_max: 1.0e+3
  lip_tol: 0.02

operations:
  steps:
    - type: "deletion"
      op: "dirichlet_restriction"
      args: { nodes: [1, 5, 7] }
      delta: { alg: 0.000, disc: 0.002, meas: 0.001 }
    - type: "epsilon"
      op: "continuation"
      args: { eps: 0.006 }
      delta: { alg: 0.006, disc: 0.002, meas: 0.001 }
    - type: "spec"
      op: "mirror_transfer"
      args: { delta_commutation: 0.010 }   # δ(i, tau) (Mirror×Collapse)
      delta: { alg: 0.010, disc: 0.000, meas: 0.000 }

spec:
  pf_bc_after_collapse:
    enabled: true
    delta_budget: 0.0
  ab_soft_commuting:
    enabled: true
    eta: 0.02            # tolerance
    fallback_order: ["birth_window", "length"]  # if Delta_comm > eta

  # HDPS / Map of Validity (experimental; toy examples only)
  hdps:
    enabled: true
    mode: "map_of_validity"
    terrain_cells: "auto"
    hunter:
      strategy: "greedy"     # or "random", "gradient"
      max_steps: 128
    mapper:
      resolution: 32
      refine_on_boundary: true

gate:
  require:
    PH1_zero: true
    Ext1_zero: true         # used only if amplitude<=1
    mu_zero: true
    nu_zero: true
    gap_tau_gt_sum_delta: true
  safety_margin:
    gap_tau: 0.03

audit:
  outputs: ["bars", "spec", "ext", "phi", "Lambda_len", "validity_map"]
  checksums: "sha256"
  restart: "summability"

length_spectrum:
  degree: 1
  tau: 0.15
  audit: "hash"            # or store eigenvalues for small instances

output:
  dir: "out/artifacts"
  overwrite: false
```

---

## Workflows and examples

### 1) Windowed protocol (post-collapse)

Run the basic collapse and audit pipeline:

```bash
akhdpst run examples/v17/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

Each window / degree produces:

- truncated barcodes,
- δ-ledger entries,
- tower diagnostics and gate verdicts.

### 2) Overlap Gate gluing (post-collapse)

Check local-to-global consistency via the Overlap Gate:

```bash
akhdpst gate overlap --run run.yaml --window w0,w1
```

Requires:

- post-collapse local equivalence up to δ-budget,
- Čech–Ext1 acyclicity,
- stability-band consistency.

### 3) τ-sweep and stability bands

Probe `(mu, nu)` across a τ grid; accept bands with stable `(mu, nu) = (0, 0)`:

```bash
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"
```

### 4) PF/BC after-collapse comparator [Spec]

Compare `Rf_*(A⊗f^*B)` vs `Rf_*A ⊗ B` after `T_tau` on a window:

```bash
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15
```

### 5) A/B soft-commuting [Spec]

Test approximate commutation of two reflectors:

```bash
akhdpst compare ab \
  --run run.yaml \
  --reflectors length birth_window \
  --eta 0.02
```

If `Delta_comm > eta`, a fallback order is used and `Delta_comm` is logged as `delta.alg`.

### 6) Length spectrum audit (Lambda_len)

Compute and audit clipped-length spectra:

```bash
akhdpst audit lambda-len \
  --dir out/artifacts \
  --degree 1 \
  --tau 0.15
```

### 7) Toy HDPS Map of Validity [Spec]

For small examples, build a toy Map of Validity over a 2D parameter space:

```bash
akhdpst hdps map \
  --run run.yaml \
  --toy \
  --grid "32x32"
```

This produces a coarse `validity_map/` artifact marking cells as `Valid`, `Obstructed`, or `Unknown`, consistent with Core gates.

---

## Update policy (after truncation)

| Update type   | Examples                                                                  | Guarantee (post `T_tau`)                                             |
| ------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Deletion-type | Dirichlet restriction; principal submatrix; PSD Loewner contraction; conservative averaging; stop addition | Non-increasing (monotone) for windowed persistence energies and spectral indicators |
| ε-continuation| Small homotopies; steps satisfying interleaving-shift bounds            | 1-Lipschitz (stability); ε recorded in δ-ledger                      |
| Inclusion-type| Add cells; relax boundary conditions; domain enlargement                 | Non-expansive (stability only)                                       |

Notes:

- Spectral indicators live on `L(C_tau F)` and are **not** f.q.i-invariants; v17.0 mandates a fixed `spectral_policy` (order / norm) and bounds in `run.yaml`.
- All [Spec] operations must:
  - be non-expansive after `T_tau` (by design),
  - log δ entries per step (`delta.alg`, `delta.disc`, `delta.meas`),
  - respect B–Gate⁺ and Overlap Gate constraints.

---

## Auditing and artifacts

```text
out/artifacts/
  bars/
    w0_deg1_trunc.json
    w1_deg1_trunc.json
  spec/
    ledger_w0.json
    ledger_w1.json
  ext/
    w0_ext1.txt
  phi/
    maps_w0_deg1.h5         # comparison maps; (mu,nu); iso_tail flag
  lambda_len/
    w0_deg1_tau015.json     # eigenvalues or hash
  validity_map/
    toy_2d_grid.json        # Map of Validity for toy HDPS run (if enabled)
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/`: truncated barcodes per window / degree.
- `spec/`: δ-ledger (algorithmic / discretization / measurement) plus [Spec] audit results.
- `ext/`: Ext1 summaries (Core only, amplitude ≤ 1).
- `phi/`: comparison maps and diagnostics `(mu, nu)`; `phi_iso_tail` flags.
- `lambda_len/`: clipped-length spectra (eigenvalues or hashes).
- `validity_map/`: optional HDPS outputs for toy examples.
- `audit_summary.json`: gate outcomes, overlap checks, stability bands.
- `checksums.txt`: SHA256 sums of all artifacts.

---

## Command reference (CLI)

```bash
# Execute a configured run
akhdpst run run.yaml

# Audit an existing run directory
akhdpst audit out/artifacts

# Overlap Gate check
akhdpst gate overlap --run run.yaml --window w0,w1

# B–Gate⁺ per window
akhdpst gate check --run run.yaml --window w0

# τ-sweep and stability bands
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"

# PF/BC after-collapse comparator [Spec]
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15

# A/B soft-commuting test [Spec]
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02

# Print tower diagnostics
akhdpst diag tower --dir out/artifacts --degree 1

# Length spectrum audit
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15

# HDPS: build a toy Map of Validity [Spec]
akhdpst hdps map --run run.yaml --toy --grid "32x32"
```

---

## Python API reference (selected)

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus, overlap_gate_check
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse, ab_soft_commute
from akhdpst.length import lambda_len

# Overlap Gate
ok_overlap = overlap_gate_check(run="run.yaml", windows=["w0", "w1"])

# B–Gate⁺ (windowed)
ok_bgate = b_gate_plus(
    window="w0",
    ph1_zero=True,
    ext1_zero=True,
    mu=0,
    nu=0,
    gap_tau=0.025,
    delta_sum=0.011,
)

# A/B soft-commuting [Spec]
ok_ab = ab_soft_commute(
    M=P_trunc[1],
    A="length",
    B="birth_window",
    eta=0.02,
    fallback=True,
)

# PF/BC comparator [Spec]
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)",
    obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]),
    tau=0.15,
)

# Stability band detection for τ
bands = detect_stability_band(
    tower=[...],
    degree=1,
    tau_sweep=[0.1, 0.15, 0.2],
)

# Length spectrum eigenvalues/hash
L = lambda_len(P_trunc[1], window=(0.0, 0.15))
```

---

## Roadmap

- **Core**
  - Further Lean / Coq formalization:
    - `T_tau`, `C_tau`, `(mu, nu)`, B–Gate⁺, Overlap Gate.
  - Automated τ-sweep and band detection with certified bounds.

- **HDPS / [Spec]**
  - Richer HDPS tooling:
    - multi-resolution Terrain Cells,
    - policy plug-ins for Hunter / Mapper / Lifter.
  - More robust toy models (finite graphs, CW-complexes) with fully implemented Maps of Validity.
  - Domain-specific adapters:
    - arithmetic / AK_AP,
    - PDE / Navier–Stokes heuristics,
    all obeying Core non-expansiveness constraints.

- **Tooling and UX**
  - Notebook templates for:
    - per-window audits,
    - δ-ledger visualization,
    - validity map visualization.
  - CI integration for example runs and audit regressions.

---

## Contributing

We welcome issues and PRs, especially in the following areas:

- Improving **Core clarity** and formalization (definitions, proofs, Lean / Coq code).
- Implementing **small, fully-worked examples** (finite graphs, toy CW-complexes).
- Extending HDPS tooling with **clearly labeled [Spec] policies**.

Guidelines:

- Keep **Core vs [Spec] explicit** in both code and docs.
- All [Spec] items must:
  - include non-expansive-after-truncation tests, and
  - log δ-ledger entries.
- Whenever possible, add minimal examples and tests (T7, T10, T11, T13, T14, T15).

Dev commands:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## Citing and references

If you use AK–HDPST v17.0 in research, please cite:

```text
AK–HDPST v17.0 / AK-OS v1.0:
High-Dimensional Projection Structural Theory and an OS for Collapse-Based Exploration

Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

Foundational references (non-exhaustive):

- T. Crawley-Boevey, *Decomposition of pointwise finite-dimensional persistence modules*, 2015.
- F. Chazal, V. de Silva, M. Glisse, S. Oudot,  
  *Structure and stability of persistence modules and barcodes*, 2016.

For the arithmetic calibration program, see the companion repository:

```text
AK_AP: Arithmetic Calibration Program for AK-OS
(Weil / FLT closed-world calibration)
URL: https://github.com/your-org/ak-ap   # placeholder
```

## Archive / OLD versions

The `OLD/` directory contains historical snapshots of AK–HDPST (v1.4–v16.0).
They are kept **as an archive and cautionary record** of earlier, over-loaded
or less-guarded designs.

- Only **v17.0** and the AK_AP modules in the top-level tree should be
  considered part of the current AK-OS design.
- OLD versions may contain obsolete claims, broader scopes, or unchecked [Spec] layers.
  They are preserved for transparency, not as recommended references.

---

## License

This project is released under the MIT License. See `LICENSE` for details.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17874722.svg)](https://doi.org/10.5281/zenodo.17874722)

---

## Appendix: Terms cheat sheet

- **Constructible 1D persistence**: finite critical set; pointwise finite-dimensional over bounded windows.
- **`T_tau`**: exact truncation removing all bars of length ≤ `tau`; idempotent; 1-Lipschitz.
- **`C_tau`**: filtered lift of `T_tau` up to filtered quasi-isomorphism; `P_i(C_tau F) ≅ T_tau(P_i F)`.
- **B–Gate⁺**: core collapse gate per window:
  - `PH1 = 0`,
  - `Ext1 = 0` (under amplitude ≤ 1),
  - `(mu, nu) = (0, 0)`,
  - `gap_tau > sum_delta`.
- **Overlap Gate**: post-collapse local-to-global gluing gate using:
  - local equivalence,
  - Čech–Ext1 acyclicity,
  - stability bands,
  - overlap δ-budget.
- **`(mu, nu)`**: generic fiber dimensions of kernel / cokernel of comparison maps after truncation; non-zero ⇒ Type IV failure.
- **Stability band**: τ-range with `(mu, nu) = (0, 0)` stable under τ-refinement.
- **PF/BC comparator**: projection formula / base change comparator applied after `T_tau` on windows ([Spec]).
- **A/B soft-commuting**: approximate commutation test for non-nested reflectors; `Delta_comm ≤ eta` or fallback + δ-logging.
- **`Lambda_len`**: length spectrum operator; windowed clipped-length multiset; isomorphism-invariant after truncation.
- **HDPS**: High-Dimensional Projection Search; search engine building a Map of Validity over parameter spaces ([Spec]).
- **Terrain Cell**: local region of parameter space where collapse characteristics are approximately uniform.
- **Map of Validity**: labeling of terrain cells as `Valid`, `Obstructed`, or `Unknown`, consistent with Core gates and diagnostics.
