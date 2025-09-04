# AK-HDPST v15.0 — AK 高次元射影構造理論

高次元射影と統制された障害除去に基づく、関手的 collapse（縮約）のための二層・監査可能な証明フレームワーク。

- コア: 1D 構成可能（constructible）persistence 上の機械検証可能な主張
- [Spec]: 明示的な仮定と監査ログに基づく安全な拡張（collapse 後は非拡大）

リポジトリは研究フレームワークとして、API、実行プロトコル、監査アーティファクトを提供します。強い保証は以下の「コアのスコープ」に限定されます。

---

## ハイライト

- 正確なトランケーション `T_tau` が長さ <= tau のバーを削除（Serre 反射）。インターリービング/ボトルネック距離に対して 1-Lipschitz
- フィルタ付き持ち上げ `C_tau` は f.q.i.（filtered quasi-isomorphism）まで一意で、`P_i(C_tau F) ~ T_tau(P_i F)`
- Collapse ゲート: 一方向のみ使用（PH1(F)=0 => Ext1(R(F),k)=0、t-正確・振幅 <= 1 の場合）
- 塔監査 `(mu, nu)`: collapse 後の比較写像の核・余核から見えない極限失敗を検出
- 更新ポリシー: 削除型は collapse 後に非増大、包含型は非拡大（安定性のみ）
- 再現性: 窓（window）単位のプロトコル、δ台帳、B-Gate+ の安全余白、バージョン付き成果物

---

## 目次

- 概要
- スコープと保証
- コンセプトと構成要素
- インストール
- クイックスタート（CLI / Python API）
- 設定ファイル（`run.yaml`）
- ワークフローと例
- 更新ポリシー（許可オペ）
- 監査と成果物
- ロードマップ
- コントリビュート
- 引用・参考文献
- ライセンス

---

## 概要

AK-HDPST v15.0 は「証明志向」フレームワークです。  
- コア: 何を証明し保証するか（構成可能 1D persistence 上）  
- [Spec]: どの仮定のもとで安全に拡張できるか（collapse 後は非拡大、監査付き）

すべての比較は `T_tau` 適用後に行います（窓プロトコル: t -> persistence -> T_tau -> compare）。  
これにより安定性保証が明確になり、塔の `(mu, nu)` で失敗を可視化できます。

---

## スコープと保証

強い主張は次に限定されます。

- 1 パラメータ・構成可能 persistence（係数は体）
- 正確な Serre 反射 `T_tau`（長さ <= tau のバーを削除、1-Lipschitz）
- フィルタ持ち上げ `C_tau`（f.q.i. まで）で `P_i(C_tau F) ~ T_tau(P_i F)`
- 一方向ブリッジのみ: t-正確・振幅 <= 1 の下で PH1(F)=0 => Ext1(R(F),k)=0
- 塔診断 `(mu, nu)` は collapse 後の比較写像の核・余核から算出

注意:
- 一般には PH1 <-> Ext1 は主張しません
- BSD, RH, Navier–Stokes などの主張は行いません

---

## コンセプトと構成要素

- `T_tau`（正確トランケーション）
  - 長さ <= tau のバーを削除する反射
  - インターリービング/ボトルネック距離に対して 1-Lipschitz

- `C_tau`（フィルタ持ち上げ、f.q.i. まで）
  - 鎖複体レベルでの持ち上げ
  - `P_i(C_tau F) ~ T_tau(P_i F)` を次数ごとに満たす

- Collapse ゲートと一方向ブリッジ
  - `CollapseAdmissible(F)` は PH1=0 かつ Ext1=0（Ext1 は上記条件下で PH1=0 から一方向使用）

- 塔診断
  - 導入射 `{F_n} -> F_infty` に対し、collapse 後の比較写像から `(mu, nu)` を定義
  - `(mu, nu) != (0, 0)` は極限での失敗（Type IV）を検出

- 更新ポリシー（collapse 後）
  - 削除型: 窓付きエネルギーやスペクトル指標が非増大
  - 包含型: 非拡大（安定性のみ）
  - スペクトル指標は f.q.i. 不変ではないため、固定ポリシー `(beta, M(tau), s)` の下で管理

