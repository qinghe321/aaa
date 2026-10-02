# -*- coding: utf-8 -*-
import sys

with open("js/main.js", "r", encoding="utf-8") as f:
    code = f.read()

# -------------------------------------------------------------
# Part 1: Fix bamboo array glitch & click to select bamboo slip
# -------------------------------------------------------------
pos_glitch = code.find("];,")
if pos_glitch == -1:
    print("Error: pos_glitch not found")
    sys.exit(1)

pos_slipElements = code.find("const slipElements = [];", pos_glitch)
if pos_slipElements == -1:
    print("Error: pos_slipElements not found")
    sys.exit(1)

# Remove duplicated entries between pos_glitch and pos_slipElements
code = code[:pos_glitch] + "];\n\n  " + code[pos_slipElements:]

# Now replace the bamboo slip generation & indicator & click handler
old_bamboo_block_start = code.find("const slipElements = [];")
old_bamboo_block_end = code.find("bambooViewport.addEventListener(\"pointerdown\"", old_bamboo_block_start)

new_bamboo_block = '''const slipElements = [];
  let currentSlipIdx = 0;
  bambooSlipsData.forEach((item, idx) => {
    const slip = document.createElement("div");
    slip.className = "slip" + (item.isKey ? " slip--key" : "") + (idx === 0 ? " is-active" : "");
    slip.innerHTML =
      '<div class="slip-glyph-box" aria-label="' + item.char + '">' + item.svg + '</div>' +
      '<span class="slip-tag">' + item.stage + '</span>';
    slip.dataset.index = idx;
    slip.dataset.char = item.char;
    slip.dataset.stage = item.detail;
    slip.addEventListener("click", () => {
      if (!dragMoved) {
        selectBambooSlip(idx);
      }
    });
    bambooTrack.appendChild(slip);
    slipElements.push(slip);
  });

  let tx = 0, scale = 1;
  let minX = 0, maxX = 0;
  let dragging = false, dragMoved = false;
  let startX = 0, startTX = 0;
  let vel = 0, lastX = 0, lastT = 0, momentumId = 0;
  let centered = false;

  function selectBambooSlip(idx) {
    if (idx < 0 || idx >= slipElements.length) return;
    currentSlipIdx = idx;
    slipElements.forEach((s, i) => s.classList.toggle("is-active", i === idx));
    const item = bambooSlipsData[idx];
    const bEra = $("#bambooCardEra");
    const bSource = $("#bambooCardSource");
    const bTitle = $("#bambooCardTitle");
    const bReason = $("#bambooCardReason");
    if (bEra) bEra.textContent = item.era;
    if (bSource) bSource.textContent = item.source;
    if (bTitle) bTitle.textContent = item.title;
    if (bReason) bReason.textContent = item.reason;
    if (bambooIndChar) bambooIndChar.textContent = item.char;
    if (bambooIndStage) bambooIndStage.textContent = item.detail;

    // 平滑平移居中该竹简
    cancelAnimationFrame(momentumId);
    const targetSlip = slipElements[idx];
    const viewW = bambooViewport.clientWidth;
    const slipCenter = (targetSlip.offsetLeft + targetSlip.offsetWidth / 2) * scale;
    const targetTX = Math.max(minX, Math.min(maxX, viewW / 2 - slipCenter));
    const startXVal = tx;
    const diff = targetTX - startXVal;
    const startTime = performance.now();
    const duration = 380;

    function animCenter(now) {
      const elapsed = now - startTime;
      const progress = Math.min(1, elapsed / duration);
      const ease = 1 - Math.pow(1 - progress, 3);
      tx = startXVal + diff * ease;
      bambooTrack.style.transform = "translateX(" + tx + "px) scale(" + scale + ")";
      if (progress < 1) {
        momentumId = requestAnimationFrame(animCenter);
      } else {
        applyBamboo();
      }
    }
    momentumId = requestAnimationFrame(animCenter);
  }

  function updateBambooIndicator() {
    if (!bambooIndChar || !bambooIndStage || !bambooViewport || slipElements.length === 0) return;
    const viewRect = bambooViewport.getBoundingClientRect();
    const viewCenter = viewRect.left + viewRect.width / 2;
    let closestItem = bambooSlipsData[0];
    let closestIdx = 0;
    let minDistance = Infinity;

    slipElements.forEach((slip, idx) => {
      const rect = slip.getBoundingClientRect();
      const slipCenter = rect.left + rect.width / 2;
      const dist = Math.abs(slipCenter - viewCenter);
      if (dist < minDistance) {
        minDistance = dist;
        closestItem = bambooSlipsData[idx];
        closestIdx = idx;
      }
    });

    bambooIndChar.textContent = closestItem.char;
    bambooIndStage.textContent = closestItem.detail;
    slipElements.forEach((s, i) => s.classList.toggle("is-active", i === closestIdx));
    const bEra = $("#bambooCardEra");
    const bSource = $("#bambooCardSource");
    const bTitle = $("#bambooCardTitle");
    const bReason = $("#bambooCardReason");
    if (bEra) bEra.textContent = closestItem.era;
    if (bSource) bSource.textContent = closestItem.source;
    if (bTitle) bTitle.textContent = closestItem.title;
    if (bReason) bReason.textContent = closestItem.reason;
  }

  function applyBamboo() {
    bambooTrack.style.transform = "translateX(" + tx + "px) scale(" + scale + ")";
    updateBambooIndicator();
  }
  function measureBamboo() {
    const trackW = bambooTrack.scrollWidth * scale;
    const viewW = bambooViewport.clientWidth;
    minX = Math.min(0, viewW - trackW - 16);
    maxX = 16;
    if (!centered) {
      const first = slipElements[0];
      if (first) {
        const kc = (first.offsetLeft + first.offsetWidth / 2) * scale;
        tx = viewW / 2 - kc;
        centered = true;
      }
    }
    tx = Math.max(minX, Math.min(maxX, tx));
    applyBamboo();
  }
  measureBamboo();
  window.addEventListener("resize", measureBamboo);

  // 扫描光跟随鼠标
  bambooViewport.addEventListener("pointermove", (e) => {
    if (scanLight) {
      const r = bambooViewport.getBoundingClientRect();
      scanLight.style.left = (e.clientX - r.left - 60) + "px";
    }
  });

  '''

