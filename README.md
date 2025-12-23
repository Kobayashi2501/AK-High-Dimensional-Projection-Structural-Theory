# AK–HDPST v17.0.1 — AK High-Dimensional Projection Structural Theory

> **AK-OS v1.0.1: an operating system for high-dimensional mathematical exploration**  
> **Core**: provable, 1D constructible persistence over a field  
> **[Spec]**: auditable, post-truncation (non-expansive) extensions and search policies

This repository contains **AK–HDPST v17.0.1**, positioned not as a “universal solver” for major conjectures, but as a **proof-oriented operating system (AK-OS)** for exploring them with explicit scope boundaries, budgets, and audit artifacts.

A companion project, **AK_AP (Arithmetic Programs) v1.0.1**, provides **closed-world calibration** on arithmetic moduli spaces (finite-field “Weil world” and “FLT world”) under the same OS, using known theorems as **boundary inputs**.

**Strong guarantees are strictly confined to the Core scope.** Everything else must be explicitly marked **[Spec]** and audited.

---

## Repository file structure (as provided in this release)

~~~text
.
├─ OLD/                                  # Old files (kept as cautionary archive; may contain obsolete claims)
│  └─ ...                                # historical snapshots (v1.x–v16.x)
├─ AK–HDPST_v17.0.1/
│  ├─ AK_HPDST_v17.0.1.tex               # XeLaTeX source (main paper)
│  └─ AK_HPDST_v17.0.1.pdf               # compiled PDF (main paper)
└─ AK–Arithmetic_Programs_v1.0.1/
   ├─ AK–Arithmetic Programs v1.0.1.tex  # XeLaTeX source (companion)
   └─ AK–Arithmetic Programs v1.0.1.pdf  # compiled PDF (companion)
~~~

---

## AK-OS v1.0.1 manifesto

### What this is

- **Not**: a claimed proof of any grand conjecture (Navier–Stokes, BSD, RH, FLT, Langlands, etc.).
- **Is**: a **modular OS** for exploration, built around:
  - an exact truncation operator `T_tau` (“bar deletion”)
  - a filtered lift `C_tau` (defined up to filtered quasi-isomorphism)
  - a **δ-ledger** for budget accounting (algorithmic / discretization / measurement)
  - **tower diagnostics** `(mu_collapse, nu_collapse)` for invisible limit failures (Type IV)
  - **windowed gates** (B–Gate⁺ / Overlap Gate) operating **after truncation**
  - a search layer **HDPS** ([Spec]) that builds a **Map of Validity** on parameter spaces

### Core vs [Spec] (v17.0.1 contract)

- **Core**
  - One-parameter, constructible persistence over a field `k`
  - Exact truncation `T_tau`: delete bars of length `<= tau` (reflective localization), idempotent, 1-Lipschitz for the interleaving distance
  - Filtered lift `C_tau` up to f.q.i., compatible with persistence:
    - `P_i(C_tau F) ≅ T_tau(P_i F)` (at the persistence layer)
  - One-way bridge (in `D^b(k-mod)` under amplitude `<= 1` and a t-exact realization):
    - `PH1(F)=0  =>  Ext^1(R(F), k)=0`
  - Tower diagnostics `(mu_collapse, nu_collapse)` computed **after truncation**, detecting Type IV failures
  - Windowed proof policy with explicit budgets and audit outputs

- **[Spec]**
  - Domain-specific realizations (arithmetic / PDE / Fukaya / Langlands, etc.), **guarded by Core**
  - HDPS: Terrain Cells, Hunter / Mapper / Lifter agents, Map of Validity
  - PF/BC after-collapse comparator, Mirror / Transfer, A/B soft-commuting policies
  - Quantitative heuristics and exploration strategies

**Rule**: every [Spec] component must be **post-truncation non-expansive** (in the project’s sense) and fully audited via δ-ledger entries and tower diagnostics.

---

## Core primitives (v17.0.1)

### Truncation and lift

- `T_tau`: exact truncation deleting barcode intervals of length `<= tau`
- `C_tau`: filtered lift (up to filtered quasi-isomorphism), with
  - `P_i(C_tau F) ≅ T_tau(P_i F)`

