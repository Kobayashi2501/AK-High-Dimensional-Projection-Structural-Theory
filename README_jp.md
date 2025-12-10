# AK–HDPST v17.0 — AK高次元射影構造理論（AK High-Dimensional Projection Structural Theory）

> **AK-OS v1.0: 高次元数学探索のためのオペレーティングシステム**  
> Core：体上の1次元構成的パーシステンスにおける、証明可能な構造  
> [Spec]：切り詰め後に非膨張（non-expansive）な拡張と探索ポリシー（監査付き）

このリポジトリには、**AK–HDPST v17.0** が含まれています。  
v17.0では、もはや「世紀の予想を一撃で解く万能理論」ではなく、  
**難問を探索するための証明指向OS（AK-OS）** として位置付けています。

別リポジトリ **AK_AP（Arithmetic Calibration Program：算術較正プログラム）** は、  
有限体上のWeil世界やFLT世界といった算術的モジュライ空間に対して、  
同じOS（AK-OS）を用いて「閉じた世界」での較正を行うプログラムです。

リポジトリのステータス：  
**研究用OSプロトタイプ** であり、参照用API・実行プロトコル・監査アーティファクトを含みます。  
**強い保証は、以下の Core 範囲に厳密に限定されます。**

---

## AK-OS v1.0 マニフェスト（宣言）

### これは何か？

- **ではないもの**：  
  Navier–Stokes、BSD、RH、FLT などの「大予想」の証明主張そのものではありません。
- **であるもの**：  
  次の要素を中核にもつ **高次元数学探索のためのモジュラーOS** です：
  - **Collapse契約**（Unified Collapse Contract：`UCC / B–Gate⁺`）
  - **切り詰め作用素** `T_tau`
  - 誤差・ギャップ・モデル不一致を記録する **δ（デルタ）台帳：δ-ledger**
  - 極限でのみ破綻する「見えない失敗」を検出する **塔診断 `(mu, nu)`**
  - パラメータ空間上に **Map of Validity（有効性地図）** を描く  
    **HDPS（High-Dimensional Projection Search）エンジン**

### Core と [Spec] の役割分担

- **Core**
  - 体 `k` 上の1パラメータ構成的パーシステンス
  - バー長が `tau` 以下の区間を削除する **正確な切り詰め** `T_tau`  
    （反射的局所化、冪等、インタリービング距離／ボトルネック距離に対して 1-Lipschitz）
  - 切り詰めに対応する鎖レベルの持ち上げ `C_tau`（フィルタ付き準同型まで一意）  
    `P_i(C_tau F) ≅ T_tau(P_i F)`
  - t-正確かつ振幅 ≤ 1 の実現関手のもとでの一方向ブリッジ：  
    `PH1(F) = 0 ⇒ Ext1(R(F), k) = 0`
  - 切り詰め後の比較射から得られる塔診断 `(mu, nu)` と、Type IV failure（有限段ではOKだが極限で破綻）
  - ウィンドウ単位のゲート（`B–Gate⁺`, Overlap Gate）と Restart / Summability による貼り合わせ

- **[Spec]**
  - Core の制御下で動く領域別の実現モジュール（数論・PDE・Fukaya など）
  - HDPS（高次元射影探索）：Terrain Cell、Map of Validity、Hunter / Mapper / Lifter エージェント
  - PF/BC after-collapse 比較器、Mirror / Transfer、A/B soft-commuting ポリシー
  - 定量的ヒューリスティクスと探索戦略  
  すべての [Spec] コンポーネントは **「切り詰め後に非膨張」** であり、  
  さらに **δ-ledger による完全な監査** を受ける必要があります。

### AK-OS が目指すもの

- 「**証明を試みる**」行為を、**地形上のナビゲーション** として扱います：
  - 入力パラメータ空間を **モジュライ空間 `M`** とみなし、
  - Collapse の可否をその上のラベル（またはスカラー場）として扱い、
    - `Valid`（ゲートを通過し、Collapse が安全に成立）
    - `Obstructed`（Type IV などの構造的破綻）
    - `Unknown`（未探索、あるいは Core 範囲外）
    に分類します。

- **証明ギャップ／数値誤差／モデル不一致** を「なかったこと」にせず、  
  **δ（デルタ）コスト** として台帳に記録します：
  - `delta.alg`：アルゴリズム／モデル化由来
  - `delta.disc`：離散化・数値誤差
  - `delta.meas`：測定・入力由来

