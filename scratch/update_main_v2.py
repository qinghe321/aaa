# -*- coding: utf-8 -*-
with open("js/main.js", "r", encoding="utf-8") as f:
    js = f.read()

# -----------------------------------------------------------------
# 1. Update bambooSlipsData with 4 dummy slips before and 4 after
# -----------------------------------------------------------------
dummy_before = '''  const dummySlipsBefore = [
    {
      char: "…",
      stage: "远古刻符 · 壹",
      detail: "仰韶文化陶尊刻符 · 契刻象形萌芽（结绳画卦）",
      era: "新石器时代 · 约公元前3500年",
      source: "出土文物：仰韶文化半坡陶器刻符",
      title: "远古刻画符号 · 伏羲画卦",
      reason: "【远古渊源】在成熟文字诞生之前，先民在陶片石器上契刻抽象图腾，笔意简古，启文字之肇始。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "远古刻符 · 贰",
      detail: "大汶口文化陶文 · 日月山象形初萌",
      era: "新石器时代 · 约公元前3000年",
      source: "出土文物：大汶口文化莒县陵阳河陶尊",
      title: "大汶口象形陶文 · 仓颉遗韵",
      reason: "【远古渊源】陶尊上出现日、月、山重叠复合图案，已具备汉字会意构形的基本雏形。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "远古刻符 · 叁",
      detail: "良渚文化玉器刻符 · 神徽契纹",
      era: "新石器时代 · 约公元前2800年",
      source: "出土文物：良渚文化反山玉琮刻符",
      title: "良渚神符 · 刻镂通神",
      reason: "【远古渊源】江南水乡良渚玉器上的线刻符号，线条纤细规整，初现敬畏神圣的图腾表意功能。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "远古刻符 · 肆",
      detail: "二里头文化陶刻 · 夏墟初曙",
      era: "夏代早期 · 约公元前1800年",
      source: "出土文物：河南偃师二里头遗址陶器刻划",
      title: "二里头夏文化刻纹 · 破晓之光",
      reason: "【远古渊源】商代甲骨文之前夕，中原王朝宫殿区陶器上出现成组契刻，汉字成熟系统即将喷薄而出！",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    }
  ];

  const dummySlipsAfter = [
    {
      char: "…",
      stage: "后世流变 · 壹",
      detail: "汉代隶书 · 破圆作方（蚕头燕尾）",
      era: "两汉时期 · 约公元前200年～公元220年",
      source: "传世法书：汉《张迁碑》《乙瑛碑》拓本",
      title: "汉隶定型 · 汉字彻底脱离古文字",
      reason: "【汉唐流变】汉魏隶变是古今文字分水岭，打破小篆圆弧曲线，代之以波磔横平竖直，书写效率大幅飞跃。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "后世流变 · 贰",
      detail: "魏晋风骨 · 钟王楷则与行草流动",
      era: "魏晋南北朝 · 约公元350年",
      source: "书圣墨宝：王羲之、钟繇传世刻帖",
      title: "魏晋风度 · 笔墨生灵",
      reason: "【汉唐流变】造纸普及带动行草狂飙，文人书法自觉时代降临，汉字成为抒发性灵的高雅艺术载体。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "后世流变 · 叁",
      detail: "盛唐楷法 · 欧颜柳赵立万世范本",
      era: "隋唐时期 · 约公元700年",
      source: "国宝碑铭：《九成宫醴泉铭》《多宝塔碑》",
      title: "大唐楷书 · 极度法度与端庄气象",
      reason: "【汉唐流变】唐楷极度成熟，法度严谨、骨肉丰匀，奠定后世雕版印刷字体（宋体、仿宋）的几何基石。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    },
    {
      char: "…",
      stage: "后世流变 · 肆",
      detail: "现代规范 · 简化与数字新生（简体「国」）",
      era: "现代 · 1956年～数字时代",
      source: "权威标准：《汉字简化方案》与 Unicode 汉字标准",
      title: "数字新生 · 穿越三千年星海",
      reason: "【当代新生】由繁至简，从刻写、印版跃迁至硅基芯片与大模型，一字千年，历久弥新。",
      isKey: false,
      isDummy: true,
      svg: `<svg viewBox="0 0 79.375 79.375" class="slip-svg"><g fill="currentColor" opacity="0.6"><circle cx="20" cy="39.68" r="3.5"/><circle cx="39.68" cy="39.68" r="3.5"/><circle cx="59.36" cy="39.68" r="3.5"/></g></svg>`
    }
  ];
'''

