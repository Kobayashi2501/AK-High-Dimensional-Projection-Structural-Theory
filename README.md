# AK-HPDST v20.0.0

## AK High-Dimensional Projection Structural Theory

> A typed, auditable, and defect-aware framework for finite proof compression, higher obstruction transport, finite-to-infinite reduction, and certified Return from internal mathematical evidence to external theorem statements.

**Author:** Atsushi Kobayashi
**Release:** v20.0.0 - Finite Proof Compression, Higher Obstruction Bridges, and Problem Demonstration Release
**Status:** Public research release with a conservative v20 Core, finite detector theorems, higher Ext interfaces, exact Known-Theorem Recovery tracks, and v20-dependent HT and UB research appendices

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21330904.svg)](https://doi.org/10.5281/zenodo.21330904)

---

## 1. Beginner's overview

AK-HPDST studies whether selected information from a complicated mathematical object can be:

1. converted into a controlled persistence or filtered representation;
2. reduced to finite, reconstructible evidence;
3. transported through homological, derived, spectral-sequence, or tower constructions;
4. checked for information loss and hidden defects;
5. returned to the original mathematical domain at an explicitly declared strength.

The framework does not treat a finite computation, an AI-generated proof sketch, a stable-looking sequence, or a successful software run as a theorem by itself.

Its central safety rule is:

```text
Internal AK pass != external theorem
unless every realization, reduction, comparison, and Return arrow is proved.
```

The basic v20 question is therefore:

```text
Can an external mathematical statement be represented by finite typed evidence,
transported without silent information loss, and returned to its native meaning
through a complete and independently auditable proof chain?
```

AK-HPDST is not an automatic universal solver. It is a proof-compression, proof-transport, and proof-audit architecture.

---

## 2. Technical summary

The v20 Core works primarily with constructible one-parameter persistence modules over a field and with finite-type filtered objects whose monitored homology profiles are Core-readable.

For a filtered object `F`, degree `n`, window `W`, and threshold `tau`, the canonical repaired evaluation is:

```text
B(n, W; F) = Window(W, P_n(F))

Eval(n, W, tau; F)
    = T_bar(tau, B(n, W; F))
```

The order is fixed:

```text
persistence -> window -> threshold deletion
```

v20 then separates the following obligations:

```text
external source semantics
    -> purpose-faithful realization
    -> Core-readable profile
    -> finite detector certificate
    -> higher obstruction transport, when invoked
    -> finite-to-infinite reduction, when required
    -> Return theorem
    -> external conclusion
```

No later success compensates for a missing earlier arrow.

The main v20 extension beyond v19 is the addition of:

* complete finite detector certificates;
* family-relative proof compression and minimal-certificate analysis;
* no-go theorems for unrestricted finite detection;
* higher degree `PH_n -> Ext^n` transport under explicit eligibility;
* transient-defect detection separated from terminal Type IV diagnostics;
* exact finite-to-infinite reduction records;
* problem-facing Known-Theorem Recovery with benchmark quarantine;
* proof-first AI, search, platform, and artifact governance.

The release also includes two v20-dependent research appendices:

* **Appendix HT:** a unified higher-transfer and Return-composition layer;
* **Appendix UB:** a re-audited library of twelve validated mathematical success cases.

These appendices extend the research system around v20. They do not silently rewrite or enlarge the frozen v20 Core.

---

## 3. What AK-HPDST v20.0.0 can do

Within its declared hypotheses, source classes, and artifact requirements, v20.0.0 can:

* form window-first persistence profiles from suitable filtered objects;
* apply hard finite-bar threshold deletion;
* certify threshold stability using a two-sided bottleneck-gap condition;
* distinguish finite observation from a complete finite proof certificate;
* certify repaired-profile zero or nonzero through stage-correct detectors;
* state detector soundness and detector completeness as separate theorems;
* compute family-relative certificate sizes and minimal stencil bounds;
* prove when no uniform complete finite detector can exist;
* transport repaired vanishing to `Ext^n` vanishing in an eligible degree-`n` realization regime;
* use natural zero-reflection only when it is separately proved;
* compare towers through actual morphisms rather than object-level resemblance;
* separate terminal/cofinal defects from long transient and short interior defects;
* build local detector atlases with overlap, coverage, and Restart obligations;
* distinguish exact comparison, metric-gap-certified comparison, and valid non-comparison;
* manage finite-to-infinite reduction, apex agreement, and derived-limit defects;
* reconstruct exact known theorem statements through non-circular Interface-Core-Reduction-Return chains;
* preserve immutable source bindings, claim status, failure routes, artifacts, and repair ancestry;
* use AI, proof assistants, search agents, and platforms without granting them automatic theorem authority.

In practical terms, v20 can answer not only:

```text
Did a computation produce zero?
```

but also:

```text
What object was evaluated?
Was the finite test complete?
At which profile stage was it applied?
What information was discarded?
Was the comparison exact or metric?
Did the finite statement really control the infinite target?
At what strength can the result be returned externally?
```

---

## 4. What v20.0.0 does not claim

This release does not prove, by itself:

* the Riemann hypothesis;
* the Birch and Swinnerton-Dyer conjecture;
* the ABC conjecture;
* a general Iwasawa main conjecture;
* the general Leopoldt conjecture;
* the general Tachikawa conjecture;
* unconditional three-dimensional Navier-Stokes regularity;
* a Clay-level Navier-Stokes result;
* a Langlands correspondence;
* homological mirror symmetry or a Fukaya-category equivalence;
* a universal cryptographic security theorem;
* a universal equivalence between persistence and derived obstruction groups;
* a universal finite detector for uncontrolled right-unbounded or multiparameter data.

In particular, v20 does not assert the unrestricted equivalence:

```text
PH_n = 0 <-> Ext^n = 0
```

The default higher obstruction direction is narrower:

```text
Eval(n, W, tau; F) = 0
    -> Ext^n(A_n(F), k) = 0
```

This implication is available only when the declared degree-`n` realization, representative, edge extractor, cohomological identification, naturality requirements, and artifact package are all valid.

The reverse implication requires a separately proved zero-reflection or faithfulness theorem.

---

## 5. Main v20 processing flow

```text
External mathematical object
        |
        v
Source statement and immutable source binding
        |
        v
Purpose-faithful realization or one-parameter extraction
        |
        v
Core-readable filtered or persistence object
        |
        v
Windowed profile B(n, W; F)
        |
        v
Hard threshold deletion T_bar(tau)
        |
        v
Repaired evaluation Eval(n, W, tau; F)
        |
        +--> complete finite detector certificate
        +--> exact or metric-gap-certified comparison
        +--> admissible representative
        +--> eligible higher Ext edge
        +--> terminal and transient defect analysis
        +--> atlas, overlap, continuation, and Restart
        +--> finite-to-infinite reduction and apex agreement
        |
        v
Typed B-Gate+ audit
        |
        v
Internal status: pass / reject / undefined / not_invoked
        |
        v
External conclusion only through a proved Return theorem
```

No arrow is inferred merely from adjacency in a diagram, common filenames, AI agreement, numerical convergence, or successful compilation.

---

## 6. Core mathematical advances in v20

### 6.1 Finite observation versus finite proof

A finite list of samples, ranks, critical values, maps, or numerical outputs is not automatically a finite proof.

A finite detector certificate must include, as applicable:

* the exact source profile and source stage;
* endpoint or germ convention;
* detector soundness;
* detector zero-completeness;
* birth, germ, stencil, or coverage exhaustiveness;
* family membership;
* an independently sourced excess or mesh bound;
* immutable artifacts and replay information.

Missing evidence gives:

```text
undefined
```

It does not give:

```text
zero
pass
not_invoked
```

### 6.2 Proof compression and MinCert

v20 treats proof compression as a family-relative mathematical question.

```text
MinCert(family, W, tau)
```

is meaningful only after the information class, endpoint policy, critical-data rule, coverage theorem, and uniform lower-bound source are fixed.

Retrospectively listing every bar of one already-known object is not counted as nontrivial proof compression.

### 6.3 Right-unbounded no-go boundary

Without additional structure, no uniform finite detector can certify a right-unbounded family with unbounded possible birth positions.

A finite certificate on such a domain must use an explicit escape condition, for example:

* a finite-birth theorem;
* eventual constancy;
* a global support bound;
* compactness;
* a finite-state reduction;
* a valid finite-to-infinite theorem.

### 6.4 Higher obstruction edges

v20 extends the degree-one edge to higher degrees under a standard eligible package.

The Core direction is:

```text
repaired PH_n vanishing
    -> Ext^n vanishing
```

The framework does not manufacture a natural bridge by synthetically placing detector values inside a complex. A natural or external interpretation requires its own realization theorem.

### 6.5 Terminal and transient defect separation

For an actual comparison morphism, terminal Type IV diagnostics monitor cofinal kernel and cokernel behavior.

```text
(mu_Collapse, nu_Collapse) = (0, 0)
```

means no monitored terminal-generic defect was detected.

It does not automatically imply:

* no long transient defect;
* no short interior defect;
* full kernel or cokernel vanishing;
* full comparison isomorphism.

v20 therefore introduces separate transient-defect profiles and complete stage-correct defect detectors.

### 6.6 Finite-to-infinite reduction

A repeated finite pattern, numerical convergence, or a long stable prefix is not an infinite theorem.

A valid reduction must identify:

* the actual directed system;
* transition morphisms;
* the finite witness or stabilization theorem;
* the genuine colimit, inverse limit, completion, or authorized source object;
* the apex;
* the comparison morphism;
* the theorem proving apex agreement;
* any `lim^1`, compactness, or derived obstruction.

---

## 7. Known-Theorem Recovery in v20

v20 introduces a controlled way to demonstrate that the full AK chain can recover a frozen known theorem at exactly its source strength.

The benchmark theorem is quarantined from the construction. Its conclusion, proof, target constants, and conclusion-derived witnesses may not be inserted into the realization or certificate.

The final compact Claim Register records two exact-strength recovery tracks and a passed G16 release gate.

### 7.1 Iwasawa growth recovery

The Iwasawa track recovers the characteristic-growth clause of Iwasawa's 1959 theorem, relative to a registered precursor package.

The recovered tail form is:

```text
c(n; A) = lambda(A) * n + mu(A) * p^n + constant
```

for sufficiently large `n`.

The track separates:

* source-side module structure inputs;
* p-primary realization;
* signed defect profiles;
* bounded-window Core certification;
* finite-to-infinite tail reduction;
* exact Return;
* independent comparison with the quarantined benchmark.

It does not prove an Iwasawa main conjecture or a class-number theorem without a separate arithmetic interface.

### 7.2 Fixed-exponent Serrin recovery

The Navier-Stokes track recovers the fixed strict-subcritical implication:

```text
u in L^6_t L^6_x
    -> interior regularity
```

for the declared unforced three-dimensional Leray-Hopf regime.

The source conclusion is quarantined until the final Return arrow.

This is an exact criterion-level recovery, not a new analytic proof and not unconditional global regularity.

---

## 8. Appendix HT - Higher Transfer and Unified Bridge Composition

Appendix HT is a v20-dependent successor research appendix that integrates the former HC, PE, SS, RL, and IW/Return materials into one mathematical transport architecture.

Its role is:

```text
AK Core = what may be certified
HT      = how certified information may be transported and composed
```

### 8.1 The five HT transfer layers

#### HC - Homological compression

HC studies exact or controlled compression of filtered and homological data while protecting the declared persistence information.

It distinguishes:

* homology preservation;
* persistence-module preservation;
* barcode preservation;
* representative preservation;
* exactness and functoriality requirements.

#### PE - Persistence-Ext reconstruction

PE develops finite persistence-to-Ext interfaces, including:

* complete finite stencils;
* Ext signatures;
* Moebius reconstruction;
* barcode and object Return;
* morphism enhancement and boundary limitations.

#### SS - Spectral-sequence transfer

SS controls pagewise information, differentials, filtrations, edge maps, extension ambiguity, and abutment Return.

A spectral sequence is not assumed to degenerate merely because it exists.

#### RL - Inverse systems and derived limits

RL separates:

* finite-stage compatibility;
* ordinary inverse or direct limits;
* derived-limit defects such as `lim^1`;
* completion;
* apex agreement;
* external Return.

#### IW / Return Theory - Native target comparison

Return Theory defines what it means to return from compressed or transformed evidence to a native mathematical target.

Return is not automatically inversion.

It may occur at different strengths, such as:

* scalar Return;
* ideal-level Return;
* module-level Return;
* object-level Return;
* derived Return;
* regularized or leading-term Return.

A weaker Return is never silently promoted to a stronger one.

### 8.2 Unified HT composition

HT supplies common interface records, a unified defect stack, status precedence, and a conditional composition theorem.

The full chain has the schematic form:

```text
source
  -> compression
  -> persistence / Ext reconstruction
  -> spectral-sequence transfer
  -> inverse-limit control
  -> native Return
```

The conclusion is limited by the weakest proved arrow in the chain.

HT therefore converts previously separate mathematical techniques into one typed transport system without claiming that every chain is available for every external problem.

---

## 9. Appendix UB - Unified Bridge validation library

Appendix UB is the v20-dependent validated case library for bridge and Return constructions.

Its role is:

```text
HT = reusable transport architecture
UB = executed mathematical validation and regression library
```

The re-audited edition contains twelve success cases because VC7L is counted as an independent case.

### 9.1 Finite reconstruction and descent

UB validates:

* exact reconstruction of box-decomposable persistence data from finite rank probes;
* minimality within the declared additive scalar-probe class;
* finite-poset reconstruction of objects and morphisms through enriched projective probes;
* Return of kernels, cokernels, exact sequences, Yoneda classes, complexes, cones, and derived triangles;
* strict object and derived descent over finite Alexandrov spaces;
* finite Cech hypercohomology on declared principal-good covers.

### 9.2 Periodic homological obstruction

UB validates finite-degree projectivity detection for declared self-injective settings, including:

* truncated-cycle self-injective Nakayama algebras;
* representation-finite self-injective algebras through finite syzygy permutation;
* periodic and finite-twist-orbit self-injective settings;
* selected representation-infinite periodic families.

These are special-class results and known-theory reconstructions or refinements. They do not solve the general Tachikawa conjecture.

### 9.3 Galois and Leopoldt Return

UB validates:

* reconstruction of an `S_3` Leopoldt kernel from fixed-subfield data;
* finite proper-subfield zero certificates;
* Frobenius-group and odd-dihedral defect propagation;
* certified p-adic regulator nonvanishing for an explicit totally real cubic field at `p = 61`;
* Return of the resulting Leopoldt vanishing to its `S_3` Galois closure.

This is not a proof of the general Leopoldt conjecture.

### 9.4 Finite-state inverse limits

For declared finite-state towers, UB validates:

```text
inverse limit = stable image of period monodromy
lim^1 = 0
```

and gives finite certificates for:

* zero inverse limit;
* apex agreement;
* derived inverse limits;
* acyclicity;
* quasi-isomorphism of derived limits.

The finite-state hypothesis is essential.

### 9.5 p-adic L-functions and Iwasawa theory

UB validates the chain:

```text
compatible finite group-ring data
    <-> bounded measure
    <-> Iwasawa algebra element
    <-> power series
    -> finite-character specializations
```

It also supplies:

* finite-precision recovery bounds;
* branchwise Mellin evaluation;
* pseudomeasure and pole handling;
* certified nonvanishing and valuation records;
* finite cyclotomic obstruction scans;
* exact finite-layer growth formulas in declared square-presented classes;
* rank and reduced torsion formulas for declared cyclotomic-singular cyclic classes;
* Bockstein leading-term certificates.

These results do not prove a general main conjecture, explicit reciprocity law, or multivariable/noncommutative Iwasawa growth theorem.

### 9.6 Analytic compactness and continuation

UB validates a complete conditional route from approximation data to regularity under a declared Serrin bound:

```text
energy and time-derivative bounds
    -> compactness
    -> strong local convergence
    -> nonlinear defect removal
    -> finite Serrin time atlas
    -> regularity, uniqueness, and continuation
```

The missing unconditional step remains the generation of the global Serrin bound itself.

### 9.7 What UB demonstrates

UB does not claim that every displayed classical ingredient is new.

Its main mathematical demonstration is that one common proof-transport architecture can be executed across:

* persistence and representation theory;
* homological algebra;
* descent and derived categories;
* Galois and p-adic arithmetic;
* inverse limits and Iwasawa theory;
* analytic compactness and PDE continuation.

---

## 10. Core, HT, and UB

The three layers have different roles.

```text
AK v20 Core
    = admissible objects, certificates, statuses, gates, and audit rules

Appendix HT
    = reusable transport, composition, defect, and Return architecture

Appendix UB
    = validated mathematical cases and regression tests
```

HT and UB are logically connected but should not be confused.

* HT states reusable transfer principles.
* UB records where those principles were actually closed.
* A UB success case does not automatically become a universal HT theorem.
* An HT interface does not automatically prove an external problem.
* Neither appendix silently modifies the frozen v20 Core.

---

## 11. Failure and status semantics

The canonical atomic statuses are:

```text
pass
reject
undefined
not_invoked
```

They have different meanings.

* `pass`: every invoked requirement is proved or validly discharged;
* `reject`: a well-typed invoked condition is evidenced false;
* `undefined`: required evidence, typing, source identity, or an object is missing;
* `not_invoked`: the clause is outside the immutable declared scope.

Typical failure routes include:

* topological repaired-profile failure;
* categorical or higher-Ext failure;
* metric, comparison, coverage, or Restart failure;
* terminal Type IV defect;
* transient interior defect;
* finite-to-infinite or apex failure;
* Return-strength mismatch;
* source contamination or benchmark circularity;
* claim, provenance, artifact, or manifest failure.

One favorable numerical margin cannot repair a missing non-scalar obligation.

---

## 12. Claim and audit discipline

Every statement is used only at its registered strength.

Typical roles include:

* Core definition;
* Core theorem or lemma;
* Core micro-theorem;
* Interface theorem;
* Bridge candidate;
* Bridge Program;
* Bridge Theorem;
* toy bridge theorem;
* Search artifact;
* operational policy;
* successor-release candidate;
* Spec;
* explicit non-claim;
* deprecated or rejected claim.

The main rules are:

```text
Registration != proof
Finite data != finite certificate
Soundness != completeness
Realization != Return
Finite prefix != infinite reduction
Terminal zero != full defect zero
Characteristic ideal != exact module
Pseudo-isomorphism != isomorphism
Derived equivalence != preferred presentation
AI output != proof
Compilation != theorem validity
Replay != mathematical truth
Manifest completeness != mathematical truth
```

The final compact Claim Register records canonical source locators, permitted use, evidence status, and release-critical recovery claims without duplicating every theorem statement or artifact hash.

---

## 13. Document architecture

### Main - Chapters 1 to 8

The Main document defines the v20 release contract:

1. scope, claim discipline, and finite-certificate rules;
2. threshold-gap metric repair and repaired-zero transport;
3. finite detector calculus and proof compression;
4. higher obstruction edges;
5. terminal and transient defect analysis;
6. windows, atlases, coverage, continuation, and Restart;
7. typed audit semantics and manifest governance;
8. Core closure, problem demonstrations, finite-to-infinite reduction, and Return boundaries.

### Foundation Appendices A to G

* **A:** barcode metric, threshold-gap repair, and zero transport;
* **B:** finite detector certificates, representatives, and proof compression;
* **C:** eligible higher Ext edges and zero-reflection boundaries;
* **D:** tower diagnostics, terminal and transient defects;
* **E:** windows, overlap, coverage, atlas, and Restart;
* **F:** typed obligations, statuses, failure routes, and non-compensation;
* **G:** manifests, dependency closure, proof objects, semantic replay, and release records.

### Appendix CM-v20

A compact pack of reusable Core micro-theorems, including finite detector, higher Ext, transient-defect, Restart, and exact reduction results.

### Appendix TB-v20

A deliberately restricted toy bridge and counterexample pack. Toy success does not establish an external-domain theorem.

### Technical Extension Appendices H to N

These develop:

* advisory spectral indicators;
* discretization and continuum transfer;
* measurement separation;
* controlled commutation;
* Mirror/Transfer comparison;
* quantale and ledger semantics;
* derived, sheaf, stack, multiparameter, and higher-categorical extension discipline.

They surround the Core but do not silently enlarge it.

### Problem Interface Appendices

These provide typed interfaces for:

* arithmetic and Iwasawa structures;
* congruence and p-adic profiles;
* categorical and Mirror/Fukaya-facing structures;
* normalization and realization;
* Navier-Stokes exploration, soundness, and proof-first programs.

### Search / Platform Appendices U to Z

These govern:

* human, AI, proof-assistant, tool, platform, and hybrid agents;
* Hunter, Mapper, and Lifter workflows;
* counterexample and certificate search;
* proof stores and certificate DAGs;
* source binding and benchmark quarantine;
* execution, replay, staleness, and reproducibility.

### Appendix HT

The integrated higher-transfer and Return-composition appendix.

### Appendix UB

The re-audited twelve-case validated bridge and Return library.

### Claim Register and Companion

* **CR-v20:** compact canonical claim-governance and release-closure index;
* **Companion:** operational calibration templates and examples, not theorem sources.

---

## 14. Repository guide

A typical v20.0.0 package is organized as follows:

```text
.
|-- README.md
|-- README_JA.md
|-- AK_HPDST_v20_0_0_PartI__Main.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part_II__Foundation_Appendices.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part_III__Technical_Extension_Appendices.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__IV__Problem_Interface_Appendices.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__V__Search_Platform_Appendices.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__Claim_Register.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__CM.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__TB.pdf
|-- AK_HPDST_v20_0_0_Appendix_Part__Companion.pdf
|-- AK_HPDST_v20_0_0_Appendeix_HT.pdf
|-- AK_HPDST_v20_0_0_Appendeix_UB.pdf
|-- source-binding and recovery-manifest files
`-- OLD/
   `-- historical materials - non-normative repair ancestry
```

Actual filenames and paths may vary by package or repository branch.

The versioned source artifacts, exact theorem locators, Claim Register, and external package manifest control normative identity.

---

## 15. Recommended reading order

For a first reading:

1. this README;
2. Main Chapter 1 - scope and safety rules;
3. Main Chapter 8 - release closure and external Return boundary;
4. Main Chapters 2 and 3 - metric repair and finite proof compression;
5. Main Chapters 4 and 5 - higher Ext and defect separation;
6. Appendix A - detailed threshold-gap and zero-transport proofs;
7. Appendix B - finite detector and MinCert theorems;
8. the final Claim Register;
9. Appendix HT - transport and Return composition;
10. Appendix UB - validated success cases.

For arithmetic and Iwasawa work, also read MS-A, MS-B, the source-binding files, and the Known-Theorem Recovery manifests.

For Navier-Stokes work, also read NS-A, NS-B, NS-C, and the Serrin source binding.

For AI, automation, or proof-platform work, also read Appendices U, V, W, X, Y, and Z.

---

## 16. Small conceptual example

Suppose a finite detector samples several points and returns zero everywhere.

That observation alone does not prove that the repaired persistence profile is zero.

AK-HPDST asks:

```text
Was every possible retained bar forced to intersect the stencil?
Were endpoint and germ conventions handled correctly?
Was the detector applied before or after threshold deletion?
Was the object inside the declared family?
Was the mesh smaller than an independently proved excess bound?
Were all artifacts fixed and replayable?
```

Only after a complete theorem answers these questions may the zero observation become a finite zero certificate.

A second example concerns infinite towers:

```text
many stable-looking finite layers
    !=
proved infinite limit
```

A valid infinite conclusion requires a stabilization, compactness, completion, finite-state, or derived-limit theorem together with apex agreement.

---

## 17. AI and automated mathematical search

AK-HPDST permits AI and automated systems to:

* propose realizations and bridge candidates;
* search for counterexamples;
* generate detector candidates;
* rank proof routes;
* produce formalization drafts;
* construct dependency graphs and manifests;
* replay computations;
* assist with literature and source binding.

The semantic boundary remains strict:

```text
Generation != verification
Search success != theorem
Consensus != proof
Self-review != independent verification
Storage != certification
Byte identity != semantic identity
Formal syntax != source-faithful meaning
```

An AI-generated object becomes theorem evidence only after conversion into the exact verifier-side schema and successful checking within the declared authority and scope.

AK-HPDST is therefore compatible with advanced mathematical AI while remaining conservative about proof status.

---

## 18. Versioning and citation discipline

When citing an AK-HPDST result, record at least:

* theory version and appendix version;
* exact source artifact;
* theorem, definition, local label, or Claim UID;
* complete hypotheses and monitored scope;
* comparison mode and detector stage;
* required source bindings and artifacts;
* Return strength;
* repair ancestry when relevant.

A README, diagram, summary, generated explanation, or later software implementation does not replace the canonical theorem statement.

For the release as a whole, cite the Zenodo DOI shown above and identify the exact version used.

---

## 19. Final interpretation

AK-HPDST v20.0.0 asks:

```text
How can a complex mathematical claim be compressed into finite evidence,
transported through several mathematical representations,
checked for hidden loss or obstruction,
and returned to its original domain without overstating the conclusion?
```

The v20 contribution is not the assertion that every mathematical problem can be collapsed or solved.

Its contribution is an architecture that separates:

* finite observation from finite proof;
* detector soundness from detector completeness;
* compression from preservation;
* persistence vanishing from higher derived vanishing;
* terminal cleanliness from transient cleanliness;
* finite-stage agreement from infinite reduction;
* realization from Return;
* ideal, module, object, and derived Return strengths;
* AI generation from verifier authority;
* internal certification from external mathematical truth.

Appendix HT turns these distinctions into a unified transport and Return calculus.

Appendix UB demonstrates that the architecture can be executed across multiple mathematical domains through twelve validated cases.

The resulting v20 research system is best described as:

```text
A finite proof-compression and proof-transport architecture
with typed defects, explicit Return strength, and auditable external boundaries.
```
