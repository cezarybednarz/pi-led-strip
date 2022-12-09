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
  console.log(req.body);
  red = req.body.r;
  green = req.body.g;
  blue = req.body.b;
  updateStrip();
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

// previous child process pid
var childPid = null;

// led strip script arguments
var mode = "color";
var red = 255;
var green = 255;
var blue = 255;

// update LED strip with command arguments
function updateStrip() {
  // TODO
  // if (childPid !== null) { 
  //   process.kill(-childPid);  
  // }
  var child = spawn(
    "sudo", [
      "python3", 
      "../scripts/strip-control.py",
      "-m", mode,
      "-r", red,
      "-g", green,
      "-b", blue
    ]
  );
  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  
  child.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
  child.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  // TODO
  // process.kill(-child.pid);
}
