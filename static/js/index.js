/*global $, jquery ,alert, console*/ 
//let { url } = require("node:inspector");
//const url = new URL('../cats', 'http://www.example.com/dogs');

$(document).ready(function(){
    $(".upload").change(function(){
        setTimeout(function(){
$(".div").text($(".upload").val())}),5000})

            $("body").one("dblclick mouseleave",".div",function(e,width) {
                
            $(this).fadeToggle(3000,function(){
                $(this).fadeToggle(2000);
            }); 
            
    
        })
    })

let inp = document.getElementsByClassName('upload');
let d = document.getElementsByClassName('div');
inp.onchange = function(){
d.innerHTML = inp.value;

}
