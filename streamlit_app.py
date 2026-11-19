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
          box-shadow: none; transition: left .07s linear, top .07s linear, filter .12s;
          z-index: 2; font-weight: 800;
        }
        .piece:active { cursor: grabbing; }
        .piece.selected { outline: none; box-shadow: inset 0 0 0 3px #293d72; z-index: 5; }
        .piece.dragging { opacity: .88; box-shadow: none; z-index: 10; }
        .piece-x2 { width: 84px; height: 84px; background: #7d8df1; color: white; font-size: 20px; }
        .piece-x-horizontal { width: 140px; height: 84px; background: #ffbf66; color: #653e08; font-size: 14px; }
        .piece-x-vertical { width: 84px; height: 140px; background: #f0ad50; color: #653e08; font-size: 14px; }
        .piece-x4-horizontal { width: 112px; height: 84px; background: #f2a979; color: #663b22; font-size: 13px; }
        .piece-x4-vertical { width: 84px; height: 112px; background: #e89a70; color: #663b22; font-size: 13px; }
        .piece-x6-horizontal { width: 168px; height: 84px; background: #e58b82; color: #642f2a; font-size: 13px; }
        .piece-x6-vertical { width: 84px; height: 168px; background: #d97770; color: #642f2a; font-size: 13px; }
        .piece-square25 { width: 140px; height: 140px; background: #69c9ad; color: #155945; font-size: 16px; }
        .piece-square16 { width: 112px; height: 112px; background: #ec9b9b; color: #6a3030; font-size: 16px; }
        .piece-square36 { width: 168px; height: 168px; background: #d7a3d8; color: #563458; font-size: 16px; }
        .tray { min-height: 150px; padding: 12px; border-radius: 12px; background: #f7f8fc; border: 1px solid #edf0f6; }
        .tray-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; color: #78849a; font-size: 12px; font-weight: 700; }
        .tray-pieces { display: flex; flex-wrap: wrap; align-content: flex-start; gap: 8px; min-height: 74px; }
        .tray .piece { position: relative; inset: auto !important; flex: 0 0 auto; }
        .tray .piece-x2 { width: 42px; height: 42px; font-size: 13px; }
        .tray .piece-x-horizontal { width: 70px; height: 42px; font-size: 11px; }
        .tray .piece-x-vertical { width: 42px; height: 70px; font-size: 11px; }
        .tray .piece-x4-horizontal { width: 56px; height: 42px; font-size: 10px; }
        .tray .piece-x4-vertical { width: 42px; height: 56px; font-size: 10px; }
        .tray .piece-x6-horizontal { width: 84px; height: 42px; font-size: 10px; }
        .tray .piece-x6-vertical { width: 42px; height: 84px; font-size: 10px; }
        .tray .piece-square25 { width: 70px; height: 70px; font-size: 14px; }
        .tray .piece-square16 { width: 56px; height: 56px; font-size: 12px; }
        .tray .piece-square36 { width: 84px; height: 84px; font-size: 12px; }
        .tray-feedback { min-height: 18px; margin: 8px 0 0; color: #9c5960; font-size: 11px; }
        .tools { display: flex; gap: 8px; margin-top: 13px; }
        .btn { border: 1px solid #dfe5ef; background: white; color: #34425d; border-radius: 10px; padding: 9px 13px; font-size: 12px; font-weight: 700; cursor: pointer; transition: .15s; }
        .btn:hover { background: #f5f7fc; border-color: #bfc9dc; }
        .btn:disabled { opacity: .45; cursor: not-allowed; }
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
        .expression .term-distractor { color: #ffaaaa; }
        .expression.result { min-height: 28px; font-size: 17px; color: #d7ddff; }
        .factorized-equation { min-height: 38px; font-size: 27px !important; color: #fff !important; }
        .formula-divider { height: 1px; margin: 13px 0; background: #ffffff20; }
        #areaSumPanel[hidden], .solution-panel[hidden] { display: none !important; }
        .quiz { margin: 12px 0 0; padding: 12px 0 0; border: 0; border-top: 1px solid #ffffff20; }
        .quiz legend { padding: 0; color: #dce3ff; font-size: 13px; font-weight: 700; }
        .choices { display: grid; gap: 7px; margin-top: 10px; }
        .choice { display: flex; align-items: center; gap: 9px; padding: 8px 10px; border: 1px solid #ffffff24; border-radius: 9px; color: #e4e9f8; font-size: 13px; cursor: pointer; }
        .choice:has(input:checked) { border-color: #9eabff; background: #ffffff12; }
        .choice input { accent-color: #9eabff; }
        .answer-feedback { min-height: 20px; margin: 8px 0 0; color: #a7e6cb; font-size: 12px; font-weight: 700; }
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
              <div><h2>큰 정사각형 만들기</h2><p class="hint">필요한 네 조각을 골라 판에 끌어 놓아 빈틈없이 채워 보세요. 크기가 다른 도형은 오답 조각이에요.</p></div>
            </div>
            <div class="board-stage">
              <div class="board" id="board" aria-label="도형을 배치하는 격자">
              </div>
            </div>
            <div class="tray">
              <div class="tray-title"><span>도형 조각</span><span>필수: x² · 5x 가로/세로 · 25 / 오답: 4x·6x 가로/세로, 16·36</span></div>
              <div class="tray-pieces" id="tray"></div>
              <p class="tray-feedback" id="trayFeedback" aria-live="polite"></p>
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
              <div id="areaSumPanel">
                <div class="equation-label">현재 배치한 도형의 넓이 합</div>
                <div class="expression empty" id="expression" aria-live="polite">아직 배치한 도형이 없어요</div>
                <div class="formula-divider"></div>
              </div>
              <button class="btn primary" id="revealBtn" type="button" disabled>완전제곱식으로 바꾸기</button>
              <div class="solution-panel" id="solutionPanel" hidden>
                <div class="expression result factorized-equation" id="factorized">(x + 5)² = 49</div>
                <fieldset class="quiz">
                  <legend>원래 방정식의 해를 모두 고른 것은?</legend>
                  <div class="choices">
                    <label class="choice"><input type="radio" name="answer" value="minus12"> x = -12만</label>
                    <label class="choice"><input type="radio" name="answer" value="plusminus5"> x = -5 또는 x = 5</label>
                    <label class="choice"><input type="radio" name="answer" value="both"> x = 2 또는 x = -12</label>
                    <label class="choice"><input type="radio" name="answer" value="plusminus7"> x = -7 또는 x = 7</label>
                    <label class="choice"><input type="radio" name="answer" value="two"> x = 2만</label>
                  </div>
                </fieldset>
                <button class="btn" id="checkAnswerBtn" type="button" disabled>정답 확인</button>
                <p class="answer-feedback" id="answerFeedback" aria-live="polite"></p>
              </div>
              <div class="progress-wrap">
                <div class="progress-info"><span>퍼즐 완성도</span><span id="progressText">0 / 4 조각</span></div>
                <div class="progress"><div class="progress-bar" id="progressBar"></div></div>
              </div>
            </section>
            <section class="card goal-card">
              <h2>오늘의 발견</h2>
              <p>비어 있는 모서리는 한 변이 5인 정사각형이에요. 단위 넓이로는 <b>5 × 5 = 25</b>이므로 양변에 25를 더하면 식이 완전제곱식이 됩니다.</p>
              <div class="complete-message" id="completeMessage">🎉 큰 정사각형을 완성했어요! 오른쪽 버튼을 눌러 식을 확인해 보세요.</div>
            </section>
          </aside>
        </div>
      </main>
      <script>
        (() => {
          const board = document.getElementById("board");
          const tray = document.getElementById("tray");
          const trayFeedback = document.getElementById("trayFeedback");
          const areaSumPanel = document.getElementById("areaSumPanel");
          const expression = document.getElementById("expression");
          const progressText = document.getElementById("progressText");
          const progressBar = document.getElementById("progressBar");
          const completeMessage = document.getElementById("completeMessage");
          const revealBtn = document.getElementById("revealBtn");
          const solutionPanel = document.getElementById("solutionPanel");
          const factorized = document.getElementById("factorized");
          const checkAnswerBtn = document.getElementById("checkAnswerBtn");
          const answerFeedback = document.getElementById("answerFeedback");
          const answerChoices = [...document.querySelectorAll('input[name="answer"]')];
          const unit = 28;
          const pieces = [];
          let selected = null;
          let drag = null;

          function createPiece(type, id, label, description, required = true) {
            const piece = document.createElement("div");
            piece.className = `piece piece-${type}`;
            piece.dataset.type = type;
            piece.dataset.id = id;
            piece.textContent = label;
            piece.setAttribute("role", "button");
            piece.setAttribute("aria-label", description);
            piece.tabIndex = 0;
            tray.appendChild(piece);
            pieces.push({ el: piece, type, id, placed: false, x: 0, y: 0, required });
            return piece;
          }

          createPiece("x2", "x2", "x²", "x 제곱 정사각형");
          createPiece("x-horizontal", "x-horizontal", "5x", "가로로 긴 5x 직사각형");
          createPiece("x-vertical", "x-vertical", "5x", "세로로 긴 5x 직사각형");
          createPiece("square25", "square25", "25", "넓이가 25인 정사각형");
          createPiece("x4-horizontal", "x4-horizontal", "4x", "가로로 긴 4x 오답 직사각형", false);
          createPiece("x4-vertical", "x4-vertical", "4x", "세로로 긴 4x 오답 직사각형", false);
          createPiece("x6-horizontal", "x6-horizontal", "6x", "가로로 긴 6x 오답 직사각형", false);
          createPiece("x6-vertical", "x6-vertical", "6x", "세로로 긴 6x 오답 직사각형", false);
          createPiece("square16", "square16", "16", "넓이가 16인 오답 정사각형", false);
          createPiece("square36", "square36", "36", "넓이가 36인 오답 정사각형", false);

          function cellsFor(piece, x, y) {
            const cells = [];
            if (piece.type === "x2") {
              for (let row = 0; row < 3; row++) {
                for (let col = 0; col < 3; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x-horizontal") {
              for (let row = 0; row < 3; row++) {
                for (let col = 0; col < 5; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x-vertical") {
              for (let row = 0; row < 5; row++) {
                for (let col = 0; col < 3; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x4-horizontal") {
              for (let row = 0; row < 3; row++) {
                for (let col = 0; col < 4; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x4-vertical") {
              for (let row = 0; row < 4; row++) {
                for (let col = 0; col < 3; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x6-horizontal") {
              for (let row = 0; row < 3; row++) {
                for (let col = 0; col < 6; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else if (piece.type === "x6-vertical") {
              for (let row = 0; row < 6; row++) {
                for (let col = 0; col < 3; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            } else {
              const side = piece.type === "square16" ? 4 : piece.type === "square36" ? 6 : 5;
              for (let row = 0; row < side; row++) {
                for (let col = 0; col < side; col++) cells.push(`${x + col * unit},${y + row * unit}`);
              }
            }
            return cells;
          }

          function dimensions(piece) {
            if (piece.type === "x2") return { width: 3 * unit, height: 3 * unit };
            if (piece.type === "x-horizontal") return { width: 5 * unit, height: 3 * unit };
            if (piece.type === "x-vertical") return { width: 3 * unit, height: 5 * unit };
            if (piece.type === "x4-horizontal") return { width: 4 * unit, height: 3 * unit };
            if (piece.type === "x4-vertical") return { width: 3 * unit, height: 4 * unit };
            if (piece.type === "x6-horizontal") return { width: 6 * unit, height: 3 * unit };
            if (piece.type === "x6-vertical") return { width: 3 * unit, height: 6 * unit };
            const side = piece.type === "square16" ? 4 : piece.type === "square36" ? 6 : 5;
            return { width: side * unit, height: side * unit };
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
            const placedCount = pieces.filter(piece => piece.required && piece.placed).length;
            progressText.textContent = `${placedCount} / 4 조각`;
            progressBar.style.width = `${(placedCount / 4) * 100}%`;

            const x2Placed = pieces.some(piece => piece.type === "x2" && piece.placed);
            const rectangleCount = pieces.filter(piece => piece.type.startsWith("x-") && piece.placed).length;
            const square25Placed = pieces.some(piece => piece.type === "square25" && piece.placed);
            const distractorAreas = pieces
              .filter(piece => !piece.required && piece.placed)
              .map(piece => ({
                "x4-horizontal": 12,
                "x4-vertical": 12,
                "x6-horizontal": 18,
                "x6-vertical": 18,
                square16: 16,
                square36: 36
              }[piece.type]));
            const terms = [];
            if (x2Placed) terms.push('<span class="term-x2">x²</span>');
            if (rectangleCount) terms.push(`<span class="term-x">${rectangleCount * 5}x</span>`);
            if (square25Placed) terms.push('<span class="term-unit">25</span>');
            for (const area of distractorAreas) terms.push(`<span class="term-distractor">${area}</span>`);
            let areaSum = terms.join(" + ");

            const filled = new Set();
            for (const piece of pieces) {
              if (piece.required && piece.placed) {
                for (const cell of cellsFor(piece, piece.x, piece.y)) filled.add(cell);
              }
            }
            const coordinates = [...filled].map(cell => cell.split(",").map(Number));
            const isSquareArrangement = coordinates.length > 0
              && Math.max(...coordinates.map(([x]) => x)) - Math.min(...coordinates.map(([x]) => x)) === 7 * unit
              && Math.max(...coordinates.map(([, y]) => y)) - Math.min(...coordinates.map(([, y]) => y)) === 7 * unit;
            const distractorPlaced = distractorAreas.length > 0;
            const complete = x2Placed && rectangleCount === 2 && square25Placed && !distractorPlaced
              && filled.size === 64
              && isSquareArrangement;
            if (complete) areaSum = "x² + 10x + 25 = 24 + 25";
            else if (x2Placed && rectangleCount === 2 && !square25Placed && !distractorPlaced) areaSum += " = 24";
            expression.innerHTML = areaSum || "아직 도형을 배치하지 않았어요";
            expression.classList.toggle("empty", !areaSum);

            trayFeedback.textContent = distractorPlaced ? "오답 조각은 필요한 빈칸의 크기와 맞지 않아요. 보관함으로 옮겨 주세요." : "";
            completeMessage.classList.toggle("show", complete);
            revealBtn.disabled = !complete;
            if (!complete) {
              areaSumPanel.hidden = false;
              solutionPanel.hidden = true;
              revealBtn.hidden = false;
              revealBtn.textContent = "완전제곱식으로 바꾸기";
              answerChoices.forEach(choice => { choice.checked = false; });
              checkAnswerBtn.disabled = true;
              answerFeedback.textContent = "";
            }
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
            const boardRect = board.getBoundingClientRect();
            const scale = boardRect.width / board.offsetWidth;
            const horizontalPosition = (event.clientX - rect.left) / rect.width;
            const verticalPosition = (event.clientY - rect.top) / rect.height;
            const pieceSize = dimensions(model);
            const x = (event.clientX - boardRect.left) / scale - horizontalPosition * pieceSize.width;
            const y = (event.clientY - boardRect.top) / scale - verticalPosition * pieceSize.height;
            setPosition(model, x, y);
            piece.classList.add("dragging");
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
            const targetX = Math.round(((event.clientX - boardRect.left) / drag.scale - drag.offsetX) / unit) * unit;
            const targetY = Math.round(((event.clientY - boardRect.top) / drag.scale - drag.offsetY) / unit) * unit;
            setPosition(drag.model, targetX, targetY);
          }

          function endDrag(event) {
            if (!drag) return;
            const { model, wasPlaced } = drag;
            let rejectedDistractor = false;
            const trayRect = tray.getBoundingClientRect();
            const droppedOnTray = event.clientX >= trayRect.left && event.clientX <= trayRect.right
              && event.clientY >= trayRect.top && event.clientY <= trayRect.bottom;
            if (droppedOnTray) {
              model.placed = false;
              model.el.classList.remove("dragging");
              model.el.style.cssText = "";
              tray.appendChild(model.el);
              choose(null);
              drag = null;
              updateEquation();
              return;
            }
            const x = Math.round((Number.parseFloat(model.el.style.left) || 0) / unit) * unit;
            const y = Math.round((Number.parseFloat(model.el.style.top) || 0) / unit) * unit;
            const { width, height } = dimensions(model);
            const withinBoard = x >= 0 && y >= 0 && x + width <= 12 * unit && y + height <= 12 * unit;
            model.el.classList.remove("dragging");
            if (withinBoard) {
              model.x = x;
              model.y = y;
              model.placed = true;
              setPosition(model, x, y);
              board.appendChild(model.el);
            } else if (!wasPlaced) {
              rejectedDistractor = !model.required;
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
            if (rejectedDistractor) trayFeedback.textContent = "이 오답 조각은 빈칸의 크기와 맞지 않아요.";
          }

          document.addEventListener("pointerdown", event => {
            const piece = event.target.closest(".piece");
            if (piece) startDrag(event, piece);
          });
          document.addEventListener("pointermove", moveDrag);
          document.addEventListener("pointerup", endDrag);
          document.addEventListener("pointercancel", endDrag);

          revealBtn.addEventListener("click", () => {
            areaSumPanel.hidden = true;
            solutionPanel.hidden = false;
            revealBtn.hidden = true;
            factorized.textContent = "(x + 5)² = 49";
          });

          answerChoices.forEach(choice => {
            choice.addEventListener("change", () => {
              checkAnswerBtn.disabled = false;
              answerFeedback.textContent = "";
            });
          });

          checkAnswerBtn.addEventListener("click", () => {
            const selectedAnswer = answerChoices.find(choice => choice.checked);
            if (!selectedAnswer) return;
            answerFeedback.textContent = selectedAnswer.value === "both"
              ? "정답이에요! x = 2 또는 x = -12입니다."
              : "다시 생각해 보세요. 제곱근을 풀 때 ± 두 경우를 모두 확인해요.";
          });

          document.getElementById("resetBtn").addEventListener("click", () => {
            for (const piece of pieces) {
              piece.placed = false;
              piece.el.classList.remove("selected", "dragging");
              piece.el.style.cssText = "";
              tray.appendChild(piece.el);
            }
            choose(null);
            trayFeedback.textContent = "";
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
