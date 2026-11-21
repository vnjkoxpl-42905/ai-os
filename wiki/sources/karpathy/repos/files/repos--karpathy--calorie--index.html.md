---
type: source
subject: "GitHub source repos/karpathy/calorie/index.html"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/calorie/index.html]
semantic-status: complete-named-text-read
---

# repos/karpathy/calorie/index.html

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/calorie/index.html), SHA-256 `9c6a7c9e0252bd7a7cfbd287e4583caf57d291d763b4f8bebe8b14d0bcebe604`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Calorie Status</title> <style> body
```

Calorie is a simple in-memory personal counter with fixed resting-burn and target-deficit assumptions; it offers no persistence or individualized medical validation. Char-rnn defines explicit recurrent, GRU and LSTM timestep graphs with dropout between layers and a log-softmax decoder. Inspection prints checkpoint options and validation losses; GPU conversion is explicitly a temporary patch. Sampling credits the Oxford practical, initializes recurrent state, supports seeded prompts, temperature or argmax, evaluates dropout mode and prints CPU fallback warnings when GPU libraries are unavailable. Checkpoint/device compatibility is warned about rather than automatically guaranteed; no model execution occurred.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calorie Status</title>

<style>
body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
}

.container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-bottom: 20px;
}

.counter {
    font-size: 48px;
    margin-bottom: 20px;
}

#deficit-count {
    font-size: 24px;
}

button {
    margin: 5px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#reset-button {
    background-color: #ff6347;
    color: white;
}

#exercise-button {
    background-color: #4caf50;
    color: white;
}

#eat-button {
    background-color: #2196f3;
    color: white;
}
</style>

</head>
<body>
    <div class="container">
        <h1>Calorie Status</h1>
        <div class="counter">
            <p id="calorie-count">0</p>
            <p id="deficit-count">0</p>
        </div>
        <button id="reset-button">Reset</button>
        <button id="exercise-button">-100 kcal</button>
        <button id="eat-button">+100 kcal</button>
    </div>

<script type="text/javascript">

// user configuration ------
// these will count our calories burned at rest
let calorieCount = 0;
const hourlyCalorieBurn = 2000 / 24.0; // burned per hour
// goal is to lose 500 kcal/day (i.e. ~1 lb/week)
let desiredDeficitCount = 0;
const hourlyCalorieTargetDeficit = 500 / 24.0;
// --------------------------

let lastUpdateTime = Date.now();

function updateCalorieCount() {
    const currentTime = Date.now();
    const elapsedHours = (currentTime - lastUpdateTime) / (1000 * 60 * 60);
    calorieCount -= elapsedHours * hourlyCalorieBurn;
    desiredDeficitCount -= elapsedHours * hourlyCalorieTargetDeficit;
    lastUpdateTime = currentTime;
    document.getElementById('calorie-count').innerText = calorieCount.toFixed(2);
    document.getElementById('deficit-count').innerText = "GOAL: " + desiredDeficitCount.toFixed(2);
    let color = calorieCount < desiredDeficitCount ? 'green' : 'red'; // green if met, red otherwise
    document.getElementById('deficit-count').style.color = color;
}

document.getElementById('reset-button').addEventListener('click', () => {
    calorieCount = 0;
    desiredDeficitCount = 0; // reset the goal counter as well
    lastUpdateTime = Date.now();
});

document.getElementById('exercise-button').addEventListener('click', () => {
    updateCalorieCount();
    calorieCount -= 100;
});

document.getElementById('eat-button').addEventListener('click', () => {
    updateCalorieCount();
    calorieCount += 100;
});

setInterval(updateCalorieCount, 500); // update counter every 500ms
</script>

</body>
</html>

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
