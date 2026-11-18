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
        .problem-card { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-top: 20px; padding: 17px 21px; border: 1px solid #dfe5fb; border-radius: 16px; background: linear-gradient(110deg, #fff 20%, #f0f3ff 100%); }
        .problem-label { color: #6775c9; font-size: 12px; font-weight: 800; }
        .problem-expression { margin-top: 5px; color: #26345d; font-size: clamp(27px, 4vw, 36px); font-weight: 850; letter-spacing: -.8px; }
        .problem-hint { max-width: 310px; color: #68748e; font-size: 13px; line-height: 1.6; }
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
          background-size: 28px 28px; border: 2px dashed #cbd4e4; border-radius: 12px;
          touch-action: none; overflow: hidden;
        }
        .piece {
          position: absolute; display: grid; place-items: center; border: 2px solid #fff;
          border-radius: 8px; cursor: grab; user-select: none; touch-action: none;
          box-shadow: 0 3px 8px #34415d20; transition: box-shadow .12s, filter .12s;
          z-index: 2; font-weight: 800;
        }
        .piece:active { cursor: grabbing; }
        .piece.selected { outline: 3px solid #293d72; outline-offset: 2px; z-index: 5; }
        .piece.dragging { opacity: .88; box-shadow: 0 8px 20px #34415d36; z-index: 10; }
        .piece-x2 { width: 112px; height: 112px; background: #7d8df1; color: white; font-size: 22px; }
        .piece-x-horizontal { width: 140px; height: 112px; background: #ffbf66; color: #653e08; font-size: 14px; }
        .piece-x-vertical { width: 112px; height: 140px; background: #f0ad50; color: #653e08; font-size: 14px; }
        .piece-square25 { width: 140px; height: 140px; background: #69c9ad; color: #155945; font-size: 16px; }
        .tray { min-height: 150px; padding: 12px; border-radius: 12px; background: #f7f8fc; border: 1px solid #edf0f6; }
        .tray-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; color: #78849a; font-size: 12px; font-weight: 700; }
        .tray-pieces { display: flex; flex-wrap: wrap; align-content: flex-start; gap: 8px; min-height: 74px; }
        .tray .piece { position: relative; inset: auto !important; flex: 0 0 auto; }
        .tray .piece-x2 { width: 56px; height: 56px; font-size: 15px; }
        .tray .piece-x-horizontal { width: 100px; height: 50px; font-size: 12px; }
        .tray .piece-x-vertical { width: 50px; height: 100px; font-size: 12px; }
        .tray .piece-square25 { width: 70px; height: 70px; font-size: 14px; }
        .tray .piece.selected { outline-offset: 1px; }
        .tools { display: flex; gap: 8px; margin-top: 13px; }
        .btn { border: 1px solid #dfe5ef; background: white; color: #34425d; border-radius: 10px; padding: 9px 13px; font-size: 12px; font-weight: 700; cursor: pointer; transition: .15s; }
        .btn:hover { background: #f5f7fc; border-color: #bfc9dc; }
        .btn.primary { color: white; border-color: #4e61d3; background: #586be0; }
        .btn.primary:hover { background: #495dcf; }
        .side { display: flex; flex-direction: column; gap: 14px; }
        .lesson-card, .equation-card, .goal-card { padding: 19px; }
        .step { display: flex; gap: 12px; align-items: flex-start; margin-top: 15px; }
        .step-num { flex: 0 0 25px; width: 25px; height: 25px; display: grid; place-items: center; border-radius: 50%; background: #eef0ff; color: #5365d5; font-weight: 800; font-size: 12px; }
        .step p { margin: 2px 0 0; color: #536078; font-size: 13px; line-height: 1.55; }
        .equation-card { background: #202c4c; color: white; border: 0; }
        .equation-card h2 { color: #dce3ff; }
        .equation-label { margin-top: 16px; color: #aeb9d8; font-size: 12px; }
        .expression { min-height: 39px; margin-top: 6px; color: #fff; font-size: clamp(22px, 3vw, 29px); font-weight: 800; letter-spacing: -.7px; overflow-wrap: anywhere; }
        .expression.empty { color: #bdc7df; font-size: 17px; font-weight: 600; letter-spacing: 0; }
        .expression .term-x2 { color: #b7c1ff; }
        .expression .term-x { color: #ffd18e; }
        .expression .term-unit { color: #8fe1c7; }
        .expression.result { min-height: 28px; font-size: 17px; color: #d7ddff; }
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
          .problem-card { align-items: flex-start; flex-direction: column; gap: 7px; padding: 14px 16px; }
          .layout { grid-template-columns: 1fr; }
          .board-card { padding: 15px; }
          .board { width: min(100%, 340px); }
          .tray { min-height: 150px; }
        }
        @media (max-width: 360px) {
          .board { width: 320px; }
        }
      </style>
    </head>
    <body>
      <main class="app">
        <div class="topline"><span class="badge">중학교 3학년 · 이차방정식</span><span>도형으로 이해하는 수학</span></div>
        <h1>완전제곱식 퍼즐</h1>
        <p class="intro">도형을 옮겨 큰 정사각형을 만들어 보세요. 조각을 놓을 때마다 넓이의 식이 바뀝니다.</p>
        <section class="problem-card" aria-label="오늘의 문제">
          <div><div class="problem-label">오늘의 문제</div><div class="problem-expression">x² + 10x = 24</div></div>
          <div class="problem-hint">빈 모서리를 넓이가 25인 정사각형으로 채워 완전제곱식을 만들어 보세요.</div>
        </section>

        <div class="layout">
          <section class="card board-card">
            <div class="section-head">
              <div><h2>큰 정사각형 만들기</h2><p class="hint">보관함의 네 조각을 판에 끌어 놓아 빈틈없이 채워 보세요.</p></div>
              <span class="badge" id="statusBadge">시작해 볼까요?</span>
            </div>
            <div class="board-stage">
              <div class="board" id="board" aria-label="도형을 배치하는 격자">
              </div>
            </div>
            <div class="tray">
              <div class="tray-title"><span>도형 조각</span><span>x² 1개 · 5x 가로/세로 각 1개 · 25 정사각형 1개</span></div>
              <div class="tray-pieces" id="tray"></div>
            </div>
            <div class="tools">
              <button class="btn" id="resetBtn" type="button">다시 시작</button>
            </div>
          </section>

          <aside class="side">
            <section class="card lesson-card">
              <h2>활동 방법</h2>
              <div class="step"><span class="step-num">1</span><p><b>x²</b> 타일을 큰 정사각형의 한쪽 모서리에 놓으세요.</p></div>
              <div class="step"><span class="step-num">2</span><p><b>가로 5x</b>와 <b>세로 5x</b> 조각을 x² 타일의 두 변에 붙여 보세요.</p></div>
              <div class="step"><span class="step-num">3</span><p>남은 <b>5 × 5</b> 모서리를 <b>25</b> 정사각형으로 채워 보세요.</p></div>
            </section>
            <section class="card equation-card">
              <h2>도형의 넓이 식</h2>
              <div class="equation-label">현재 배치한 도형의 넓이 합</div>
              <div class="expression empty" id="expression" aria-live="polite">아직 배치한 도형이 없어요</div>
              <div class="formula-divider"></div>
              <div class="equation-label">완성제곱식으로 바꾸기</div>
              <div class="expression result" id="equationStep">퍼즐을 완성하면 식이 나타나요</div>
              <div class="expression result" id="factorized"></div>
              <div class="progress-wrap">
                <div class="progress-info"><span>퍼즐 완성도</span><span id="progressText">0 / 4 조각</span></div>
                <div class="progress"><div class="progress-bar" id="progressBar"></div></div>
              </div>
            </section>
            <section class="card goal-card">
              <h2>오늘의 발견</h2>
              <p>비어 있는 모서리는 한 변이 5인 정사각형이에요. 단위 넓이로는 <b>5 × 5 = 25</b>이므로 양변에 25를 더하면 식이 완전제곱식이 됩니다.</p>
              <div class="complete-message" id="completeMessage">🎉 완성! x² + 10x + 25 = 24 + 25<br>(x + 5)² = 49</div>
            </section>
          </aside>
        </div>
      </main>
      <script>
        (() => {
          const board = document.getElementById("board");
          const tray = document.getElementById("tray");
          const expression = document.getElementById("expression");
          const progressText = document.getElementById("progressText");
          const progressBar = document.getElementById("progressBar");
          const statusBadge = document.getElementById("statusBadge");
          const completeMessage = document.getElementById("completeMessage");
          const equationStep = document.getElementById("equationStep");
          const factorized = document.getElementById("factorized");
          const unit = 28;
          const pieces = [];
          let selected = null;
          let drag = null;

          function createPiece(type, id, label, description) {
            const piece = document.createElement("div");
            piece.className = `piece piece-${type}`;
            piece.dataset.type = type;
            piece.dataset.id = id;
            piece.textContent = label;
            piece.setAttribute("role", "button");
            piece.setAttribute("aria-label", description);
            piece.tabIndex = 0;
            tray.appendChild(piece);
            pieces.push({ el: piece, type, id, placed: false, x: 0, y: 0 });
            return piece;
          }

          createPiece("x2", "x2", "x²", "x 제곱 정사각형");
          createPiece("x-horizontal", "x-horizontal", "5x", "가로로 긴 5x 직사각형");
          createPiece("x-vertical", "x-vertical", "5x", "세로로 긴 5x 직사각형");
          createPiece("square25", "square25", "25", "넓이가 25인 정사각형");

          function cellsFor(piece, x, y) {
            const cells = [];
            if (piece.type === "x2") {
              for (let row = 0; row < 4; row++) {
                for (let col = 0; col < 4; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x-horizontal") {
              for (let row = 0; row < 4; row++) {
                for (let col = 0; col < 5; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x-vertical") {
              for (let row = 0; row < 5; row++) {
                for (let col = 0; col < 4; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "square25") {
              for (let row = 0; row < 5; row++) {
                for (let col = 0; col < 5; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            }
            return cells;
          }

          function dimensions(piece) {
            if (piece.type === "x2") return { width: 4 * unit, height: 4 * unit };
            if (piece.type === "x-horizontal") return { width: 5 * unit, height: 4 * unit };
            if (piece.type === "x-vertical") return { width: 4 * unit, height: 5 * unit };
            return { width: 5 * unit, height: 5 * unit };
          }

          function validPlacement(piece, x, y) {
            const { width, height } = dimensions(piece);
            if (x < 0 || y < 0 || x + width > 12 * unit || y + height > 12 * unit) return false;
            const occupied = new Set();
            for (const other of pieces) {
              if (other === piece || !other.placed) continue;
              for (const cell of cellsFor(other, other.x, other.y)) occupied.add(cell);
            }
            return cellsFor(piece, x, y).every(cell => !occupied.has(cell));
          }

          function setPosition(piece, x, y) {
            piece.el.style.left = `${x}px`;
            piece.el.style.top = `${y}px`;
            piece.el.style.position = "absolute";
          }

          function choose(piece) {
            if (selected) selected.el.classList.remove("selected");
            selected = piece;
            if (selected) selected.el.classList.add("selected");
          }

          function updateEquation() {
            const placedCount = pieces.filter(piece => piece.placed).length;
            progressText.textContent = `${placedCount} / 4 조각`;
            progressBar.style.width = `${(placedCount / 4) * 100}%`;

            const x2Placed = pieces.some(piece => piece.type === "x2" && piece.placed);
            const rectangleCount = pieces.filter(piece => piece.type.startsWith("x-") && piece.placed).length;
            const square25Placed = pieces.some(piece => piece.type === "square25" && piece.placed);
            const terms = [];
            if (x2Placed) terms.push('<span class="term-x2">x²</span>');
            if (rectangleCount) terms.push(`<span class="term-x">${rectangleCount * 5}x</span>`);
            if (square25Placed) terms.push('<span class="term-unit">25</span>');
            let areaSum = terms.join(" + ");
            if (x2Placed && rectangleCount === 2 && !square25Placed) areaSum += " = 24";
            expression.innerHTML = areaSum || "아직 도형을 배치하지 않았어요";
            expression.classList.toggle("empty", !areaSum);

            const filled = new Set();
            for (const piece of pieces) {
              if (piece.placed) {
                for (const cell of cellsFor(piece, piece.x, piece.y)) filled.add(cell);
              }
            }
            const coordinates = [...filled].map(cell => cell.split(",").map(Number));
            const isSquareArrangement = coordinates.length > 0
              && Math.max(...coordinates.map(([x]) => x)) - Math.min(...coordinates.map(([x]) => x)) === 8 * unit
              && Math.max(...coordinates.map(([, y]) => y)) - Math.min(...coordinates.map(([, y]) => y)) === 8 * unit;
            const complete = x2Placed && rectangleCount === 2 && square25Placed
              && filled.size === 81
              && isSquareArrangement;
            statusBadge.textContent = complete ? "정사각형 완성!" : `${placedCount} / 4 조각 배치`;
            completeMessage.classList.toggle("show", complete);
            equationStep.textContent = complete ? "x² + 10x + 25 = 24 + 25" : "모든 조각이 서로 붙으면 등식이 완성돼요";
            factorized.textContent = complete ? "(x + 5)² = 49" : "";
          }

          function startDrag(event, piece) {
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
            const horizontalPosition = (event.clientX - rect.left) / rect.width;
            const verticalPosition = (event.clientY - rect.top) / rect.height;
            const pieceSize = dimensions(model);
            drag = {
              model, wasPlaced, scale,
              offsetX: horizontalPosition * pieceSize.width,
              offsetY: verticalPosition * pieceSize.height
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
              model.el.style.left = "";
              model.el.style.top = "";
              model.el.style.position = "";
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

          document.getElementById("resetBtn").addEventListener("click", () => {
            for (const piece of pieces) {
              piece.placed = false;
              piece.el.classList.remove("selected", "dragging");
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
