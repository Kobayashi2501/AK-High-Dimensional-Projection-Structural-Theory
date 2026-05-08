# AK–HDPST v18 — AK High-Dimensional Projection Structural Theory

> **AK–HDPST v18: an auditable collapse-oriented proof interface framework**  
> **Core**: windowed barcode evaluation over one-parameter constructible persistence  
> **Interface**: external-domain conclusions require explicit soundness bridges  
> **Platform**: search, AI assistance, proof stores, DAGs, and replay are audit infrastructure, not proof

This repository contains **AK–HDPST v18**, the repaired v18-series architecture of AK High-Dimensional Projection Structural Theory.

AK–HDPST v18 is **not** presented as a universal solver for major conjectures.

It is a structured framework for:

- projecting external mathematical objects into Core-readable persistence data,
- evaluating collapse through windowed and thresholded barcode profiles,
- tracking tower failures through declared comparison artifacts,
- separating Core verification from external-domain theorem claims,
- managing AI-assisted search, proof candidates, bridge programs, proof stores, and reproducibility records.

The central v18 principle is:

```text
Core pass does not imply an external theorem without a proved bridge.
```

---

## Repository file structure

```text
.
├─ OLD/
│  └─ ...                                  # historical snapshots; may contain obsolete claims
├─ AK-HDPST_v18/
│  ├─ AK_HDPST_v18.tex                     # XeLaTeX source
│  └─ AK_HDPST_v18.pdf                     # compiled PDF
├─ Appendices/
│  ├─ Appendix_A_to_Z/
│  ├─ Appendix_NS/
│  ├─ Appendix_MS/
│  └─ Appendix_AGI/
├─ Companions/
│  ├─ Companion_1_Arithmetic_Calibration.md
│  └─ Companion_2_Execution_Reproducibility.md
└─ README.md
```

Actual file names may vary depending on the release package.

---

## What v18 is

AK–HDPST v18 is a repaired architecture built around strict claim separation.

Every major statement should be classified as one of:

```text
Core definition
Core theorem
Interface definition
Bridge candidate
Bridge theorem
Spec
Operational policy
Search artifact
Companion template
Non-claim
```

The purpose is to prevent the following invalid jump:

```text
high-dimensional projection
  -> collapse-like behavior
  -> external conjecture solved
```

In v18, the valid route is stricter:

```text
external object
  -> declared realization
  -> Core-readable persistence object
  -> windowed evaluation
  -> gate / diagnostic / ledger check
  -> Core verdict
  -> external theorem only if a bridge theorem is proved
```

---

## Core evaluation in v18

The central repaired Core object is the windowed, thresholded barcode evaluation:

```text
Eval(i, W, tau; F)
  = T_bar_tau( W_W P_i(F) )
```

Informally:

- `F` is a filtered or persistence-derived object.
- `P_i(F)` is the degree `i` persistence profile.
- `W_W` means restriction to a declared window `W`.
- `T_bar_tau` deletes barcode intervals of length `<= tau`.
- `Eval(i,W,tau;F)` is the repaired Core-visible profile.

The preferred lightweight notation in this README is:

```text
Eval_{i,W,tau}(F)
```

---

## Repaired Core primitives

### 1. Windowed barcode evaluation

```text
Eval_{i,W,tau}(F)
```

This is the primary Core-readable object used for collapse evaluation.

---

### 2. Admissible representative

```text
C_{tau,W}F
```

This is not a global strict filtered lift.

It is an admissible representative used only when the required compatibility and eligibility conditions are declared.

---

### 3. Tower comparison artifact

```text
phi_{i,W,tau}
```

This replaces older informal “after-collapse comparison map” language.

The intended schematic form is:

```text
phi_{i,W,tau}:
  ColimProfile_{i,W,tau}(F_bullet)
    -> ApexProfile_{i,W,tau}(F_infty)
```

---

### 4. Type IV diagnostics

```text
(mu_Collapse, nu_Collapse)
```

These are monitored tower diagnostics derived from the declared tower comparison artifact.

A clean diagnostic state is written as:

```text
(mu_Collapse, nu_Collapse) = (0,0)
```

---

### 5. Ledger budget

```text
Sigma_delta < gap_tau
```

