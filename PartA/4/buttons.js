function btn1()
{
n=document.getElementById('input1').value;
if(isNaN(n)){
alert("Please enter numbers only");
}
else{
var result= n*2;
document.getElementById('result').innerHTML= result;
}
}

function btn2()
{
n=document.getElementById('input1').value;
if(isNaN(n)){
alert("Please enter numbers only");
}
else{
var result= n*n;
document.getElementById('result').innerHTML= result;
}
}
