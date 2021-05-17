console.log("Hello world!");

function Draw() {
    console.log("Draw")
  
    var path = new Path();
    // Give the stroke a color
    path.strokeColor = 'black';
    var start = new Point(100, 100);
    // Move to start and draw a line from there
    path.moveTo(start);
    // Note the plus operator on Point objects.
    // PaperScript does that for us, and much more!
    path.lineTo(start + [ 100, -50 ]);
}

Draw();

/*
d3.selectAll(".food").on("click", FoodSelected);

// click handler
function FoodSelected(d, i) {
  d3.select(this)
    .attr("xlink:href", "./img/Slice_of_pizza.svg")
    .attr("height", 45)
    .attr("width", 45);
}

d3.select("body").on("keydown", KeyPress);

function isPointInPoly(poly, pt){
  for(var c = false, i = -1, l = poly.length, j = l - 1; ++i < l; j = i)
      ((poly[i].y <= pt.y && pt.y < poly[j].y) || (poly[j].y <= pt.y && pt.y < poly[i].y))
      && (pt.x < (poly[j].x - poly[i].x) * (pt.y - poly[i].y) / (poly[j].y - poly[i].y) + poly[i].x)
      && (c = !c);
  return c;
}

function KeyPress(){
  player = d3.select(".player")
  if(d3.event.keyCode === 37) //Left Arrow
  {
    player.attr("x", Number(player.attr("x")) - 5)
  }
  else if(d3.event.keyCode === 38) // Up Arrow
  {
    player.attr("y", Number(player.attr("y")) - 5)
  }
  else if(d3.event.keyCode === 39) // Right Arrow
  {
    player.attr("x", Number(player.attr("x")) + 5)
  }
  else if(d3.event.keyCode === 40) // Down Arrow
  {
    player.attr("y", Number(player.attr("y")) + 5)
  }
}
*/
  /*
	// Create a Paper.js Path to draw a line into it:
	var path = new Path();
	// Give the stroke a color
	path.strokeColor = 'black';
	var start = new Point(100, 100);
	// Move to start and draw a line from there
	path.moveTo(start);
	// Note the plus operator on Point objects.
	// PaperScript does that for us, and much more!
  path.lineTo(start + [ 100, -50 ]);
  

		// Get a reference to the canvas object
		var canvas = document.getElementById('myCanvas');
		// Create an empty project and a view for the canvas:
		paper.setup(canvas);
		// Create a Paper.js Path to draw a line into it:
		var path = new paper.Path();
		// Give the stroke a color
		path.strokeColor = 'black';
		var start = new paper.Point(100, 100);
		// Move to start and draw a line from there
		path.moveTo(start);
		// Note that the plus operator on Point objects does not work
		// in JavaScript. Instead, we need to call the add() function:
		path.lineTo(start.add([ 200, -50 ]));
		// Draw the view now:
        paper.view.draw();
  */