- `run.yaml` とアウトプットアーティファクト、δ-ledger により  
  **再現可能で批判しやすい実行プロトコル** を提供します。

### このプロジェクトの読み方

- **純粋数学として読む場合**：  
  Core 部分を `D^b(k-mod)` やパーシステンスの候補定理として扱い、  
  [Spec] 部分は「仮定付き・実装依存の拡張」として扱ってください。

- **ソフトウェアアーキテクチャとして読む場合**：  
  AK–HDPST を、  
  - Collapse 操作の安定化、
  - 探索エージェントの協調、
  - 定量的証拠の記録  
  を担う **数学探索OS** とみなしてください。

- **人間×AI協働のケーススタディとして読む場合**：  
  - 人間が **アイデア／制約／OS的な直感（どんなOSが欲しいか）** を出し、
  - LLM が **形式化・構造化・LaTeX／コードスケルトン** を担当しています。

---

## 「世紀の予想を解く理論」から「探索OS」への転換

### 初期フェーズ（v10–v14）：過積載な「万能解法フレームワーク」

- 目標：  
  Navier–Stokes、BSD、RH、Langlands… を、ひとつの巨大な理論で「全部まとめて」殴る。
- 材料：
  - 導来圏、岩澤理論、Fukaya圏、Denef–Pas 構造、Langlands 風ゲート、
  - トロピカル幾何、ミラー対称性 など、多数のハイエンド概念が一気に登場。
- 問題点：
  - アイデアとしては刺激的だが、**過剰に積みすぎ＋検証不能**。
  - 概念が重すぎて、全体の整合性を人力でチェックするのは実質不可能。
  - **「鏡張りの迷宮」** のようになり、見た目はすごいがどこまで正しいか不明瞭。

### 中期フェーズ（v15–v16）：ラディカルな簡素化とガードレール

- フォーカスを次に絞り込み：
  - 主舞台を **体上の1次元構成的パーシステンス** に限定。
  - 中心的な正確関手を **バー削除トランケーション `T_tau`** に固定。
  - `PH1 ⇒ Ext1` の一方向ブリッジを、明示的な仮定のもとで `D^b(k-mod)` に限定。
  - δ-ledger とウィンドウ付きプロトコルで **監査可能なパイプライン** を整備。
- 結果：
  - **Scope and Guarantees（適用範囲と保証）** が Core として明確化。
  - ドメイン特化の重い構造は **[Spec] へ退避 or 切り捨て**。

### v17.0：OSへのピボット — HDPS と閉じた世界での較正

v17.0 では、プロジェクトの立ち位置を明確に変更します：

- 以前：  
  「いつか世紀の難問も解けるかもしれない巨大フレームワーク」
- これから：  
  「**難問を探索するためのOS（AK-OS）**。境界線を明示して提供する」

主な変更点：

1. **HDPS（High-Dimensional Projection Search）と Map of Validity**
   - 入力パラメータ空間を高次元モジュライ空間 `M` とみなす。
   - Collapse の可否を `M` 上のラベル／スカラー場として：
     - `Valid`（Collapse 成功・ゲート通過）
     - `Obstructed`（Type IV 等の構造的障害）
     - `Unknown`（未探索・Core 範囲外）
     として配置。
   - HDPS は **Terrain Cell（局所セル）** を張り、  
     **Hunter / Mapper / Lifter** という役割をもつエージェント群によって  
     **Map of Validity（有効性地図）** を構築・洗練します。

2. **AK_AP（算術較正プログラム）による「閉じた世界」のテスト**

   Navier–Stokes 等の「開いた世界」に行く前に、まず：

   - すでに真理が確定している **算術世界で OS をテスト** します：
     - `M_Weil`：有限体上の多様体のモジュライ（Weil世界）
     - `M_FLT`：半安定楕円曲線／Frey データの変形空間（FLT世界）
   - 従来の大定理（Deligne の有限体RH、Wiles–Taylor によるモジュラー性／FLT）を  
     **Core-Input（外部入力の公理）** として扱います。
   - HDPS＋UCC によって、OS が次を再現できるかをテストします：
     - `M_Weil` 上に「**Plain of Truth（真理の平面）**」が現れる（欠陥ポテンシャルがゼロ）
     - `M_FLT` の Frey 領域が、Type IV collapse failure により  
       **構造的に空（Global Obstruction）** と判定される
   - これは **新しい証明ではなく、較正（Calibration）** です：  
     OS が既知の定理と整合的に振る舞うかを確認する段階です。

