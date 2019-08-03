//const axios = require('axios')
const url = 'http://localhost/v1/aiseki/aggregate'

axios.get(url).then(res => {
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {

    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: res.data.result.labels,
        datasets: res.data.result.data.map( (val) => {
            return {
                label: val.branch_nm,
                data: val.visitors
            }
        })
    },

    // Configuration options go here
    options: {}
});

})