- [Spec] 層
  - 幾何/算術/トロピカル・ミラー/ランズランズ風/数理 PDE などのパイプラインは collapse 後の非拡大を条件に許可し、塔診断で監査
  - 外部実現（Sheaf/Fukaya）は PF/BC や action フィルタ等の仮定の下でのみ使用

---

## インストール

本リポジトリは Python パッケージと CLI を提供します。

```bash
# クローン
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

# 仮想環境（推奨）
python -m venv .venv
source .venv/bin/activate  # Windows は .venv\Scripts\activate

# インストール
pip install -e ".[all]"
```

オプション:
- `.[viz]` 可視化
- `.[lean]` / `.[coq]` 形式化スタブ

---

## クイックスタート

### 最小 CLI

```bash
# 設定ファイル雛形
cp examples/minimal/run.yaml ./run.yaml

# 実行
akhdpst run run.yaml

# 監査
akhdpst audit out/artifacts
```

### 最小 Python API

```python
from akhdpst.core import T_tau, C_tau, collapse_admissible
from akhdpst.audit import audit_tower
from akhdpst.io import load_filtered_complex

F = load_filtered_complex("data/example.h5")

tau = 0.15
F_tau = C_tau(F, tau)  # f.q.i. までの持ち上げ
P_tau = {i: T_tau(F.persistence(i), tau) for i in [0,1,2]}

ok = collapse_admissible(F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True)
print("CollapseAdmissible =", ok)

tower = [F_t for F_t in ...]
mu, nu = audit_tower(tower, tau=tau)
print("mu =", mu, "nu =", nu)
```

---

## 設定ファイル（`run.yaml`）

1 つのファイルで、窓・tau・オペ・δ台帳・ゲート条件を管理。成果物はチェックサムで相互リンク。

```yaml
meta:
  name: "demo-v15.0"
  seed: 42
  version: "15.0"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"          # bars | chain
  degrees: [0, 1]

windows:                   # 右開区間（MECE）
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"
  reflector: "T_tau"

operations:
  policy:
    type: "mixed"          # deletion | inclusion | mixed
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

gate:                      # B-Gate+ 条件
  require:
    PH1_zero: true
    Ext1_zero: true        # t-exact・振幅 <= 1 の範囲のみ評価
    mu_zero: true
    nu_zero: true
    gap_tau_gt_sum_delta: true

audit:
  outputs: ["bars", "spec", "ext", "phi"]
  checksums: "sha256"
  restart: "summability"

output:
  dir: "out/artifacts"
  overwrite: false
```

---

## ワークフローと例

### 1) 窓プロトコル

- 必ず `T_tau` 適用後に比較:
  - 窓ごとに t を評価
  - persistence 化
  - `T_tau` 適用
  - 写像比較と `(mu, nu)` 監査

```bash
akhdpst run examples/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

### 2) Collapse ゲート

- 条件:
  - PH1(F)=0
  - Ext1(R(F),k)=0（上記条件下で PH1(F)=0 から一方向）
  - mu=0, nu=0
  - gap_tau > sum(delta)

```bash
akhdpst gate check --run run.yaml --window w0
```

### 3) Spec パイプラインと監査

- Spec の各ステップは collapse 後に非拡大であること。δ台帳に必ず記録。

```bash
akhdpst run examples/spec/mirror.yaml
akhdpst audit out/artifacts --show-delta-ledger
```

---

## 更新ポリシー（許可オペ）

collapse 後における経験則:

| 種別 | 例 | collapse 後の保証 |
| --- | --- | --- |
| 削除型 | ディリクレ制限、主小行列、PSD Loewner 収縮、保守的平均化 | 窓付き persistence エネルギー・スペクトル指標の非増大 |
| 包含型 | セル追加、境界条件緩和、ハンドル付加 | 非拡大（安定性のみ） |

注意:
- `L(C_tau F)` 上のスペクトル指標は f.q.i. 不変ではないため、`(beta, M(tau), s)` の固定ポリシーで運用
- Spec は collapse 後の非拡大と δ台帳記録を必須とする

---

## 監査と成果物

実行ごとに再現可能な成果物を出力し、相互にチェックサムでリンクします。

例のディレクトリ構成:

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

- `bars/`: 窓・次数ごとのトランケーション後バーコード
- `spec/`: δ台帳と仮定チェック
- `ext/`: Ext 監査（該当時）
- `phi/`: 比較写像と `(mu, nu)` のレポート
- `audit_summary.json`: ゲート判定と診断の集約
- `checksums.txt`: すべての成果物の SHA256

---

## コマンド（CLI）

```bash
# 実行
akhdpst run run.yaml

