// run by typing "node newton-approx.js"
// console.log("hello world")

var func1 =(x) => ( (3*x) + 4 - (Math.pow(Math.E, x) )) // f(x)
var func2 =(x) => (3 - Math.pow(Math.E, x)); // f'(x)

var func3 =(x) => (x + 3 - Math.pow(Math.E, x)) // f(x)
var func4 =(x) => (1 - Math.pow(Math.E, x)) // f'(x)

var func5 =(x) => (( 5 * Math.sin(x) ) - x) // f(x)
var func6 =(x) => (( 5 * Math.cos(x) ) - 1) // f'(x)

var calculateNext = (x) => { 
    // use func3 / func4 for testing, 
    // use func1 / func2 for actual, 
    var result = (x - (func5(x)/func6(x)) )
    return result.toFixed(6)
}

var calulateAllIterative = () => 
{
    var x = 2
    for (var i = 0; i < 10; i++)
    {
        x = calculateNext(x);
        console.log(i, x)
    }
}

console.log("calulateAllIterative")
calulateAllIterative()

var calulateAllRecursive = (i, x, prevX) => 
{
    if (x == prevX)
    {
        return;
    }
    var nextX = calculateNext(x);
    console.log(i++, x)
    calulateAllRecursive(i, nextX, x)
}

// console.log("calulateAllRecursive")
// calulateAllRecursive(0, 0.4, 0)