This is the audit budget condition.

It records whether accumulated defects remain below the declared gap.

---

## Core pass in v18

A Core pass is a statement about the Core-readable object only.

A typical v18 Core pass may require:

```text
Eval_{1,W,tau}(F) = 0
```

```text
Ext^1 = 0 only in the eligible regime
```

```text
(mu_Collapse, nu_Collapse) = (0,0)
```

```text
Sigma_delta < gap_tau
```

```text
required artifacts and manifest records are present
```

A Core pass does **not** automatically imply:

```text
Navier-Stokes regularity
BSD
ABC
RH
Iwasawa main conjecture
Langlands theorem
Fukaya or mirror theorem
cryptographic security
```

Those require separate bridge theorems.

---

## Core vs Interface vs Spec

### Core

The Core layer contains theorem-grade internal statements about:

- constructible one-parameter persistence,
- windowed barcode evaluation,
- threshold deletion,
- admissible representatives,
- eligible use of `Ext^1`,
- tower diagnostics,
- ledger budget checks,
- gate verdicts,
- manifest requirements.

---

### Interface

The Interface layer defines how external domains may connect to the Core.

Examples:

- arithmetic interfaces,
- Iwasawa tower interfaces,
- Navier-Stokes interfaces,
- mirror / categorical interfaces,
- Fukaya-side interfaces,
- cryptographic interfaces.

An interface may define a route into the Core, but it does not prove an external theorem by itself.

---

### Spec

`[Spec]` marks a proposed, exploratory, or conditional component.

A `[Spec]` statement is not a theorem.

```text
[Spec] != theorem
```

---

## Bridge discipline

The most important v18 rule is:

```text
Bridge Program != Bridge Theorem
```

A bridge theorem is required whenever one wants to move from:

```text
Core-visible condition
```

to:

```text
external-domain conclusion
```

or from:

```text
external-domain structure
```

to:

```text
Core-readable behavior
```

A bridge candidate must remain marked as candidate or `[Spec]` until proved.

---

## Problem Interface Appendices

The v18 appendices are not written as solved-problem appendices.

They are **Problem Interface Appendices**.

Their function is to specify:

```text
external source data
realization route
Core-readable target
Eval_{i,W,tau}
C_{tau,W}F if needed
phi_{i,W,tau} if tower diagnostics are used
ledger treatment
bridge status
explicit non-claims
```

---

### Navier-Stokes appendices

The Navier-Stokes appendices are organized as:

```text
NS-A: Exploration Protocol
NS-B: Theoretical Soundness Layer
NS-C: Proof-First Program
```

They do not prove Navier-Stokes regularity.

Their purpose is to state what would be required before a Core pass could be interpreted as a PDE theorem.

---

### Arithmetic / MS appendices

The arithmetic-facing appendices organize:

```text
arithmetic source data
cyclotomic and Iwasawa towers
congruence defects
Selmer-like structures
mirror / categorical comparison
Fukaya-side calibration
```

They do not prove BSD, ABC, RH, or Iwasawa main conjectures.

---

### AGI / normalization appendices

The AGI-facing appendices define normalization, platform, and interface behavior.

They do not turn AI output into proof.

---

## Search / Platform layer

Appendices U-Z define the Search / Platform layer.

This layer supports:

```text
agents
search protocols
bridge programs
validity maps
certificate DAGs
proof stores
execution records
reproducibility manifests
```

It does not enlarge the Core.

---

## Main non-confusion rules

```text
AI output != proof
```

```text
Search result != theorem
```

```text
Bridge Program != Bridge Theorem
```

```text
Validity Map != proof
```

```text
Certificate DAG != proof by existence
```

```text
Proof Store storage != certification
```

```text
Execution != proof
```

```text
Replay pass != theorem validity
```

```text
R5 reproducibility != theorem validity
```

```text
Core pass != external theorem without a proved bridge
```

---

## Companion documents

### Companion 1: Arithmetic Calibration Companion

Companion 1 provides operational templates for arithmetic calibration.

It includes templates for:

```text
arithmetic source records
cyclotomic tower calibration
Iwasawa module calibration
congruence defect records
arithmetic ledgers
Type IV proxy records
bridge calibration records
mirror / categorical calibration
Fukaya-side calibration
```

