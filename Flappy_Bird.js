// variables for using\\\\\\\\\\\\\
var rect = 20;
var birdX = getWidth() / 4;
var birdY = 0;
var fps = 1000 / 60;
var bird = new Rectangle(rect, rect);
var score = 0;
var scoreDisplay = new Text(score, "30pt Arial");
var blockWidth = 20;
var blockLength = 225;
var randomPos;

// storage of columns
var blockArr = [];

// variables for moving the bird
var direction = 0;
var gravity = -1;
var terminal = -10;


///// background image
var IMAGE_URL = "https://codehs.com/uploads/17ff713a6d1e0cab200f90ab6330c3c4";
var IMAGE_WIDTH = 400;
var IMAGE_HEIGHT = 480;
var IMAGE_X = getWidth() / 2 - IMAGE_WIDTH / 2;
var IMAGE_Y = getHeight() / 2 - IMAGE_HEIGHT / 2; 

    var image = new WebImage(IMAGE_URL);
    image.setSize(IMAGE_WIDTH, IMAGE_HEIGHT);
    image.setPosition(IMAGE_X, IMAGE_Y);
    
    add(image);



function start(){
    init();
    birdimage();
    setTimer(update, fps);
    createBlock();
    setTimer(createBlock, 2000);
    keyDownMethod(controls); 
}

function init(){
    var image_URL = "https://codehs.com/uploads/a5f0be9c6481c85fd8f4d866b28aa3a2";
    var image_width = 20;
    var image_height = 20;

    var image = new WebImage(image_URL);
    image.setSize(image_width, image_height);
    image.setPosition(birdX, getHeight() / 2);
    
    add(image);
    bird.setPosition(birdX, getHeight() / 2);
    bird.setColor(Color.YELLOW);
    add(bird);
    
    scoreDisplay.setPosition(20,45);
    scoreDisplay.setColor(Color.WHITE);
    add(scoreDisplay);
}

function createBlock(){
    randomPos = Randomizer.nextInt(0, 480 - blockLength);
    var block = new Rectangle(blockWidth, blockLength);
    block.setPosition(400, randomPos);
    add(block);
    blockArr.push(block);
}

// update the game
function update(){
    if(bird.y <= 0 || bird.y >= getHeight()){
        gameOver();
    }
    
    // makes the bird fall
    bird.move(0, inv(direction));
    if(direction > terminal){
        direction += gravity;
    }
    
    // changes the positions of the columns
    for(var i = 0; i < blockArr.length; i++){
        blockArr[i].move(-2, 0);
        
        // adds points
        if(blockArr[i].x == bird.x){
            score += 1;
        }
    }
    
    collisionCheck();
    
    scoreDisplay.setText(score);
}

function collisionCheck(){
    for(var i = 0; i < blockArr.length; i++){
        if(bird.x >= blockArr[i].x && bird.x <= blockArr[i].x + blockWidth && bird.y >= blockArr[i].y && bird.y <= blockArr[i].y + blockLength){
            gameOver();
        }
    }
}

function gameOver(){
    stopTimer(update);
    
    var text = new Text("Game Over!", "30pt Arial");
    text.setPosition(100, 200);
    text.setColor(Color.RED);
    add(text);
}

function controls(e){
    if(e.keyCode == Keyboard.SPACE){
        direction = 10;
    }
}

//inverts the variable
function inv(v){
    return v * -1;
}

///bird image
function birdimage(){
    var image_URL = "https://codehs.com/uploads/a5f0be9c6481c85fd8f4d866b28aa3a2";
    var image_width = 20;
    var image_height = 20;

    var image = new WebImage(image_URL);
    image.setSize(image_width, image_height);
    image.setPosition(birdX, getHeight() / 2);
    
    add(image);
}