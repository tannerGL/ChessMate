/*

Chess Mate 2022
@author Tanner Lindsay

*/

// Set up the chessboard
var chessboard = document.querySelector('.chessboard');
var cells = chessboard.querySelectorAll('td');
var selectedCell = null;
var game = new Chess();

// Add click event listeners to each cell
cells.forEach(function(cell) {
  cell.addEventListener('click', handleCellClick);
});

// Handle clicks on cells
function handleCellClick(event) {
  var cell = event.target;
  console.log(selectedCell);
  // If a cell is already selected, try to move the piece
  if (selectedCell) {
    var source = selectedCell.getAttribute('data-position');
    var target = cell.getAttribute('data-position');
    var move = game.move({from: source, to: target});
    console.log(source + " " + target);
    // If the move is legal, update the board and clear the selection
    if (move) {
      updateBoard();
      selectedCell.classList.remove('selected');
      selectedCell = null;
    }
  }
  // Otherwise, select the cell
  else {
    selectedCell = cell.parentElement;
    selectedCell.classList.add('selected');
  }
}

// Update the board to reflect the current game state
function updateBoard() {
  cells.forEach(function(cell) {
    var position = cell.getAttribute('data-position');
    var piece = game.get(position);
    
    // If there is a piece on the cell, add an image
    if (piece) {
      var img = document.createElement('img');
      img.src = '/static/images/' + piece.type + piece.color + '.png';
      cell.appendChild(img);
    }
    // Otherwise, clear the cell
    else {
      cell.innerHTML = '';
    }
  });
}

// Set up the new game button
var newGameButton = document.querySelector('#new-game');
newGameButton.addEventListener('click', function() {
  game = new Chess();
  updateBoard();
});

// Set up the undo button
var undoButton = document.querySelector('#undo');
undoButton.addEventListener('click', function() {
  game.undo();
  updateBoard();
});

// Initialize the board
updateBoard();