code = code[:old_bamboo_block_start] + new_bamboo_block + code[old_bamboo_block_end:]
print("Part 1 (Bamboo) successfully updated")

# -------------------------------------------------------------
# Part 2: Section 6 Printing (Woodblock vs Movable Type)
# -------------------------------------------------------------
h7_idx = code.find("6. 第三幕 · 印刷")
if h7_idx == -1:
    print("Error: h7_idx not found")
    sys.exit(1)
# Back up to comment start
h7_start = code.rfind("/* ============================================================", 0, h7_idx)

h8_idx = code.find("7. 第四幕 · 电与通信")
h8_start = code.rfind("/* ============================================================", 0, h8_idx)

new_print_code = '''/* ============================================================
     6. 第三幕 · 印刷：雕版（单版死字） vs 活字（以字生万卷）
  ============================================================ */
  const printModeBtns = $$(".print-mode-btn");
  const printClassics = $("#printClassics");
  const classicPills = $$(".classic-pill");
  const printViewBlock = $("#printViewBlock");
  const printViewType = $("#printViewType");
  const woodblockGrid = $("#woodblockGrid");
  const blockTryNewBtn = $("#blockTryNewBtn");
  const blockWarning = $("#blockWarning");
  const typeTrayGrid = $("#typeTrayGrid");
  const pressGrid = $("#pressGrid");
  const pressBookTitle = $("#pressBookTitle");
  const pressStatus = $("#pressStatus");
  const metricReuse = $("#metricReuse");
  const metricTime = $("#metricTime");
  const metricOutput = $("#metricOutput");

  // 经典典籍数据源
  const classicsData = {
    datong: {
      name: "《礼记·大同篇》",
      title: "当前排印：《礼记·礼运大同篇》",
      chars: Array.from("大道之行也天下为公选贤与能讲信修睦故人不独亲其亲不独子其子")
    },
    qianziwen: {
      name: "《千字文》",
      title: "当前排印：《千字文·开篇》",
      chars: Array.from("天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往秋收冬藏闰余成岁")
    },
    yueyang: {
      name: "《岳阳楼记》",
      title: "当前排印：《岳阳楼记·名篇》",
      chars: Array.from("先天下之忧而忧后天下之乐而乐居庙堂之高则忧其民处江湖之远")
    }
  };

  // 雕版初始化：死死刻好的《大同篇》前24字
  if (woodblockGrid) {
    const blockChars = classicsData.datong.chars;
    woodblockGrid.innerHTML = "";
    blockChars.forEach((ch) => {
      const d = document.createElement("div");
      d.className = "wood-char";
      d.textContent = ch;
      woodblockGrid.appendChild(d);
    });
  }

  // 雕版“尝试印新书”警告
  let blockWarnTimer = 0;
  if (blockTryNewBtn) {
    blockTryNewBtn.addEventListener("click", () => {
      clearTimeout(blockWarnTimer);
      if (printViewBlock) {
        printViewBlock.classList.remove("shake-effect");
        void printViewBlock.offsetWidth;
        printViewBlock.classList.add("shake-effect");
      }
      if (blockWarning) {
        blockWarning.style.display = "block";
        blockWarnTimer = setTimeout(() => {
          blockWarning.style.display = "none";
        }, 3600);
      }
    });
  }

  // 毕昇泥活字字盘库（从三部经典中提取字模，随取随排）
  const traySet = new Set();
  Object.values(classicsData).forEach((item) => item.chars.forEach((c) => traySet.add(c)));
  const trayChars = Array.from(traySet);
  if (typeTrayGrid) {
    typeTrayGrid.innerHTML = "";
    trayChars.forEach((ch) => {
      const cell = document.createElement("div");
      cell.className = "tray-cell";
      cell.textContent = ch;
      cell.dataset.char = ch;
      typeTrayGrid.appendChild(cell);
    });
  }

  // 活字飞入拼排动画
  let typeAnimTimer = 0;
  function composeClassic(bookKey) {
    clearTimeout(typeAnimTimer);
    const data = classicsData[bookKey] || classicsData.datong;
    if (pressBookTitle) pressBookTitle.textContent = data.title;
    if (pressStatus) {
      pressStatus.textContent = "字模重组调度中…";
      pressStatus.classList.remove("ready");
    }
    if (!pressGrid) return;
    pressGrid.innerHTML = "";

    // 高亮字盘中将被选中的字模
    const trayCells = $$(".tray-cell", typeTrayGrid);
    trayCells.forEach((c) => c.classList.remove("in-use"));
    data.chars.forEach((ch) => {
      const match = trayCells.find((c) => c.dataset.char === ch);
      if (match) match.classList.add("in-use");
    });

    data.chars.forEach((ch, i) => {
      const typeEl = document.createElement("div");
      typeEl.className = "press-type-cell";
      typeEl.textContent = ch;
      typeEl.style.opacity = "0";
      typeEl.style.transform = "scale(0.3) translateY(-18px)";
      pressGrid.appendChild(typeEl);

      setTimeout(() => {
        typeEl.style.transition = "all 0.35s cubic-bezier(0.2, 0.9, 0.3, 1.2)";
        typeEl.style.opacity = "1";
        typeEl.style.transform = "scale(1) translateY(0)";
      }, i * 36);
    });

    typeAnimTimer = setTimeout(() => {
      if (pressStatus) {
        pressStatus.textContent = "字模飞入排版就绪 ✓";
        pressStatus.classList.add("ready");
      }
    }, data.chars.length * 36 + 200);
  }

  // 印刷模式切换（雕版 vs 活字）
  function setPrintMode(mode) {
    printModeBtns.forEach((b) => b.classList.toggle("is-active", b.dataset.mode === mode));
    if (mode === "type") {
      if (printViewBlock) printViewBlock.style.display = "none";
      if (printViewType) printViewType.style.display = "block";
      if (printClassics) printClassics.style.display = "flex";
      if (metricReuse) metricReuse.textContent = "100%（字模无限循环重组）";
      if (metricTime) metricTime.textContent = "半日（拆卸拼排立等可印）";
      if (metricOutput) {
        metricOutput.textContent = "万卷齐发（文明信息大爆发）";
        metricOutput.classList.add("metric-card__val--accent");
      }
      composeClassic("datong");
    } else {
      if (printViewBlock) printViewBlock.style.display = "block";
      if (printViewType) printViewType.style.display = "none";
      if (printClassics) printClassics.style.display = "none";
      if (metricReuse) metricReuse.textContent = "0%（单版死字不可改）";
      if (metricTime) metricTime.textContent = "数月至一年（重砍木板重雕版）";
      if (metricOutput) {
        metricOutput.textContent = "单版单本（品种受限）";
        metricOutput.classList.remove("metric-card__val--accent");
      }
    }
  }

  printModeBtns.forEach((btn) => {
    btn.addEventListener("click", () => setPrintMode(btn.dataset.mode));
  });

  classicPills.forEach((pill) => {
    pill.addEventListener("click", () => {
      classicPills.forEach((p) => p.classList.remove("is-active"));
      pill.classList.add("is-active");
      composeClassic(pill.dataset.book);
    });
  });

  '''

