const express = require('express')
const path = require('path');
const app = express()
const exec = require('child_process');
const bodyParser = require('body-parser')
const spawn = require('child_process').spawn;
const port = 80

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/index.html'));
})

app.post('/color', (req, res) => {
  red = req.body.r;
  green = req.body.g;
  blue = req.body.b;
  updateStrip();
})

app.post('/brightness', (req, res) => {
  brightness = req.body.brightness;
  updateStrip();
  res.end()
})

app.post('/speed', (req, res) => {
  speed = req.body.speed;
  updateStrip();
  res.end()
})

app.post('/mode', (req, res) => {
  mode = req.body.mode;
  updateStrip();
  res.end()
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

// previous child processes pids
var previousPid  = null;

// led strip script arguments
var mode = "color";
var brightness = 100;
var speed = 200;
var red = 255;
var green = 255;
var blue = 255;

// update LED strip with command arguments
function updateStrip() {
  if (previousPid !== null) {
    try {
      process.kill(previousPid, "SIGTERM");
    } catch {
      console.error("process already finished");
    }
  }
  children = [];
  var child = spawn(
    "python3", [
      "../scripts/strip-control.py",
      "-m", mode,
      "-r", red,
      "-g", green,
      "-b", blue,
      "-B", brightness,
      "-s", speed,
    ]
  );
  previousPid = child.pid;
  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  child.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  child.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}
