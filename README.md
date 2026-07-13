# AK-HPDST v19.0.0

## AK High-Dimensional Projection Structural Theory

> **A typed and auditable framework for projecting mathematical structures into persistence data, evaluating thresholded collapse, diagnosing failures, and controlling the route from internal evidence to external theorem claims.**

**Author:** Atsushi Kobayashi  
**Release:** v19.0.0 — Threshold-Gap Metric Repair Release  
**Status:** Research framework with a proved Core, conditional interfaces, toy bridges, search infrastructure, and explicit non-claims

---

## 1. Beginner's overview

AK-HPDST studies complicated mathematical structures by converting selected information into **persistent-homology profiles**, represented by barcodes.

A barcode contains intervals (“bars”). Informally:

- a long bar represents a feature that persists across a wide range;
- a short bar represents a feature that disappears quickly;
- an infinite bar represents a feature that survives indefinitely in the unwindowed profile.

AK-HPDST does not simply delete short bars and declare success. It records:

1. what external object was used;
2. how it was converted into Core-readable persistence data;
3. which window and threshold were selected;
4. which bars were retained or deleted;
5. whether the result is stable under the declared comparison error;
6. whether representatives, morphisms, tower data, and other non-numerical evidence exist;
7. which claim is proved, conditional, operational, speculative, rejected, or merely historical.

The central safety rule is:

> **A Core pass is not an external-domain theorem unless a separate Interface or Bridge Theorem has been proved.**

---

## 2. What AK-HPDST v19.0.0 can do

Within its declared hypotheses and data types, v19.0.0 can:

- convert suitable filtered objects into constructible one-parameter persistence profiles;
- restrict a profile to a declared window before threshold processing;
- delete finite bars whose lengths are at most a chosen threshold;
- certify when that hard deletion is stable under a bottleneck-distance perturbation;
- distinguish exact comparisons from metric comparisons;
- record admissible filtered representatives of repaired persistence profiles;
- derive a **one-way** degree-one implication from persistent vanishing to an `Ext^1` vanishing statement in the eligible realization regime;
- compare a directed tower with its declared apex using an actual comparison morphism;
- detect terminal-generic kernel and cokernel defects through Type IV diagnostics;
- manage overlap, continuation, and restart records for local-to-global analysis;
- classify failures into typed categories rather than reporting only “success” or “failure”;
- generate immutable manifests, claim references, proof-object records, and replay data;
- use human or AI search aggressively while keeping search output outside the proof verdict until independently verified.

AK-HPDST is therefore best understood as a **proof-interface and certification architecture**, not as an automatic conjecture solver.

---

## 3. What AK-HPDST v19.0.0 does not claim

This release does **not** prove, by itself:

- the Navier–Stokes regularity problem;
- the Riemann hypothesis;
- the Birch and Swinnerton-Dyer conjecture;
- the ABC conjecture;
- an Iwasawa main conjecture;
- a Langlands correspondence;
- mirror symmetry or a Fukaya-category equivalence;
- a cryptographic security theorem;
- a universal equivalence between persistent homology and `Ext` groups.

In particular, v19.0.0 does not assert the unconditional equivalence

$$
PH_1 = 0 \quad\Longleftrightarrow\quad \operatorname{Ext}^1 = 0.
$$

The currently proved Core direction is conditional and one-way:

$$
\operatorname{Eval}_{1,W,\tau}(F)=0
\quad\Longrightarrow\quad
\operatorname{Ext}^1\!\left(R(C_{\tau,W}F),k\right)=0,
$$

only when the admissible representative, realization, amplitude, and edge-eligibility requirements are satisfied.

---

## 4. The main processing flow

```text
External mathematical object
        |
        v
Declared realization or extraction
        |
        v
Core-readable filtered / persistence object
        |
        v
Persistence profile P_i(F)
        |
        v
Window restriction W_W P_i(F)
        |
        v
Hard threshold deletion T^bar_tau
        |
        v
Repaired evaluation Eval_{i,W,tau}(F)
        |
        +--> exact or metric-gap-certified comparison
        +--> admissible representative / eligible Ext-edge
        +--> overlap, continuation, and restart records
        +--> tower comparison and Type IV diagnostics
        |
        v
B-Gate+ and typed audit
        |
        v
Core verdict: pass / reject / undefined / not_invoked
        |
        v
External conclusion only through a proved Interface or Bridge Theorem
```

---

## 5. Minimal mathematical model

### 5.1 Working persistence regime

The Core works primarily with constructible one-parameter persistence modules over a field $k$:

$$
\operatorname{Pers}^{\mathrm{cons}}_k
\subset
[(\mathbb{R},\leq),\operatorname{Vect}_k].
$$

