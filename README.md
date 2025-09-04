# AK-HDPST v15.0 — AK High-Dimensional Projection Structural Theory

Two-layer, auditable proof framework for functorial collapse via higher-dimensional projections and controlled obstruction removal.

- Core: machine-checkable statements in 1D constructible persistence over a field
- [Spec]: safe extensions under explicit, auditable hypotheses, non-expansive after truncation

Repository status: research framework with reference APIs, run protocol, and audit artifacts. Strong guarantees are confined to the Core scope below.

---

## Key ideas at a glance

- Exact truncation `T_tau` deletes all bars of length <= tau; 1-Lipschitz for interleavings/bottleneck distance
- Filtered lift `C_tau` exists up to filtered quasi-isomorphism (f.q.i.) with `P_i(C_tau F) ~ T_tau(P_i F)`
- Collapse gate: use only the one-way implication PH1(F)=0 => Ext1(R(F),k)=0 under t-exact, amplitude <= 1
- Tower diagnostics: kernel/cokernel metrics `(mu, nu)` on comparison maps detect invisible limit failures
- Update policy: deletion-type are non-increasing after truncation; inclusion-type are non-expansive (stability-only)
- Reproducibility: windowed protocol, delta-ledger, B-Gate+ safety margin, versioned artifacts

---

## Table of contents

- Overview
- Scope and guarantees
- Concepts and components
- Installation
- Quickstart (CLI and Python API)
- Configuration (`run.yaml`)
- Workflows and examples
- Update policy (allowed operations)
- Auditing and artifacts
- Roadmap
- Contributing
- Citing and references
- License

---

## Overview

AK-HDPST v15.0 is a proof-oriented framework that separates:
- Core: what is proved and guaranteed (constructible 1D persistence over a field), and
- [Spec]: what is permitted as an extension under explicit, auditable hypotheses.

All comparisons are performed after truncation by `T_tau`, following the windowed protocol:
t -> persistence -> T_tau -> compare

This keeps stability guarantees tight and measurable and makes failures detectable via `(mu, nu)` on towers.

---

## Scope and guarantees

Strong claims are limited to:
- One-parameter, constructible persistence over a field k
- Exact Serre reflector `T_tau` removing bars of length <= tau; 1-Lipschitz
- Filtered lift `C_tau` up to f.q.i. with `P_i(C_tau F) ~ T_tau(P_i F)`
- One-way bridge only: PH1(F)=0 implies Ext1(R(F),k)=0 under t-exact realization with amplitude <= 1
- Tower diagnostics `(mu, nu)` computed from kernels/cokernels of comparison maps after truncation

We do not assert PH1 <-> Ext1 in general. No claims about BSD, RH, or Navier–Stokes.

---

## Concepts and components

- `T_tau` (exact truncation)
  - Exact reflective localization that deletes bars of length <= tau
  - 1-Lipschitz for interleaving/bottleneck distance in the constructible 1D range

- `C_tau` (filtered lift, up to f.q.i.)
  - Filtered chain-level lift, unique up to filtered quasi-isomorphism
  - Satisfies degreewise `P_i(C_tau F) ~ T_tau(P_i F)`

- Collapse gate and one-way bridge
  - `CollapseAdmissible(F)` holds if PH1(F)=0 and Ext1(R(F),k)=0
  - Proven implication used: PH1(F)=0 => Ext1(R(F),k)=0, under t-exact, amplitude <= 1

- Tower diagnostics
  - For a directed system `{F_n} -> F_infty`, define comparison maps after truncation
  - `(mu, nu)` are sums of dimensions of kernels/cokernels across degrees
  - `(mu, nu) != (0, 0)` witnesses limit failures not visible at finite levels

- Update policy (post-truncation)
  - Deletion-type: non-increasing for windowed persistence energies and spectral indicators
  - Inclusion-type: non-expansive (stability-only)
  - Spectral indicators are controlled by a fixed policy `(beta, M(tau), s)`; not invariants up to f.q.i.

- [Spec] layer
  - Pipelines (e.g., degeneration, arithmetic towers, tropical/mirror, Langlands-flavored, PDE regularization) are permitted only as non-expansive after truncation and audited by `(mu, nu)`
  - Derived/sheaf-theoretic and symplectic/Fukaya realizations included only with explicit projection-formula/base-change or action-filtration hypotheses

---

## Installation

This repository ships a reference Python package and CLI.

