let gmatData = []
let lineData = []
let lineLables = []
let barLables = []
let barData = []
let dataAttr=['Problem Solving','Data Sufficiency','Critical Reasoning','Sentence Correction']

import {finalRes} from '../../gmat_questions/js/gmat_grid'
console.log(finalRes)
console.log(lineData)

// 1. FETCH DATA FROM THE DATABASE AND HIDING UNNECESSARY DATA ON THE PAGE
axios.get('http://127.0.0.1:8000/api/get_answers').then(res => {
  gmatData = res.data;
  console.log(gmatData)
}).catch(err => console.log(err))

function convertData(num){
    let avg = 0
    let n = 0
    gmatData.forEach(elem => {
        if(!elem.answers.length) return;
        else{
            elem.answers.forEach( answ =>{
                if(answ.question_number === num)
                    {
                        console.log(num)
                        console.log(answ.time_spent)
                        avg += answ.time_spent
                        n++
                    }
            })
        }
    })
    if(n!==0)
        return avg/n
}

document.getElementById("quant").onclick = () => {
    console.log(finalRes)
    lineData = []
    lineLables = []
    for(let i=1; i<6; i++)
    {
        lineLables.push(`${i}`)
        lineData.push(convertData(i))
    }
    console.log(lineData)
    console.log(lineLables)

    new Chart(document.getElementById("line-chart").getContext('2d'), {
        type: 'line',
        data: {
            lables: lineLables,
            datasets: [{
                lable: "Total",
                data: lineData,
                borderColor: "#3e95cd",
                fill: false,   
            },],
        },
        options: {
            title: {
              display: true,
              text: 'Average time spent per question'
            }
          }
    });

    new Chart(document.getElementById("radar-chart").getContext('2d'), {
        type: 'radar',
        data: {
            lables: dataAttr,
            datasets: [{
                lable: "Total",
                backgroundColor: "rgba(179,181,198,0.2)",
                borderColor: "rgba(179,181,198,1)",
                pointBorderColor: "#fff",
                pointBackgroundColor: "rgba(179,181,198,1)",
                data: [3,4,5,4,5],
                borderColor: "#3e95cd",
                fill: false,   
            },],
        },
        options: {
            title: {
              display: true,
              text: 'Average scores per question'
            }
          }
    });
    
}







