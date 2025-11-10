import React, { useState } from "react";
import "./App.css"; // optional styling file

function App() {
  const [display, setDisplay] = useState("0");
  const [memory, setMemory] = useState([]);

  const clearDisplay = () => setDisplay("0");

  const backspace = () => {
    setDisplay((prev) =>
      prev.length > 1 ? prev.slice(0, -1) : "0"
    );
  };

  const append = (char) => {
    setDisplay((prev) =>
      prev === "0" && char !== "." ? char : prev + char
    );
  };

  const calculate = () => {
    try {
      const expr = display.replace(/÷/g, "/").replace(/×/g, "*");
      const result = eval(expr); // simple eval for demo
      setMemory([{ expr: display, result }, ...memory]);
      setDisplay(String(result));
    } catch {
      setDisplay("Error");
    }
  };

  const negate = () => {
    try {
      const val = parseFloat(display);
      setDisplay(String(-val));
    } catch {
      setDisplay("Error");
    }
  };

  const copyResult = async () => {
    try {
      await navigator.clipboard.writeText(display);
    } catch {}
  };

  const pasteNumber = async () => {
    try {
      const text = await navigator.clipboard.readText();
      if (!isNaN(text)) setDisplay(text);
    } catch {}
  };

  const clearMemory = () => setMemory([]);

  return (
    <div className="container">
      <div className="calculator">
        <div className="display">{display}</div>
        <div className="buttons">
          <button className="other" onClick={clearDisplay}>C</button>
          <button className="other" onClick={backspace}>⌫</button>
          <button className="other" onClick={() => append("%")}>%</button>
          <button className="op" onClick={() => append("÷")}>÷</button>

          <button className="num" onClick={() => append("7")}>7</button>
          <button className="num" onClick={() => append("8")}>8</button>
          <button className="num" onClick={() => append("9")}>9</button>
          <button className="op" onClick={() => append("×")}>×</button>

          <button className="num" onClick={() => append("4")}>4</button>
          <button className="num" onClick={() => append("5")}>5</button>
          <button className="num" onClick={() => append("6")}>6</button>
          <button className="op" onClick={() => append("-")}>−</button>

          <button className="num" onClick={() => append("1")}>1</button>
          <button className="num" onClick={() => append("2")}>2</button>
          <button className="num" onClick={() => append("3")}>3</button>
          <button className="op" onClick={() => append("+")}>+</button>

          <button className="other" onClick={negate}>±</button>
          <button className="num" onClick={() => append("0")}>0</button>
          <button className="other" onClick={() => append(".")}>.</button>
          <button className="op" onClick={calculate}>=</button>

          <button className="other wide" onClick={copyResult}>Copy</button>
          <button className="other wide" onClick={pasteNumber}>Paste</button>
          <button className="other wide" onClick={clearMemory}>Clear Memory</button>
        </div>
      </div>

      <div className="memory">
        <h3>Memory Bank</h3>
        <ul>
          {memory.map((m, i) => (
            <li key={i}>
              {m.expr} = {m.result}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