3. **適用範囲についての明示的な正直さ**

   - v17.0 は、Navier–Stokes / BSD / RH / FLT の証明を **一切主張しません**。
   - 代わりに、次のような **明示的なOS＋プロトコル** を提供します：
     - Core の明確な境界、
     - [Spec] の仮定と依存関係、
     - δ-ledger と監査アーティファクトに基づく探索ワークフロー。

---

## v16.0 → v17.0 の主な変更点

### コンセプト面

- **OS フレーミング（AK-OS v1.0）**
  - プロジェクト全体を「数学探索OS」として再定義。
  - Core と [Spec] の分離を、文書構造・コード構造ともに明示化。
  - **実行プロトコル／δ-ledger／監査** に重心を置いた記述へ。

- **HDPS（High-Dimensional Projection Search）の導入**
  - **Terrain Cell** と **Map of Validity** を一級市民の概念として導入。
  - **Hunter / Mapper / Lifter** の各ロールを明示化（探索・地図更新・モデル間リフティング）。
  - すべての比較・評価は必ず **`T_tau` 適用後（post-truncation）** に行う方針を徹底。

- **AK_AP による「閉じた世界での較正」**
  - AK_AP リポジトリで、AK-OS を：
    - `M_Weil`（有限体Weil世界）
    - `M_FLT`（Frey / FLT世界）
    に適用。
  - Deligne と Wiles を **Core-Input 公理** として扱い、  
    OS がそれと矛盾しない形で：
    - `M_Weil` を「Plain of Truth」、  
    - `M_FLT` の Frey locus を「構造的空集合」と認識するかをテスト。
  - HDPS＋Map of Validity の **閉じた世界での具体例** を提供。

### Core / [Spec] の技術的整理

- **Core 側の明確化**
  - すべての Core 結果は `D^b(k-mod)`（体係数・1次元構成的パーシステンス・振幅≤1実現）上に制限。
  - 塔診断 `(mu, nu)` と Type IV failure の定義を、**必ず `T_tau` 後の世界** に揃えるよう整理。
  - `PH1 ⇔ Ext1` のような「双方向同値」は全否定、  
    多パラメータや超えた設定への暗黙の拡張も禁止。

- **[Spec] レイヤの再配置**
  - Langlands・Fukaya・Denef–Pas などの重い構造は、  
    本体から切り離し、**[Spec] Appendices または別文書**として退避。
  - PF/BC after-collapse、Mirror / Transfer、A/B soft-commuting、HDPS ポリシーはすべて [Spec] と明示し：
    - `T_tau` 適用後の非膨張性、
    - δ-ledger へのログ  
    を必須条件としました。

- **run プロトコルとアーティファクト**
  - v16.0 のウィンドウ付きプロトコルを継承したうえで拡張：
    - `run.yaml` に任意の HDPS 設定ブロックを追加可能。
    - 監査アーティファクトに、小規模な玩具例に対する **Validity Map のスナップショット** を追加。
  - IMRN / AIM 型テストスイート（T7, T10, T11, T13, T14, T15）は  
    **Core の検証用テスト** として維持。

---

## 目次

- AK-OS v1.0 マニフェスト
- 「Big-Conjecture Solver」から「Exploration OS」へ
- v17.0 での変更点
- Overview（概要）
- Scope and guarantees（Core の適用範囲と保証）
- Core と [Spec] の中身
- Concepts and components（主要コンセプト）
- Installation（インストール）
- Quickstart（CLI / Python API）
- Configuration（`run.yaml`）
- Workflows and examples（ワークフローと例）
- Update policy（切り詰め後の更新則）
- Auditing and artifacts（監査と成果物）
- Command reference（CLI コマンド）
- Python API reference（抜粋）
- Roadmap
- Contributing
- Citing and references
- License
- Appendix: 用語チートシート

---

## Overview（概要）

AK–HDPST v17.0 は、**AK-OS** のカーネルとなる  
高次元 Collapse と有効性マップのための証明指向OSです。  

明確に：

- **Core**
  - 体上の1次元構成的パーシステンス
  - `D^b(k-mod)`（導来圏）上の、振幅制御付き実現
  における **証明可能／形式化可能な保証**