# Find bambooSlipsData definition
bamboo_data_idx = js.find("const bambooSlipsData = [")
if bamboo_data_idx == -1:
    print("Error: bambooSlipsData not found")
    import sys; sys.exit(1)

js = js[:bamboo_data_idx] + dummy_before + "\n  " + js[bamboo_data_idx:]

# Now change `const bambooSlipsData = [` into `const rawHistoricalSlips = [`
js = js.replace("const bambooSlipsData = [", "const rawHistoricalSlips = [", 1)

# Find the end of rawHistoricalSlips and compose bambooSlipsData
old_slip_elements_start = js.find("const slipElements = [];")
compose_code = '''const bambooSlipsData = [...dummySlipsBefore, ...rawHistoricalSlips, ...dummySlipsAfter];

  const slipElements = [];
  let currentSlipIdx = 4; // 默认聚焦第1个真实历史字形（商代甲骨）
  bambooSlipsData.forEach((item, idx) => {
    const slip = document.createElement("div");
    slip.className = "slip" + (item.isKey ? " slip--key" : "") + (item.isDummy ? " slip--pad" : "") + (idx === 4 ? " is-active" : "");
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
'''

old_bamboo_loop_end = js.find("let tx = 0, scale = 1;", old_slip_elements_start)
js = js[:old_slip_elements_start] + compose_code + "\n  " + js[old_bamboo_loop_end:]

# Update measureBamboo to guarantee no clamping on real slips 1..9
old_measure_start = js.find("function measureBamboo() {")
old_measure_end = js.find("window.addEventListener(\"resize\", measureBamboo);", old_measure_start) + len('window.addEventListener("resize", measureBamboo);')

new_measure_code = '''function measureBamboo() {
    if (!bambooViewport || slipElements.length === 0) return;
    const viewW = bambooViewport.clientWidth;
    const firstSlip = slipElements[0];
    const lastSlip = slipElements[slipElements.length - 1];

    // 以两端竹简居中位置作为最极端的滑动边界，确保第1位到第9位真实竹简完全居中不受任何阻碍
    minX = viewW / 2 - (lastSlip.offsetLeft + lastSlip.offsetWidth / 2) * scale;
    maxX = viewW / 2 - (firstSlip.offsetLeft + firstSlip.offsetWidth / 2) * scale;
    if (minX > maxX) { const tmp = minX; minX = maxX; maxX = tmp; }

    if (!centered) {
      // 首次加载精准居中第1个历史字形（商代甲骨·初文，索引为4）
      const realFirst = slipElements[4];
      if (realFirst) {
        const kc = (realFirst.offsetLeft + realFirst.offsetWidth / 2) * scale;
        tx = viewW / 2 - kc;
        centered = true;
      }
    }
    tx = Math.max(minX, Math.min(maxX, tx));
    applyBamboo();
  }
  measureBamboo();
  window.addEventListener("resize", measureBamboo);'''

js = js[:old_measure_start] + new_measure_code + js[old_measure_end:]

print("1. BambooSlipsData and sliding boundaries successfully updated!")

# -----------------------------------------------------------------
# 2. Update Printing metric text
# -----------------------------------------------------------------
js = js.replace('metricOutput.textContent = "万卷齐发（文明信息大爆发）";', 'metricOutput.textContent = "万卷齐发";')
js = js.replace('metricTime.textContent = "半日（拆卸拼排立等可印）";', 'metricTime.textContent = "半日";')
js = js.replace('metricOutput.textContent = "单版单本（品种受限）";', 'metricOutput.textContent = "单版单本";')
js = js.replace('metricTime.textContent = "数月至一年（重砍木板重雕版）";', 'metricTime.textContent = "数月至一年";')
print("2. Printing metric text updated!")

