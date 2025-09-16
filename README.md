# AK–HDPST v16.0 — AK High-Dimensional Projection Structural Theory

Two-layer, auditable proof framework for functorial collapse via higher-dimensional projections and controlled obstruction removal.

- Core: machine-checkable statements in 1D constructible persistence over a field
- [Spec]: safe, non-expansive-after-truncation extensions with explicit, auditable hypotheses

Repository status: research framework with reference APIs, run protocol, and audit artifacts. Strong guarantees are confined to the Core scope below.

Simple flow (measurement order):
t  →  persistence `P_i`  →  truncation `T_tau`  →  compare/audit
```

---

## What’s new in v16.0 (vs v15.0)

- Windowed infrastructure
  - Overlap Gate upgraded (windowed, post-collapse gluing; Čech–Ext¹ acyclicity on overlaps; δ-budgets on overlaps)
  - Window Stack (WinFib) as a Grothendieck-fibration-style bookkeeping scaffold
  - Stability bands: τ-sweep and band detection for tower audits; robust band-based gating
- Safety and auditing
  - B–Gate⁺ safety margin per window; Restart/Summability to paste certificates globally
  - δ-ledger standardized and layered: algorithmic (incl. Mirror–Collapse and A/B residuals), discretization, measurement
  - Canonical run schema fields: overlap_checks, spectral_policy (ascending order; op/fro norm), spectral_bounds, Lambda_len audit, phi_iso_tail
- Diagnostics and comparators
  - Tower diagnostics (μ, ν) formalized for kernels/cokernels after truncation; invisible Type IV failures (finite-level OK, limit fails)
  - PF/BC after-collapse comparator (projection formula/base change evaluated post `T_tau` on windows)
  - A/B soft-commuting policy for non-nested torsion reflectors with additive Δ_comm budgets
- Quantitative structures
  - Length spectrum operator `Lambda_len` (windowed clipped-length multiset; isomorphism-invariant after truncation)
  - Tropical/weak-group collapse tools [Spec]: windowed energy dominance contracts; group-action proxies on bar-basis
- Domain hooks [Spec]
  - Fukaya action-filtration pipeline (continuation 1-Lipschitz; stop addition deletion-type; tower stability with (μ, ν))
  - Three-layer (Gal → Trans → Funct) Langlands-style gates with windowed layer kernels and PF/BC audits
- Formal test suite (IMRN/AiM-ready)
  - T14 Overlap Gate gluing; T15 Length spectrum audit; T7 Saturation gate; T10 A/B tests; T13 δ-budget additivity; T11 Restart/Summability

---

## Table of contents

- Overview
- Scope and guarantees
- What’s in Core (provable) vs [Spec] (auditable)
- Concepts and components
- Installation
- Quickstart (CLI and Python API)
- Configuration (`run.yaml`)
- Workflows and examples
- Update policy (allowed operations)
- Auditing and artifacts
- Command reference
- Python API reference (selected)
- Roadmap
- Contributing
- Citing and references
- License
- Appendix: Terms cheat sheet

---

## Overview

AK–HDPST v16.0 is a proof-oriented framework that cleanly separates:
- Core: proved, machine-checkable guarantees in constructible 1D persistence over a field, and
- [Spec]: operational extensions that are non-expansive after truncation and fully audited (δ-ledger, overlap gluing, stability bands).

All comparisons follow the windowed, single-layer protocol (post-truncation):
t → persistence `P_i` → `T_tau` → compare/audit

This ensures metric stability, transparent failure modes (e.g., Type IV), and reproducible pipelines.

---

## Scope and guarantees (Core)

Strong claims are limited to:
- One-parameter, constructible persistence over a field k
- Exact Serre reflector `T_tau` (deletes bars of length ≤ τ); exact, idempotent, 1‑Lipschitz (interleaving/bottleneck)
- Filtered lift `C_tau` up to filtered quasi-isomorphism (f.q.i.) with `P_i(C_tau F) ≅ T_tau(P_i F)`
- One-way bridge only: `PH1(F)=0 ⇒ Ext1(R(F), k)=0` under a t‑exact realization with amplitude ≤ 1 (no converse)
- Tower diagnostics `(mu, nu)` from kernels/cokernels of comparison maps after truncation; detect invisible limit failures (Type IV)
- Windowed gating: B–Gate⁺ (PH1/Ext1/(μ,ν)/safety margin) and Overlap Gate (post-collapse local-to-global)

Not claimed:
- No global equivalence `PH1 ⇔ Ext1`
- No statements about BSD, RH, or Navier–Stokes beyond [Spec]-level protocols
- No beyond-constructible or multi-parameter guarantees

---

## What’s in Core vs [Spec]

Core (provable):
- Exact truncation `T_tau` and 1‑Lipschitz stability
- Filtered lift `C_tau` up to f.q.i.
- One-way PH1 ⇒ Ext1 (amplitude ≤ 1)
- Tower diagnostics `(mu,nu)`, τ-sweeps, stability bands
- B–Gate⁺ (safety margin) and Overlap Gate (Čech–Ext¹ on overlaps)
- Restart/Summability to paste windowed certificates into global ones
- Length spectrum correctness (clipped-length multiset; isomorphism invariance after truncation)

[Spec] (auditable, non-expansive after truncation):
- PF/BC after-collapse comparator (proper/smooth + field coeffs)
- Mirror/Transfer with δ‑controlled commutation (natural 2‑cell; additive and post‑processing non‑increasing)
- A/B soft‑commuting policy for non‑nested reflectors (Δ_comm to δ‑ledger)
- Tropical/weak-group collapse proxies
- Three-layer Langlands gates (Gal/Trans/Funct)
- Fukaya realization with action filtration (continuation 1‑Lipschitz; stops deletion‑type)

---

## Concepts and components

- `T_tau` (exact truncation)
  - Exact reflective localization that deletes bars of length ≤ τ
  - Idempotent; 1‑Lipschitz for interleaving/bottleneck
- `C_tau` (filtered lift, up to f.q.i.)
  - Chain-level lift with `P_i(C_tau F) ≅ T_tau(P_i F)`
- Collapse gate (B–Gate⁺)
  - On each window: PH1(F)=0; Ext1(R(F),k)=0 (eligible only under amplitude ≤ 1); μ=ν=0; safety margin `gap_tau > Σ delta`
- Overlap Gate (post-collapse)
  - Local equivalence (after truncation) on overlaps; Čech–Ext¹ acyclicity; δ-budget on overlap; stability-band check
- Tower diagnostics
  - Comparison map after `T_tau`: `(mu, nu)` = generic fiber dims of ker/coker; Type IV when `(mu,nu)≠(0,0)`
- Stability bands
  - τ-sweep; band detection; robust gating over contiguous τ ranges with `(mu,nu)=(0,0)`
- PF/BC after-collapse comparator [Spec]
  - Compute PF/BC objectwise in t; transport to persistence; apply `T_tau`; compare on windows
- Mirror/Transfer commutation [Spec]
  - Natural 2‑cell `Mirror ∘ C_tau ⇒ C_tau ∘ Mirror` with uniform δ(i,τ); additive along pipelines; post‑processing non‑increasing
- A/B soft‑commuting [Spec]
  - For non‑nested reflectors; test Δ_comm ≤ η; else fallback order and log Δ_comm to δ‑ledger
- Length spectrum operator `Lambda_len`
  - Windowed clipped-length eigenvalues (unordered multiset) equal clipped barcode lengths; invariant under isomorphism after truncation

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
pip install -e ".[all]"     # extras: [viz], [lean], [coq]
```

