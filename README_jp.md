# AK–HDPST v18 — AK高次元射影構造理論

> **AK–HDPST v18：監査可能なCollapse指向の証明接続フレームワーク**  
> **Core**：一パラメータ構成可能Persistence上の窓付きバーコード評価  
> **Interface**：外部領域の結論には明示的なsoundness bridgeが必要  
> **Platform**：探索、AI支援、Proof Store、DAG、Replayは監査基盤であり、証明そのものではない

本リポジトリは、**AK–HDPST v18**、すなわちAK高次元射影構造理論のv18系修正版アーキテクチャを収録する。

AK–HDPST v18は、主要未解決問題に対する万能解法として提示されるものではない。

本理論は、以下を目的とする構造的フレームワークである。

- 外部数学対象をCoreで読めるPersistenceデータへ射影すること
- 窓付き・しきい値付きバーコードプロファイルによりCollapseを評価すること
- 明示されたtower comparison artifactにより塔構造の失敗を追跡すること
- Core検証と外部領域の定理主張を分離すること
- AI支援探索、証明候補、Bridge Program、Proof Store、再現性記録を管理すること

v18の中心原則は次である。

```text
Core pass does not imply an external theorem without a proved bridge.
```

日本語では、

```text
Coreが通過しても、証明済みbridgeなしに外部定理は従わない。
```

---

## リポジトリ構成

```text
.
├─ OLD/
│  └─ ...                                  # 履歴版。古い主張を含む可能性あり
├─ AK-HDPST_v18/
│  ├─ AK_HDPST_v18.tex                     # XeLaTeXソース
│  └─ AK_HDPST_v18.pdf                     # コンパイル済みPDF
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

実際のファイル名は、リリースパッケージによって異なる場合がある。

---

## v18とは何か

AK–HDPST v18は、主張の厳密な分離を中心に再構成されたアーキテクチャである。

主要な記述は、原則として以下のいずれかに分類される。

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

目的は、次のような不正な飛躍を防ぐことである。

```text
高次元射影
  -> Collapse的挙動
  -> 外部予想の解決
```

v18で許される経路は、より厳密である。

```text
外部対象
  -> 宣言された実現
  -> Core-readable persistence object
  -> 窓付き評価
  -> gate / diagnostic / ledger check
  -> Core verdict
  -> 証明済みbridge theoremがある場合のみ外部定理
```

---

## v18におけるCore評価

修正後Coreの中心対象は、窓付き・しきい値付きバーコード評価である。

```text
Eval(i, W, tau; F)
  = T_bar_tau( W_W P_i(F) )
