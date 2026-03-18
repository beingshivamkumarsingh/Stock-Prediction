let predictionChart
let compareChart
let forecastChart


async function predict(){

let stock = document.getElementById("stock").value

let res = await fetch("/predict/" + stock)

let data = await res.json()

drawPrediction(data.actual,data.predicted)

drawComparison(data.errors)

drawForecast(data.forecast)

document.getElementById("bestModel").innerHTML =
"Best Model : " + data.best_model

loadSignal(stock)


}



function drawPrediction(actual,predicted){

if(predictionChart) predictionChart.destroy()

predictionChart = new Chart(document.getElementById("predictionChart"),{

type:"line",

data:{

labels:actual.map((_,i)=>i),

datasets:[

{
label:"Actual Price",
data:actual,
borderColor:"blue",
fill:false
},

{
label:"Predicted Price",
data:predicted,
borderColor:"red",
fill:false
}

]

}

})

}



function drawComparison(errors){

if(compareChart) compareChart.destroy()

compareChart = new Chart(document.getElementById("compareChart"),{

type:"bar",

data:{

labels:Object.keys(errors),

datasets:[{

label:"RMSE Error",

data:Object.values(errors),

backgroundColor:"orange"

}]

}

})

}



function drawForecast(future){

if(forecastChart) forecastChart.destroy()

forecastChart = new Chart(document.getElementById("forecastChart"),{

type:"line",

data:{

labels:future.map((_,i)=>"Day "+(i+1)),

datasets:[{

label:"30 Day Forecast",

data:future,

borderColor:"green",

fill:false

}]

}

})

}



async function loadSignal(stock){

let res = await fetch("/signal/" + stock)

let data = await res.json()

let box = document.getElementById("signalBox")

if(data.signal=="BUY"){

box.className="buy"
box.innerHTML="🟢 BUY SIGNAL"

}

else if(data.signal=="SELL"){

box.className="sell"
box.innerHTML="🔴 SELL SIGNAL"

}

else{

box.className="hold"
box.innerHTML="🟡 HOLD"

}

}



