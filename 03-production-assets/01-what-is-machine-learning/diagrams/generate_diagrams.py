import os

diag_dir = "."
os.makedirs(diag_dir, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(diag_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 1. Core ML Mental Model
svg_mental_model = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 8px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 20px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
    .arrow { stroke: #58a6ff; stroke-width: 3px; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 10 5 L 0 8 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <text x="400" y="40" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="bold" text-anchor="middle">Core ML Mental Model</text>
  <rect x="250" y="80" width="300" height="60" class="box"/>
  <text x="400" y="110" class="text">Data / Experience</text>
  <path d="M 400 140 L 400 180" class="arrow"/>
  <rect x="250" y="180" width="300" height="60" class="box"/>
  <text x="400" y="210" class="text">Learning Procedure</text>
  <path d="M 400 240 L 400 280" class="arrow"/>
  <rect x="250" y="280" width="300" height="60" class="box" stroke="#58a6ff"/>
  <text x="400" y="310" class="text" fill="#58a6ff">Trained Model</text>
  <path d="M 400 340 L 400 380" class="arrow"/>
  <rect x="250" y="380" width="300" height="60" class="box"/>
  <text x="400" y="410" class="text">New Input</text>
  <path d="M 400 440 L 400 480" class="arrow"/>
  <rect x="250" y="480" width="300" height="60" class="box" fill="#1f6feb"/>
  <text x="400" y="510" class="text" fill="#ffffff">Prediction</text>
</svg>"""

# 2. Traditional vs ML
svg_trad_vs_ml = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="500" viewBox="0 0 900 500">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title { fill: #ffffff; font-family: sans-serif; font-size: 22px; font-weight: bold; text-anchor: middle; }
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 6px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 16px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
    .arrow { stroke: #58a6ff; stroke-width: 2.5px; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 10 5 L 0 8 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <text x="450" y="40" class="title">Traditional Programming vs. Machine Learning</text>
  <text x="225" y="90" fill="#8b949e" font-family="sans-serif" font-size="18" text-anchor="middle">Traditional Programming</text>
  <rect x="75" y="130" width="130" height="50" class="box"/>
  <text x="140" y="155" class="text">Input Data</text>
  <rect x="245" y="130" width="130" height="50" class="box"/>
  <text x="310" y="155" class="text">Explicit Rules</text>
  <path d="M 205 155 L 245 155" class="arrow"/>
  <path d="M 310 180 L 310 230" class="arrow"/>
  <rect x="160" y="230" width="300" height="50" class="box" fill="#1f6feb"/>
  <text x="310" y="255" class="text" fill="#ffffff">Computer Program / Result</text>
  <text x="675" y="90" fill="#8b949e" font-family="sans-serif" font-size="18" text-anchor="middle">Machine Learning</text>
  <rect x="525" y="130" width="140" height="50" class="box"/>
  <text x="595" y="155" class="text">Examples</text>
  <rect x="695" y="130" width="140" height="50" class="box"/>
  <text x="765" y="155" class="text">Learning Alg.</text>
  <path d="M 665 155 L 695 155" class="arrow"/>
  <path d="M 765 180 L 765 230" class="arrow"/>
  <rect x="615" y="230" width="300" height="50" class="box" stroke="#58a6ff"/>
  <text x="765" y="255" class="text" fill="#58a6ff">Trained Model</text>
</svg>"""

# 3. Training vs Inference
svg_train_inference = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="450" viewBox="0 0 900 450">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title { fill: #ffffff; font-family: sans-serif; font-size: 22px; font-weight: bold; text-anchor: middle; }
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 6px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 15px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
    .arrow { stroke: #58a6ff; stroke-width: 2.5px; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 10 5 L 0 8 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <text x="450" y="40" class="title">Phase 1: Training vs. Phase 2: Inference</text>
  <text x="225" y="90" fill="#238636" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">TRAINING (Learning)</text>
  <rect x="75" y="130" width="300" height="50" class="box"/>
  <text x="225" y="155" class="text">Historical Data + Labels</text>
  <path d="M 225 180 L 225 220" class="arrow"/>
  <rect x="75" y="220" width="300" height="50" class="box" fill="#238636" stroke="#2ea043"/>
  <text x="225" y="245" class="text" fill="#ffffff">Trained Model Output</text>

  <text x="675" y="90" fill="#1f6feb" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">INFERENCE (Production)</text>
  <rect x="525" y="130" width="300" height="50" class="box"/>
  <text x="675" y="155" class="text">Trained Model + New Input</text>
  <path d="M 675 180 L 675 220" class="arrow"/>
  <rect x="525" y="220" width="300" height="50" class="box" fill="#1f6feb"/>
  <text x="675" y="245" class="text" fill="#ffffff">Real-time Prediction</text>
</svg>"""

# 4. Supervised Learning Flow
svg_supervised = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title { fill: #ffffff; font-family: sans-serif; font-size: 22px; font-weight: bold; text-anchor: middle; }
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 6px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 16px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
    .arrow { stroke: #58a6ff; stroke-width: 2.5px; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 10 5 L 0 8 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <text x="400" y="40" class="title">Supervised Learning Data Flow</text>
  <rect x="250" y="80" width="300" height="50" class="box"/>
  <text x="400" y="105" class="text">Features (X: Inputs)</text>
  <rect x="250" y="150" width="300" height="50" class="box"/>
  <text x="400" y="175" class="text">Labels (Y: Correct Answers)</text>
  <path d="M 400 200 L 400 250" class="arrow"/>
  <rect x="200" y="250" width="400" height="60" class="box" stroke="#58a6ff"/>
  <text x="400" y="280" class="text" fill="#58a6ff">Learning Algorithm (Optimization)</text>
  <path d="M 400 310 L 400 360" class="arrow"/>
  <rect x="250" y="360" width="300" height="50" class="box" fill="#1f6feb"/>
  <text x="400" y="385" class="text" fill="#ffffff">Predictive Model</text>
</svg>"""

# 5. Generalization Concept
svg_generalization = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title { fill: #ffffff; font-family: sans-serif; font-size: 22px; font-weight: bold; text-anchor: middle; }
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 6px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 15px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
  </style>
  <text x="450" y="40" class="title">The Generalization Spectrum</text>
  
  <rect x="50" y="90" width="240" height="240" class="box"/>
  <text x="170" y="125" fill="#f85149" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Underfitting</text>
  <text x="170" y="170" class="text">Model is too simple.</text>
  <text x="170" y="200" class="text">Misses patterns entirely.</text>
  <text x="170" y="260" fill="#8b949e" font-family="sans-serif" font-size="14" text-anchor="middle">High Bias</text>

  <rect x="330" y="90" width="240" height="240" class="box" stroke="#2ea043"/>
  <text x="450" y="125" fill="#2ea043" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Good Generalization</text>
  <text x="450" y="170" class="text">Balanced complexity.</text>
  <text x="450" y="200" class="text">Performs well on new data.</text>
  <text x="450" y="260" fill="#8b949e" font-family="sans-serif" font-size="14" text-anchor="middle">Optimal Balance</text>

  <rect x="610" y="90" width="240" height="240" class="box"/>
  <text x="730" y="125" fill="#f85149" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">Overfitting</text>
  <text x="730" y="170" class="text">Memorizes training noise.</text>
  <text x="730" y="200" class="text">Fails on unseen data.</text>
  <text x="730" y="260" fill="#8b949e" font-family="sans-serif" font-size="14" text-anchor="middle">High Variance</text>
</svg>"""

# 6. Spam Classifier Example
svg_spam_classifier = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <style>
    .title { fill: #ffffff; font-family: sans-serif; font-size: 22px; font-weight: bold; text-anchor: middle; }
    .box { fill: #161b22; stroke: #30363d; stroke-width: 2px; rx: 6px; }
    .text { fill: #c9d1d9; font-family: sans-serif; font-size: 15px; font-weight: bold; text-anchor: middle; dominant-baseline: middle; }
    .arrow { stroke: #58a6ff; stroke-width: 2.5px; fill: none; marker-end: url(#arrow); }
  </style>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 10 5 L 0 8 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <text x="450" y="40" class="title">Real-world Example: Spam Email Classifier</text>
  
  <rect x="50" y="160" width="160" height="60" class="box"/>
  <text x="130" y="195" class="text">Incoming Email</text>

  <path d="M 210 190 L 270 190" class="arrow"/>

  <rect x="270" y="150" width="180" height="80" class="box"/>
  <text x="360" y="180" class="text">Feature Extractor</text>
  <text x="360" y="205" fill="#8b949e" font-family="sans-serif" font-size="12" text-anchor="middle">("FREE", "Win", links)</text>

  <path d="M 450 190 L 510 190" class="arrow"/>

  <rect x="510" y="150" width="160" height="80" class="box" stroke="#58a6ff"/>
  <text x="590" y="195" class="text" fill="#58a6ff">Trained ML Model</text>

  <path d="M 670 190 L 730 190" class="arrow"/>

  <rect x="730" y="150" width="120" height="80" class="box" fill="#1f6feb"/>
  <text x="790" y="185" class="text" fill="#ffffff">Spam /</text>
  <text x="790" y="205" class="text" fill="#ffffff">Not Spam</text>
</svg>"""

# Writing all files
write_svg("core-ml-mental-model.svg", svg_mental_model)
write_svg("traditional-vs-ml.svg", svg_trad_vs_ml)
write_svg("training-vs-inference.svg", svg_train_inference)
write_svg("supervised-learning-flow.svg", svg_supervised)
write_svg("generalization-concept.svg", svg_generalization)
write_svg("spam-classifier-example.svg", svg_spam_classifier)

print("All 6 master diagrams successfully generated!")