```

直感的には、以下を意味する。

- `F` はフィルター付き対象、またはPersistence由来の対象である。
- `P_i(F)` は次数 `i` のPersistence profileである。
- `W_W` は宣言された窓 `W` への制限である。
- `T_bar_tau` は長さ `<= tau` のバーコード区間を削除する操作である。
- `Eval(i,W,tau;F)` は修正後Coreで読む評価プロファイルである。

本READMEでは、簡易表記として以下を用いる。

```text
Eval_{i,W,tau}(F)
```

---

## 修正後Coreの基本要素

### 1. 窓付きバーコード評価

```text
Eval_{i,W,tau}(F)
```

これは、Collapse評価に用いる主要なCore-readable objectである。

---

### 2. Admissible representative

```text
C_{tau,W}F
```

これは、旧式の大域的な厳密filtered liftではない。

必要な互換性条件とeligible条件が宣言された場合にのみ用いられる、許容代表である。

---

### 3. Tower comparison artifact

```text
phi_{i,W,tau}
```

これは、旧式の曖昧な “after-collapse comparison map” という表現を置き換えるものである。

意図される概略形は次である。

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

これらは、宣言されたtower comparison artifactから得られる監視対象の塔診断である。

cleanな診断状態は、以下のように書く。

```text
(mu_Collapse, nu_Collapse) = (0,0)
```

---

### 5. Ledger budget

```text
Sigma_delta < gap_tau
```

これは監査用の予算条件である。

蓄積された欠陥量が、宣言されたgapを下回るかどうかを記録する。

---

## v18におけるCore pass

Core passは、Core-readable objectについての判定である。

典型的なv18 Core passでは、以下が要求される場合がある。

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

Core passは、以下を自動的には意味しない。

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

これらには、別途bridge theoremが必要である。

---

## Core / Interface / Spec の分離

### Core

Core層には、以下に関する定理級の内部主張が含まれる。

- 一パラメータ構成可能Persistence
- 窓付きバーコード評価
- しきい値削除
- admissible representative
- eligible regimeにおける `Ext^1` の使用
- tower diagnostics
- ledger budget check
- gate verdict
- manifest requirement

---

### Interface

Interface層は、外部領域がCoreへ接続する方法を定義する。

例：

- 算術interface
- 岩澤塔interface
- Navier-Stokes interface
- mirror / categorical interface
- Fukaya-side interface
- cryptographic interface

InterfaceはCoreへの経路を定義できるが、それ自体では外部定理を証明しない。

---

### Spec

`[Spec]` は、提案的・探索的・条件付きの構成要素を示す。

`[Spec]` statement は定理ではない。

```text
[Spec] != theorem
```

---

## Bridge discipline

v18で最も重要な規則は次である。

```text
Bridge Program != Bridge Theorem
```

以下の移行を行うには、bridge theoremが必要である。

```text
Core-visible condition
```

から、

```text
external-domain conclusion
```

へ移る場合。

または、

```text
external-domain structure
```

から、

```text
Core-readable behavior
```

へ移る場合。

Bridge candidateは、証明されるまではcandidateまたは`[Spec]`として扱わなければならない。

---

## Problem Interface Appendices

v18のappendixは、未解決問題を解いた章として書かれていない。

それらは **Problem Interface Appendices** である。

機能は、以下を明示することである。

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

Navier-Stokes appendicesは、以下の構成を持つ。

```text
NS-A: Exploration Protocol
NS-B: Theoretical Soundness Layer
NS-C: Proof-First Program
```

これらはNavier-Stokes正則性を証明しない。

目的は、Core passをPDE定理として解釈する前に、何が必要かを明示することである。

---

### Arithmetic / MS appendices

算術向けappendicesは、以下を整理する。

```text
arithmetic source data
cyclotomic and Iwasawa towers
congruence defects
Selmer-like structures
mirror / categorical comparison
Fukaya-side calibration
```

これらは、BSD、ABC、RH、岩澤主予想を証明しない。

---

### AGI / normalization appendices

AGI向けappendicesは、normalization、platform、interfaceの挙動を定義する。

これらは、AI出力を証明へ変換しない。

---

## Search / Platform layer

Appendix U-Zは、Search / Platform layerを定義する。

この層は、以下を支援する。

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

この層はCoreを拡張しない。

---

## 主要な非混同原則

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

Companion 1は、算術校正のための運用テンプレートを提供する。

含まれるテンプレートは以下である。

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

重要規則：

```text
mu_Iw != mu_Collapse by default
```

Companion 1は運用補助であり、算術定理の源泉ではない。

---

### Companion 2: Execution / Reproducibility Companion

Companion 2は、実行と再現性のためのテンプレートを提供する。

含まれるテンプレートは以下である。

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

重要規則：

```text
Execution and reproducibility templates are operational aids, not proofs.
```

---

## 概念的な実行プロトコル

v18の実行は、修正後の順序に従うべきである。

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

外部定理として解釈するには、追加で以下が必要である。

```text
Core verdict
  -> proved bridge theorem
  -> external-domain conclusion
```

---

## 推奨実行artifact

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

artifactが存在するだけでは、証明を意味しない。

---

## `run.yaml` の例

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

## `eval.json` の例

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

## `diagnostics.json` の例

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

## `ledger.json` の例

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

## `gate.json` の例

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

## v17.x から v18 への変更点

### 概念上の変更

v17.xでは、AK-HDPSTはCore / Spec分離を持つ探索OSとして位置づけられていた。

v18では、これを以下へ修正・強化した。

```text
an auditable collapse-oriented proof interface framework
```

主要な変化は次である。

```text
from:
  truncation-first exploration OS

to:
  windowed Core evaluation + explicit bridge discipline + proof governance
```

---

### Core記法の変更

旧表現：

```text
T_tau
C_tau
after-collapse comparison map
DiagZero
```

v18での推奨表現：

```text
Eval_{i,W,tau}(F)
C_{tau,W}F
phi_{i,W,tau}
(mu_Collapse, nu_Collapse) = (0,0)
Sigma_delta < gap_tau
```

---

### Claim status の変更

v18では、明示的なstatus分離が必要である。

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

### Platform層の変更

v18では、より明確なgovernance shellが追加された。

```text
Agent Semantics
Hunter / Mapper / Lifter Protocols
Bridge Programs
Validity Map and Certificate DAG
AI Platform and Proof Store
Execution and Reproducibility Schema
```

---

## v18以降のロードマップ

推奨される次の作業は、大きなappendixをさらに増やすことではない。

小さく検証可能な補強に集中すべきである。

---

### Priority 1: AK v18 Claim Register

すべてのclaim、definition、bridge、spec、non-claimのregisterを作成する。

```text
Goal:
  prevent Spec / theorem / bridge confusion
