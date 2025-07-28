const express = require('express');
const app = express();
const cors = require('cors');

const districts  = require('./districts.json')

app.get('/',(req,res)=>{
    res.send(`<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>tamilnadu district and taluk fetch api</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #fff;
        }

        .main-content {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            max-width: 800px;
        }

        h1, h2, h4 {
            margin-bottom: 10px;
            color: #333;
        }

        p {
            font-weight: 500;
            margin: 5px 0;
        }

        a {
            color: #0066cc;
            font-weight: bold;
        }

        .code-block {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            margin: 10px 0;
        }
        code{
            background-color: black;
            color: white;
            margin-left: 20px;
            padding: 2px;
        }
        h1 {
        margin-top: 30px;
        margin-bottom: 10px;
        color: #2c3e50;
}

ul {
    padding-left: 20px;
    margin-top: 0;
    margin-bottom: 20px;
}

ul li {
    margin-bottom: 8px;
    font-weight: 500;
    color: #34495e;
}

    </style>
</head>
<body>
    <div class="main-content">
        <h1>Welcome</h1>
        <p>This API is used to fetch the districts and taluks of Tamil Nadu.</p>
        <p>Data is referred from the link below:</p>
        <a href="https://www.tnpsc.gov.in/english/districts.html">Click Here to Visit</a>

        <h2>Response Format</h2>
        <div class="code-block">
            {
            <br>&nbsp;&nbsp;"The Nilgiris": ["Udagamandalam", "Coonoor", "Gudalur", "Kothagiri", "Kundah", "Pandalur"],
            <br>&nbsp;&nbsp;"Kancheepuram": ["Kancheepuram", "Kundrathur", "Sriperumbudur", "Uthiramerur", "Walajabad"],
            <br>&nbsp;&nbsp;...
            <br>
            }
        </div>
        
        <h2>Available Endpoints</h2>

        <h4>1. <code>GET -> /all</code></h4>
        <p>Returns all districts and their taluks.</p>
        <p>Response Type - <code>{"District" : [array of taluks]} - json (contains all districts)</code> </p>
        <hr>
        <h4>2. <code>GET -> /districts</code></h4>
        <p>Returns only the list of districts.</p>
        <p>Response Type - <code>{"districts" : [array of districts]} - json</code> </p>
        <hr>
        <h4>3. <code>GET -> /taluks --- Query Varible - district_name
        </code></h4>
        <p>Returns taluks for the specified district.</p>
        <p>Response Type - <code>{"taluks" : [array of taluks]} - json</code> </p>
        <hr>
        <h4>4. <code>GET -> /check_taluk --- Query Varibles - district_name and taluk_name
        </code></h4>
        <p>Returns a message indicating whether the district and taluk match.</p>
        <p>Response Type - <code>{"found" : true or false} - json</code> </p>
        <h1>Notes</h1>
<ul>
    <li>All this data is taken from the official government website.</li>
    <li>There will be no issue with upper or lower case, but correct spelling is required.</li>
    <li>This API is created only for educational purposes and to gain experience.</li>
    <li>Use the correct query parameter variable names to receive a successful response.</li>
</ul>
    </div>
</body>
</html>
`)
})

app.get('/all',(req,res)=>{
    res.json(districts)
})

app.get('/districts',(req,res)=>{
    
    const dists = Object.keys(districts);
    res.json({"districts":dists});
})
app.get('/taluks',(req,res)=>{
    const district_name = req.query.district_name
    var cap_dis = district_name.charAt(0).toUpperCase() + district_name.slice(1).toLowerCase();
    if(!districts[cap_dis]){
        res.json({"error":"District not found"})
    }
    res.json({"taluks":districts[cap_dis]})
})

app.get('/check_taluk',(req,res)=>{
    const district_name = req.query.district_name
    const taluk_name = req.query.taluk_name
    var cap_dis = district_name.charAt(0).toUpperCase() + district_name.slice(1).toLowerCase();
    var cap_taluk = taluk_name.charAt(0).toUpperCase() + taluk_name.slice(1).toLowerCase(); 
    if(districts[cap_dis].includes(cap_taluk)){
        res.json({"found":true})
    }else{
        res.json({"found":false})
    }
})
module.exports = app;