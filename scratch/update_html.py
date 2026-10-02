# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Printing metrics in index.html
html = html.replace(
    '<span class="metric-card__val metric-card__val--accent" id="metricOutput">单版单本（受限）</span>',
    '<span class="metric-card__val metric-card__val--accent" id="metricOutput">单版单本</span>'
)

# 2. Add Chip Lab into Chapter 6 inside #chipStage
old_chip_stage_end = '''        </div>
      </div>

      <div class="chip-lines reveal">'''

new_chip_lab = '''        </div>
      </div>

      <!-- 芯片动手实验台 (Interactive Chip Lab) -->
      <div class="chip-lab reveal" id="chipLab">
        <div class="chip-lab__header">
          <div class="chip-lab__title-box">
            <span class="chip-lab__badge">上手体验 · HARDWARE LAB</span>
            <h3 class="chip-lab__title">芯片微架构与汉字运载动手实验台</h3>
          </div>
          <div class="chip-lab__plain-hint" id="labPlainHint">
            💡 <strong>通俗白话速懂</strong>：<span id="labHintText">CPU 像精细钟表匠，时钟以 5.1GHz 极速震荡，逐条指令把「国」字拆为 3 个机器字节（E5 9B BD）进行移位搬运；而昇腾 NPU 则是立体印刷流水线，把汉字映射为 4096 维张量，在 3D Cube 阵列中以每秒数十万亿次并行压印计算！</span>
          </div>
        </div>

        <div class="chip-lab__body">
          <!-- Intel 实验控制区 -->
          <div class="lab-panel lab-panel--intel" id="labPanelIntel">
            <div class="lab-panel__top">
              <span class="panel-label">Intel® Core™ x86-64 标量运算视窗</span>
              <span class="panel-clock" id="intelClockDisplay">时钟: 5.1 GHz · 运行中</span>
            </div>
            
            <div class="register-visual">
              <span class="reg-label">RAX 64-bit 物理寄存器状态：</span>
              <div class="reg-slots" id="regSlots">
                <span class="reg-byte" data-b="0">00</span>
                <span class="reg-byte" data-b="1">00</span>
                <span class="reg-byte" data-b="2">00</span>
                <span class="reg-byte" data-b="3">00</span>
                <span class="reg-byte" data-b="4">00</span>
                <span class="reg-byte is-filled" data-b="5">E5</span>
                <span class="reg-byte is-filled" data-b="6">9B</span>
                <span class="reg-byte is-filled" data-b="7">BD</span>
              </div>
              <span class="reg-note" id="regNote">UTF-8 机器码 [E5 9B BD] 载入 RAX 寄存器低 24 位</span>
            </div>

            <div class="lab-actions">
              <button class="lab-btn" id="btnLoadRax">① 写入 RAX 寄存器 (MOVQ)</button>
              <button class="lab-btn" id="btnShrqRax">② 8位字节逻辑右移 (SHRQ)</button>
              <button class="lab-btn" id="btnL3Probe">③ 探测 L3 缓存 (Ring Bus)</button>
            </div>
          </div>

          <!-- 昇腾 实验控制区 -->
          <div class="lab-panel lab-panel--ascend" id="labPanelAscend" style="display: none;">
            <div class="lab-panel__top">
              <span class="panel-label">华为昇腾 Ascend 910B 3D Cube 张量运算视窗</span>
              <span class="panel-clock">3D Cube: 320 TFLOPS (FP16)</span>
            </div>

            <div class="cube-visual">
              <span class="reg-label">DaVinci 3D Cube 16×16×16 矩阵乘阵列网格状态：</span>
              <div class="cube-grid-box" id="cubeGridBox">
                <!-- 16个矩阵计算单元格 -->
                <i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i>
                <i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i>
                <i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i>
                <i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i><i class="cube-cell"></i>
              </div>
              <span class="reg-note" id="cubeNote">Query × Key_T 矩阵乘法单元就绪，单周期执行 4096 次乘加 (MACs)</span>
            </div>

            <div class="lab-actions">
              <button class="lab-btn lab-btn--ascend" id="btnHbmPull">① HBM2E 显存拉取词向量</button>
              <button class="lab-btn lab-btn--ascend" id="btnCubeMatmul">② 3D Cube 矩阵乘点火 (MatMul)</button>
              <button class="lab-btn lab-btn--ascend" id="btnVectorSoftmax">③ Vector Softmax 概率归一</button>
            </div>
          </div>
        </div>
      </div>

      <div class="chip-lines reveal">'''