- **[Spec]**
  - `T_tau` 適用後に非膨張であることを前提に、
  - δ-ledger と塔診断 `(mu, nu)` による監査のもとで動く、
  - 領域別の実現モジュールと探索ポリシー

という区別を持ちます。

すべての定量的比較は、次の **post-truncation プロトコル** に従います：

```text
t  →  persistence P_i  →  truncation T_tau  →  compare / audit / map_validity
```

これにより：

- メトリック安定性（1-Lipschitz）、
- Type IV を含む破綻モードの透明性、
- 再現可能で監査可能な探索パイプライン

が保証されます。

---

## Scope and guarantees（Core の適用範囲と保証）

Core の強い主張は、次の設定に **厳密に限定** されます：

- **圏・対象**
  - 1パラメータ構成的パーシステンス（有限臨界値・有限次元）
  - 係数は **体** `k`
  - 実現関手は `D^b(k-mod)` へのもので、必要な場合は振幅 ≤ 1

- **切り詰め `T_tau`**
  - バーコードの長さ ≤ `tau` の区間を削除する **正確な反射的局所化**。
  - 冪等・インタリービング／ボトルネック距離に対して 1-Lipschitz。
  - 単調性や非膨張性に関する主張は、**必ず `T_tau` 適用後** でのみ行います。

- **フィルタ付き持ち上げ `C_tau`**
  - 鎖レベルにおける lift（フィルタ付き準同型まで一意）。
  - 任意の次数 `i` に対して：  
    `P_i(C_tau F) ≅ T_tau(P_i F)`

- **ブリッジ `PH1 ⇒ Ext1`**
  - t-正確・振幅 ≤ 1 の実現の下では：  
    `PH1(F) = 0` なら `Ext1(R(F), k) = 0`
  - 逆向き（`Ext1 = 0 ⇒ PH1 = 0`）は主張しません。  
    したがって、`PH1 ⇔ Ext1` の大域的同値も一切主張しません。

- **塔診断 `(mu, nu)`**
  - 切り詰め後の段階間比較射から、核・余核の一般繊維次元として定義。
  - Type IV failure：  
    各有限段ではゲートを通過しているが、極限の比較で `(mu, nu) ≠ (0, 0)` となる場合。
  - τ-sweep と Stability band により、 `(mu, nu) = (0, 0)` が局所的に安定な τ の範囲を検出。

- **Gating（ゲート）**
  - B–Gate⁺（Collapse ゲート：ウィンドウ毎）
    - `PH1(F) = 0`
    - `Ext1(R(F), k) = 0`（振幅 ≤ 1 のときのみ重視）
    - `(mu, nu) = (0, 0)`
    - 安全マージン：`gap_tau > sum_delta`（δ-ledger の合計との比較）
  - Overlap Gate（post-collapse）
    - `T_tau` 適用後の重なり領域での局所同値（予算内）
    - Čech–Ext1 のアシクリック性
    - Stability band 一致
    - 重なり領域に対する δ予算の管理

**主張しないこと：**

- `PH1 ⇔ Ext1` のような大域的同値。
- 1次元構成的パーシステンスを超えた多パラメータ設定での保証。
- BSD、RH、Navier–Stokes、Langlands などに対する直接的な定理。  
  それらへの関わりは、すべて [Spec] モジュールと外部入力（例：AK_AP）を介してのみ行われます。

---

## Core と [Spec] の中身

### Core（証明可能／形式化可能）

- 正確な切り詰め `T_tau` と、その 1-Lipschitz 安定性。
- `T_tau` に対応する鎖レベルの持ち上げ `C_tau`（f.q.i. まで一意）。
- 振幅 ≤ 1 での `PH1 ⇒ Ext1` 一方向ブリッジ。
- 塔診断 `(mu, nu)`、τ-sweep と Stability band。
- B–Gate⁺、Overlap Gate（cut 後の Čech–Ext1 による局所→大域貼り合わせ）。
- Restart / Summability によるウィンドウ証明のグローバル貼り合わせ。
- 長さスペクトル作用素 `Lambda_len`：
  - 切り詰め後のバーコード長さと同値の「長さ多重集合」を返す。
  - `T_tau` 適用後の同型に対して不変。

### [Spec]（監査付き・切り詰め後非膨張）