Important rule:

```text
mu_Iw != mu_Collapse by default
```

Companion 1 is operational support, not an arithmetic theorem source.

---

### Companion 2: Execution / Reproducibility Companion

Companion 2 provides execution and reproducibility templates.

It includes templates for:

```text
run.yaml
artifact_manifest.json
eval.json
ledger.json
diagnostics.json
gate.json
proof_store_entry.json
reproducibility_manifest.json
verification records
audit records
R0-R5 reproducibility checklist
```

Important rule:

```text
Execution and reproducibility templates are operational aids, not proofs.
```

---

## Conceptual run protocol

A v18 execution should follow the repaired order:

```text
external data
  -> realization
  -> persistence profile
  -> window restriction
  -> threshold barcode deletion
  -> Eval_{i,W,tau}
  -> gate / diagnostic / ledger
  -> manifest / proof-store / replay
  -> Core verdict
```

External theorem interpretation requires an additional step:

```text
Core verdict
  -> proved bridge theorem
  -> external-domain conclusion
```

---

## Suggested execution artifacts

```text
out/artifacts/
  eval/
    eval_W0_deg1_tau.json
  representatives/
    C_tau_W_F_record.json
  diagnostics/
    diagnostics_W0_deg1_tau.json
  tower/
    phi_i_W_tau.json
  ledger/
    ledger_W0.json
  gate/
    gate_W0.json
  proof_store/
    proof_store_entry.json
  replay/
    reproducibility_manifest.json
  checksums/
    checksums.txt
```

Artifact existence alone does not imply proof.

---

## Example `run.yaml` schema

```yaml
meta:
  name: "demo-v18"
  version: "18"
  seed: 1337

data:
  input: "data/example.h5"
  backend: "bars"
  degrees: [0, 1]

windows:
  - label: "W0"
    range: "[0.0, 0.5)"
  - label: "W1"
    range: "[0.5, 1.0)"

threshold:
  tau: 0.15
  deletion_policy: "delete bars of length <= tau"

evaluation:
  expression: "Eval_{i,W,tau}(F)"
  records:
    enabled: true
    output: "out/artifacts/eval/"

representative:
  use_C_tau_W_F: false
  record: null

tower_diagnostics:
  enabled: true
  artifact: "phi_{i,W,tau}"
  output: "out/artifacts/diagnostics/"

ledger:
  enabled: true
  condition: "Sigma_delta < gap_tau"
  gap_tau: 0.03
  output: "out/artifacts/ledger/"

gate:
  type: "B-Gate+"
  require:
    Eval_1_zero: true
    Ext1_zero_if_eligible: true
    TypeIV_clean: true
    budget_pass: true

audit:
  outputs:
    - "eval"
    - "diagnostics"
    - "ledger"
    - "gate"
    - "checksums"
  checksums: "sha256"

non_claims:
  - "Successful execution is not proof by itself."
  - "Replay pass is not theorem validity."
  - "Core pass does not imply external theorem without a proved bridge."
```

---

## Example `eval.json`

```json
{
  "evaluation": {
    "id": "eval-0001",
    "input_object": "F",
    "degree": 1,
    "window": "W0",
    "threshold": "tau=0.15",
    "expression": "Eval_{i,W,tau}(F)",
    "barcode_policy": "delete bars of length <= tau",
    "result": "zero / nonzero / pending",
    "status": "candidate / computed / verified / failed",
    "non_claims": [
      "The existence of eval.json does not imply evaluation correctness.",
      "Evaluation summary is not audit-sufficient without reconstructible data."
    ]
  }
}
```

---

## Example `diagnostics.json`

```json
{
  "diagnostics": {
    "id": "diag-0001",
    "diagnostic_type": "TypeIV",
    "tower_artifact": "phi_{i,W,tau}",
    "source_profile": "ColimProfile_{i,W,tau}(F_bullet)",
    "target_profile": "ApexProfile_{i,W,tau}(F_infty)",
    "mu_Collapse": "value_or_pending",
    "nu_Collapse": "value_or_pending",
    "verdict": "clean / obstructed / pending / failed",
    "non_claims": [
      "A Type IV proxy is not a monitored Type IV diagnostic.",
      "A monitored diagnostic requires a declared phi_{i,W,tau} artifact."
    ]
  }
}
```