# -----------------------------------------------------------------
# 3. Chapter 5: Run encode ONLY on click, not on load
# -----------------------------------------------------------------
old_run_encode_call = "runEncode();\n\n  /* ============================================================\n     9. 第六幕 · 芯片"
if old_run_encode_call in js:
    new_init_canvas = '''// 初始状态仅显示静态字形与编码，不自动播放粒子动画，等待用户主动点击「拆解」
  function initEncodeCanvas() {
    showEncode("国");
    const W = encodeCanvas.width, H = encodeCanvas.height;
    ecx.clearRect(0, 0, W, H);
    ecx.font = "600 100px serif";
    ecx.fillStyle = "#E9E4D8";
    ecx.textAlign = "center";
    ecx.textBaseline = "middle";
    ecx.fillText("国", 130, H / 2);
    
    // 提示文字
    ecx.font = "14px sans-serif";
    ecx.fillStyle = "rgba(114, 214, 208, 0.7)";
    ecx.textAlign = "left";
    ecx.fillText("👈 点击上方「拆解」按钮，观察汉字如何实时粒子化分解为 0 / 1 二进制数据流", 250, H / 2 - 8);
    ecx.font = "12px monospace";
    ecx.fillStyle = "rgba(255, 255, 255, 0.35)";
    ecx.fillText("UTF-8: E5 9B BD  |  UNICODE: U+56FD  |  TOKEN ID: 7654", 250, H / 2 + 20);
  }
  initEncodeCanvas();

  /* ============================================================
     9. 第六幕 · 芯片'''
    js = js.replace(old_run_encode_call, new_init_canvas)
    print("3. Chapter 5 Computer animation fixed to run on click!")
else:
    print("Warning: old_run_encode_call target not matched exactly, checking alternative...")
    js = js.replace("runEncode();\n\n  /* ============================================================",
                    '''function initEncodeCanvas() {
    showEncode("国");
    const W = encodeCanvas.width, H = encodeCanvas.height;
    ecx.clearRect(0, 0, W, H);
    ecx.font = "600 100px serif";
    ecx.fillStyle = "#E9E4D8";
    ecx.textAlign = "center";
    ecx.textBaseline = "middle";
    ecx.fillText("国", 130, H / 2);
    ecx.font = "14px sans-serif";
    ecx.fillStyle = "rgba(114, 214, 208, 0.7)";
    ecx.textAlign = "left";
    ecx.fillText("👈 点击上方「拆解」按钮，观察汉字如何实时粒子化分解为 0 / 1 二进制数据流", 250, H / 2);
  }
  initEncodeCanvas();

  /* ============================================================''')

# -----------------------------------------------------------------
# 4. Chapter 6 Chip Lab Interactivity & Tab Sync
# -----------------------------------------------------------------
chip_sec_start = js.find("/* ============================================================\n     9. 第六幕 · 芯片")
chip_sec_end = js.find("/* ============================================================\n     10. 第七幕")

