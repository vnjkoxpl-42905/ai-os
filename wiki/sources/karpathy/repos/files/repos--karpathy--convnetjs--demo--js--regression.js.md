---
type: source
subject: "GitHub source repos/karpathy/convnetjs/demo/js/regression.js"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/js/regression.js]
semantic-status: complete-named-text-read
---

# repos/karpathy/convnetjs/demo/js/regression.js

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/convnetjs/demo/js/regression.js), SHA-256 `ef7f28e376b60a655765e21682a58f1e2134c757cb42fdac9d17588d58029428`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "var N, data, labels; var ss = 30.0; // scale for drawing var layer_defs, net,".

Regression demo learns sampled x*sin(x) points and displays fitted output and selected neuron functions while users add points or change architecture. RL demo separates sensory input, policy action, environment transition and reward learning; reward combines wall distance, forward movement and food/poison, while visualization exposes sensors, network activations and rolling reward. Simulation speed explicitly reduces drawing overhead, snapshot loading stops learning and controls distinguish acting from training. Toy geometry and reward shaping do not prove general-purpose performance; regression neuron plotting uses grid-count as neuron count and may read undefined values. These mechanisms were inspected without running browser eval.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text

var N, data, labels;
var ss = 30.0; // scale for drawing

var layer_defs, net, trainer;

// create neural net
var t = "layer_defs = [];\n\
layer_defs.push({type:'input', out_sx:1, out_sy:1, out_depth:1});\n\
layer_defs.push({type:'fc', num_neurons:20, activation:'relu'});\n\
layer_defs.push({type:'fc', num_neurons:20, activation:'sigmoid'});\n\
layer_defs.push({type:'regression', num_neurons:1});\n\
\n\
net = new convnetjs.Net();\n\
net.makeLayers(layer_defs);\n\
\n\
trainer = new convnetjs.SGDTrainer(net, {learning_rate:0.01, momentum:0.0, batch_size:1, l2_decay:0.001});\n\
";

var lix=2; // layer id of layer we'd like to draw outputs of
function reload() {
  eval($("#layerdef").val());

  // refresh buttons
  var t = '';
  for(var i=1;i<net.layers.length-1;i++) { // ignore input and regression layers (first and last)
    var butid = "button" + i;
    t += "<input id=\""+butid+"\" value=\"" + net.layers[i].layer_type +"\" type=\"submit\" onclick=\"updateLix("+i+")\" style=\"width:80px; height: 30px; margin:5px;\";>";
  }
  $("#layer_ixes").html(t);
  $("#button"+lix).css('background-color', '#FFA');
}
function updateLix(newlix) {
  $("#button"+lix).css('background-color', ''); // erase highlight
  lix = newlix;
  $("#button"+lix).css('background-color', '#FFA');
}
 
function regen_data() {
  N = parseInt($("#num_data").val());
  data = [];
  labels = [];
  for(var i=0;i<N;i++) {
    var x = Math.random()*10-5;
    var y = x*Math.sin(x);
    data.push([x]);
    labels.push([y]);
  }
}

function myinit(){
  regen_data();
  $("#layerdef").val(t);
  reload();
}
 
function update(){
  // forward prop the data
  
  var netx = new convnetjs.Vol(1,1,1);
  avloss = 0.0;

  for(var iters=0;iters<50;iters++) {
    for(var ix=0;ix<N;ix++) {
      netx.w = data[ix];
      var stats = trainer.train(netx, labels[ix]);
      avloss += stats.loss;
    }
  }
  avloss /= N*iters;

}

function draw(){
    
    ctx.clearRect(0,0,WIDTH,HEIGHT);
    ctx.fillStyle = "black";

    var netx = new convnetjs.Vol(1,1,1);

    // draw decisions in the grid
    var density= 5.0;
    var draw_neuron_outputs = $("#layer_outs").is(':checked');
    
    // draw final decision
    var neurons = [];
    ctx.beginPath();
    for(var x=0.0; x<=WIDTH; x+= density) {

      netx.w[0] = (x-WIDTH/2)/ss;
      var a = net.forward(netx);
      var y = a.w[0];

      if(draw_neuron_outputs) {
        neurons.push(net.layers[lix].out_act.w); // back these up
      }

      if(x===0) ctx.moveTo(x, -y*ss+HEIGHT/2);
      else ctx.lineTo(x, -y*ss+HEIGHT/2);
    }
    ctx.stroke();

    // draw individual neurons on first layer
    if(draw_neuron_outputs) {
      var NL = neurons.length;
      ctx.strokeStyle = 'rgb(250,50,50)';
      for(var k=0;k<NL;k++) {
        ctx.beginPath();
        var n = 0;
        for(var x=0.0; x<=WIDTH; x+= density) {
          if(x===0) ctx.moveTo(x, -neurons[n][k]*ss+HEIGHT/2);
          else ctx.lineTo(x, -neurons[n][k]*ss+HEIGHT/2);
          n++;
        }
        ctx.stroke();
      }
    }
  
    // draw axes
    ctx.beginPath();
    ctx.strokeStyle = 'rgb(50,50,50)';
    ctx.lineWidth = 1;
    ctx.moveTo(0, HEIGHT/2);
    ctx.lineTo(WIDTH, HEIGHT/2);
    ctx.moveTo(WIDTH/2, 0);
    ctx.lineTo(WIDTH/2, HEIGHT);
    ctx.stroke();

    // draw datapoints. Draw support vectors larger
    ctx.strokeStyle = 'rgb(0,0,0)';
    ctx.lineWidth = 1;
    for(var i=0;i<N;i++) {
      drawCircle(data[i]*ss+WIDTH/2, -labels[i]*ss+HEIGHT/2, 5.0);
    }

    ctx.fillStyle = "blue";
    ctx.font = "bold 16px Arial";
    ctx.fillText("average loss: " + avloss, 20, 20);
}

function mouseClick(x, y, shiftPressed){
  
  // add datapoint at location of click
  data.push([(x-WIDTH/2)/ss]);
  labels.push([-(y-HEIGHT/2)/ss]);
  N += 1;

}

function keyDown(key){
}

function keyUp(key) {

}

$(function() {
    
});
```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