This restriction matters. Wild, uncontrolled, infinite-rank, or genuinely multiparameter data are not automatically Core-readable.

### 5.2 Window-first evaluation

For a filtered object $F$, degree $i$, right-open window $W=[u,u')$, and threshold $\tau>0$, define the pre-threshold profile

$$
B_{i,W}(F):=\mathcal{W}_W P_i(F),
$$

and the repaired evaluation

$$
\operatorname{Eval}_{i,W,\tau}(F)
:=
T^{\mathrm{bar}}_{\tau}\!\left(B_{i,W}(F)\right)
=
T^{\mathrm{bar}}_{\tau}\!\left(\mathcal{W}_W P_i(F)\right).
$$

The order is fixed:

$$
\text{persistence} \;\longrightarrow\; \text{window} \;\longrightarrow\; \text{threshold deletion}.
$$

Windowing and deletion do not commute in general.

### 5.3 Hard threshold deletion

For a barcode $B$,

$$
T^{\mathrm{bar}}_{\tau}(B)
:=
\{I\in B\mid \ell(I)>\tau\text{ or }\ell(I)=+\infty\}.
$$

Thus:

- finite bars with $\ell(I)\leq\tau$ are deleted;
- finite bars with $\ell(I)>\tau$ are retained;
- infinite bars are retained before bounded-window clipping.

The operation is idempotent:

$$
T^{\mathrm{bar}}_{\tau}
T^{\mathrm{bar}}_{\tau}(B)
=
T^{\mathrm{bar}}_{\tau}(B).
$$

However, hard deletion is **not globally non-expansive** under the standard bottleneck metric.

---

## 6. The main v19 repair: threshold-gap-safe stability

The major correction in v19.0.0 is the rejection of global non-expansiveness for positive-threshold hard deletion.

Define threshold clearance by

$$
\operatorname{clear}_{\tau}(B)
:=
\inf_{I\in B_{\mathrm{fin}}}
|\ell(I)-\tau|,
$$

with $\operatorname{clear}_{\tau}(B)=+\infty$ when $B$ has no finite bars.

For a finite family $\mathcal{B}$,

$$
\operatorname{gap}_{\tau}(\mathcal{B})
:=
\min_{B\in\mathcal{B}}
\operatorname{clear}_{\tau}(B).
$$

The repaired stability theorem is:

> If $d_B(B,C)\leq\varepsilon$ and the finite bars of both $B$ and $C$ avoid the closed band $[\tau-\varepsilon,\tau+\varepsilon]$, then

$$
d_B\!\left(T^{\mathrm{bar}}_{\tau}B,T^{\mathrm{bar}}_{\tau}C\right)
\leq
\varepsilon.
$$

This is a **two-sided** certificate. Checking only one barcode is insufficient.

A ledger-based metric comparison must also establish

$$
\operatorname{val}_B(\mathfrak d_{\mathrm{met}})
<
\operatorname{gap}_{\tau}(\mathcal{B}),
$$

where the scalarized ledger value is proved to upper-bound the actual bottleneck discrepancy used by the comparison.

---

## 7. Core components

The following grouping is explanatory. It does not replace the formal chapter and appendix boundaries.

### Core A — Persistence and barcode layer

Creates the Core-readable persistence profile $P_i(F)$ and its barcode decomposition in the declared constructible one-parameter regime.

**Purpose:** represent structural persistence in a form that can be windowed, compared, and audited.

### Core B — Windowed projection layer

Restricts the profile to a declared window:

$$
B_{i,W}(F)=\mathcal{W}_W P_i(F).
$$

**Purpose:** examine a controlled region rather than treating all scales as one undifferentiated object.

**Important:** a bounded window may clip an infinite bar into a short finite bar.

### Core C — Collapse layer

Applies hard threshold deletion:

$$
\operatorname{Eval}_{i,W,\tau}(F)
=
T^{\mathrm{bar}}_{\tau}(B_{i,W}(F)).
$$

**Purpose:** remove finite bars at or below the threshold and retain the declared repaired profile.

**Important:** this is a barcode-level operation by default, not a global exact functor on all morphisms.

### Core D — Comparison and metric-safety layer

Every consumed comparison uses exactly one runtime mode:

- `exact` — an actual equality or persistence-profile isomorphism is proved;
- `metric_gap_certified` — a bottleneck bound and two-sided threshold-gap record are supplied;
- `not_compared` — no comparison inference belongs to the declared scope.

**Purpose:** prevent an exact statement, an approximate statement, and an absent comparison from being confused.

### Core E — Representative and Ext-edge layer

An admissible representative $C_{\tau,W}F$ may represent the repaired profile in declared degrees. In the eligible regime, the degree-one Core vanishing can discharge an `Ext^1` clause:

$$
\operatorname{Eval}_{1,W,\tau}(F)=0
\Longrightarrow
\operatorname{Ext}^1\!\left(R(C_{\tau,W}F),k\right)=0.
$$

**Purpose:** connect persistence-level vanishing to a derived-category statement without claiming an unconditional equivalence.

### Core F — Tower and Type IV diagnostic layer

For a directed tower and declared apex, Type IV requires an actual comparison morphism

$$
\phi_{i,W,\tau}:
\operatorname{ColimProfile}_{i,W,\tau}(F_{\bullet})
\longrightarrow
\operatorname{ApexProfile}_{i,W,\tau}(F_{\infty}).
$$

When terminal-tameness is established, define

$$
\mu_{i,W,\tau}
:=
\operatorname{tgdim}_W(\ker\phi_{i,W,\tau}),
$$

$$
\nu_{i,W,\tau}
:=
\operatorname{tgdim}_W(\operatorname{coker}\phi_{i,W,\tau}).
$$

A clean monitored state is

$$
(\mu_{\mathrm{Collapse}},\nu_{\mathrm{Collapse}})=(0,0).
$$

This excludes monitored terminal-generic kernel and cokernel defects. It does not automatically prove that the whole comparison morphism is an isomorphism.

### Core G — Gate, failure, and audit layer

`B-Gate+` combines the required clauses without cancellation.

A pass may require:

1. degree-one repaired vanishing;
2. valid comparison-mode records;
3. eligible `Ext^1` vanishing when the Ext clause is invoked;
4. Type IV either `not_invoked` by scope or `certified_zero` with valid artifacts;
5. a passing metric budget for metric comparisons;
6. all required non-scalar obligations;
7. a complete and consistent manifest with admissible claim use.

A favorable numerical margin cannot repair a missing representative, morphism, eligibility record, proof artifact, or claim-status record.

---

## 8. Failure taxonomy

Failures are nonexclusive. One run may have several failure types.

| Type | Meaning | Typical example |
|---|---|---|
| Type I | Topological failure | $\operatorname{Eval}_{1,W,\tau}(F)\neq 0$ |
| Type II | Categorical failure in the eligible regime | Invoked and well-typed $\operatorname{Ext}^1\neq 0$ |
| Type III | Operational, metric, representative, or functorial failure | Missing gap record, invalid comparison, missing morphism, undefined required diagnostic |
| Type IV | Tower-level terminal-generic obstruction | $(\mu_{\mathrm{Collapse}},\nu_{\mathrm{Collapse}})\neq(0,0)$ |
| Type V | Claim-status, provenance, or manifest failure | A Spec, AI output, rejected claim, or incomplete record is reported as theorem evidence |

Missing evidence is normally `undefined`; it must not be silently encoded as zero or pass.

---

## 9. Claim discipline

Every meaningful statement must be read at its registered strength.

Common roles include:

- Core definition;
- Core theorem or lemma;
- metric-repair theorem;
- operational policy;
- Interface definition or theorem;
- Bridge candidate, Bridge Program, or Bridge Theorem;
- toy bridge theorem;
- Search artifact;
- Companion template;
- Spec;
- explicit non-claim;
- deprecated or rejected claim.

The governing rules are:

```text
Registration is not proof.
Spec is not theorem.
Bridge Program is not Bridge Theorem.
AI output is not proof.
Execution is not proof.
Replayability is not mathematical truth.
Core pass is not an external theorem without a proved transport theorem.
```

When a source, register, summary, or implementation disagrees, the weaker safe interpretation governs until a new immutable repair is issued.

---

## 10. Document architecture

### Main — Chapters 1–8

The Main document defines the release-wide contract:

1. scope, claim discipline, and metric-repair contract;
2. barcode metrics, threshold deletion, and gap-safe stability;
3. windowed evaluation, comparison records, and representatives;
4. eligible realization and the one-way $PH_1\Rightarrow\operatorname{Ext}^1$ edge;
5. failure taxonomy and Type IV diagnostics;
6. window logic, overlap, $\kappa$-Restart, and record-level gluing;
7. typed audit semantics and Core sovereignty;
8. Core closure and the external Interface boundary.

### Foundation Appendices A–G

- **A:** barcode metric and threshold-gap repair;
- **B:** filtered representatives;
- **C:** eligible realization and canonical Ext-edge;
- **D:** tower diagnostics and terminal-generic Type IV defects;
- **E:** windows, overlaps, restart, and gluing;
- **F:** typed obligations, statuses, and dependency closure;
- **G:** canonical manifest schema, proof objects, and replayability.

### Technical Extension Appendices H–N

These develop advisory indicators, discretization, measurement, controlled commutation, transfer ledgers, quantale semantics, and higher-categorical extensions. They do not silently enlarge the proved Core.

### Problem Interface Appendices

These specify how external domains may attempt to enter the Core:

- arithmetic, cyclotomic, Iwasawa, congruence, mirror, and Fukaya-facing interfaces;
- normalization interfaces;
- Navier–Stokes exploration, soundness, and proof-first programs.

An interface defines a typed route. It is not an external theorem unless the required transport theorem is proved.

### Search / Platform Appendices U–Z

These govern:

- human, AI, tool, and platform agents;
- Hunter / Mapper / Lifter search workflows;
- Bridge Programs;
- validity maps and certificate DAGs;
- proof stores;
- execution and reproducibility schemas.

Search is proposer-side by default. Core verdicts are verifier-side.

### Claim Register, CM, TB, and Companion

- **CR-v19:** canonical claim identity, status, permitted use, and repair ancestry;
- **CM-v19:** reusable Core micro-theorems at their exact proved strength;
- **TB-v19:** deliberately restricted toy bridge theorems;
- **Companion:** operational calibration and execution templates, not theorem sources.

---

## 11. Repository guide

A typical v19.0.0 release package is organized as follows:

```text
.
├─ README.md
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
   └─ historical materials — non-normative and potentially incorrect
```

Actual paths may vary by package or branch. The versioned source artifact and Claim Register control the normative identity.

---

## 12. Recommended reading order

For a first reading:

1. this README;
2. Main Chapter 1 — scope and safety rules;
3. Main Chapter 8 — what is actually proved and what remains conditional;
4. Main Chapters 2–3 — windowing, threshold deletion, and metric repair;
5. Main Chapters 4–5 — Ext-edge and tower diagnostics;
6. Appendix A — detailed proof of threshold-gap-safe stability;
7. CR-v19 — exact claim status and permitted use;
8. other appendices according to the target domain.

For implementation or audit work, also read Appendices F, G, U, Y, Z, and the Companion.

---

## 13. A small conceptual example

Suppose a windowed barcode has finite bar lengths

$$
0.08,\quad 0.21,\quad 0.73
$$

and choose $\tau=0.20$.

Hard deletion removes the $0.08$ bar and retains the $0.21$ and $0.73$ bars.

However, the $0.21$ bar lies very close to the threshold. If a comparison error could change its length across $0.20$, the retained/deleted classification is not robust.

Therefore AK-HPDST asks for both:

1. a certified discrepancy bound $\varepsilon$;
2. a two-sided threshold gap larger than that bound.

The calculation is not interpreted as stable merely because the software produced a barcode.

---

## 14. Why the `OLD/` directory is retained

The historical materials are intentionally preserved as **repair ancestry and a warning against claim inflation**.

Some old documents may contain obsolete, unsupported, or overstrong formulations, including unconditional readings of

$$
PH_1=0=\operatorname{Ext}^1
$$

or an unrestricted equivalence between the two sides.

These statements are **not normative in v19.0.0**.

The `OLD/` directory exists to show:

- which claims were previously overextended;
- why the present one-way eligible bridge is narrower;
- why rejected claims must remain visible rather than being silently erased;
- how immutable repair ancestry supports mathematical and audit accountability.

Do not use `OLD/` material as current theorem evidence. Cite the v19.0.0 source and its Claim Register entry instead.

---

## 15. AI and automated search

AK-HPDST allows AI systems and automated tools to:

- propose realizations, windows, thresholds, and bridge candidates;
- search for counterexamples;
- rank proof routes;
- generate formalization candidates;
- build maps, DAGs, manifests, and replay records;
- critique or audit candidate arguments.

But the semantic boundary is strict:

```text
Generation != verification
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

AK-HPDST v19.0.0 provides a disciplined answer to the question:

> **How can a complex mathematical object be projected into a simpler persistence-based representation, processed by a controlled collapse operation, and then evaluated without confusing evidence, approximation, computation, and proof?**

Its central contribution is not a claim that every problem collapses. Its contribution is an architecture that makes the following distinctions explicit and auditable:

- projection versus preservation;
- short-bar deletion versus stable deletion;
- exact equality versus metric control;
- persistence vanishing versus derived vanishing;
- local profile agreement versus tower-level agreement;
- search output versus theorem evidence;
- Core certification versus external mathematical truth.

That separation is the foundation of the v19.0.0 release.