### Collapse admissibility (Core)

A basic Core predicate (used throughout the pipeline):

- `CollapseAdmissible(F) := (PH1(F)=0) AND (Ext^1(R(F),k)=0)`

The one-way bridge makes the Ext condition *dischargeable* from `PH1=0` under the stated hypotheses; no global converse is claimed.

### Tower diagnostics and “tail isomorphism”

v17.0.1 packages “absence of invisible limit obstruction” as:

- `DiagZero := (mu_collapse, nu_collapse) = (0,0)`

This is the canonical way the paper expresses “no Type IV / tail obstruction” on a certified window/cell.

### B–Gate⁺ (after-collapse gate)

**Definition (Core, windowed, after truncation):** on a right-open window `W=[u,u')` at threshold `tau`, **B–Gate⁺ passes** if:

1. `PH1(C_tau F | W) = 0`
2. `Ext^1(R(C_tau F | W), k) = 0` (eligibility checked)
3. `DiagZero` (i.e., `(mu_collapse, nu_collapse)=(0,0)`)
4. Budget check: `gap_tau > sum_delta` (δ-ledger)

This is the project’s canonical “collapse contract” at the window level.

### Overlap Gate (after-collapse coherence)

For overlapping windows `W_a, W_b`, the Overlap Gate enforces (post-truncation) coherence on overlaps, with:

- overlap distance bound (interleaving distance on cropped, truncated data) `<= sum_delta_ab`
- budget margin `gap_tau > sum_delta_ab`
- `DiagZero`

The Overlap Gate is the mechanism used to paste window-local certificates into coherent global / multi-window artifacts.

---

## v17.0.1 positioning: from “solver” to “OS”

### Why this pivot exists

Earlier versions tried to unify multiple heavy domains at once. v17.x makes an explicit pivot:

- **From**: “one gigantic framework that might prove everything”
- **To**: a **proof-oriented OS** that cleanly separates
  - what is proved and stable (**Core**),
  - what is operational, domain-dependent, or heuristic (**[Spec]**),
  - and what is uncertain (budgeted and audited).

### What v17.0.1 adds on top of v17.0 (documentation-level)

v17.0.1 is a **patch release** whose primary goal is **auditability and boundary clarity**:

- reference / label / cross-reference hygiene (duplicate labels and unresolved refs removed)
- tightened “Core vs [Spec]” marking for statements that were previously easy to misread
- minimum bibliographic anchors for “standard facts” (so reviewers can classify leaps vs citations)
- canonicalization of “Type IV diagnostics” phrasing via `DiagZero`

These are “trust-surface” upgrades: they improve third-party auditability without expanding the Core scope.

---

## AK_AP (Arithmetic Programs) — v1.0.1 companion

AK_AP is a companion program/paper that performs **closed-world calibration** on arithmetic moduli spaces using AK-OS.

**Principle**: AK_AP does **not** claim new proofs of Deligne or Wiles–Taylor. Instead, those are treated as **boundary inputs** in a world where the truth is known, and the OS is tested for consistency and auditability:

- `M_Weil`: finite-field Weil world (Deligne as boundary input)
- `M_FLT`: FLT world / Frey data (Wiles–Taylor / modularity as boundary input)

### Critical compatibility rule (v17.0.1)

To remain consistent with AK-OS:

- **B–Gate⁺ is reserved for the v17.0.1 Core definition** (windowed, post-truncation, budgeted, with `DiagZero`).
- Any arithmetic-specific checks (e.g., defect potentials / modularity potentials) must be treated as **pre-gates** (sanity checks) or **[Spec] measurements**, logged to the δ-ledger, and must not silently redefine B–Gate⁺.

If you publish AK_AP outputs, present them as:

- “calibration / consistency evidence under declared budgets,” not as proofs.

---

## How to read this project

- **As mathematics**: treat Core as the only “theorem-grade” layer; treat [Spec] as auditable, implementation-dependent extensions.
- **As software architecture**: view AK-OS as a pipeline OS for truncation-first stability, budget accounting, and failure diagnosis.
- **As AI × human collaboration**: the OS is designed to make exploration reproducible and criticizable (run manifests + artifacts), not “mystical.”