---

## Example `ledger.json`

```json
{
  "ledger": {
    "id": "ledger-0001",
    "components": [
      {
        "symbol": "delta_disc",
        "source": "discretization",
        "value_or_bound": "declared"
      },
      {
        "symbol": "delta_bridge",
        "source": "bridge transfer",
        "value_or_bound": "declared"
      }
    ],
    "aggregate": {
      "Sigma_delta": "computed_or_declared",
      "gap_tau": "declared",
      "condition": "Sigma_delta < gap_tau",
      "result": "pass / fail / pending"
    },
    "non_claims": [
      "The existence of ledger.json does not imply budget pass.",
      "Budget pass does not replace B-Gate+ or diagnostics."
    ]
  }
}
```

---

## Example `gate.json`

```json
{
  "gate": {
    "id": "gate-0001",
    "type": "B-Gate+",
    "clauses": [
      {
        "statement": "Eval_{1,W,tau}(F) = 0",
        "result": "pass / fail / pending"
      },
      {
        "statement": "Ext1 = 0 in eligible regime",
        "result": "pass / fail / not_applicable / pending"
      },
      {
        "statement": "Type IV diagnostics clean using phi_{i,W,tau}",
        "result": "pass / fail / pending"
      },
      {
        "statement": "Sigma_delta < gap_tau",
        "result": "pass / fail / pending"
      }
    ],
    "final_verdict": "pass / fail / pending / blocked",
    "non_claims": [
      "The existence of gate.json does not imply gate pass.",
      "Clause-level support is required."
    ]
  }
}
```

---

## What changed from v17.x to v18

### Conceptual change

v17.x framed AK-HDPST as an exploration OS with Core / Spec separation.

v18 repairs and strengthens this into:

```text
an auditable collapse-oriented proof interface framework
```

The main shift is:

```text
from:
  truncation-first exploration OS

to:
  windowed Core evaluation + explicit bridge discipline + proof governance
```

---

### Core notation change

Older language:

```text
T_tau
C_tau
after-collapse comparison map
DiagZero
```

v18 preferred language:

```text
Eval_{i,W,tau}(F)
C_{tau,W}F
phi_{i,W,tau}
(mu_Collapse, nu_Collapse) = (0,0)
Sigma_delta < gap_tau
```

---

### Claim-status change

v18 requires explicit status separation:

```text
Core theorem
Interface definition
Bridge candidate
Bridge theorem
Spec
Operational policy
Search artifact
Non-claim
Companion template
```

---

### Platform change

v18 adds a clearer governance shell:

```text
Agent Semantics
Hunter / Mapper / Lifter Protocols
Bridge Programs
Validity Map and Certificate DAG
AI Platform and Proof Store
Execution and Reproducibility Schema
```

---

## Roadmap after v18

The recommended next steps are not to add more broad appendices.

The next work should focus on small, verifiable strengthening.

---

### Priority 1: AK v18 Claim Register

Create a register of all claims, definitions, bridges, specs, and non-claims.

```text
Goal:
  prevent Spec / theorem / bridge confusion
```

---

### Priority 2: Core Micro-Theorem Pack

Prove small Core results about:

```text
window restriction compatibility
threshold deletion idempotence
deletion-type monotonicity
gap stability
ledger-safe perturbation
```

---

### Priority 3: Arithmetic Toy Bridge Pack

Build a finite or toy Iwasawa-like tower and prove a small bridge:

```text
eventual tower stability
  -> clean AK tower diagnostic
```

---

### Priority 4: Iwasawa Interface Skeleton

Prepare the real arithmetic route:

```text
Iwasawa tower
Selmer complex
p-adic structure
Core-readable realization
phi_{i,W,tau}
mu_Iw / mu_Collapse separation
```

---

### Priority 5: Bridge Theorem Workbench

Create templates for promoting:

```text
Bridge Candidate -> Bridge Theorem
```

---

### Priority 6: Minimal Formal Governance Core

Formalize the governance layer first:

```text
Spec cannot be used as theorem
Bridge Program cannot discharge Bridge Theorem
Stored object is not verified object
Core pass does not imply external theorem without bridge
```