- HDPS：Terrain Cell、Hunter / Mapper / Lifter、Map of Validity 構成。
- PF/BC after-collapse 比較器：
  - 導来レベルで PF / BC を評価し、
  - パーシステンスへ押し出し、
  - `T_tau` をかけた上でウィンドウ比較。
- Mirror / Transfer の可換性：
  - 自然な 2-セルと δ 制御付き可換性。
  - パイプラインに沿って δ を加法的に管理、後処理で非増大。
- A/B soft-commuting ポリシー：
  - 入れ子でない反射子の近似可換性テスト。
  - `Delta_comm ≤ eta` なら許容、超過なら順序変更＋δログ。
- 領域別実現フック：
  - 数論／Langlands ゲート
  - PDE／Navier–Stokes のヒューリスティクス
  - Fukaya の action-filtration  
  などを、すべて「切り詰め後非膨張＋δ-ledger ログ」の制約下で扱います。

---

## Concepts and components（主要コンポーネント）

- **`T_tau`（正確な切り詰め）**
  - 長さ ≤ `tau` のバーを削除する反射的局所化。
  - 冪等・パーシステンスの標準距離に対して 1-Lipschitz。

- **`C_tau`（フィルタ付き持ち上げ）**
  - 鎖レベルの lift（f.q.i. まで一意）。
  - パーシステンスレベルでは `T_tau` と整合：
    `P_i(C_tau F) ≅ T_tau(P_i F)`。

- **Collapse Gate（`B–Gate⁺`）**
  - ウィンドウごとに次をチェック：
    - `PH1(F) = 0`
    - `Ext1(R(F), k) = 0`（振幅 ≤ 1 のとき）
    - `(mu, nu) = (0, 0)`
    - `gap_tau > sum_delta`（安全マージン）

- **Overlap Gate（post-collapse）**
  - `T_tau` 適用後の重なりで：
    - 局所的同値（δ予算内）、
    - Čech–Ext1 アシクリック性、
    - Stability band 一致
    を要求。

- **塔診断 `(mu, nu)`**
  - 切り詰め後の比較射から核・余核次元として算出。
  - `(mu, nu) ≠ (0, 0)` は Type IV failure の指標。

- **Stability band**
  - `tau` の範囲で `(mu, nu) = (0, 0)` が τ の微少変動に対して安定。
  - Collapse が「しっかり動いている」帯域として利用。

- **長さスペクトル作用素 `Lambda_len`**
  - 切り詰め後のバー長と同値な多重集合を返す。
  - `T_tau` 適用後の同型に対して不変。

- **HDPS / Map of Validity [Spec]**
  - **Terrain Cell**：Collapse 挙動がほぼ一定な局所パラメータ領域。
  - **Hunter**：δ-ledger とゲート結果にもとづき探索候補を提案。
  - **Mapper**：セルを細分化し、Map of Validity を更新。
  - **Lifter**：粗いモデル→細かいモデルへのリフトを担当（例：離散→連続）。
  - **Map of Validity**：各セルを `Valid / Obstructed / Unknown` にラベリングし、Core ゲートと矛盾しないよう保つ。

---

## Installation（インストール）

```bash
# 1) クローン
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

# 2) 仮想環境
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) インストール
pip install -e ".[all]"     # extras: [viz], [lean], [coq], [hdps]
```

---

## Quickstart（クイックスタート）

### 最小限の CLI 実行

```bash
# 実行設定ファイルを用意
cp examples/v17/minimal/run.yaml ./run.yaml

# ウィンドウ＋post-collapse プロトコルで実行
akhdpst run run.yaml

# ウィンドウ毎のゲート判定・塔診断・δ-ledger を確認
akhdpst audit out/artifacts

# （任意）玩具例について簡単な Map of Validity を構成
akhdpst hdps map --run run.yaml --toy
```

### 最小限の Python API

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse
from akhdpst.length import lambda_len

# フィルタ付き鎖複体または次数別パーシステンスをロード
F = ...  # user load

# tau で切り詰め（パーシステンスと鎖レベルlift）
tau = 0.15
P_trunc = {i: T_tau(F.persistence(i), tau) for i in [0, 1]}
F_trunc = C_tau(F, tau)  # up to f.q.i.

# Collapseゲート（t-正確・振幅<=1のときのみ一方向ブリッジを使用）
ok_gate = collapse_admissible(
    F,
    realization="Db(k-mod)",
    t_exact=True,
    amplitude_leq_1=True,
)

