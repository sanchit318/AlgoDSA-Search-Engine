//Run my server in this file

const express = require("express");
const ejs = require("ejs"); //View Engine
const path = require("path");

const spawn = require("child_process").spawn;

//Creating our Server
const app = express();
app.use(express.json());

//Setting up EJS
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "/public"))); //Successfully registered public folder as a static resource.

const PORT = 8000;

//GET request to home page
app.get("/", (req, res) => {
  res.render("index"); //Whenever someone visits '/', my app will go to look in the views directory,
  //that if any file with name index.ejs(attach extension ejs automatically) exists or not..
  //If it exists, it will send that as a response, else it will throw error.
});

app.get("/search", (req, res) => {
  //handles the requests (Ex - fetch request)
  const query = req.query;
  const question = query.question;
  //variable question contains the Query string now
  // console.log(question);

  //Storing the query string to text file
  var fs = require("fs");
  fs.readFile("QueryString.txt", "utf-8", function (err, data) {
    if (err) throw err;

    var newValue = question;
    // console.log(question);

    fs.writeFile("QueryString.txt", newValue, "utf-8", function (err, data) {
      if (err) throw err;
      //        console.log('Done!');
    });
  });

  // We need to stringify the data as
  // python cannot directly read JSON
  // as command line argument.
  let stringified_question = JSON.stringify(question);
  // console.log(stringified_question);

  // setTimeout( ()=>{

  // });

  var spawn = require("child_process").spawn,
    py = spawn("python", ["QueryProcess.py"]),
    data = stringified_question,
    dataString = "";

  py.stdout.on("data", function (data) {
    dataString += data.toString();
  });
  py.stdout.on("end", function () {
    console.log("Returned array :", dataString);

    //   arr=dataString;
    //   console.log(dataString[4]);
    // console.log(typeof dataString);
  });
  py.stdin.write(JSON.stringify(data));
  py.stdin.end();

  setTimeout(() => {
    var arr = []; // an array of strings
    //Reading data from SearchResult.txt
    fs.readFile("SearchResult.txt", function (err, data) {
      if (err) throw err;
      console.log("Fine");
      var array = data.toString().split("\n");
      for (i in array) {
        // Printing the response array
        console.log(array[i]);
        console.log(typeof array[i]);
        arr.push(array[i]);
      }
      res.json(arr);
    });
    // console.log(typeof(arr));
  }, 10000);

  //TF-IDF Algo run by python program now using the data from .txt file

  //the Algo will update the "SearchResult.txt" file with the search results.
  //We have to fetch it's content and deliver it to the user

  //List of 5 questions
  // setTimeout( () =>{
  //     const arr=[
  //         {
  //             str:question,
  //             title:"dsfsd",
  //             url:"efd.com",
  //         },
  //         {str:question,
  //             title:"dsfsd",
  //             url:"efd.com",
  //         },
  //         {str:question,
  //             title:"dsfsd",
  //             url:"efd.com",
  //         },
  //         {str:question,
  //             title:"dsfsd",
  //             url:"efd.com",
  //         },
  //         {str:question,
  //             title:"dsfsd",
  //             url:"efd.com",
  //         }
  //     ];
  //     res.json(arr);
  // },1000);
});

//Assigning PORT to out application
app.listen(8000, () => {
  console.log("server is running on PORT " + PORT);
});
