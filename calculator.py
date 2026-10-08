<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Эко-след школьной формы</title>
  <style>
    :root {
      --bg-body: #F2F4F7;
      --card-bg: #FFFFFF;
      --text-main: #333333;
      --text-secondary: #666666;
      --accent: #5A7D9A; /* приглушённый серо-синий */
      --accent-hover: #4A6B82;
      --border: #CCCCCC;
    }
    body {
      font-family: Arial, Helvetica, sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      margin: 0;
      padding: 0;
    }
    header {
      background-color: #E8EBF0;
      color: var(--text-main);
      padding: 2rem 1rem;
      text-align: center;
      border-bottom: 1px solid var(--border);
    }
    .container {
      max-width: 960px;
      margin: 0 auto;
      padding: 1.5rem;
    }
    h2 {
      text-align: center;
      color: var(--text-main);
      margin-bottom: 1.5rem;
    }

    /* Калькулятор */
    .calc-card {
      background: var(--card-bg);
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      border: 1px solid var(--border);
    }
    .form-row {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 1rem;
    }
    .form-col {
      flex: 1 1 280px;
    }
    label {
      display: block;
      margin-top: 0.75rem;
      font-weight: 600;
      color: var(--text-main);
    }
    select, input[type="range"] {
      width: 100%;
      margin-top: 0.5rem;
      padding: 0.6rem;
      border: 1px solid var(--border);
      border-radius: 4px;
      font-size: 1rem;
    }
    .range-value {
      margin-left: 0.5rem;
      font-weight: bold;
      color: var(--accent);
    }
    .checkbox-group {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-top: 0.75rem;
      padding-top: 0.75rem;
      border-top: 1px dashed var(--border);
    }
    .result-box {
      margin-top: 2rem;
      padding: 1.5rem;
      background: #F9FAFC;
      border: 2px solid var(--accent);
      border-radius: 8px;
      text-align: center;
    }
    .result-value {
      font-size: 2.5rem;
      font-weight: bold;
      color: #2B3C50;
      line-height: 1.2;
    }
    .result-note {
      color: var(--text-secondary);
      margin-top: 0.5rem;
      font-style: italic;
    }
    button {
      background-color: var(--accent);
      color: white;
      border: none;
      padding: 0.8rem 1.4rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 1rem;
      transition: background 0.2s;
    }
    button:hover {
      background-color: var(--accent-hover);
    }
    button.secondary {
      background-color: #9CA3AF;
      margin-left: 0.5rem;
    }
    button.secondary:hover {
      background-color: #6B7280;
    }

    /* Таблица */
    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      border-radius: 6px;
      overflow: hidden;
    }
    th, td {
      padding: 0.8rem 1rem;
      border-bottom: 1px solid var(--border);
      text-align: left;
    }
    th {
      background: #EFF1F5;
      font-weight: 600;
    }
    .highlight-col {
      background: rgba(90, 125, 154, 0.1);
      font-weight: 600;
      color: #2B3C50;
    }

    /* Карточки советов */
    .tips-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
    }
    .tip-card {
      background: #FAFAFA;
      border: 1px solid var(--border);
      padding: 1rem;
      border-radius: 6px;
    }
    .tip-card h4 {
      margin: 0 0 0.3rem 0;
      color: var(--accent);
    }

    /* Блок кода */
    pre {
      background: #1E1E1E;
      color: #D4D4D4;
      padding: 1rem;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 0.9rem;
    }
    code {
      font-family: Consolas, monospace;
    }
  </style>
</head>
<body>
  <header>
    <h1>Веб-сайт «Эко-след школьной формы»</h1>
    <p>Расчёт срока службы вещей и варианты продления их ресурса</p>
  </header>

  <div class="container">
    <!-- Актуальность -->
    <section>
      <h2>Актуальность проекта</h2>
      <div style="display:flex; gap:1rem; flex-wrap:wrap;">
        <div style="flex:1;