# 塔診断（tau ごと）；Stability band
mu, nu = audit_tower(
    tower=[F0, F1, F2, F_inf],
    tau=tau,
    degrees=[0, 1],
)
bands = detect_stability_band(
    tower=[F0, F1, F2, F_inf],
    degree=1,
    tau_sweep=[0.1, 0.15, 0.2],
)

# PF/BC after-collapse 比較器（ウィンドウ＋post T_tau）[Spec]
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)",
    obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]),
    tau=tau,
)

# 長さスペクトル監査（ウィンドウ＋切り詰め長）
eig = lambda_len(P_trunc[1], window=(0.0, tau))
```

---

## Configuration（`run.yaml`）— v17.0 スキーマ概要

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
  # 半開区間 [a, b)、MECE（重なりなし・漏れなし）、被覆は監査対象
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"         # f.q.i.まで一意な持ち上げ
  reflector: "T_tau"    # パーシステンスレベルでの正確な切り詰め

overlap_checks:
  local_equiv: true       # post-collapse同値（δ予算内）
  cech_ext1_ok: true      # Čech–Ext1アシクリック性
  stability_band_ok: true # bandと整合する塔挙動

spectral_policy:
  order: "ascending"      # 必須
  norm: "op"              # "op" or "fro"（必須）
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
    eta: 0.02            # 許容誤差
    fallback_order: ["birth_window", "length"]  # Delta_comm > eta のときの順序

  # HDPS / Map of Validity（実験的；玩具例のみ）
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
    Ext1_zero: true         # 振幅<=1のときのみ使用
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
  audit: "hash"            # 小さい例では固有値そのものを保存してもよい

output:
  dir: "out/artifacts"
  overwrite: false
```

---

## Workflows and examples（ワークフローと例）

### 1) ウィンドウ付き post-collapse プロトコル

Collapse と監査の基本パイプライン：

```bash
akhdpst run examples/v17/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

各ウィンドウ・各次数に対して：

- 切り詰めバーコード、
- δ-ledger、
- 塔診断とゲート判定

が生成されます。

### 2) Overlap Gate による貼り合わせ（post-collapse）

局所→大域の整合性をチェック：

```bash
akhdpst gate overlap --run run.yaml --window w0,w1
```

条件：

- post-collapse 同値（δ予算内）、
- Čech–Ext1 アシクリック性、
- Stability band 一致。

### 3) τ-sweep と Stability band 検出

`(mu, nu)` を τ グリッド上で走査し、安定に `(0, 0)` が保たれる帯域を受理：

```bash
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"
```

### 4) PF/BC after-collapse 比較 [Spec]

`Rf_*(A⊗f^*B)` と `Rf_*A ⊗ B` を、`T_tau` 後の同じウィンドウで比較：

```bash
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15
```

### 5) A/B soft-commuting [Spec]

2つの反射子の近似可換性をテスト：

```bash
akhdpst compare ab \
  --run run.yaml \
  --reflectors length birth_window \
  --eta 0.02
```

`Delta_comm > eta` のときは、`fallback_order` に従った順序を採用し、  
`Delta_comm` を `delta.alg` としてログします。

### 6) 長さスペクトル監査（Lambda_len）

切り詰め長さスペクトルを算出・監査：

```bash
akhdpst audit lambda-len \
  --dir out/artifacts \
  --degree 1 \
  --tau 0.15
```

### 7) 玩具例での HDPS Map of Validity [Spec]

2次元パラメータ空間上で粗い Map of Validity を構成：

```bash
akhdpst hdps map \
  --run run.yaml \
  --toy \
  --grid "32x32"