# 監査
akhdpst audit out/artifacts

# B-Gate+ 判定（窓ごと）
akhdpst gate check --run run.yaml --window w0

# バーコードの簡易可視化
akhdpst viz bars --dir out/artifacts --degree 1

# 塔診断
akhdpst diag tower --dir out/artifacts --degree 0
```

---

## Python API（抜粋）

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus
from akhdpst.audit import audit_tower, summarize_audit
from akhdpst.spec import run_spec_pipeline

# persistence レベルの正確トランケーション
P_trunc = T_tau(P, tau=0.2)

# フィルタ持ち上げ（f.q.i. まで）
F_trunc = C_tau(F, tau=0.2)

# ゲート（Ext の一方向ブリッジを内部使用）
ok_gate = collapse_admissible(
    F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True
)
ok_bgate = b_gate_plus(window="w0", mu=0, nu=0, gap_tau=0.05, delta_sum=0.01)

# 塔診断
mu, nu = audit_tower(tower=[F0, F1, F2, F_inf], tau=0.2, degrees=[0,1])

# Spec パイプライン（collapse 後非拡大、δ台帳必須）
spec_out = run_spec_pipeline(F, items=[...], tau=0.2, ledger=ledger)
```

---

## ロードマップ

- 形式化スタブと証明（Lean/Coq）: 反射・診断・ゲート
- tau スイープと安定帯の自動検出
- 大規模バーコード/鎖複体の GPU・並列化
- 窓監査・δ台帳可視化ノートブック
- PDE・Fukaya などの Spec 契約拡充（action フィルタ支援）

---

## コントリビュート

Issue / PR 歓迎です:
- コアと [Spec] の分離をコード・ドキュメントで明確に
- Spec 追加は「collapse 後非拡大・δ台帳記録」を満たすこと
- 最小例と `examples/`・`tests/` の更新を同梱

開発コマンド:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## 引用・参考文献

研究成果で AK-HDPST v15.0 を使用する場合は引用をお願いします。

```
AK–HDPST v15.0: Exact Truncation, Collapse Gate, and Auditable Spec Extensions
Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

主要参考:
- Crawley-Boevey (2015): pointwise finite-dimensional persistence modules の分解
- Chazal, de Silva, Glisse, Oudot (2016): persistence modules とバーコードの構造・安定性

---

## ライセンス

MIT License（`LICENSE` を参照）。

---

## 付録: 用語チートシート

- 構成可能 1D persistence: 有界窓で有限臨界集合・各点有限次元
- `T_tau`: 長さ <= tau のバーを削除する正確反射、1-Lipschitz
- `C_tau`: `T_tau` のフィルタ持ち上げ（f.q.i. まで）、`P_i(C_tau F) ~ T_tau(P_i F)`
- Collapse ゲート: PH1(F)=0 かつ Ext1(R(F),k)=0（上記条件下で一方向のみ使用）
- B-Gate+: PH1=0、Ext1=0（適用域のみ）、mu=nu=0、gap_tau > sum(delta)
- `(mu, nu)`: collapse 後の比較写像の核・余核の generic 次元合計。極限の見えない失敗を検出
- 窓プロトコル: t -> persistence -> T_tau -> compare（右開・非重複の MECE 窓）
- [Spec]: collapse 後非拡大の拡張。δ台帳に記録し、塔診断で監査