html = html.replace(old_chip_stage_end, new_chip_lab)

# 3. Update Chapter 7 AI (horizontal feature bar + 3 columns including linear projection + softmax)
old_ai_start = '<div class="transformer-pipeline reveal" id="transformerPipeline">'
old_ai_end = '      <p class="scene-copy reveal">字形 → 字符 → 编码 → 数据 → Transformer 注意力与解码涌现。<br>千年一字，在百亿参数的神经网络中凝聚为对文明最深沉的理解。</p>'

idx_ai_start = html.find(old_ai_start)
idx_ai_end = html.find(old_ai_end)
if idx_ai_start == -1 or idx_ai_end == -1:
    print("Error: AI section boundaries not found in index.html")
    import sys; sys.exit(1)

new_ai_html = '''<div class="transformer-pipeline reveal" id="transformerPipeline">
        <!-- 顶部：横向输入特征提取流水线 (字形 ➔ 字符 ➔ 编码 ➔ 数据) -->
        <div class="pipeline-feature-row" id="pipelineFeatureRow">
          <div class="feature-row-head">
            <span class="row-tag">01~04 输入特征提取 · FEATURE EXTRACTION (横向流式布局)</span>
            <span class="row-sub">汉字视觉符号 ➔ 4096维连续语义空间张量</span>
          </div>
          <div class="feature-steps-bar">
            <!-- 阶段1: 字形 -->
            <div class="pipeline-step step--glyph is-active" id="stepGlyph">
              <span class="step-num">01</span>
              <div class="step-content">
                <div class="step-header">
                  <span class="step-name">字形</span>
                  <span class="step-sub">Visual Glyph</span>
                </div>
                <div class="step-visual step-visual--char">国</div>
                <div class="step-desc">笔画骨架与字体栅格点阵</div>
              </div>
            </div>

            <div class="pipeline-arrow-right">➔</div>

            <!-- 阶段2: 字符 -->
            <div class="pipeline-step step--token" id="stepToken">
              <span class="step-num">02</span>
              <div class="step-content">
                <div class="step-header">
                  <span class="step-name">字符 (Token)</span>
                  <span class="step-sub">Token ID</span>
                </div>
                <div class="token-badge">Token: "国" · ID #7654</div>
                <div class="step-desc">分词器离散符号映射</div>
              </div>
            </div>

            <div class="pipeline-arrow-right">➔</div>

            <!-- 阶段3: 编码 -->
            <div class="pipeline-step step--encode" id="stepEncode">
              <span class="step-num">03</span>
              <div class="step-content">
                <div class="step-header">
                  <span class="step-name">字符编码</span>
                  <span class="step-sub">Encoding</span>
                </div>
                <div class="code-badge">U+56FD · E5 9B BD</div>
                <div class="step-desc">计算机底层统一数字码</div>
              </div>
            </div>

            <div class="pipeline-arrow-right">➔</div>

            <!-- 阶段4: 数据 -->
            <div class="pipeline-step step--data" id="stepData">
              <span class="step-num">04</span>
              <div class="step-content">
                <div class="step-header">
                  <span class="step-name">数据 (Embedding)</span>
                  <span class="step-sub">高维稠密连续向量</span>
                </div>
                <div class="vector-preview" id="vectorPreview">
                  <span>[+0.382,</span><span>-0.714,</span><span>+0.891, ... -0.450]</span>
                </div>
                <div class="step-desc">4096维连续语义空间坐标</div>
              </div>
            </div>
          </div>
        </div>

        <!-- 向量注入过渡条 -->
        <div class="feature-to-neural-flow">
          <div class="flow-pulse-line"></div>
          <span class="flow-pulse-label">⬇ 4096维高维连续语义向量注入 Transformer 深度认知与概率分布网络 ⬇</span>
        </div>

        <!-- 核心三列并行全景：①Transformer核心 ➔ ②线性投影与Softmax(独立列) ➔ ③预测词表 -->
        <div class="pipeline-3col-grid" id="pipeline3ColGrid">
          <!-- 第1列：Transformer 核心架构 (Encoder / Decoder) -->
          <div class="pipeline-col col--backbone">
            <div class="col-title">① TRANSFORMER 核心架构 (ENCODER / DECODER)</div>
            <div class="model-block model-block--encoder" id="blockEncoder">
              <div class="model-badge">海量语料预训练 · ENCODER</div>
              <div class="layer-title">多头自注意力机制 (Multi-Head Attention)</div>
              <div class="attention-matrix">
                <span class="att-head" id="head1">Head 1: 华夏/文明 (0.94)</span>
                <span class="att-head" id="head2">Head 2: 政治/政权 (0.89)</span>
                <span class="att-head" id="head3">Head 3: 疆域/万姓 (0.86)</span>
              </div>
              <div class="layer-sub">前馈网络 (FFN) + LayerNorm 残差连接</div>
            </div>

            <div class="trans-flow-arrow">⬇ 跨注意力 (Cross-Attention) 深度交互</div>

            <div class="model-block model-block--decoder" id="blockDecoder">
              <div class="model-badge">自回归解码生成 · DECODER</div>
              <div class="layer-title">因果掩码自注意力 (Causal Attention)</div>
              <div class="decoder-status" id="decoderStatus">计算后验隐状态向量 H...</div>
            </div>
          </div>

          <!-- 第2列：[线性投影 + Softmax 概率分布] 独立专列 -->
          <div class="pipeline-col col--projection" id="colProjection">
            <div class="col-title">② 线性投影 & SOFTMAX 概率分布 (独立计算列)</div>
            
            <div class="proj-block proj-block--linear" id="blockLinear">
              <div class="proj-badge">DIMENSION PROJECTION</div>
              <div class="layer-title">高维线性投影矩阵 (Linear Layer)</div>
              <div class="math-eq">未归一化分值 $\mathbf{Z} = \mathbf{H} \cdot \mathbf{W}_v + \mathbf{b}$</div>
              <div class="proj-dims">
                <span class="dim-tag">隐状态: 4096维</span>
                <span class="dim-arrow">➔</span>
                <span class="dim-tag dim-tag--vocab">词表空间: 150,000维</span>
              </div>
              <div class="layer-sub">将高维抽象语义投射至庞大汉字词汇表</div>
            </div>

            <div class="trans-flow-arrow">⬇ 指数归一化激活 (Normalized Probability)</div>

            <div class="proj-block proj-block--softmax" id="blockSoftmax">
              <div class="proj-badge">EXPONENTIAL NORMALIZATION</div>
              <div class="layer-title">Softmax 概率归一化函数</div>
              <div class="math-formula">
                $P(w_i) = \frac{\exp(z_i / \tau)}{\sum_j \exp(z_j / \tau)}$
              </div>
              <div class="softmax-specs">
                <span class="spec-item">温度调节系数 $\tau = 0.7$</span>
                <span class="spec-item spec-item--active" id="softmaxStatus">概率分布已收敛锁定 ✓</span>
              </div>
              <div class="layer-sub">将全实数分值转换为严格归一化概率分布</div>
            </div>
          </div>

          <!-- 第3列：输出预测词表 -->
          <div class="pipeline-col col--vocab" id="colVocab">
            <div class="col-title">③ 预测词表概率分布 · CANDIDATES</div>
            <div class="output-vocab-list" id="outputVocabList">
              <div class="vocab-header">
                <span>预测关联词语</span>
                <span>置信度</span>
              </div>
              <div class="vocab-item" data-word="中国">
                <span class="vocab-word">中国</span>
                <div class="vocab-bar-box"><div class="vocab-bar" style="width: 86%;"></div></div>
                <span class="vocab-prob">86.4%</span>
              </div>
              <div class="vocab-item is-highlight" data-word="国家">
                <span class="vocab-word">国家 <span class="vocab-tag">核心语义</span></span>
                <div class="vocab-bar-box"><div class="vocab-bar vocab-bar--prime" style="width: 98%;"></div></div>
                <span class="vocab-prob vocab-prob--prime">98.2%</span>
              </div>
              <div class="vocab-item" data-word="国土">
                <span class="vocab-word">国土</span>
                <div class="vocab-bar-box"><div class="vocab-bar" style="width: 68%;"></div></div>
                <span class="vocab-prob">68.5%</span>
              </div>
              <div class="vocab-item" data-word="国民">
                <span class="vocab-word">国民</span>
                <div class="vocab-bar-box"><div class="vocab-bar" style="width: 53%;"></div></div>
                <span class="vocab-prob">53.1%</span>
              </div>
              <div class="vocab-item" data-word="国运">
                <span class="vocab-word">国运</span>
                <div class="vocab-bar-box"><div class="vocab-bar" style="width: 42%;"></div></div>
                <span class="vocab-prob">42.0%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

html = html[:idx_ai_start] + new_ai_html + html[idx_ai_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully!")