```

`validity_map/` 以下に、セルごとに `Valid / Obstructed / Unknown` を付与したマップが出力されます  
（Core ゲートと矛盾しないよう構成）。

---

## Update policy（切り詰め後の更新則）

| 更新タイプ       | 例                                                                           | `T_tau` 適用後の保証                                       |
|------------------|------------------------------------------------------------------------------|------------------------------------------------------------|
| Deletion-type    | Dirichlet制限・主小行列・PSD Loewner縮退・保守的な平均化・stop追加           | ウィンドウごとのエネルギー／スペクトル指標が単調非増加     |
| ε-continuation   | 小さなホモトピー・インタリービング条件を満たす小ステップ                   | 1-Lipschitz 安定性；ε は δ-ledger に記録                   |
| Inclusion-type   | セル追加・境界条件の緩和・領域拡大                                          | 非膨張（安定性のみ；単調性は主張しない）                  |

メモ：

- スペクトル指標は `L(C_tau F)` 上で定義されており、  
  f.q.i. 不変量ではありません。v17.0 では `run.yaml` に  
  `spectral_policy`（順序／ノルム）と `spectral_bounds` を必須指定としています。
- すべての [Spec] 操作は：
  - `T_tau` 適用後に非膨張となるよう設計され、
  - ステップごとに `delta.alg / delta.disc / delta.meas` をログし、
  - B–Gate⁺ と Overlap Gate の制約を尊重しなければなりません。

---

## Auditing and artifacts（監査と成果物）

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
    maps_w0_deg1.h5         # 比較射; (mu,nu); iso_tail フラグ
  lambda_len/
    w0_deg1_tau015.json     # 固有値またはハッシュ
  validity_map/
    toy_2d_grid.json        # 玩具HDPS実行の Map of Validity（有効性マップ）
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/`：ウィンドウ／次数ごとの切り詰めバーコード。
- `spec/`：δ-ledger（アルゴリズム／離散化／測定）＋ [Spec] 監査結果。
- `ext/`：Ext1 サマリ（振幅 ≤ 1 の Core 設定に限る）。
- `phi/`：比較射データ・`(mu, nu)`・`phi_iso_tail` フラグなど。
- `lambda_len/`：長さスペクトル（固有値またはハッシュ）。
- `validity_map/`：HDPS 有効性マップ（玩具例のみ）。
- `audit_summary.json`：ゲート結果・Overlapチェック・Stability band 情報。
- `checksums.txt`：すべての成果物の SHA256 ハッシュ。

---

## Command reference（CLI コマンド）

```bash
# 設定ファイルにもとづき実行
akhdpst run run.yaml

# 既存の実行ディレクトリを監査
akhdpst audit out/artifacts

# Overlap Gate チェック
akhdpst gate overlap --run run.yaml --window w0,w1

# B–Gate⁺（Collapseゲート）をウィンドウ単位で実行
akhdpst gate check --run run.yaml --window w0

# τ-sweep と Stability band 検出
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"

# PF/BC after-collapse 比較 [Spec]
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15

# A/B soft-commuting テスト [Spec]
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02

# 塔診断を表示
akhdpst diag tower --dir out/artifacts --degree 1

# 長さスペクトル監査
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15

# HDPS：玩具例での Map of Validity 構成 [Spec]
akhdpst hdps map --run run.yaml --toy --grid "32x32"
```

---

## Python API reference（抜粋）

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus, overlap_gate_check
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse, ab_soft_commute
from akhdpst.length import lambda_len

# Overlap Gate
ok_overlap = overlap_gate_check(run="run.yaml", windows=["w0", "w1"])

# B–Gate⁺（ウィンドウごとの Collapse ゲート）
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

# PF/BC 比較 [Spec]
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)",
    obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]),
    tau=0.15,
)

# τ に対する Stability band 検出
bands = detect_stability_band(
    tower=[...],
    degree=1,
    tau_sweep=[0.1, 0.15, 0.2],
)