---

## Quickstart

### Minimal CLI run

```bash
# Prepare a run configuration
cp examples/v16/minimal/run.yaml ./run.yaml

# Execute the pipeline (windowed, post-collapse)
akhdpst run run.yaml

# Inspect gate verdicts and δ-ledger per window
akhdpst audit out/artifacts
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
P_trunc = {i: T_tau(F.persistence(i), tau) for i in [0,1]}
F_trunc = C_tau(F, tau)  # up to f.q.i.

# Gate check (one-way bridge used only with t-exact, amplitude<=1)
ok_gate = collapse_admissible(
    F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True
)

# Tower diagnostics (per tau); stability bands
mu, nu = audit_tower(tower=[F0, F1, F2, F_inf], tau=tau, degrees=[0,1])
bands = detect_stability_band(tower=[F0, F1, F2, F_inf], degree=1, tau_sweep=[0.1,0.15,0.2])

# PF/BC after-collapse comparator (windowed, post T_tau)
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)", obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]), tau=tau
)

# Length spectrum audit (windowed clipped-length multiset)
eig = lambda_len(P_trunc[1], window=(0.0, tau))
```

---

## Configuration (`run.yaml`) — v16.0 schema highlights

```yaml
meta:
  name: "demo-v16.0"
  seed: 1337
  version: "16.0"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"       # bars | chain
  degrees: [0, 1]

windows:
  # Right-open; MECE; window coverage is audited
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"         # filtered lift (up to f.q.i.)
  reflector: "T_tau"    # exact truncation at persistence

overlap_checks:
  local_equiv: true      # post-collapse equivalence up to budget
  cech_ext1_ok: true     # Čech–Ext¹ acyclicity on overlaps
  stability_band_ok: true

spectral_policy:
  order: "ascending"     # MANDATORY (v16.0)
  norm: "op"             # "op" or "fro" (MANDATORY)
spectral_bounds:
  lambda_min: 1.0e-8
  lambda_max: 1.0e+3
  lip_tol: 0.02

operations:
  steps:
    - type: "deletion"
      op: "dirichlet_restriction"
      args: { nodes: [1,5,7] }
      delta: { alg: 0.000, disc: 0.002, meas: 0.001 }
    - type: "epsilon"
      op: "continuation"
      args: { eps: 0.006 }
      delta: { alg: 0.006, disc: 0.002, meas: 0.001 }
    - type: "spec"
      op: "mirror_transfer"
      args: { delta_commutation: 0.010 }   # δ(i,τ) (Mirror×Collapse)
      delta: { alg: 0.010, disc: 0.000, meas: 0.000 }

spec:
  pf_bc_after_collapse: { enabled: true, delta_budget: 0.0 }
  ab_soft_commuting:
    enabled: true
    eta: 0.02            # tolerance
    fallback_order: ["birth_window", "length"]  # if Δ_comm > η

gate:
  require:
    PH1_zero: true
    Ext1_zero: true       # used only if amplitude<=1
    mu_zero: true
    nu_zero: true
    gap_tau_gt_sum_delta: true
  safety_margin:
    gap_tau: 0.03

audit:
  outputs: ["bars", "spec", "ext", "phi", "Lambda_len"]
  checksums: "sha256"
  restart: "summability"

length_spectrum:
  degree: 1
  tau: 0.15
  audit: "hash"         # or store eigenvalues for small instances

output:
  dir: "out/artifacts"
  overwrite: false
```

