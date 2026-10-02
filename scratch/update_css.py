# -*- coding: utf-8 -*-
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update .c-comment (no italic, bold, readable color)
css = css.replace(
    ".c-comment { color: #636e72; font-style: italic; }",
    ".c-comment { color: #78a6c8; font-style: normal; font-weight: 700; }"
)

# 2. Add styles for dummy padding bamboo slips and Chip Lab and AI 3-column layout
additional_styles = '''
/* 占位扩展竹简样式 */
.slip--pad {
  opacity: 0.42;
  cursor: pointer;
  transition: opacity .3s, transform .3s;
}
.slip--pad:hover {
  opacity: 0.85;
}
.slip--pad .slip-tag {
  color: #888;
  border-top-color: rgba(255,255,255,.1);
}

/* 芯片动手实验台 (Interactive Chip Lab) */
.chip-lab {
  margin-top: 36px;
  background: rgba(8, 16, 28, 0.85);
  border: 1px solid rgba(114, 214, 208, 0.3);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
  text-align: left;
}
.chip-lab__header {
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 16px;
}
.chip-lab__badge {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--cyan);
  letter-spacing: 2px;
  background: rgba(114, 214, 208, 0.12);
  padding: 4px 10px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 8px;
}
.chip-lab__title {
  font-family: var(--sans);
  font-size: 18px;
  color: var(--cold-white);
  margin: 0 0 10px 0;
}
.chip-lab__plain-hint {
  font-size: 13px;
  line-height: 1.6;
  color: #d1d8e0;
  background: rgba(255, 255, 255, 0.04);
  border-left: 3px solid var(--gold);
  padding: 10px 14px;
  border-radius: 0 6px 6px 0;
}
.lab-panel {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.lab-panel__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--sans);
  font-size: 13px;
  color: var(--cold-white);
}
.panel-clock {
  font-family: var(--mono);
  font-size: 12px;
  color: var(--cyan);
  background: rgba(114, 214, 208, 0.1);
  padding: 3px 8px;
  border-radius: 4px;
}
.register-visual, .cube-visual {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 14px 18px;
}
.reg-label {
  display: block;
  font-size: 12px;
  color: var(--txt-dim);
  margin-bottom: 10px;
  font-family: var(--sans);
}
.reg-slots {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 8px;
}
.reg-byte {
  width: 44px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 4px;
  font-family: var(--mono);
  font-size: 14px;
  color: var(--txt-dim);
  transition: all 0.3s;
}
.reg-byte.is-filled {
  border-color: var(--cyan);
  background: rgba(114, 214, 208, 0.2);
  color: var(--cyan);
  font-weight: 700;
  box-shadow: 0 0 12px rgba(114, 214, 208, 0.4);
}
.reg-byte.pulse-active {
  animation: regPulse 0.5s ease-out;
}
@keyframes regPulse {
  0% { transform: scale(1.15); background: rgba(243, 156, 18, 0.6); color: #fff; }
  100% { transform: scale(1); }
}
.reg-note {
  display: block;
  font-size: 12px;
  color: #a4b0be;
  font-family: var(--sans);
}
.cube-grid-box {
  display: grid;
  grid-template-columns: repeat(4, 38px);
  gap: 6px;
  margin-bottom: 10px;
}
.cube-cell {
  width: 38px;
  height: 38px;
  border-radius: 4px;
  background: rgba(46, 213, 115, 0.08);
  border: 1px solid rgba(46, 213, 115, 0.25);
  transition: all 0.25s;
}
.cube-cell.active {
  background: rgba(46, 213, 115, 0.6);
  box-shadow: 0 0 16px rgba(46, 213, 115, 0.8);
  border-color: #fff;
}
.lab-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
.lab-btn {
  padding: 9px 16px;
  border-radius: 6px;
  border: 1px solid var(--cyan);
  background: rgba(114, 214, 208, 0.12);
  color: var(--cyan);
  font-family: var(--sans);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s;
}
.lab-btn:hover {
  background: rgba(114, 214, 208, 0.28);
  box-shadow: 0 0 16px rgba(114, 214, 208, 0.4);
  transform: translateY(-1px);
}
.lab-btn--ascend {
  border-color: #2ed573;
  color: #2ed573;
  background: rgba(46, 213, 115, 0.12);
}
.lab-btn--ascend:hover {
  background: rgba(46, 213, 115, 0.28);
  box-shadow: 0 0 16px rgba(46, 213, 115, 0.4);
}

/* ============================================================
   第七幕 · AI 横向输入特征行 + 3列全景架构
   ============================================================ */
.pipeline-feature-row {
  background: rgba(10, 18, 30, 0.7);
  border: 1px solid rgba(114, 214, 208, 0.25);
  border-radius: 10px;
  padding: 16px 20px;
  margin-top: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}
.feature-row-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding-bottom: 8px;
}
.row-tag {
  font-family: var(--sans);
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--cyan);
  font-weight: 600;
}
.row-sub {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--txt-dim);
}
.feature-steps-bar {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  gap: 12px;
}
.feature-steps-bar .pipeline-step {
  flex: 1;
  min-width: 0;
}
.pipeline-arrow-right {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: rgba(114, 214, 208, 0.4);
  user-select: none;
}
.feature-to-neural-flow {
  text-align: center;
  margin: 18px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
.flow-pulse-line {
  width: 2px;
  height: 24px;
  background: linear-gradient(180deg, var(--cyan), transparent);
  animation: pulseDown 1.5s infinite;
}
@keyframes pulseDown {
  0% { opacity: 0.2; transform: scaleY(0.6); }
  50% { opacity: 1; transform: scaleY(1); }
  100% { opacity: 0.2; transform: scaleY(0.6); }
}
.flow-pulse-label {
  font-family: var(--sans);
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--cyan);
  background: rgba(114, 214, 208, 0.08);
  padding: 4px 16px;
  border-radius: 100px;
  border: 1px solid rgba(114, 214, 208, 0.2);
}

/* 3列并行全景网格 */
.pipeline-3col-grid {
  display: grid;
  grid-template-columns: 1.15fr 1.25fr 0.9fr;
  gap: 16px;
  width: 100%;
  align-items: stretch;
}
.col--projection {
  background: rgba(10, 20, 32, 0.75);
}
.proj-block {
  background: rgba(6, 12, 20, 0.85);
  border: 1px solid rgba(114, 214, 208, 0.25);
  border-radius: 6px;
  padding: 12px 16px;
  text-align: left;
  margin-bottom: 8px;
  transition: all 0.35s var(--ease);
}
.proj-block.lit {
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(114, 214, 208, 0.3);
}
.proj-badge {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--gold);
  letter-spacing: 1.5px;
  margin-bottom: 4px;
}
.math-eq, .math-formula {
  font-family: "KaTeX_Main", "Times New Roman", serif;
  font-size: 13px;
  color: var(--cold-white);
  background: rgba(255, 255, 255, 0.04);
  padding: 6px 10px;
  border-radius: 4px;
  margin: 6px 0;
}
.proj-dims {
  display: flex;
  align-items: center;
  gap: 6px;
  margin: 6px 0;
}
.dim-tag {
  font-family: var(--mono);
  font-size: 10px;
  background: rgba(114, 214, 208, 0.1);
  color: var(--cyan);
  padding: 2px 6px;
  border-radius: 3px;
}
.dim-tag--vocab {
  background: rgba(184, 154, 98, 0.15);
  color: var(--gold);
}
.dim-arrow {
  font-size: 10px;
  color: var(--txt-dim);
}
.softmax-specs {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;
}
.spec-item {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--txt-dim);
}
.spec-item--active {
  color: var(--cyan);
  font-weight: 600;
}

@media (max-width: 960px) {
  .feature-steps-bar {
    flex-direction: column;
  }
  .pipeline-arrow-right {
    transform: rotate(90deg);
    margin: 4px 0;
  }
  .pipeline-3col-grid {
    grid-template-columns: 1fr;
  }
}
'''

css += "\n" + additional_styles

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("css/style.css updated successfully!")