# 長さスペクトル（固有値またはハッシュ）
L = lambda_len(P_trunc[1], window=(0.0, 0.15))
```

---

## Roadmap

- **Core**
  - Lean / Coq による形式化の拡充：
    - `T_tau`, `C_tau`, `(mu, nu)`, B–Gate⁺, Overlap Gate など。
  - τ-sweep・Stability band 検出の自動化と、厳密な評価付きの実装。

- **HDPS / [Spec]**
  - HDPS ツール群の拡充：
    - 多段階解像度の Terrain Cell、
    - Hunter / Mapper / Lifter 用のポリシープラグイン。
  - 有効性マップが完全に実装された **有限グラフ／小さなCW複体** などの玩具モデルの追加。
  - 領域別アダプタ：
    - 算術／AK_AP、
    - PDE／Navier–Stokes ヒューリスティクス  
    を、Core の非膨張制約のもとで設計。

- **ツール／UX**
  - Jupyter Notebook テンプレート：
    - ウィンドウごとの監査、
    - δ-ledger 可視化、
    - 有効性マップの可視化。
  - CI（継続的インテグレーション）への組み込み（サンプルrunと監査の回帰テスト）。

---

## Contributing

Issue・PR を歓迎します。特に：

- **Core の明瞭化／形式化**（定義・証明・Lean/Coq コード）。
- 完全に追いきれる **小さな例（有限グラフ・玩具CW複体）** の実装。
- HDPS ツールに対する **[Spec] と明示した探索ポリシー** の実装。

ガイドライン：

- コードとドキュメントの両方で、**Core と [Spec] の境界を明示** してください。
- すべての [Spec] コンポーネントは：
  - `T_tau` 適用後の非膨張テスト、
  - δ-ledger ログ
  を含む必要があります。
- 可能であれば、T7, T10, T11, T13, T14, T15 のような **最小限テスト／例** を追加してください。

開発用コマンド：

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## Citing and references（引用）

本プロジェクト（AK–HDPST v17.0 / AK-OS v1.0）を研究等で利用する場合、次のように引用してください：

```text
AK–HDPST v17.0 / AK-OS v1.0:
High-Dimensional Projection Structural Theory and an OS for Collapse-Based Exploration

Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

基礎となる参考文献（抜粋）：

- T. Crawley-Boevey, “Decomposition of pointwise finite-dimensional persistence modules”, 2015.
- F. Chazal, V. de Silva, M. Glisse, S. Oudot,  
  “Structure and stability of persistence modules and barcodes”, 2016.

算術較正プログラムについては、別リポジトリを参照してください：

```text
AK_AP: Arithmetic Calibration Program for AK-OS
(Weil / FLT closed-world calibration)
URL: https://github.com/your-org/ak-ap   # placeholder
```

`OLD/` フォルダには AK–HDPST v1.4〜v16.0 の歴史的スナップショットが入っています。
あくまで**戒めとアーカイブ**として残しているものであり、

- 現行設計として有効なのは **v17.0＋同梱 AK_AP** のみ
- OLD 版にはスコープ過大・検証不十分な主張が含まれる可能性があります

という前提でご覧ください。

---

## License（ライセンス）

本プロジェクトは MIT License のもとで公開されています。  
詳細は `LICENSE` ファイルを参照してください。

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17874722.svg)](https://doi.org/10.5281/zenodo.17874722)

---

## Appendix: 用語チートシート

- **構成的1次元パーシステンス**：有限個の臨界点・有界ウィンドウ上で有限次元となるパーシステンス。
- **`T_tau`**：長さ ≤ `tau` のバーを削除する正確切り詰め。冪等・1-Lipschitz。
- **`C_tau`**：`T_tau` に対応するフィルタ付き持ち上げ（f.q.i. まで一意）。  
  `P_i(C_tau F) ≅ T_tau(P_i F)`。
- **B–Gate⁺**：Collapse ゲート（ウィンドウ単位）。  
  `PH1 = 0`, `Ext1 = 0`（振幅 ≤ 1）、`(mu, nu) = (0, 0)`, `gap_tau > sum_delta` を要求。
- **Overlap Gate**：post-collapse での局所→大域貼り合わせゲート。  
  局所同値・Čech–Ext1 アシクリック性・Stability band・δ予算をチェック。
- **`(mu, nu)`**：切り詰め後の比較射における核／余核の一般繊維次元。非ゼロなら Type IV failure。
- **Stability band**：τ の変動に対して `(mu, nu) = (0, 0)` が安定に保たれる τ 帯域。
- **PF/BC comparator**：`T_tau` 適用後のウィンドウ上で射影公式／ベースチェンジを比較する [Spec] ツール。
- **A/B soft-commuting**：入れ子でない反射子の近似可換性テスト。`Delta_comm ≤ eta` か、そうでなければ順序変更＋δログ。
- **`Lambda_len`**：長さスペクトル作用素。ウィンドウごとの切り詰めバー長多重集合を返し、`T_tau` 後同型に対して不変。
- **HDPS**：High-Dimensional Projection Search。パラメータ空間上に Map of Validity を構成する探索エンジン（[Spec]）。
- **Terrain Cell**：Collapse 挙動がほぼ一様とみなせる局所パラメータ領域。
- **Map of Validity**：Terrain Cell ごとに `Valid / Obstructed / Unknown` を付与した有効性マップ。Core ゲート・塔診断と整合。