Key schema additions (v16.0):
- `overlap_checks` (Overlap Gate — local_equiv, cech_ext1_ok, stability_band_ok)
- `spectral_policy.order="ascending"` and `norm="op"|"fro"` (mandatory)
- `spectral_bounds` and `lip_tol`
- `length_spectrum` (`Lambda_len` audit)
- δ-ledger per step; `gap_tau` for safety margin
- A/B soft-commuting with `eta` + fallback order

---

## Workflows and examples

### 1) Windowed protocol (post-collapse)

- For each right-open window:
  - Compute persistence
  - Apply `T_tau`
  - Compare maps, compute `(mu,nu)`, and audit delta-ledger

```bash
akhdpst run examples/v16/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

### 2) Overlap Gate gluing (post-collapse)

- Requirements per overlapping window:
  - Post-collapse local equivalence up to δ-budget
  - Čech–Ext¹ acyclicity holds (degree 1)
  - Stability-band condition (no near‑τ accumulation; `(mu,nu)=(0,0)`)

```bash
akhdpst gate overlap --run run.yaml --window w0,w1
```

### 3) τ‑sweep & stability bands

- Probe `(mu,nu)` across a τ grid; accept bands with `(mu,nu)=(0,0)` stable under refinement

```bash
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"
```

### 4) PF/BC after-collapse comparator [Spec]

- Compare `Rf_*(A⊗f^*B)` vs `Rf_*A ⊗ B` after `T_tau`, on the same window

```bash
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15
```

### 5) A/B soft-commuting [Spec]

- Test Δ_comm ≤ η; else fallback order and log Δ_comm as δ^{alg}

```bash
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02
```

### 6) Length spectrum audit (Lambda_len)

- Compute windowed clipped-length multiset and store hash/eigs

```bash
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15
```

---

## Update policy (after truncation)

| Update type   | Examples                                                                  | Guarantee (post `T_tau`)                                             |
| ---           | ---                                                                       | ---                                                                   |
| Deletion-type | Dirichlet restriction; principal submatrix; PSD Loewner contraction; conservative averaging; stop addition | Non-increasing (monotone) for windowed persistence energies and spectral indicators |
| ε‑continuation| Small homotopies; small steps satisfying interleaving shift bound         | 1‑Lipschitz (stability); record ε in δ‑ledger                         |
| Inclusion-type| Add cells; relax boundary conditions; domain enlargement                  | Non-expansive (stability only)                                        |

Notes:
- Spectral indicators are computed on `L(C_tau F)`; they are not f.q.i.-invariants. v16.0 mandates a fixed `spectral_policy` (ordering/norm) + bounds in `run.yaml`.
- [Spec] items (PF/BC comparator, Mirror/Transfer, A/B policy, tropical tools) must log δ to the ledger and pass B–Gate⁺ per window.

---

## Auditing and artifacts

```
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
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/`: truncated barcodes per window/degree
- `spec/`: δ-ledger (alg/disc/meas) + [Spec] audit results
- `ext/`: Ext¹ summaries (eligible only under amplitude ≤ 1)
- `phi/`: comparison maps; `(mu,nu)`; `phi_iso_tail` status
- `lambda_len/`: clipped-length multiset (eigs or hash)
- `audit_summary.json`: gate outcomes; overlap checks; stability bands
- `checksums.txt`: SHA256 sums of all artifacts

---

## Command reference (CLI)

```bash
# Execute a configured run
akhdpst run run.yaml