---

## Run protocol (conceptual)

All comparisons and decisions follow a post-truncation order:

~~~text
t  →  persistence P_i  →  truncation T_tau  →  compare / audit / gate / map_validity
~~~

Outputs are organized as auditable artifacts (barcodes, ledgers, diagnostics, checksums) so that third parties can rerun and criticize.

---

## Installation (illustrative; repository-dependent)

~~~bash
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[all]"
~~~

> Note: the actual package layout and extras depend on the repository implementation.  
> This README describes the OS and audit contract; code scaffolding may vary.

---

## Quickstart (illustrative)

### Minimal CLI run

~~~bash
# Prepare a run configuration (example path)
cp examples/v17.0.1/minimal/run.yaml ./run.yaml

# Execute the windowed post-truncation pipeline
akhdpst run run.yaml

# Inspect gate verdicts, tower diagnostics, and δ-ledger per window
akhdpst audit out/artifacts --by-window
~~~

### Minimal Python API (illustrative)

~~~python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import b_gate_plus
from akhdpst.tower import audit_tower

F = ...   # load filtered object / persistence
tau = 0.15
W = (0.0, 0.5)  # right-open in the protocol; represented here as a pair

# Truncation at persistence level
P1_trunc = T_tau(F.persistence(1), tau)

# Filtered lift (up to f.q.i.)
F_trunc = C_tau(F, tau)

# Tower diagnostics (after truncation)
mu, nu = audit_tower(tower=[...], tau=tau, degree=1)

# Gate check (windowed)
ok = b_gate_plus(
    F=F,
    window=W,
    tau=tau,
    mu=mu,
    nu=nu,
    gap_tau=0.03,
    sum_delta=0.011,
)
~~~

---

## Configuration (`run.yaml`) — v17.0.1 schema highlights (illustrative)

~~~yaml
meta:
  name: "demo-v17.0.1"
  seed: 1337
  version: "17.0.1"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"       # bars | chain
  degrees: [0, 1]

windows:
  - label: "w0"
    range: [0.0, 0.5)   # right-open; MECE; coverage audited
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"
  reflector: "T_tau"

gate:
  require:
    PH1_zero: true
    Ext1_zero: true         # only used if eligibility holds (amplitude<=1 etc.)
    DiagZero: true          # (mu_collapse, nu_collapse) = (0,0)
    gap_tau_gt_sum_delta: true
  safety_margin:
    gap_tau: 0.03

audit:
  outputs: ["bars", "ledger", "tower", "gate", "checksums"]
  checksums: "sha256"

output:
  dir: "out/artifacts"
  overwrite: false
~~~

---

## Auditing and artifacts (conceptual)

~~~text
out/artifacts/
  bars/
    w0_deg1_trunc.json
    w1_deg1_trunc.json
  ledger/
    ledger_w0.json
    ledger_w1.json
  tower/
    phi_maps_w0_deg1.json     # comparison maps; (mu,nu); tail flags
  gate/
    gate_w0.json
    gate_w1.json
  run.yaml
  audit_summary.json
  checksums.txt
~~~

- `bars/`: truncated barcodes per window / degree.
- `ledger/`: δ-ledger per window (algorithmic / discretization / measurement).
- `tower/`: comparison maps and diagnostics `(mu_collapse, nu_collapse)`; tail/isomorphism flags.
- `gate/`: gate outcomes (B–Gate⁺, Overlap Gate where applicable).
- `audit_summary.json`: rollups across windows.
- `checksums.txt`: SHA256 sums for reproducibility.

---

## Update policy (post-truncation)

All monotonicity / stability claims are stated **after** truncation `T_tau`.

| Update type    | Examples (illustrative)                                              | Guarantee (post `T_tau`)                                   |
|---------------|-----------------------------------------------------------------------|------------------------------------------------------------|
| Deletion-type | restrictions, conservative contractions, controlled averaging         | monotone non-increasing for selected post-trunc indicators |
| ε-continuation| small homotopies under interleaving bounds                            | 1-Lipschitz stability; ε logged in δ-ledger                |
| Inclusion-type| adding cells / enlarging domains                                      | stability-only (non-expansive), not monotone               |