```

---

### Priority 2: Core Micro-Theorem Pack

以下に関する小さなCore定理を証明する。

```text
window restriction compatibility
threshold deletion idempotence
deletion-type monotonicity
gap stability
ledger-safe perturbation
```

---

### Priority 3: Arithmetic Toy Bridge Pack

有限型またはtoy Iwasawa-like towerを構築し、小さなbridgeを証明する。

```text
eventual tower stability
  -> clean AK tower diagnostic
```

---

### Priority 4: Iwasawa Interface Skeleton

本格的な算術ルートを準備する。

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

以下を昇格させるためのテンプレートを作成する。

```text
Bridge Candidate -> Bridge Theorem
```

---

### Priority 6: Minimal Formal Governance Core

まずgovernance layerを形式化する。

```text
Spec cannot be used as theorem
Bridge Program cannot discharge Bridge Theorem
Stored object is not verified object
Core pass does not imply external theorem without bridge
```

---

## Installation

以下は例示である。

```bash
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e ".[all]"
```

実際のpackage layoutは異なる場合がある。

---

## Quickstart

以下は例示である。

```bash
# v18用の最小run configurationを準備
cp examples/v18/minimal/run.yaml ./run.yaml

# repaired evaluation / diagnostics / ledger pipelineを実行
akhdpst run run.yaml

# Core-facing recordsを窓単位で監査
akhdpst audit out/artifacts --by-window
```

---

## Minimal Python API

例示のみ。

```python
from akhdpst.eval import eval_window_threshold
from akhdpst.diagnostics import compute_typeIV
from akhdpst.ledger import check_budget
from akhdpst.gate import b_gate_plus

F = load_filtered_object("data/example.h5")

tau = 0.15
W = (0.0, 0.5)
degree = 1

# 窓付き・しきい値付きrepaired evaluation
E = eval_window_threshold(F, degree=degree, window=W, tau=tau)

# phi_{i,W,tau}を用いた宣言済みtower diagnostic
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

Contributionは、v18の非混同原則を維持しなければならない。

### Required

- Claim statusを明示すること。
- Core、Interface、Bridge、Spec、Operational claimを分離すること。
- AI outputをproofとして扱わないこと。
- 保存されたartifactをcertifiedとして扱わないこと。
- 再現性をtheorem validityとして扱わないこと。
- `Eval_{i,W,tau}`、`C_{tau,W}F`、`phi_{i,W,tau}` を一貫して用いること。
- defectにはledger treatmentを含めること。
- exampleやtemplateにはnon-claim clausesを含めること。

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

---

## Terms cheat sheet

```text
Eval_{i,W,tau}(F)
  窓付き・しきい値付きバーコード評価。

C_{tau,W}F
  宣言された互換性条件のもとでのみ用いるadmissible representative。

phi_{i,W,tau}
  宣言されたtower comparison artifact。

mu_Collapse, nu_Collapse
  監視対象のType IV tower diagnostics。

Sigma_delta < gap_tau
  Ledger budget condition。

B-Gate+
  repaired evaluation、eligible Ext clause、Type IV diagnostics、
  ledger budgetを用いるCore gate。

Bridge Candidate
  提案されたcross-layer implication。まだ定理ではない。

Bridge Theorem
  証明済みcross-layer implication。

Bridge Program
  Bridge candidateのためのproof-management program。定理ではない。

Validity Map
  navigation and status map。証明ではない。

Certificate DAG
  dependency structure。存在するだけでは証明ではない。

Proof Store
  storage and registry infrastructure。certificationではない。

Replay pass
  reproducibility result。theorem validityではない。

Spec
  明示的に非定理である探索的・条件付きstatement。
```

---

## Final v18 statement

AK-HDPST v18は、以下のように読むべきである。

```text
A framework for making collapse-based projection, persistence evaluation,
tower diagnostics, bridge programs, and proof-management infrastructure
auditable without confusing exploration, storage, execution, or Core pass
with external theorem proof.
```

日本語では、

```text
AK-HDPST v18は、Collapseに基づく射影、Persistence評価、
塔診断、Bridge Program、証明管理基盤を監査可能に扱うための
フレームワークであり、探索・保存・実行・Core passを
外部定理の証明と混同しないための体系である。
```

最短の要約は次である。

```text
AK-HDPST v18 is not a universal solver.
It is an auditable proof-interface framework for collapse-oriented exploration.
```

日本語では、

```text
AK-HDPST v18は万能解法ではない。
Collapse指向探索のための、監査可能な証明接続フレームワークである。
```