```bash
# 1) Clone
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

# 2) Create environment (recommended)
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3) Install
pip install -e ".[all]"
```

Optional extras:
- `.[viz]` for visualization backends
- `.[lean]` or `.[coq]` to install stubs for formalization workflows

---

## Quickstart

### Minimal CLI run

```bash
# Prepare a run configuration
cp examples/minimal/run.yaml ./run.yaml

# Execute the pipeline
akhdpst run run.yaml

# Inspect audit summary
akhdpst audit out/artifacts
```

### Minimal Python API

```python
from akhdpst.core import T_tau, C_tau, collapse_admissible
from akhdpst.audit import audit_tower
from akhdpst.io import load_filtered_complex

# Load a filtered chain complex
F = load_filtered_complex("data/example.h5")

# Truncate at tau
tau = 0.15
F_tau = C_tau(F, tau)  # chain-level lift (up to f.q.i.)
P_tau = {i: T_tau(F.persistence(i), tau) for i in [0,1,2]}

# Check collapse gate (one-way use)
ok = collapse_admissible(F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True)
print("CollapseAdmissible =", ok)

# Tower audit
tower = [F_t for F_t in ...]  # user-provided directed system
mu, nu = audit_tower(tower, tau=tau)
print("mu =", mu, "nu =", nu)
```

---

## Configuration (`run.yaml`)

A single file captures windows, tau, operations, delta-ledger, and gate conditions. All outputs carry cross-linked checksums for audit and reproducibility.

```yaml
# run.yaml
meta:
  name: "demo-v15.0"
  seed: 42
  version: "15.0"
  author: "your-name"

data:
  input: "data/example.h5"     # filtered complex or persistence representation
  backend: "bars"              # bars | chain
  degrees: [0, 1]              # degrees for diagnostics

windows:
  # Right-open intervals; non-overlapping; full coverage optional
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"                # chain-level lift (up to f.q.i.)
  reflector: "T_tau"           # persistence-level exact truncation

operations:
  policy:                       # monotonicity and stability policy
    type: "mixed"               # deletion | inclusion | mixed
    beta: 0.9
    M_tau: "auto"
    s: 2
  steps:
    - type: "deletion"
      op: "dirichlet_restriction"
      args: {nodes: [1, 5, 7]}
    - type: "inclusion"
      op: "add_edges"
      args: {pairs: [[2,3],[5,8]]}

spec:
  enabled: true
  items:
    - name: "mirror_transfer"
      hypotheses: ["nonexpansive_after_truncation", "delta_controlled_commutation"]
      delta_budget: 0.01
    - name: "projection_formula"
      hypotheses: ["base_change_ok", "window_protocol_ok"]
      delta_budget: 0.00

gate:
  # B-Gate+ safety margin per window
  require:
    PH1_zero: true
    Ext1_zero: true     # used only with t-exact realization, amplitude <= 1
    mu_zero: true
    nu_zero: true
    gap_tau_gt_sum_delta: true

audit:
  outputs: ["bars", "spec", "ext", "phi"]
  checksums: "sha256"
  restart: "summability"        # paste window certificates into global one

output:
  dir: "out/artifacts"
  overwrite: false
```

---

## Workflows and examples

### 1) Windowed protocol

- Always compare after truncation:
  - For each window t-range
  - Compute persistence
  - Apply `T_tau`
  - Compare maps and audit `(mu, nu)`