**Important note**: spectral indicators on realized chain-level objects are not f.q.i.-invariants; v17.0.1 therefore enforces a fixed policy and budgets (and logs any deviations).

---

## What’s new in v17.0.1 (vs v16.x)

### Conceptual

- OS framing tightened: AK–HDPST is explicitly an **exploration OS** with provable Core guarantees.
- HDPS and the Map of Validity remain **[Spec]** and must be audited.
- Closed-world calibration via AK_AP is positioned as consistency testing, not proof.

### Technical / audit-facing

- Stronger separation of Core vs [Spec] claims in the writing.
- Reference hygiene: duplicate labels and unresolved references removed.
- Minimum bibliographic anchors for standard facts (improves third-party audit classification).
- Canon phrasing for Type IV diagnostics via `DiagZero`.

---

## Roadmap (high level)

- **Core**
  - additional formalization (Lean / Coq): `T_tau`, `C_tau`, `(mu,nu)`, B–Gate⁺, Overlap Gate
  - more automated τ-sweep and stability-band diagnostics with certified bounds

- **[Spec]**
  - HDPS tooling improvements: multi-resolution terrain cells; agent policies with explicit δ-budgets
  - richer toy models with fully implemented validity maps
  - domain adapters (arithmetic / PDE / symplectic) that respect Core constraints

---

## Contributing (policy)

- Keep **Core vs [Spec] explicit** in docs and code.
- Every [Spec] component must:
  - include post-truncation non-expansiveness tests (as applicable), and
  - log δ-ledger entries.
- Prefer minimal, reproducible examples with auditable artifacts.

---

## Citing and references (templates)

If you use AK–HDPST v17.0.1 in research, please cite:

~~~text
AK–HDPST v17.0.1 / AK-OS v1.0.1:
High-Dimensional Projection Structural Theory and an OS for collapse-based exploration.

Authors: Atsushi Kobayashi, et al.
Year: 2025
Repository / archive: (insert URL or DOI)
~~~

Foundational references (non-exhaustive; illustrative):

- T. Crawley-Boevey, *Decomposition of pointwise finite-dimensional persistence modules*, 2015.
- F. Chazal, V. de Silva, M. Glisse, S. Oudot, *Structure and stability of persistence modules and barcodes*, 2016.

For the arithmetic calibration program:

~~~text
AK_AP v1.0.1: Arithmetic Programs for AK-OS (closed-world calibration)
Repository / archive:
~~~

---

## License

MIT (see `LICENSE`).
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18029366.svg)](https://doi.org/10.5281/zenodo.18029366)
---

## Appendix: Terms cheat sheet

- **Constructible 1D persistence**: finite critical set; pointwise finite-dimensional over bounded windows.
- **`T_tau`**: exact truncation removing all bars of length `<= tau`; idempotent; 1-Lipschitz.
- **`C_tau`**: filtered lift of `T_tau` up to filtered quasi-isomorphism; `P_i(C_tau F) ≅ T_tau(P_i F)`.
- **`DiagZero`**: `(mu_collapse, nu_collapse)=(0,0)`; “no tail obstruction / no Type IV” on a window.
- **B–Gate⁺ (Core)**: windowed after-collapse gate requiring:
  - `PH1=0`,
  - `Ext^1=0` (eligible; amplitude<=1 regime),
  - `DiagZero`,
  - budget margin `gap_tau > sum_delta`.
- **Overlap Gate (Core)**: overlap coherence gate with distance bound, budget margin, and `DiagZero`.
- **`(mu_collapse, nu_collapse)`**: tower diagnostics derived from comparison maps after truncation; non-zero signals invisible limit failure (Type IV).
- **HDPS ([Spec])**: search layer building a Map of Validity (`Valid` / `Obstructed` / `Unknown`) under Core guards.
- **δ-ledger**: budget accounting for algorithmic / discretization / measurement deviations.