# Audit an existing run directory
akhdpst audit out/artifacts

# Overlap Gate check
akhdpst gate overlap --run run.yaml --window w0,w1

# B–Gate+ per window
akhdpst gate check --run run.yaml --window w0

# τ‑sweep and stability bands
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"

# PF/BC after-collapse comparator
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15

# A/B soft-commuting test
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02

# Print tower diagnostics
akhdpst diag tower --dir out/artifacts --degree 1

# Length spectrum audit
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15
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
ok_overlap = overlap_gate_check(run="run.yaml", windows=["w0","w1"])

# B–Gate+ (windowed)
ok_bgate = b_gate_plus(
    window="w0",
    ph1_zero=True,
    ext1_zero=True,
    mu=0, nu=0,
    gap_tau=0.025,
    delta_sum=0.011
)

# Mirror/Transfer (δ‑controlled commutation)
ok_mirror = ab_soft_commute(
    M=P_trunc[1], A="length", B="birth_window", eta=0.02, fallback=True
)

# PF/BC comparator
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)", obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]), tau=0.15
)

# Stability band detection for τ
bands = detect_stability_band(tower=[...], degree=1, tau_sweep=[0.1,0.15,0.2])

# Length spectrum eigenvalues/hash
L = lambda_len(P_trunc[1], window=(0.0, 0.15))  # eigs or hash
```

---

## Roadmap

- Auto τ‑sweep and band detection (robust refinement; band‑wise gating)
- Extended Overlap Gate tooling (nerve API; typed acceptance per simplex)
- Richer spec modules (arithmetic/Langlands, PDE, Fukaya) with δ‑controls
- Formalization expansions (Lean/Coq): `T_tau`, `(mu,nu)`, gates, PF/BC transport, A/B policy
- Notebook templates (per-window audits, δ‑ledger/overlap visualization)

---

## Contributing

We welcome issues and PRs:
- Keep Core vs [Spec] explicit (code/docs)
- [Spec] items must include non‑expansive‑after‑truncation checks + δ‑ledger entries
- Add minimal examples and tests (T7, T10, T11, T13, T14, T15)

Dev commands:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## Citing and references

If you use AK–HDPST v16.0 in research, please cite:

```
AK–HDPST v16.0: Windowed Collapse, Overlap Gate, PF/BC After-Collapse, and Auditable Pipelines
Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

Foundational references:
- Crawley‑Boevey (2015): Decomposition of pointwise finite‑dimensional persistence modules
- Chazal, de Silva, Glisse, Oudot (2016): Structure and stability of persistence modules and barcodes

---

## License

This project is released under the MIT License. See `LICENSE` for details.

---

## Appendix: Terms cheat sheet

- Constructible 1D persistence: finite critical set; p.f.d. on bounded windows
- `T_tau`: exact truncation removing all bars of length ≤ τ; idempotent; 1‑Lipschitz
- `C_tau`: filtered lift of `T_tau` up to f.q.i.; `P_i(C_tau F) ≅ T_tau(P_i F)`
- B–Gate⁺: PH1=0; Ext1=0 (eligible only under amplitude ≤ 1); `(mu,nu)=(0,0)`; `gap_tau > Σ delta`
- Overlap Gate: post‑collapse local-to-global gluing; Čech–Ext¹ on overlaps; stability band; δ‑overlap budget
- `(mu, nu)`: generic fiber dims of ker/coker of comparison map after truncation; Type IV if nonzero
- Stability band: τ‑range with `(mu,nu)=(0,0)` stable under sweep refinement
- PF/BC comparator: PF/BC applied after `T_tau` on the same window/τ
- A/B soft‑commuting: test Δ_comm ≤ η; else fallback and log Δ_comm as δ^{alg}
- Lambda_len: windowed clipped-length operator; isomorphism‑invariant after truncation
