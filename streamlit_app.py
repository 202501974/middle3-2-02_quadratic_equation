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
          touch-action: none; overflow: visible;
        }
        .piece {
          position: absolute; width: var(--piece-width); height: var(--piece-height);
          display: grid; place-items: center; border: 2px solid #fff;
          border-radius: 8px; cursor: grab; user-select: none; touch-action: none;
          box-shadow: none; transition: left .07s linear, top .07s linear, filter .12s;
          z-index: 2; font-weight: 800;
        }
        .piece:active { cursor: grabbing; }
        .piece.selected { outline: none; box-shadow: inset 0 0 0 3px #293d72; z-index: 5; }
        .piece.dragging { opacity: .88; box-shadow: none; z-index: 10; }
        .board .piece.dragging { z-index: 20; }
        .piece-x2 { background: #7d8df1; color: white; font-size: 20px; }
        .piece-x-horizontal, .piece-x-vertical {
          background: hsl(var(--rectangle-color-hue, 35deg) 75% 78%);
          background: oklch(82% 0.1 var(--rectangle-color-hue, 35deg));
          color: #413631; font-size: 14px;
        }
        .piece-distractor-rect {
          background: hsl(calc(var(--rectangle-color-hue, 35deg) - 29deg) 75% 78%);
          background: oklch(82% 0.1 calc(var(--rectangle-color-hue, 35deg) - 29deg));
          color: #413631; font-size: 13px;
        }
        .piece-square { background: #69c9ad; color: #155945; font-size: 16px; }
        .piece-distractor-square { background: #d7a3d8; color: #563458; font-size: 16px; }
        .tray { min-height: 150px; padding: 12px; border-radius: 12px; background: #f7f8fc; border: 1px solid #edf0f6; }
        .tray-title { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; color: #78849a; font-size: 12px; font-weight: 700; }
        .tray-pieces { display: flex; flex-wrap: wrap; align-content: flex-start; gap: 8px; min-height: 74px; }
        .tray .piece { position: relative; inset: auto !important; flex: 0 0 auto; width: calc(var(--piece-width) / 2); height: calc(var(--piece-height) / 2); font-size: 11px; }
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
        .solving-steps { margin-top: 12px; color: #66583e; font-size: 15px; font-weight: 700; line-height: 1.9; overflow-wrap: anywhere; }
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
          <div><div class="problem-label" id="problemLabel">오늘의 문제</div><div class="problem-expression" id="problemExpression">x² + 10x = 24</div></div>
        </section>

        <div class="layout">
          <section class="card board-card">
            <div class="section-head">
              <div><h2>큰 정사각형 만들기</h2><p class="hint" id="activityHint">필요한 네 조각을 골라 판에 끌어 놓아 빈틈없이 채워 보세요. 크기가 다른 도형은 오답 조각이에요.</p></div>
            </div>
            <div class="board-stage">
              <div class="board" id="board" aria-label="도형을 배치하는 격자">
              </div>
            </div>
            <div class="tray">
              <div class="tray-title"><span>도형 조각</span></div>
              <div class="tray-pieces" id="tray"></div>
              <p class="tray-feedback" id="trayFeedback" aria-live="polite"></p>
            </div>
            <div class="tools">
              <button class="btn" id="resetBtn" type="button">다시 시작</button>
              <button class="btn primary" id="nextProblemBtn" type="button" hidden>다른 문제 풀어보기</button>
            </div>
          </section>

          <aside class="side">
            <section class="card lesson-card">
              <h2>활동 방법</h2>
              <div class="step"><span class="step-num">1</span><p>조각을 퍼즐 판 위에 올려 보세요.</p></div>
              <div class="step"><span class="step-num">2</span><p>조각을 옮겨 큰 정사각형을 만들어 보세요.</p></div>
              <div class="step"><span class="step-num">3</span><p>도형의 넓이 합이 어떻게 변하는지 살펴보세요.</p></div>
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
                  <div class="choices" id="choices"></div>
                </fieldset>
                <button class="btn" id="checkAnswerBtn" type="button" disabled>정답 확인</button>
                <p class="answer-feedback" id="answerFeedback" aria-live="polite"></p>
              </div>
              <div class="progress-wrap">
                <div class="progress-info"><span>퍼즐 완성도</span><span id="progressText">0 / 4 조각</span></div>
                <div class="progress"><div class="progress-bar" id="progressBar"></div></div>
              </div>
            </section>
            <section class="card goal-card" id="processCard" hidden>
              <h2>이차방정식 풀이 과정</h2>
              <div class="solving-steps" id="processHint"></div>
              <div class="solving-steps" id="solvingSteps" hidden></div>
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
          const processCard = document.getElementById("processCard");
          const processHint = document.getElementById("processHint");
          const solvingSteps = document.getElementById("solvingSteps");
          const revealBtn = document.getElementById("revealBtn");
          const solutionPanel = document.getElementById("solutionPanel");
          const factorized = document.getElementById("factorized");
          const checkAnswerBtn = document.getElementById("checkAnswerBtn");
          const answerFeedback = document.getElementById("answerFeedback");
          const choices = document.getElementById("choices");
          const problemExpression = document.getElementById("problemExpression");
          const problemLabel = document.getElementById("problemLabel");
          const nextProblemBtn = document.getElementById("nextProblemBtn");
          const unit = 28;
          const pieces = [];
          const problems = [
            { coefficient: 5, rightSide: 24 },
            { coefficient: 4, rightSide: 9 },
            { coefficient: 3, rightSide: 16 },
            { coefficient: 6, rightSide: 13 },
            { coefficient: 7, rightSide: 32 },
            { coefficient: 8, rightSide: 17 },
            { coefficient: 2, rightSide: 21 },
            { coefficient: 9, rightSide: 19 },
            { coefficient: 8, rightSide: 57 },
            { coefficient: 7, rightSide: 51 },
            { coefficient: 6, rightSide: 28 }
          ];
          let problemIndex = 0;
          let problem = problems[problemIndex];
          let selected = null;
          let drag = null;

          function createPiece({ type, id, label, description, columns, rows, required = true, term }) {
            const piece = document.createElement("div");
            piece.className = `piece piece-${type}`;
            piece.textContent = label;
            piece.setAttribute("role", "button");
            piece.setAttribute("aria-label", description);
            piece.tabIndex = 0;
            setPieceSize(piece, columns, rows);
            tray.appendChild(piece);
            pieces.push({ el: piece, type, id, columns, rows, required, term, placed: false, x: 0, y: 0 });
            return piece;
          }

          function setPieceSize(piece, columns, rows) {
            piece.style.setProperty("--piece-width", `${columns * unit}px`);
            piece.style.setProperty("--piece-height", `${rows * unit}px`);
          }

          function buildPieces() {
            const a = problem.coefficient;
            const wrongCoefficients = [a - 1, a + 1];
            const wrongSquares = [a - 1, a + 1];
            pieces.length = 0;
            tray.replaceChildren();
            board.replaceChildren();
            createPiece({ type: "x2", id: "x2", label: "x²", description: "x 제곱 정사각형", columns: 3, rows: 3, term: "x²" });
            createPiece({ type: "x-horizontal", id: "x-horizontal", label: `${a}x`, description: `가로로 긴 ${a}x 직사각형`, columns: a, rows: 3, term: `${a}x` });
            createPiece({ type: "x-vertical", id: "x-vertical", label: `${a}x`, description: `세로로 긴 ${a}x 직사각형`, columns: 3, rows: a, term: `${a}x` });
            createPiece({ type: "square", id: "square-correct", label: `${a * a}`, description: `넓이가 ${a * a}인 정사각형`, columns: a, rows: a, term: `${a * a}` });
            for (const coefficient of wrongCoefficients) {
              for (const direction of ["horizontal", "vertical"]) {
                createPiece({
                  type: "distractor-rect",
                  id: `rect-${coefficient}-${direction}`,
                  label: `${coefficient}x`,
                  description: `${direction === "horizontal" ? "가로" : "세로"}로 긴 ${coefficient}x 오답 직사각형`,
                  columns: direction === "horizontal" ? coefficient : 3,
                  rows: direction === "horizontal" ? 3 : coefficient,
                  required: false,
                  term: `${coefficient}x`
                });
              }
            }
            for (const side of wrongSquares) {
              createPiece({
                type: "distractor-square",
                id: `square-${side * side}`,
                label: `${side * side}`,
                description: `넓이가 ${side * side}인 오답 정사각형`,
                columns: side,
                rows: side,
                required: false,
                term: `${side * side}`
              });
            }
            problemExpression.textContent = `x² + ${2 * a}x = ${problem.rightSide}`;
            problemLabel.textContent = problemIndex === 0 ? "오늘의 문제" : `도전 문제 ${problemIndex} / ${problems.length - 1}`;
            processHint.textContent = `x² + ${2 * a}x = ${problem.rightSide}`;
            solvingSteps.innerHTML = "";
            answerChoicesMarkup();
          }

          function answerChoicesMarkup() {
            const a = problem.coefficient;
            const root = Math.sqrt(a * a + problem.rightSide);
            const firstRoot = -a + root;
            const secondRoot = -a - root;
            const formatRoot = value => `${value}`;
            const options = [
              { value: "first-only", label: `x = ${firstRoot}만` },
              { value: "opposite-pair", label: `x = -${a} 또는 x = ${a}` },
              { value: "both", label: `x = ${firstRoot} 또는 x = ${secondRoot}` },
              { value: "root-pair", label: `x = ${-a - root - 1} 또는 x = ${-a + root + 1}` },
              { value: "second-only", label: `x = ${secondRoot}만` }
            ];
            choices.replaceChildren();
            for (const option of options) {
              const label = document.createElement("label");
              label.className = "choice";
              const input = document.createElement("input");
              input.type = "radio";
              input.name = "answer";
              input.value = option.value;
              input.addEventListener("change", () => {
                checkAnswerBtn.disabled = false;
                answerFeedback.textContent = "";
                solvingSteps.hidden = true;
                nextProblemBtn.hidden = true;
              });
              label.append(input, document.createTextNode(` ${option.label}`));
              choices.appendChild(label);
            }
            buildSolvingSteps(root, firstRoot, secondRoot, formatRoot);
          }

          function buildSolvingSteps(root, firstRoot, secondRoot, formatRoot) {
            const a = problem.coefficient;
            const rightSide = problem.rightSide;
            solvingSteps.innerHTML = [
              `x² + ${2 * a}x = ${rightSide}`,
              `x² + ${2 * a}x + ${a * a} = ${rightSide} + ${a * a}`,
              `(x + ${a})² = ${a * a + rightSide}`,
              `x + ${a} = ±${root}`,
              `x = ${formatRoot(firstRoot)} 또는 x = ${formatRoot(secondRoot)}`
            ].map(step => `<div>${step}</div>`).join("");
          }

          function answerChoicesList() {
            return [...choices.querySelectorAll('input[name="answer"]')];
          }

          function setupProblem() {
            problem = problems[problemIndex];
            document.documentElement.style.setProperty("--rectangle-color-hue", `${35 + problemIndex * 31}deg`);
            const a = problem.coefficient;
            const rightSide = problem.rightSide;
            problemExpression.textContent = `x² + ${2 * a}x = ${rightSide}`;
            problemLabel.textContent = problemIndex === 0 ? "오늘의 문제" : "도전 문제";
            processHint.textContent = `x² + ${2 * a}x = ${rightSide}`;
            factorized.textContent = `(x + ${a})² = ${a * a + rightSide}`;
            processCard.hidden = true;
            nextProblemBtn.hidden = true;
            areaSumPanel.hidden = false;
            solutionPanel.hidden = true;
            revealBtn.hidden = false;
            revealBtn.disabled = true;
            revealBtn.textContent = "완전제곱식으로 바꾸기";
            processHint.hidden = false;
            solvingSteps.hidden = true;
            checkAnswerBtn.disabled = true;
            answerFeedback.textContent = "";
            trayFeedback.textContent = "";
            buildPieces();
            updateEquation();
          }

          function cellsFor(piece, x, y) {
            const cells = [];
            for (let row = 0; row < piece.rows; row++) {
              for (let col = 0; col < piece.columns; col++) {
                cells.push(`${x + col * unit},${y + row * unit}`);
              }
            }
            return cells;
          }

          function dimensions(piece) {
            return { width: piece.columns * unit, height: piece.rows * unit };
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

            const x2Placed = pieces.some(piece => piece.required && piece.type === "x2" && piece.placed);
            const rectangleCount = pieces.filter(piece => piece.required && piece.type.startsWith("x-") && piece.placed).length;
            const squarePlaced = pieces.some(piece => piece.required && piece.type === "square" && piece.placed);
            const distractorPieces = pieces
              .filter(piece => !piece.required && piece.placed)
            const distractorAreas = distractorPieces.map(piece => piece.term);
            const distractorX = distractorPieces.reduce((sum, piece) =>
              sum + (piece.term.endsWith("x") ? Number.parseInt(piece.term, 10) : 0), 0);
            const distractorConstant = distractorPieces.reduce((sum, piece) =>
              sum + (piece.term.endsWith("x") ? 0 : Number(piece.term)), 0);
            const terms = [];
            if (x2Placed) terms.push('<span class="term-x2">x²</span>');
            const xCoefficient = rectangleCount * problem.coefficient + distractorX;
            if (xCoefficient) {
              const termClass = distractorX ? "term-distractor" : "term-x";
              terms.push(`<span class="${termClass}">${xCoefficient}x</span>`);
            }
            const constant = (squarePlaced ? problem.coefficient ** 2 : 0) + distractorConstant;
            if (constant) {
              const termClass = distractorConstant ? "term-distractor" : "term-unit";
              terms.push(`<span class="${termClass}">${constant}</span>`);
            }
            let areaSum = terms.join(" + ");

            const filled = new Set();
            for (const piece of pieces) {
              if (piece.required && piece.placed) {
                for (const cell of cellsFor(piece, piece.x, piece.y)) filled.add(cell);
              }
            }
            const coordinates = [...filled].map(cell => cell.split(",").map(Number));
            const targetSide = problem.coefficient + 3;
            const isSquareArrangement = coordinates.length > 0
              && Math.max(...coordinates.map(([x]) => x)) - Math.min(...coordinates.map(([x]) => x)) === (targetSide - 1) * unit
              && Math.max(...coordinates.map(([, y]) => y)) - Math.min(...coordinates.map(([, y]) => y)) === (targetSide - 1) * unit;
            const distractorPlaced = distractorAreas.length > 0;
            const complete = x2Placed && rectangleCount === 2 && squarePlaced && !distractorPlaced
              && filled.size === targetSide ** 2
              && isSquareArrangement;
            if (complete) areaSum = `x² + ${2 * problem.coefficient}x + ${problem.coefficient ** 2} = ${problem.rightSide} + ${problem.coefficient ** 2}`;
            else if (x2Placed && rectangleCount === 2 && !squarePlaced && !distractorPlaced) areaSum += ` = ${problem.rightSide}`;
            expression.innerHTML = areaSum || "아직 도형을 배치하지 않았어요";
            expression.classList.toggle("empty", !areaSum);

            trayFeedback.textContent = distractorPlaced ? "방정식을 다시 한번 확인해 주세요." : "";
            revealBtn.disabled = !complete;
            if (!complete) {
              areaSumPanel.hidden = false;
              solutionPanel.hidden = true;
              revealBtn.hidden = false;
              revealBtn.textContent = "완전제곱식으로 바꾸기";
              processHint.hidden = false;
              solvingSteps.hidden = true;
              nextProblemBtn.hidden = true;
              answerChoicesList().forEach(choice => { choice.checked = false; });
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
              setPieceSize(model.el, model.columns, model.rows);
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
            if (rejectedDistractor) trayFeedback.textContent = "방정식을 다시 한번 확인해 주세요.";
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
            processHint.hidden = true;
            solvingSteps.hidden = true;
          });

          checkAnswerBtn.addEventListener("click", () => {
            const selectedAnswer = answerChoicesList().find(choice => choice.checked);
            if (!selectedAnswer) return;
            const correct = selectedAnswer.value === "both";
            answerFeedback.textContent = correct
              ? `정답이에요! ${solvingSteps.lastElementChild.textContent}`
              : "다시 생각해 보세요. 제곱근을 풀 때 ± 두 경우를 모두 확인해요.";
            solvingSteps.hidden = false;
            processCard.hidden = false;
            nextProblemBtn.hidden = !correct || problemIndex >= problems.length - 1;
          });

          nextProblemBtn.addEventListener("click", () => {
            if (problemIndex >= problems.length - 1) return;
            problemIndex += 1;
            setupProblem();
          });

          document.getElementById("resetBtn").addEventListener("click", () => {
            for (const piece of pieces) {
              piece.placed = false;
              piece.el.classList.remove("selected", "dragging");
              piece.el.style.cssText = "";
              setPieceSize(piece.el, piece.columns, piece.rows);
              tray.appendChild(piece.el);
            }
            choose(null);
            trayFeedback.textContent = "";
            updateEquation();
          });

          setupProblem();
        })();
      </script>
    </body>
    </html>
    """,
    height=1120,
    scrolling=True,
)