---

## Installation

The following is illustrative.

```bash
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e ".[all]"
```

Actual package layout may vary.

---

## Quickstart

The following commands are illustrative.

```bash
# Prepare a v18 run configuration
cp examples/v18/minimal/run.yaml ./run.yaml

# Execute a repaired evaluation / diagnostics / ledger pipeline
akhdpst run run.yaml

# Inspect Core-facing records
akhdpst audit out/artifacts --by-window
```

---

## Minimal Python API

Illustrative only.

```python
from akhdpst.eval import eval_window_threshold
from akhdpst.diagnostics import compute_typeIV
from akhdpst.ledger import check_budget
from akhdpst.gate import b_gate_plus

F = load_filtered_object("data/example.h5")

tau = 0.15
W = (0.0, 0.5)
degree = 1

# Repaired windowed evaluation
E = eval_window_threshold(F, degree=degree, window=W, tau=tau)

# Declared tower diagnostic using phi_{i,W,tau}
mu, nu = compute_typeIV(
    tower="declared_tower",
    degree=degree,
    window=W,
    tau=tau,
    artifact="phi_i_W_tau.json"
)

# Ledger budget check
budget_ok = check_budget(
    sigma_delta=0.011,
    gap_tau=0.030
)

# Gate check
ok = b_gate_plus(
    eval_1_zero=E.is_zero(),
    ext1_zero_if_eligible=True,
    typeIV_clean=(mu == 0 and nu == 0),
    budget_ok=budget_ok
)
```

---

## Contributing policy

Contributions should preserve v18 non-confusion rules.

### Required

- Mark claim status explicitly.
- Separate Core, Interface, Bridge, Spec, and Operational claims.
- Do not treat AI output as proof.
- Do not treat stored artifacts as certified.
- Do not treat reproducibility as theorem validity.
- Use `Eval_{i,W,tau}`, `C_{tau,W}F`, and `phi_{i,W,tau}` consistently.
- Include ledger treatment for defects.
- Include non-claim clauses for examples and templates.

### Not allowed

```text
Spec -> theorem without proof
Bridge Program -> Bridge Theorem without proof
Core pass -> external theorem without bridge
Storage -> certification
Replay pass -> theorem validity
AI confidence -> proof
```

---

## Citation template

```text
AK-HDPST v18:
AK High-Dimensional Projection Structural Theory,
an auditable collapse-oriented proof interface framework.

Author: Atsushi Kobayashi
Year: 2026
Repository / DOI: insert URL or DOI
```

---

## License

```text
MIT
```

See `LICENSE`.
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20078142.svg)](https://doi.org/10.5281/zenodo.20078142)

---

## Terms cheat sheet

```text
Eval_{i,W,tau}(F)
  Windowed, thresholded barcode evaluation.

C_{tau,W}F
  Admissible representative used only under declared compatibility.

phi_{i,W,tau}
  Declared tower comparison artifact.

mu_Collapse, nu_Collapse
  Monitored Type IV tower diagnostics.

Sigma_delta < gap_tau
  Ledger budget condition.

B-Gate+
  Core gate using repaired evaluation, eligible Ext clause if invoked,
  Type IV diagnostics, and ledger budget.

Bridge Candidate
  Proposed cross-layer implication, not yet theorem.

Bridge Theorem
  Proved cross-layer implication.

Bridge Program
  Proof-management program for bridge candidates, not theorem.

Validity Map
  Navigation and status map, not proof.

Certificate DAG
  Dependency structure, not proof by existence.

Proof Store
  Storage and registry infrastructure, not certification.

Replay pass
  Reproducibility result, not theorem validity.

Spec
  Explicitly non-theorem exploratory or conditional statement.
```

---

## Final v18 statement

AK-HDPST v18 should be read as:

```text
A framework for making collapse-based projection, persistence evaluation,
tower diagnostics, bridge programs, and proof-management infrastructure
auditable without confusing exploration, storage, execution, or Core pass
with external theorem proof.
```

The shortest summary is:

```text
AK-HDPST v18 is not a universal solver.
It is an auditable proof-interface framework for collapse-oriented exploration.
```