```bash
akhdpst run examples/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

### 2) Collapse gate check

- Gate conditions:
  - PH1(F)=0
  - Ext1(R(F),k)=0 (one-way inference from PH1(F)=0 under t-exact, amplitude <= 1)
  - mu=0 and nu=0 on towers
  - gap_tau > sum(delta) in each window

```bash
akhdpst gate check --run run.yaml --window w0
```

### 3) Spec pipeline with audit

- Spec steps must be non-expansive after truncation and must log delta to the ledger

```bash
akhdpst run examples/spec/mirror.yaml
akhdpst audit out/artifacts --show-delta-ledger
```

---

## Update policy (allowed operations)

The following rule-of-thumb holds after truncation:

| Update type | Examples | Guarantee after truncation |
| --- | --- | --- |
| Deletion-type | Dirichlet restriction; principal submatrix; PSD Loewner contraction; conservative averaging | Non-increasing (monotone) for windowed persistence energies and spectral indicators |
| Inclusion-type | Add cells; relax boundary conditions; attach handles | Non-expansive (stability-only) |

Notes:
- Spectral indicators on `L(C_tau F)` are not f.q.i.-invariants; they are controlled via the fixed policy `(beta, M(tau), s)`.
- Keep all Spec steps in the non-expansive regime and account for deltas in the ledger.

---

## Auditing and artifacts

All runs produce a reproducible set of artifacts with cross-linked hashes.

Directory layout (example):

```
out/artifacts/
  bars/
    w0_degree1_trunc.json
    w1_degree1_trunc.json
  spec/
    ledger_w0.json
    ledger_w1.json
  ext/
    Rw0_ext1.txt
  phi/
    maps_w0_degree1.h5
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/` contains truncated barcodes per window and degree
- `spec/` contains delta-ledger entries and hypotheses checks
- `ext/` contains Ext-related summaries where applicable
- `phi/` contains serialized comparison maps and `(mu, nu)` reports
- `audit_summary.json` aggregates gate outcomes and diagnostics
- `checksums.txt` lists SHA256 sums for all artifacts

---

## Command reference (CLI)

```bash
# Execute a configured run
akhdpst run run.yaml

# Audit an existing run directory
akhdpst audit out/artifacts

# Check B-Gate+ conditions per window
akhdpst gate check --run run.yaml --window w0

# Visualize truncated barcodes (ASCII)
akhdpst viz bars --dir out/artifacts --degree 1

# Print tower diagnostics
akhdpst diag tower --dir out/artifacts --degree 0
```

---

## Python API reference (selected)

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus
from akhdpst.audit import audit_tower, summarize_audit
from akhdpst.spec import run_spec_pipeline

# Exact truncation at persistence layer
P_trunc = T_tau(P, tau=0.2)

# Filtered lift (up to f.q.i.)
F_trunc = C_tau(F, tau=0.2)

# Gate checks (one-way bridge used internally; t_exact and amplitude flags required)
ok_gate = collapse_admissible(
    F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True
)
ok_bgate = b_gate_plus(window="w0", mu=0, nu=0, gap_tau=0.05, delta_sum=0.01)

# Tower diagnostics
mu, nu = audit_tower(tower=[F0, F1, F2, F_inf], tau=0.2, degrees=[0,1])

# Spec pipeline (non-expansive after truncation; delta-ledger enforced)
spec_out = run_spec_pipeline(F, items=[...], tau=0.2, ledger=ledger)
```

---

## Roadmap

- Formalization stubs and proofs (Lean, Coq) for reflectors, diagnostics, and gates
- Auto tau-sweep and stability-band detection
- GPU/parallel backends for large barcodes and filtered complexes
- Notebook templates for per-window audits and delta-ledger visualization
- Expanded Spec contracts for PDE and Fukaya categories (action-filtration tooling)

---

## Contributing

We welcome issues and pull requests:
- Keep Core and [Spec] separation explicit in code and docs
- Add or extend Spec items only with non-expansive-after-truncation checks and delta-ledger entries
- Include minimal examples and update `examples/` and `tests/`

Development commands:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## Citing and references

If you use AK-HDPST v15.0 in research, please cite:

```
AK–HDPST v15.0: Exact Truncation, Collapse Gate, and Auditable Spec Extensions
Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

Related foundational references:
- Crawley-Boevey (2015): Decomposition of pointwise finite-dimensional persistence modules
- Chazal, de Silva, Glisse, Oudot (2016): Structure and stability of persistence modules and barcodes

---

## License

This project is released under the MIT License. See `LICENSE` for details.

---

## Appendix: Terms cheat sheet

- Constructible 1D persistence: finite critical set; pointwise finite-dimensional on bounded windows
- `T_tau`: exact truncation removing all bars of length <= tau; 1-Lipschitz
- `C_tau`: filtered lift of `T_tau` up to f.q.i.; `P_i(C_tau F) ~ T_tau(P_i F)`
- Collapse gate: PH1(F)=0 and Ext1(R(F),k)=0 (one-way implication used only under stated conditions)
- B-Gate+: requires PH1=0, Ext1=0 (under conditions), mu=nu=0, and gap_tau > sum(delta)
- `(mu, nu)`: sums of kernel/cokernel dimensions of comparison maps after truncation; detect invisible limit failures
- Window protocol: t -> persistence -> T_tau -> compare; right-open, non-overlapping windows
- [Spec]: extensions that are non-expansive after truncation; all deltas recorded in the ledger and audited by `(mu, nu)`