new_chip_js = '''/* ============================================================
     9. 第六幕 · 芯片：Intel Core Ultra vs 华为昇腾 910B 专业微架构 + 动手实验台
  ============================================================ */
  const chipTabs = $$(".chip-tab");
  const chipViews = $$(".chip-arch-view");
  const labPanelIntel = $("#labPanelIntel");
  const labPanelAscend = $("#labPanelAscend");
  const labHintText = $("#labHintText");

  // Intel Lab 控件
  const btnLoadRax = $("#btnLoadRax");
  const btnShrqRax = $("#btnShrqRax");
  const btnL3Probe = $("#btnL3Probe");
  const regSlots = $("#regSlots");
  const regNote = $("#regNote");
  const regBytes = $$(".reg-byte", regSlots);

  // 昇腾 Lab 控件
  const btnHbmPull = $("#btnHbmPull");
  const btnCubeMatmul = $("#btnCubeMatmul");
  const btnVectorSoftmax = $("#btnVectorSoftmax");
  const cubeGridBox = $("#cubeGridBox");
  const cubeCells = $$(".cube-cell", cubeGridBox);
  const cubeNote = $("#cubeNote");

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
      // 联动实验台面板
      if (labPanelIntel) labPanelIntel.style.display = targetChip === "intel" ? "flex" : "none";
      if (labPanelAscend) labPanelAscend.style.display = targetChip === "ascend" ? "flex" : "none";
      if (labHintText) {
        if (targetChip === "intel") {
          labHintText.textContent = "CPU 像精细钟表匠，时钟以 5.1GHz 极速震荡，逐条指令把「国」字拆为 3 个机器字节（E5 9B BD）进行移位搬运；";
        } else {
          labHintText.textContent = "华为昇腾 NPU 则是立体印刷流水线，把「国」字映射为 4096 维连续张量，在 3D Cube 阵列中以每秒 320 万亿次乘加极速轰鸣！";
        }
      }
    });
  });

  // Intel Lab 实验交互
  if (btnLoadRax) {
    btnLoadRax.addEventListener("click", () => {
      regBytes.forEach((b, i) => {
        b.classList.remove("pulse-active");
        if (i < 5) { b.textContent = "00"; b.classList.remove("is-filled"); }
      });
      regBytes[5].textContent = "E5"; regBytes[5].classList.add("is-filled", "pulse-active");
      regBytes[6].textContent = "9B"; regBytes[6].classList.add("is-filled", "pulse-active");
      regBytes[7].textContent = "BD"; regBytes[7].classList.add("is-filled", "pulse-active");
      if (regNote) regNote.textContent = "✅ MOVQ 执行完毕：64位 RAX 寄存器装入「国」字 UTF-8 机器码 [0x0000000000E59BBD]";
    });
  }
  if (btnShrqRax) {
    btnShrqRax.addEventListener("click", () => {
      regBytes.forEach((b) => b.classList.add("pulse-active"));
      regBytes[5].textContent = "00"; regBytes[5].classList.remove("is-filled");
      regBytes[6].textContent = "E5"; regBytes[6].classList.add("is-filled");
      regBytes[7].textContent = "9B"; regBytes[7].classList.add("is-filled");
      if (regNote) regNote.textContent = "✅ SHRQ RAX, 8 移位完毕：RAX 变为 [0x000000000000E59B]，成功对齐高位字节！";
    });
  }
  if (btnL3Probe) {
    btnL3Probe.addEventListener("click", () => {
      regBytes.forEach((b) => b.classList.add("pulse-active"));
      if (regNote) regNote.textContent = "⚡ L3 高速缓存探针命中 (TAG_MATCH)：Ring Bus 环形总线高速传输，延迟从内存 80ns 骤降为 11.2ns！";
    });
  }

  // 昇腾 Lab 实验交互
  if (btnHbmPull) {
    btnHbmPull.addEventListener("click", () => {
      cubeCells.forEach((c, i) => {
        setTimeout(() => c.classList.toggle("active", i % 2 === 0), i * 30);
      });
      if (cubeNote) cubeNote.textContent = "🚀 HBM2E 显存总线激活：以 1.2 TB/s 超高带宽将「国」字 4096 维 Token 向量载入片上高速 SRAM！";
    });
  }
  if (btnCubeMatmul) {
    btnCubeMatmul.addEventListener("click", () => {
      cubeCells.forEach((c) => c.classList.add("active"));
      if (cubeNote) cubeNote.textContent = "🔥 DaVinci 3D Cube 点火：16×16×16 矩阵乘单元全速运转，单周期并行完成 4096 次乘加 (MACs)，算力释放 318.6 TFLOPS！";
    });
  }
  if (btnVectorSoftmax) {
    btnVectorSoftmax.addEventListener("click", () => {
      cubeCells.forEach((c, i) => {
        c.classList.toggle("active", i < 8);
      });
      if (cubeNote) cubeNote.textContent = "✨ Vector 矢量单元执行 Softmax 激活：自注意力得分矩阵迅速完成归一化，输出后验概率！";
    });
  }

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

js = js[:chip_sec_start] + new_chip_js + js[chip_sec_end:]
print("4. Chip Lab and interactive functions added!")

# -----------------------------------------------------------------
# 5. Chapter 7 AI: Horizontal Feature Bar + 3-Column Pipeline + Softmax Column
# -----------------------------------------------------------------
ai_sec_start = js.find("/* ============================================================\n     10. 第七幕 · 人工智能")
ai_sec_end = js.find("/* ============================================================\n     11. 尾声")

new_ai_js = '''/* ============================================================
     10. 第七幕 · 人工智能：横向输入特征提取 + 3列 Transformer (含线性投影与 Softmax 专列)
  ============================================================ */
  const aiPlayBtn = $("#aiPlayBtn");
  const playIcon = $("#playIcon");
  const playText = $("#playText");
  const stepGlyph = $("#stepGlyph");
  const stepToken = $("#stepToken");
  const stepEncode = $("#stepEncode");
  const stepData = $("#stepData");
  const blockEncoder = $("#blockEncoder");
  const blockDecoder = $("#blockDecoder");
  const head1 = $("#head1");
  const head2 = $("#head2");
  const head3 = $("#head3");
  const decoderStatus = $("#decoderStatus");
  const blockLinear = $("#blockLinear");
  const blockSoftmax = $("#blockSoftmax");
  const softmaxStatus = $("#softmaxStatus");
  const vocabItems = $$(".vocab-item");

  let aiIsPlaying = true;
  let aiCycleTimer = null;
  let aiCycleStart = 0;
  const cycleDuration = 9600; // 0.8倍速慢速叙事流循环周期 9.6s

  const stepsList = [stepGlyph, stepToken, stepEncode, stepData];
  const headsList = [head1, head2, head3];

  function runAiStep(elapsed) {
    // 0.0s - 2.8s: 顶部横向特征提取 01 -> 02 -> 03 -> 04 顺次流转
    stepGlyph.classList.toggle("is-active", elapsed >= 0 && elapsed < 9200);
    stepToken.classList.toggle("is-active", elapsed >= 800 && elapsed < 9200);
    stepEncode.classList.toggle("is-active", elapsed >= 1600 && elapsed < 9200);
    stepData.classList.toggle("is-active", elapsed >= 2400 && elapsed < 9200);

    // 3.4s: 第1列 Transformer 核心架构 (Encoder / Decoder)
    if (blockEncoder) {
      blockEncoder.classList.toggle("lit", elapsed >= 3400 && elapsed < 9200);
    }
    if (head1) head1.classList.toggle("lit", elapsed >= 3800 && elapsed < 9200);
    if (head2) head2.classList.toggle("lit", elapsed >= 4400 && elapsed < 9200);
    if (head3) head3.classList.toggle("lit", elapsed >= 5000 && elapsed < 9200);

    if (blockDecoder) {
      blockDecoder.classList.toggle("lit", elapsed >= 5600 && elapsed < 9200);
    }
    if (decoderStatus) {
      if (elapsed >= 5600 && elapsed < 9200) {
        decoderStatus.textContent = "跨注意力交互完成：生成 4096 维后验隐状态向量 H ✓";
      } else {
        decoderStatus.textContent = "计算后验隐状态向量 H...";
      }
    }

    // 6.2s: 第2列 [线性投影 + Softmax 概率分布] 独立专列计算激活
    if (blockLinear) {
      blockLinear.classList.toggle("lit", elapsed >= 6200 && elapsed < 9200);
    }
    if (blockSoftmax) {
      blockSoftmax.classList.toggle("lit", elapsed >= 6800 && elapsed < 9200);
    }
    if (softmaxStatus) {
      if (elapsed >= 6800 && elapsed < 9200) {
        softmaxStatus.textContent = "全词表 Softmax 指数归一化已收敛锁定 ✓";
        softmaxStatus.style.color = "var(--cyan)";
      } else {
        softmaxStatus.textContent = "概率分布计算中...";
        softmaxStatus.style.color = "var(--txt-dim)";
      }
    }

    // 7.4s ~ 9.0s: 第3列 候选词表自上而下展开，国家金色耀眼光辉锁定
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
      if (aiPlayBtn) aiPlayBtn.classList.remove("is-paused");
      if (playIcon) playIcon.textContent = "⏸";
      if (playText) playText.textContent = "0.8× 自动推演中";
      startAiCycle();
    } else {
      if (aiPlayBtn) aiPlayBtn.classList.add("is-paused");
      if (playIcon) playIcon.textContent = "▶";
      if (playText) playText.textContent = "已暂停 · 点击推演";
      cancelAnimationFrame(aiCycleTimer);
    }
  }

  if (aiPlayBtn) {
    aiPlayBtn.addEventListener("click", toggleAiPlay);
  }

  // 鼠标悬停探查
  stepsList.forEach((st) => {
    if (!st) return;
    st.addEventListener("mouseenter", () => {
      if (aiIsPlaying) cancelAnimationFrame(aiCycleTimer);
      st.classList.add("is-hovered");
    });
    st.addEventListener("mouseleave", () => {
      st.classList.remove("is-hovered");
      if (aiIsPlaying) startAiCycle();
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

js = js[:ai_sec_start] + new_ai_js + js[ai_sec_end:]
print("5. Chapter 7 AI horizontal feature bar and 3-column state machine updated!")

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("ALL main.js updates written successfully!")