code = code[:h7_start] + new_print_code + code[h8_start:]
print("Part 2 (Printing) successfully updated")

# -------------------------------------------------------------
# Part 3: Section 9 Chip (Intel Core Ultra vs HUAWEI Ascend 910B)
# -------------------------------------------------------------
h10_idx = code.find("9. 第六幕 · 芯片")
if h10_idx == -1:
    print("Error: h10_idx not found")
    sys.exit(1)
h10_start = code.rfind("/* ============================================================", 0, h10_idx)

h11_idx = code.find("10. 第七幕 · AI")
h11_start = code.rfind("/* ============================================================", 0, h11_idx)

new_chip_code = '''/* ============================================================
     9. 第六幕 · 芯片：Intel Core Ultra vs 华为昇腾 910B 专业微架构
  ============================================================ */
  const chipTabs = $$(".chip-tab");
  const chipViews = $$(".chip-arch-view");

  const chipUnitDescriptions = {
    pcore: {
      title: "P-Core Redwood Cove 流水线执行中",
      lines: [
        '<span class="c-kw">FETCH_DECODE:</span> 6-wide 乱序执行超标量指令窗',
        '<span class="c-kw">MOVQ</span>  <span class="c-reg">RAX</span>, 0x0000000000E59BBD <span class="c-comment">; 将「国」UTF-8 装入 64位 RAX 寄存器</span>',
        '<span class="c-kw">EXEC_LATENCY:</span> <span class="c-val">0.24 ns</span> | <span class="c-kw">BRANCH_PRED:</span> <span class="c-val">99.7%</span> | <span class="c-kw">IPC:</span> <span class="c-val">4.12</span>'
      ]
    },
    ecore: {
      title: "E-Core Crestmont 能效核心并发集群",
      lines: [
        '<span class="c-kw">THREAD_POOL:</span> 8 线程高能效集群并行解析字符流',
        '<span class="c-kw">SHRQ</span>  <span class="c-reg">RAX</span>, 0x08 <span class="c-comment">; 8位字节对齐移位，并行执行 UTF-8 解码</span>',
        '<span class="c-kw">POWER_DRAW:</span> <span class="c-val">1.2W</span> | <span class="c-kw">CLUSTER_THROUGHPUT:</span> <span class="c-val">1.8 Gops/W</span>'
      ]
    },
    l3: {
      title: "Shared L3 Smart Cache (24MB 环形总线高速互联)",
      lines: [
        '<span class="c-kw">RING_BUS:</span> 双向时钟 4.8GHz 高速互联环路',
        '<span class="c-kw">L3_PROBE:</span> TAG_MATCH hit for Unicode [U+56FD]',
        '<span class="c-kw">L3_HIT_RATE:</span> <span class="c-val">98.6%</span> | <span class="c-kw">CACHE_LATENCY:</span> <span class="c-val">11.2 ns</span>'
      ]
    },
    imc: {
      title: "Integrated Memory Controller (DDR5-5600 双通道)",
      lines: [
        '<span class="c-kw">DRAM_ACCESS:</span> DDR5 64-bit 突发传输通道',
        '<span class="c-kw">BURST_READ:</span> 批量载入中文汉字字符字库点阵表',
        '<span class="c-kw">BANDWIDTH:</span> <span class="c-val">89.6 GB/s</span> | <span class="c-kw">BUS_UTIL:</span> <span class="c-val">28.4%</span>'
      ]
    },
    cube: {
      title: "DaVinci 3D Cube 阵列 (16×16×16 矩阵乘加张量核心)",
      lines: [
        '<span class="c-kw">cube::MatMul</span>(Tensor_Q[1, 64, 64], Tensor_K_T[1, 64, 64]) <span class="c-comment">// Cube 16×16 矩阵乘加速</span>',
        '<span class="c-kw">FP16_MACC:</span> 单周期并行执行 4096 次乘加运算 (MACs)',
        '<span class="c-kw">TENSOR_TFLOPS:</span> <span class="c-val">318.6 TFLOPS</span> | <span class="c-kw">CUBE_UTIL:</span> <span class="c-val">94.8%</span>'
      ]
    },
    vector: {
      title: "Vector 计算单元 (Softmax & LayerNorm 矢量激活流水线)",
      lines: [
        '<span class="c-kw">vector::Softmax</span>(Score_Matrix, FP16) <span class="c-comment">// Vector 执行自注意力归一化</span>',
        '<span class="c-kw">vector::LayerNorm</span>(Hidden_States, Epsilon=1e-5)',
        '<span class="c-kw">VECTOR_LATENCY:</span> <span class="c-val">0.05 ms</span> | <span class="c-kw">ALU_WIDTH:</span> <span class="c-val">256-bit SIMD</span>'
      ]
    },
    scalar: {
      title: "Scalar 标量计算单元 (程序控制流与地址计算)",
      lines: [
        '<span class="c-kw">scalar::Branch</span>(Condition=Loop_Done) <span class="c-comment">// Transformer 层迭代控制</span>',
        '<span class="c-kw">scalar::AddrGen</span>(Base_Addr=0x7F00, Offset=Token_ID*4096)',
        '<span class="c-kw">CYCLE_COUNT:</span> <span class="c-val">124 cycles</span> | <span class="c-kw">STATUS:</span> <span class="c-val">NORMAL</span>'
      ]
    },
    hbm: {
      title: "32GB HBM2E 堆叠显存 (1.2TB/s 极致带宽)",
      lines: [
        '<span class="c-kw">acl::EmbeddingLookup</span>(TokenID=<span class="c-val">7654</span>, Dim=<span class="c-val">4096</span>) <span class="c-comment">// 显存读取 4096 维词向量</span>',
        '<span class="c-kw">SILICON_INTERPOSER:</span> 4层 3D 硅通孔 (TSV) 超宽位宽总线',
        '<span class="c-kw">HBM_THROUGHPUT:</span> <span class="c-val">1192 GB/s</span> | <span class="c-kw">READ_EFFICIENCY:</span> <span class="c-val">99.1%</span>'
      ]
    }
  };

  chipTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      chipTabs.forEach((t) => t.classList.remove("is-active"));
      tab.classList.add("is-active");
      const targetChip = tab.dataset.chip;
      chipViews.forEach((v) => {
        const isMatch = v.dataset.view === targetChip;
        v.style.display = isMatch ? "block" : "none";
        v.classList.toggle("is-active", isMatch);
      });
    });
  });

  // 单元点击/悬停实时更新微架构监视器
  const allDieUnits = $$("[data-unit]");
  allDieUnits.forEach((unit) => {
    const unitKey = unit.dataset.unit;
    const desc = chipUnitDescriptions[unitKey];
    if (!desc) return;

    function applyUnitMonitor() {
      allDieUnits.forEach((u) => u.classList.remove("unit-focused"));
      unit.classList.add("unit-focused");
      const parentView = unit.closest(".chip-arch-view");
      if (!parentView) return;
      const titleEl = $(".monitor-title", parentView);
      const bodyEl = $(".monitor-body", parentView);
      if (titleEl) titleEl.textContent = desc.title;
      if (bodyEl) {
        bodyEl.innerHTML = desc.lines.map((l) => '<div class="code-line">' + l + "</div>").join("");
      }
    }

    unit.addEventListener("mouseenter", applyUnitMonitor);
    unit.addEventListener("click", applyUnitMonitor);
  });

  // 芯片三段文案随进入视口依次浮现
  const chipLines = $(".chip-lines");
  const chipLinesObs = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) { chipLines.classList.add("in"); chipLinesObs.disconnect(); } });
  }, { threshold: 0.4 });
  chipLinesObs.observe(chipLines);

  '''

