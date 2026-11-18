import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="완전제곱식 퍼즐",
    page_icon="🧩",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp { background: #f5f7fb; }
    [data-testid="stHeader"], footer { visibility: hidden; }
    .block-container { max-width: 1180px; padding-top: 1.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    """
    <!doctype html>
    <html lang="ko">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        :root {
          color-scheme: light;
          font-family: "Pretendard", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
          color: #17233c;
          background: #f5f7fb;
        }
        * { box-sizing: border-box; }
        body { margin: 0; background: #f5f7fb; }
        button { font: inherit; }
        .app { max-width: 1120px; margin: 0 auto; padding: 18px 20px 30px; }
        .topline { display: flex; align-items: center; gap: 10px; color: #66738d; font-size: 13px; font-weight: 700; }
        .badge { padding: 6px 10px; border-radius: 999px; background: #e8edff; color: #4a5bca; }
        h1 { margin: 13px 0 7px; font-size: clamp(25px, 4vw, 34px); letter-spacing: -1.3px; }
        .intro { margin: 0; color: #65718a; line-height: 1.65; }
        .layout { display: grid; grid-template-columns: minmax(0, 1.35fr) minmax(290px, .85fr); gap: 18px; margin-top: 23px; align-items: stretch; }
        .card { background: #fff; border: 1px solid #e8ecf4; border-radius: 18px; box-shadow: 0 8px 26px #26385b0a; }
        .board-card { padding: 20px; }
        .section-head { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
        h2 { margin: 0; font-size: 17px; letter-spacing: -.4px; }
        .hint { margin: 5px 0 0; color: #7a859a; font-size: 12px; line-height: 1.5; }
        .board-stage { display: grid; place-items: center; margin: 20px auto 16px; }
        .board {
          position: relative; width: min(100%, 360px); aspect-ratio: 1;
          background-color: #fbfcff;
          background-image: linear-gradient(#e9edf5 1px, transparent 1px), linear-gradient(90deg, #e9edf5 1px, transparent 1px);
          background-size: 40px 40px; border: 2px dashed #cbd4e4; border-radius: 12px;
          touch-action: none; overflow: hidden;
        }
        .board::before { content: ""; position: absolute; inset: 0 auto auto 0; width: 280px; height: 280px; border: 2px solid #8e9bb3; pointer-events: none; }
        .axis-label { position: absolute; color: #8490a5; font-size: 11px; font-weight: 700; }
        .axis-x { top: 286px; left: 112px; }
        .axis-y { top: 111px; left: -7px; transform: rotate(-90deg); }
        .piece {
          position: absolute; display: grid; place-items: center; border: 2px solid #fff;
          border-radius: 8px; cursor: grab; user-select: none; touch-action: none;
          box-shadow: 0 3px 8px #34415d20; transition: box-shadow .12s, filter .12s;
          z-index: 2; font-weight: 800;
        }
        .piece:active { cursor: grabbing; }
        .piece.selected { outline: 3px solid #293d72; outline-offset: 2px; z-index: 5; }
        .piece.dragging { opacity: .88; box-shadow: 0 8px 20px #34415d36; z-index: 10; }
        .piece-x2 { width: 160px; height: 160px; background: #7d8df1; color: white; font-size: 26px; }
        .piece-x { width: 160px; height: 40px; background: #ffbf66; color: #653e08; font-size: 14px; }
        .piece-unit { width: 40px; height: 40px; background: #69c9ad; color: #155945; font-size: 12px; border-radius: 7px; }
        .fixed { cursor: default; }
        .tray { min-height: 118px; padding: 12px; border-radius: 12px; background: #f7f8fc; border: 1px solid #edf0f6; }
        .tray-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; color: #78849a; font-size: 12px; font-weight: 700; }
        .tray-pieces { display: flex; flex-wrap: wrap; align-content: flex-start; gap: 8px; min-height: 74px; }
        .tray .piece { position: relative; inset: auto !important; flex: 0 0 auto; }
        .tray .piece-x { width: 92px; height: 32px; font-size: 12px; }
        .tray .piece-unit { width: 32px; height: 32px; }
        .tray .piece.selected { outline-offset: 1px; }
        .board .piece.x-vertical { width: 40px; height: 160px; }
        .tools { display: flex; gap: 8px; margin-top: 13px; }
        .btn { border: 1px solid #dfe5ef; background: white; color: #34425d; border-radius: 10px; padding: 9px 13px; font-size: 12px; font-weight: 700; cursor: pointer; transition: .15s; }
        .btn:hover { background: #f5f7fc; border-color: #bfc9dc; }
        .btn.primary { color: white; border-color: #4e61d3; background: #586be0; }
        .btn.primary:hover { background: #495dcf; }
        .btn:disabled { opacity: .45; cursor: not-allowed; }
        .side { display: flex; flex-direction: column; gap: 14px; }
        .lesson-card, .equation-card, .goal-card { padding: 19px; }
        .step { display: flex; gap: 12px; align-items: flex-start; margin-top: 15px; }
        .step-num { flex: 0 0 25px; width: 25px; height: 25px; display: grid; place-items: center; border-radius: 50%; background: #eef0ff; color: #5365d5; font-weight: 800; font-size: 12px; }
        .step p { margin: 2px 0 0; color: #536078; font-size: 13px; line-height: 1.55; }
        .equation-card { background: #202c4c; color: white; border: 0; }
        .equation-card h2 { color: #dce3ff; }
        .equation-label { margin-top: 16px; color: #aeb9d8; font-size: 12px; }
        .expression { min-height: 39px; margin-top: 6px; color: #fff; font-size: clamp(22px, 3vw, 29px); font-weight: 800; letter-spacing: -.7px; overflow-wrap: anywhere; }
        .expression .term-x2 { color: #b7c1ff; }
        .expression .term-x { color: #ffd18e; }
        .expression .term-unit { color: #8fe1c7; }
        .expression.result { font-size: 20px; color: #d7ddff; }
        .formula-divider { height: 1px; margin: 13px 0; background: #ffffff20; }
        .progress-wrap { margin-top: 15px; }
        .progress-info { display: flex; justify-content: space-between; color: #b9c4df; font-size: 11px; margin-bottom: 7px; }
        .progress { height: 7px; border-radius: 10px; background: #ffffff20; overflow: hidden; }
        .progress-bar { height: 100%; width: 0; background: linear-gradient(90deg, #7d8df1, #73d5b5); border-radius: inherit; transition: width .2s; }
        .goal-card { background: #fff9eb; border-color: #f4e8c9; }
        .goal-card h2 { color: #77551d; }
        .goal-card p { margin: 8px 0 0; color: #806b46; font-size: 12px; line-height: 1.6; }
        .complete-message { display: none; margin-top: 12px; padding: 10px; border-radius: 10px; background: #eaf8f1; color: #257653; font-size: 12px; font-weight: 700; line-height: 1.5; }
        .complete-message.show { display: block; }
        @media (max-width: 760px) {
          .app { padding: 14px 12px 24px; }
          .layout { grid-template-columns: 1fr; }
          .board-card { padding: 15px; }
          .board { width: min(100%, 320px); }
          .axis-x { top: 252px; left: 90px; }
          .axis-y { top: 96px; }
          .tray { min-height: 100px; }
        }
        @media (max-width: 360px) {
          .board { width: 280px; }
          .axis-x { top: 220px; left: 75px; }
        }
      </style>
    </head>
    <body>
      <main class="app">
        <div class="topline"><span class="badge">중학교 3학년 · 이차방정식</span><span>도형으로 이해하는 수학</span></div>
        <h1>완전제곱식 퍼즐</h1>
        <p class="intro">도형을 옮겨 큰 정사각형을 만들어 보세요. 조각을 놓을 때마다 넓이의 식이 바뀝니다.</p>

        <div class="layout">
          <section class="card board-card">
            <div class="section-head">
              <div><h2>큰 정사각형 만들기</h2><p class="hint">조각을 격자에 끌어 놓으세요. 직사각형은 회전할 수 있어요.</p></div>
              <span class="badge" id="statusBadge">시작해 볼까요?</span>
            </div>
            <div class="board-stage">
              <div class="board" id="board" aria-label="도형을 배치하는 격자">
                <div class="piece piece-x2 fixed" style="left:0;top:0" aria-label="x 제곱 타일">x²</div>
                <span class="axis-label axis-x">x + 3</span>
                <span class="axis-label axis-y">x + 3</span>
              </div>
            </div>
            <div class="tray">
              <div class="tray-title"><span>도형 조각</span><span>직사각형 6개 · 정사각형 9개</span></div>
              <div class="tray-pieces" id="tray"></div>
            </div>
            <div class="tools">
              <button class="btn" id="rotateBtn" type="button" disabled>↻ 선택한 조각 회전</button>
              <button class="btn" id="resetBtn" type="button">다시 시작</button>
            </div>
          </section>

          <aside class="side">
            <section class="card lesson-card">
              <h2>활동 방법</h2>
              <div class="step"><span class="step-num">1</span><p>큰 정사각형의 왼쪽 위에 있는 <b>x²</b> 타일을 살펴보세요.</p></div>
              <div class="step"><span class="step-num">2</span><p><b>x</b> 직사각형을 두 변에 붙여 놓고, 필요하면 회전하세요.</p></div>
              <div class="step"><span class="step-num">3</span><p>남은 모서리를 <b>1</b> 정사각형으로 채워 완성해 보세요.</p></div>
            </section>
            <section class="card equation-card">
              <h2>도형의 넓이 식</h2>
              <div class="equation-label">현재 배치한 도형의 넓이 합</div>
              <div class="expression" id="expression" aria-live="polite">x²</div>
              <div class="formula-divider"></div>
              <div class="equation-label">완성하면 이렇게 정리돼요</div>
              <div class="expression result" id="result">x² + 6x + 9</div>
              <div class="progress-wrap">
                <div class="progress-info"><span>퍼즐 완성도</span><span id="progressText">1 / 16 조각</span></div>
                <div class="progress"><div class="progress-bar" id="progressBar"></div></div>
              </div>
            </section>
            <section class="card goal-card">
              <h2>오늘의 발견</h2>
              <p>각 변에 붙인 직사각형과 모서리의 작은 정사각형까지 합치면, 한 변의 길이가 <b>x + 3</b>인 큰 정사각형이 됩니다.</p>
              <div class="complete-message" id="completeMessage">🎉 완성! x² + 6x + 9 = (x + 3)²<br>도형으로 완전제곱식을 만들었어요.</div>
            </section>
          </aside>
        </div>
      </main>
      <script>
        (() => {
          const board = document.getElementById("board");
          const tray = document.getElementById("tray");
          const expression = document.getElementById("expression");
          const result = document.getElementById("result");
          const progressText = document.getElementById("progressText");
          const progressBar = document.getElementById("progressBar");
          const rotateBtn = document.getElementById("rotateBtn");
          const statusBadge = document.getElementById("statusBadge");
          const completeMessage = document.getElementById("completeMessage");
          const unit = 40;
          const pieces = [];
          let selected = null;
          let drag = null;

          function createPiece(type, id) {
            const piece = document.createElement("div");
            piece.className = `piece piece-${type}`;
            piece.dataset.type = type;
            piece.dataset.id = id;
            piece.textContent = type === "x" ? "x" : "1";
            piece.setAttribute("role", "button");
            piece.setAttribute("aria-label", type === "x" ? "x 직사각형 조각" : "1 정사각형 조각");
            piece.tabIndex = 0;
            tray.appendChild(piece);
            pieces.push({ el: piece, type, id, placed: false, x: 0, y: 0, vertical: false });
            return piece;
          }

          for (let i = 0; i < 6; i++) createPiece("x", `x-${i}`);
          for (let i = 0; i < 9; i++) createPiece("unit", `unit-${i}`);

          function cellsFor(piece, x, y, vertical = piece.vertical) {
            if (piece.type === "unit") return [`${x},${y}`];
            const cells = [];
            if (piece.type === "x" && vertical) {
              for (let row = 0; row < 4; row++) cells.push(`${x},${y + row * unit}`);
            } else if (piece.type === "x") {
              for (let col = 0; col < 4; col++) cells.push(`${x + col * unit},${y}`);
            } else {
              for (let row = 0; row < 4; row++) for (let col = 0; col < 4; col++) cells.push(`${x + col * unit},${y + row * unit}`);
            }
            return cells;
          }

          function validPlacement(piece, x, y, vertical = piece.vertical) {
            const width = piece.type === "unit" || (piece.type === "x" && vertical) ? unit : 4 * unit;
            const height = piece.type === "unit" ? unit : (piece.type === "x" && !vertical) ? unit : 4 * unit;
            if (x < 0 || y < 0 || x + width > 7 * unit || y + height > 7 * unit) return false;
            const occupied = new Set(["0,0", "40,0", "80,0", "120,0", "0,40", "40,40", "80,40", "120,40", "0,80", "40,80", "80,80", "120,80", "0,120", "40,120", "80,120", "120,120"]);
            for (const other of pieces) {
              if (other === piece || !other.placed) continue;
              for (const cell of cellsFor(other, other.x, other.y)) occupied.add(cell);
            }
            return cellsFor(piece, x, y, vertical).every(cell => !occupied.has(cell));
          }

          function setPosition(piece, x, y) {
            piece.el.style.left = `${x}px`;
            piece.el.style.top = `${y}px`;
            piece.el.style.position = "absolute";
            if (piece.type === "x") {
              piece.el.classList.toggle("x-vertical", piece.vertical);
            }
          }

          function choose(piece) {
            if (selected) selected.el.classList.remove("selected");
            selected = piece;
            if (selected) selected.el.classList.add("selected");
            rotateBtn.disabled = !selected || selected.type !== "x";
          }

          function updateEquation() {
            const xCount = pieces.filter(p => p.type === "x" && p.placed).length;
            const unitCount = pieces.filter(p => p.type === "unit" && p.placed).length;
            const filled = new Set(["0,0", "40,0", "80,0", "120,0", "0,40", "40,40", "80,40", "120,40", "0,80", "40,80", "80,80", "120,80", "0,120", "40,120", "80,120", "120,120"]);
            for (const piece of pieces) {
              if (piece.placed) for (const cell of cellsFor(piece, piece.x, piece.y)) filled.add(cell);
            }
            const terms = ['<span class="term-x2">x²</span>'];
            if (xCount) terms.push(`<span class="term-x">${xCount === 1 ? "" : xCount}x</span>`);
            if (unitCount) terms.push(`<span class="term-unit">${unitCount}</span>`);
            expression.innerHTML = terms.join(" + ");
            const count = 1 + xCount + unitCount;
            progressText.textContent = `${count} / 16 조각`;
            progressBar.style.width = `${(count / 16) * 100}%`;
            const complete = xCount === 6 && unitCount === 9 && filled.size === 49;
            statusBadge.textContent = complete ? "완성했어요!" : `${xCount}x · ${unitCount}개 배치`;
            completeMessage.classList.toggle("show", complete);
            result.textContent = complete ? "x² + 6x + 9 = (x + 3)²" : "x² + 6x + 9";
          }

          function startDrag(event, piece) {
            if (piece.classList.contains("fixed")) return;
            event.preventDefault();
            const model = pieces.find(item => item.el === piece);
            if (!model) return;
            choose(model);
            const rect = piece.getBoundingClientRect();
            const wasPlaced = model.placed;
            if (wasPlaced) {
              model.x = Number.parseInt(piece.style.left, 10) || model.x;
              model.y = Number.parseInt(piece.style.top, 10) || model.y;
            } else {
              piece.style.width = "";
              piece.style.height = "";
              board.appendChild(piece);
            }
            piece.classList.add("dragging");
            const boardRect = board.getBoundingClientRect();
            const scale = boardRect.width / board.offsetWidth;
            drag = {
              model, wasPlaced, scale,
              offsetX: (event.clientX - rect.left) / scale,
              offsetY: (event.clientY - rect.top) / scale
            };
            piece.setPointerCapture(event.pointerId);
          }

          function moveDrag(event) {
            if (!drag) return;
            const boardRect = board.getBoundingClientRect();
            const x = (event.clientX - boardRect.left) / drag.scale - drag.offsetX;
            const y = (event.clientY - boardRect.top) / drag.scale - drag.offsetY;
            const el = drag.model.el;
            el.style.left = `${x}px`;
            el.style.top = `${y}px`;
          }

          function endDrag(event) {
            if (!drag) return;
            const { model, wasPlaced } = drag;
            const x = Math.round((Number.parseFloat(model.el.style.left) || 0) / unit) * unit;
            const y = Math.round((Number.parseFloat(model.el.style.top) || 0) / unit) * unit;
            model.el.classList.remove("dragging");
            if (validPlacement(model, x, y)) {
              model.x = x;
              model.y = y;
              model.placed = true;
              setPosition(model, x, y);
              board.appendChild(model.el);
            } else if (!wasPlaced) {
              model.placed = false;
              model.el.classList.remove("selected");
              tray.appendChild(model.el);
              choose(null);
            } else {
              setPosition(model, model.x, model.y);
            }
            drag = null;
            updateEquation();
          }

          document.addEventListener("pointerdown", event => {
            const piece = event.target.closest(".piece");
            if (piece) startDrag(event, piece);
          });
          document.addEventListener("pointermove", moveDrag);
          document.addEventListener("pointerup", endDrag);
          document.addEventListener("pointercancel", endDrag);

          function rotateSelected() {
            if (!selected || selected.type !== "x") return;
            const nextVertical = !selected.vertical;
            if (selected.placed && !validPlacement(selected, selected.x, selected.y, nextVertical)) {
              statusBadge.textContent = "그 자리는 회전할 수 없어요";
              return;
            }
            selected.vertical = nextVertical;
            if (selected.placed) setPosition(selected, selected.x, selected.y);
            else {
              selected.el.classList.toggle("x-vertical", nextVertical);
              selected.el.style.width = nextVertical ? "32px" : "92px";
              selected.el.style.height = nextVertical ? "92px" : "32px";
            }
            statusBadge.textContent = "조각을 회전했어요";
          }

          rotateBtn.addEventListener("click", rotateSelected);
          document.addEventListener("keydown", event => {
            if (event.key === "r" || event.key === "R") rotateSelected();
          });

          document.getElementById("resetBtn").addEventListener("click", () => {
            for (const piece of pieces) {
              piece.placed = false;
              piece.vertical = false;
              piece.el.classList.remove("x-vertical", "selected", "dragging");
              piece.el.style.cssText = "";
              tray.appendChild(piece.el);
            }
            choose(null);
            statusBadge.textContent = "시작해 볼까요?";
            updateEquation();
          });

          updateEquation();
        })();
      </script>
    </body>
    </html>
    """,
    height=1120,
    scrolling=True,
)
