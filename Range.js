/**
 * Created by yenerozsoy on 09.02.18.
 */

$(document).ready(function() {
    var slider = document.getElementsByName('slider');
    const output = document.querySelector("output");
    document.addEventListener('DOMContentLoaded', function() {
        output.value = slider.value;
    });

    slider[0].addEventListener("input", function () {
        output.value = this.value;
        $.ajax({
        type: "POST",
        url: "http://192.168.0.120:5000/helligkeit",
        data: { brightness: this.value}
    }).done(function( o ) {
   // do something
    	});
    });
});

var hh = 0;
var color = "#FF0000";
var colorObj = w3color(color);
function mouseOverColor(hex) {
    document.getElementById("divpreview").style.visibility = "visible";
    document.getElementById("divpreview").style.backgroundColor = hex;
    document.body.style.cursor = "pointer";
}

function mouseOutMap() {
    if (hh == 0) {
        document.getElementById("divpreview").style.visibility = "hidden";
    } else {
        hh = 0;
    }
    document.getElementById("divpreview").style.backgroundColor = colorObj.toHexString();
    document.body.style.cursor = "";
}

window.onload = function() {
    var x = document.createElement("input");
    x.setAttribute("type", "color");
    if (x.type == "text") {
        document.getElementById("html5DIV").style.visibility = "hidden";
    }
}

function clickColor(hex) {
    $.ajax({
        type: "POST",
        url: "http://192.168.0.120:5000/farbe",
        data: { color: hex}
    }).done(function( o ) {
   // do something
    });
    console.log(0);
}

function postData(input) {
    $.ajax({
        type: "POST",
        url: "http://192.168.0.120:5000/helligkeit",
        data: { brightness: input}
    }).done(function( o ) {
   // do something
    });
}

function clickButton() {
    var button = document.getElementById("button");
    var status = button.checked;
    $.ajax({
        type: "POST",
        url: "http://192.168.0.120:5000/ambi",
        data: { status: this.status },
        success: function(response) {
            console.log(response);
        }
    }).done(function(data) {
        console.log(data);
    });}