code = code[:h10_start] + new_chip_code + code[h11_start:]
print("Part 3 (Chip) successfully updated")

# -------------------------------------------------------------
# Part 4: Section 10 AI (Left-to-Right Flow + 0.8x Transformer loop)
# -------------------------------------------------------------
h11_idx = code.find("10. 第七幕 · AI")
if h11_idx == -1:
    print("Error: h11_idx not found after replacement")
    sys.exit(1)
h11_start = code.rfind("/* ============================================================", 0, h11_idx)

h12_idx = code.find("11. 尾声")
h12_start = code.rfind("/* ============================================================", 0, h12_idx)

new_ai_code = '''/* ============================================================
     10. 第七幕 · 人工智能：左右全景 Transformer 认知架构 (0.8x 自动推演)
  ============================================================ */
  const aiPlayBtn = $("#aiPlayBtn");
  const playIcon = $("#playIcon");
  const playText = $("#playText");
  const stepGlyph = $("#stepGlyph");
  const stepToken = $("#stepToken");
  const stepEncode = $("#stepEncode");
  const stepData = $("#stepData");
  const bridgeStream = $("#bridgeStream");
  const blockEncoder = $("#blockEncoder");
  const blockDecoder = $("#blockDecoder");
  const head1 = $("#head1");
  const head2 = $("#head2");
  const head3 = $("#head3");
  const decoderStatus = $("#decoderStatus");
  const vocabItems = $$(".vocab-item");

  let aiIsPlaying = true;
  let aiCycleTimer = null;
  let aiCycleStart = 0;
  const cycleDuration = 9600; // 0.8倍速慢速叙事流循环周期 9.6s

  const stepsList = [stepGlyph, stepToken, stepEncode, stepData];
  const headsList = [head1, head2, head3];

  function runAiStep(elapsed) {
    // 0.0s - 0.9s: 步骤01 字形
    stepGlyph.classList.toggle("is-active", elapsed >= 0 && elapsed < 9200);
    // 1.0s: 步骤02 字符 Token
    stepToken.classList.toggle("is-active", elapsed >= 1000 && elapsed < 9200);
    // 2.0s: 步骤03 字符编码
    stepEncode.classList.toggle("is-active", elapsed >= 2000 && elapsed < 9200);
    // 3.0s: 步骤04 4096维向量 Embedding
    stepData.classList.toggle("is-active", elapsed >= 3000 && elapsed < 9200);

    // 3.8s: 中间神经网络流光桥梁激活
    if (bridgeStream) {
      bridgeStream.classList.toggle("flowing", elapsed >= 3800 && elapsed < 9200);
    }

    // 4.6s: 右侧 Transformer Encoder 多头注意力激活
    if (blockEncoder) {
      blockEncoder.classList.toggle("active", elapsed >= 4600 && elapsed < 9200);
    }
    if (head1) head1.classList.toggle("lit", elapsed >= 4800 && elapsed < 9200);
    if (head2) head2.classList.toggle("lit", elapsed >= 5400 && elapsed < 9200);
    if (head3) head3.classList.toggle("lit", elapsed >= 6000 && elapsed < 9200);

    // 6.6s: Decoder 因果解码激活
    if (blockDecoder) {
      blockDecoder.classList.toggle("active", elapsed >= 6600 && elapsed < 9200);
    }
    if (decoderStatus) {
      if (elapsed >= 6600 && elapsed < 9200) {
        decoderStatus.textContent = "Softmax 归一化后验概率分布计算完毕 ✓";
      } else {
        decoderStatus.textContent = "计算后验词表概率分布...";
      }
    }

    // 7.4s ~ 9.0s: 词表从上到下按概率顺次点亮，国家以金色高光锁定
    const vocabDelay = [7400, 7800, 8300, 8600, 8900];
    vocabItems.forEach((item, i) => {
      const t = vocabDelay[i] || 7400;
      item.classList.toggle("lit", elapsed >= t && elapsed < 9200);
    });
  }

  function startAiCycle() {
    if (!aiIsPlaying) return;
    const now = performance.now();
    aiCycleStart = now;

    function frame() {
      if (!aiIsPlaying) return;
      const current = performance.now();
      let elapsed = (current - aiCycleStart) % cycleDuration;
      runAiStep(elapsed);
      aiCycleTimer = requestAnimationFrame(frame);
    }
    cancelAnimationFrame(aiCycleTimer);
    aiCycleTimer = requestAnimationFrame(frame);
  }

  function toggleAiPlay() {
    aiIsPlaying = !aiIsPlaying;
    if (aiIsPlaying) {
      if (aiPlayBtn) aiPlayBtn.classList.add("is-playing");
      if (playIcon) playIcon.textContent = "⏸";
      if (playText) playText.textContent = "0.8× 自动推演中";
      startAiCycle();
    } else {
      if (aiPlayBtn) aiPlayBtn.classList.remove("is-playing");
      if (playIcon) playIcon.textContent = "▶";
      if (playText) playText.textContent = "已暂停 · 点击推演";
      cancelAnimationFrame(aiCycleTimer);
    }
  }

  if (aiPlayBtn) {
    aiPlayBtn.addEventListener("click", toggleAiPlay);
  }

  // 鼠标悬停交互探查
  stepsList.forEach((st) => {
    if (!st) return;
    st.addEventListener("mouseenter", () => {
      if (aiIsPlaying) {
        cancelAnimationFrame(aiCycleTimer);
      }
      st.classList.add("is-hovered");
    });
    st.addEventListener("mouseleave", () => {
      st.classList.remove("is-hovered");
      if (aiIsPlaying) {
        startAiCycle();
      }
    });
  });

  headsList.forEach((hd) => {
    if (!hd) return;
    hd.addEventListener("mouseenter", () => {
      headsList.forEach((h) => h.classList.remove("head-hover"));
      hd.classList.add("head-hover");
    });
    hd.addEventListener("mouseleave", () => {
      hd.classList.remove("head-hover");
    });
  });

  // 默认启动 0.8x 推演流
  startAiCycle();

  '''

code = code[:h11_start] + new_ai_code + code[h12_start:]
print("Part 4 (AI) successfully updated")

# Write the updated code back to js/main.js
with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(code)

print("js/main.js written successfully! Total bytes:", len(code))
